# Infraestrutura Global da AWS

**Fonte:** https://aws.amazon.com/pt/about-aws/global-infrastructure/  
**Data de acesso:** 2026-05-06

---

## O que é

A infraestrutura global da AWS é a nuvem mais segura, confiável e abrangente do mercado, projetada para executar aplicações em qualquer lugar do mundo. Com data centers otimizados e múltiplas zonas de disponibilidade por região, a AWS maximiza resiliência, desempenho e inovação.

O backbone de rede global usa mais de **9 milhões de quilômetros de cabeamento de fibra óptica**, garantindo transferência de dados mais rápida, latência reduzida e melhor desempenho de aplicações.

---

## Números da Infraestrutura (2024–2025)

| Métrica | Valor |
|---|---|
| Regiões geográficas lançadas | **39** |
| Zonas de Disponibilidade (AZs) | **123** |
| POPs do CloudFront | **Mais de 750** |
| Caches de borda regionais | **13** |
| Zonas Locais + Zonas Wavelength | **43** (33 Zonas Locais + Zonas Wavelength) |

**Expansão anunciada:** +7 AZs e +2 regiões (Arábia Saudita e Chile).

---

## Regiões por Continente

### América do Norte — 9 Regiões, 31 AZs

- AWS GovCloud (Leste dos EUA)
- AWS GovCloud (Oeste dos EUA)
- Canadá (Central)
- Oeste do Canadá (Calgary)
- México (Centro)
- Oeste dos EUA (Norte da Califórnia)
- Leste dos EUA (Norte da Virgínia)
- Leste dos EUA (Ohio)
- Oeste dos EUA (Oregon)

**Locais de borda na América do Norte:** Ashburn (VA), Atlanta (GA), Boston (MA), Chicago (IL), Columbus (OH), Dallas/Fort Worth (TX), Denver (CO), Hayward (CA), Houston (TX), Jacksonville (FL), Kansas City (MO), Los Angeles (CA), Miami (FL), Minneapolis (MN), Montreal, entre outros — total de 31 locais.

### América do Sul
- São Paulo (Brasil)

### Europa
- Frankfurt (Alemanha)
- Irlanda
- Londres (Reino Unido)
- Milão (Itália)
- Paris (França)
- Espanha
- Estocolmo (Suécia)
- Zurique (Suíça)

### Oriente Médio
- Bahrein
- Emirados Árabes Unidos (EAU)
- Israel (Tel Aviv)

### África
- África do Sul (Cidade do Cabo)

### Ásia-Pacífico
- Hong Kong
- Hyderabad (Índia)
- Jacarta (Indonésia)
- Mumbai (Índia)
- Osaka (Japão)
- Seul (Coreia do Sul)
- Singapura
- Tóquio (Japão)

### Austrália e Nova Zelândia
- Sydney (Austrália)
- Melbourne (Austrália)
- Nova Zelândia

---

## Conceitos-chave

### Região (Region)
Área geográfica independente composta por múltiplas Zonas de Disponibilidade. Cada região é isolada das demais para garantir tolerância a falhas e estabilidade.

### Zona de Disponibilidade (Availability Zone — AZ)
Data center (ou cluster de data centers) fisicamente separado dentro de uma região. Interconectados por redes de baixa latência, alta capacidade e totalmente redundantes. Cada região tem **no mínimo 3 AZs**.

### Zona Local (Local Zone)
Extensão de uma região AWS posicionada em grandes centros metropolitanos. Reduz a latência para usuários finais em cidades específicas. Ideal para aplicações sensíveis à latência como jogos, streaming e renderização em tempo real.

### AWS Wavelength
Infraestrutura AWS embutida nas redes 5G das operadoras de telecomunicações. Permite executar aplicações com latência de milissegundo único diretamente na borda da rede móvel.

### AWS Outposts
Rack de hardware AWS instalado fisicamente no data center do cliente (on-premises). Oferece uma experiência de nuvem híbrida verdadeiramente consistente — mesmos serviços, APIs e ferramentas da AWS, mas rodando localmente.

### Zona Local Dedicada (Dedicated Local Zone)
Infraestrutura de nuvem criada especificamente para um cliente ou jurisdição, para atender a requisitos regulatórios e de soberania digital. Operada pela AWS, mas isolada e dedicada.

### CloudFront (CDN)
Rede de entrega de conteúdo (CDN) da AWS com mais de 750 Pontos de Presença (POPs) e 13 caches de borda regionais distribuídos globalmente. Distribui conteúdo com baixa latência para usuários finais.

---

## Benefícios da Infraestrutura Global

### 1. Segurança e Conformidade
- Infraestrutura projetada para atender aos requisitos de segurança mais rigorosos
- Conformidade com regulamentações locais e globais (GDPR, LGPD, HIPAA, etc.)
- Suporte a soberania digital com Zonas Locais Dedicadas

### 2. Alta Disponibilidade e Resiliência
- Mínimo de 3 AZs por região garante continuidade mesmo com falha de um data center inteiro
- Regiões isoladas entre si evitam propagação de falhas
- SLAs de disponibilidade acima de 99,99% para serviços críticos

### 3. Performance
- Backbone de fibra óptica proprietário de 9+ milhões de km
- Transferência de dados mais rápida entre regiões
- Latência reduzida com Zonas Locais e Wavelength
- CloudFront com 750+ POPs para entrega de conteúdo

### 4. Ampla Variedade de Ofertas
- Nuvem pública (Regiões + AZs)
- Borda (Local Zones, Wavelength)
- On-premises (Outposts)
- Dedicado (Dedicated Local Zones)
- CDN (CloudFront)

---

## Soberania Digital

A AWS oferece soluções para clientes que precisam manter controle total sobre seus dados dentro de fronteiras nacionais ou jurisdicionais:

- **Zonas Locais Dedicadas:** infraestrutura isolada e dedicada para atender requisitos regulatórios específicos de um país ou setor
- **AWS GovCloud:** regiões isoladas para workloads do governo dos EUA com requisitos de compliance como FedRAMP e ITAR
- **Residência de dados:** controles para garantir que dados nunca saiam de uma região específica

---

## Sustentabilidade

A AWS compromete-se com operações 100% com energia renovável e redução do impacto ambiental dos data centers, utilizando:
- Eficiência energética superior à média da indústria
- Parcerias com produtores de energia renovável globalmente
- Iniciativas de comunidade local nas regiões onde opera

---

## Rede Global da AWS

O backbone de rede privado da AWS conecta todas as regiões, AZs, POPs e data centers, trazendo:
- Menor latência vs. internet pública
- Maior segurança (tráfego não transita pela internet pública)
- Largura de banda consistente e previsível

---

## Tags

`aws` `infraestrutura-global` `regiões` `zonas-de-disponibilidade` `cloudfront` `outposts` `wavelength` `zonas-locais` `soberania-digital` `cloud` `alta-disponibilidade` `cdn`
