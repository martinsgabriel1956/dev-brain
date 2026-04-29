---
date: 2026-03-29
tags: [tech-mentor, system-design, cases, youtube, streaming, hls, cdn, encoding]
skill: tech-mentor-system-design/references/system-design-cases
level: arquiteto
---

# Case: YouTube / Video Streaming

## Contexto

Video streaming é um dos sistemas mais complexos em termos de infraestrutura porque combina três problemas distintos: **processamento intensivo de upload** (transcodificação assíncrona), **entrega eficiente de conteúdo** (CDN + ABR), e **escala de storage** (petabytes com acesso em padrão radicalmente diferente por idade do conteúdo).

---

## Requisitos

**Funcionais:**
- Upload de vídeo (qualidade original)
- Transcodificação para múltiplas qualidades (360p, 720p, 1080p, 4K)
- Streaming adaptativo: player muda qualidade conforme a banda disponível
- Search, comments, likes

**Não-funcionais (escala real):**
```
500 horas de vídeo uploaded por minuto
1B horas assistidas por dia
Storage total: ~1 exabyte
Disponibilidade: 99,99%
```

---

## Pipeline de Upload

O upload nunca deve passar pelo backend da aplicação — vídeos são grandes demais.

```
[1] Client solicita presigned URL ao Backend
    → Backend gera S3 Presigned URL (PUT, TTL 1h)
    → Retorna URL ao cliente

[2] Client faz upload direto para S3 (não passa pelo backend)
    → S3 recebe o vídeo original (raw)
    → Emite evento: s3:ObjectCreated

[3] S3 event → SQS → Transcoding Workers (EC2/ECS — escala horizontal)
    Por vídeo, workers paralelos:
      - Transcodifica para cada qualidade (FFmpeg)
      - Gera thumbnails (frames em 5s, 10s, 30s)
      - Extrai metadados (duração, resolução, codec, bitrate)
      - Divide em segmentos HLS/DASH (2-10s cada)

[4] Outputs → S3 (vídeos transcodificados + segmentos + thumbnails)
    → CDN (CloudFront) distribui globalmente

[5] Metadata → PostgreSQL
    Status: PROCESSING → READY

[6] Notificação ao uploader (email / push notification)
```

---

## Adaptive Bitrate Streaming (ABR)

O player nunca faz download do vídeo inteiro. Ele consome segmentos de 2-10 segundos, cada um disponível em múltiplas qualidades.

### HLS (HTTP Live Streaming) — padrão Apple, amplamente adotado

```
Manifesto master (.m3u8):
  #EXTM3U
  #EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=640x360
  360p/index.m3u8
  #EXT-X-STREAM-INF:BANDWIDTH=2800000,RESOLUTION=1280x720
  720p/index.m3u8
  #EXT-X-STREAM-INF:BANDWIDTH=5000000,RESOLUTION=1920x1080
  1080p/index.m3u8

Manifesto de qualidade (720p/index.m3u8):
  #EXTM3U
  #EXT-X-TARGETDURATION:6
  #EXTINF:6.0,
  segment_001.ts
  #EXTINF:6.0,
  segment_002.ts
  ...
```

O player:
1. Faz download do manifesto master
2. Escolhe qualidade inicial com base em bandwidth estimado
3. A cada segmento, reavalia: bandwidth atual > threshold? sobe qualidade. < threshold? desce.
4. Buffer de 30s de antecipação → troca de qualidade não causa rebuffering

### DASH (Dynamic Adaptive Streaming over HTTP) — padrão aberto, usado no YouTube

Mesmo conceito do HLS, manifesto em XML (MPD — Media Presentation Description). Mais flexível, suporte a DRM (Widevine, PlayReady).

---

## CDN Strategy

Segmentos de vídeo são **imutáveis** — uma vez gerados, nunca mudam. Isso permite cache agressivo.

```
Segmento: TTL 365 dias no CDN (conteúdo popular)
Manifesto: TTL curto (60s) — pode mudar se novos segmentos forem adicionados

Distribuição:
  Upload → S3 (origem)
  Play   → CloudFront edge node mais próximo do usuário
           → miss → busca na origem → cacheia no edge
           → hit  → serve direto (sem latência de rede intercontinental)

Pré-aquecimento (popular content):
  Ao atingir N views → push proativo do vídeo para edges estratégicos
  Evita cache miss em cascata quando conteúdo viraliza
```

---

## Storage por Temperatura

Conteúdo novo tem tráfego intenso. Conteúdo antigo raramente é acessado. Storage hierárquico reduz custo drasticamente.

```
Hot (últimos 30 dias, ~5% do volume, ~80% do tráfego):
  → S3 Standard
  → CDN com cache agressivo (TTL 365 dias)

Warm (30 dias – 1 ano):
  → S3 Standard-IA (Infrequent Access) — ~40% mais barato
  → CDN com TTL moderado

Cold (> 1 ano, cauda longa — 90% do volume, <5% do tráfego):
  → S3 Glacier (~80% mais barato que Standard)
  → CDN sem cache (transcode on-demand se necessário)
  → Restauração: 3-5 horas (Glacier) ou minutos (Glacier Instant Retrieval)
```

---

## Transcodificação — Decisões de Design

### Por que múltiplas qualidades?

Usuário em 3G recebe 360p (baixo bitrate, arquivos menores). Usuário em fibra recebe 4K. O player decide automaticamente — sem intervenção do usuário.

### Paralelismo por segmento

Um vídeo de 2h transcodificado sequencialmente = horas de processamento. Com workers paralelos:

```
Vídeo original (2h) → dividido em 720 segmentos de 10s
  → 720 workers em paralelo transcodificando cada segmento
  → Tempo de transcodificação: ~minutos, não horas

Coordenação: SQS com 1 mensagem por segmento por qualidade
  → N workers consomem as mensagens em paralelo
  → DLQ para segmentos que falharam (retry automático)
```

### Codec

```
H.264: compatibilidade máxima, compressão moderada
H.265 (HEVC): 2× melhor compressão, menos compatível, licença cara
AV1 (Google): open-source, melhor compressão que HEVC, encoding mais lento
              → YouTube usa AV1 para conteúdo popular (economiza CDN/storage)
VP9: open-source, melhor que H.264, usado no YouTube para 4K
```

---

## Estimativas de Escala

```
Upload:
  500h de vídeo/min × 60min = 30.000h/hora
  Vídeo 1h a 720p ≈ 1.5GB
  30.000 × 1.5GB = 45TB de vídeo ingerido por hora

Transcodificação:
  1h de vídeo → ~4h de CPU para todas as qualidades (sem paralelismo)
  Com workers paralelos: ~10min para um vídeo de 1h
  Workers necessários: elástico, auto-scaling com base no tamanho da fila SQS

Storage:
  1h de vídeo em todas as qualidades (360p a 4K) ≈ 8GB
  30.000h/hora × 8GB = 240TB/hora de storage gerado
  Custo mitigado pelo storage hierárquico (Glacier para cold)

Streaming:
  1B horas/dia ÷ 86.400s = ~11.5M streams simultâneos
  Bitrate médio 720p: 2.5 Mbps
  11.5M × 2.5 Mbps = ~28 Tbps de saída de CDN
  → Distribui entre centenas de PoPs globais do CloudFront
```

---

## Trade-offs

| Decisão | Escolha | Por quê |
|---|---|---|
| Upload direto para S3 | Presigned URL | Backend não vira gargalo de I/O |
| Transcodificação | Workers paralelos por segmento | Escala elástica, tempo proporcional |
| Streaming | HLS/DASH + ABR | Player adapta qualidade sem rebuffering |
| CDN | TTL agressivo (365 dias) | Segmentos são imutáveis — cache máximo |
| Storage | Hierárquico (Hot/Warm/Cold) | 90% do volume em Glacier = 80% de economia |
| Codec | AV1 para popular, H.264 para base | Tradeoff compressão vs compatibilidade |

---

## Problemas a Aprofundar em Entrevista

**"Como funciona o DRM (proteção de conteúdo)?"**
Widevine (Google) + PlayReady (Microsoft) + FairPlay (Apple). Segmentos criptografados com chave por sessão. Player solicita licença ao License Server antes de reproduzir — sem chave, o segmento não decodifica.

**"Como lidar com picos de viralização?"**
Pré-aquecimento proativo do CDN ao detectar crescimento anômalo de views (anomaly detection no stream de eventos). Reduz cache miss em cascata quando um vídeo explode.

**"Como o YouTube implementa resumo de vídeo / capítulos?"**
Metadados no banco + timestamps no manifesto. Cada capítulo aponta para um segmento específico — seek é O(1) pelo índice do manifesto.

---

## Conceitos Relacionados

[[cdn]] · [[mensageria]] · [[cache]] · [[horizontal-vs-vertical-scaling]] · [[observabilidade]] · [[numeros-de-latencia]]

---

*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-03-29*
