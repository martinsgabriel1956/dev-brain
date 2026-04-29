---
date: 2026-04-23
tags: [tech-mentor, mobile, publicacao, aso, app-store, play-store, screenshots, reviews]
skill: tech-mentor-mobile/references/publicacao
level: arquiteto
---

# Publicação e ASO — Estratégia de Lançamento, A/B Testing, Gestão de Reviews

## Contexto
ASO (App Store Optimization) é o SEO do mundo mobile. Um app tecnicamente excelente com ASO ruim pode ter download rate 10x menor que um app mediano bem otimizado. A lógica é a mesma de qualquer canal de aquisição: impressão → clique → install → retenção. Cada etapa tem alavancas específicas.

## Como Funciona

### Funil de conversão na store

```
Impressão (usuário vê o app nos resultados/explorar)
  ↓ CTR (click-through rate) — impactado por: ícone, nome, rating
Página do produto (usuário vê os detalhes)
  ↓ CVR (conversion rate) — impactado por: screenshots, descrição, reviews
Install
  ↓ Retenção D1/D7/D30 — impactado pelo produto em si
```

### Otimização de elementos de ASO

**Ícone:**
- Sem texto (fica ilegível em tamanhos pequenos)
- Contraste alto — visível em fundos brancos e escuros
- Símbolo reconhecível, não composto
- Teste A/B antes de fixar — ícone impacta CTR diretamente

**Nome do app (App Store: 30 chars, Play Store: 50 chars):**
```
Padrão: [Nome da Marca] - [Benefício principal]
Exemplo: "Jobber: Gestão para Serviços" (não "Jobber Pro")

Inclua: keyword principal no nome se relevante
Evite: palavras genéricas sem diferenciação
```

**Subtítulo (App Store) / Short description (Play Store):**
```
App Store: 30 chars
Play Store: 80 chars
→ Segunda oportunidade de incluir keywords relevantes
→ Foco no benefício, não na feature
```

**Keywords (App Store — 100 chars):**
```
- Separados por vírgula, sem espaço
- Não repetir palavras que já estão no nome/subtítulo
- Incluir variações ortográficas, sinônimos
- Focar em keywords com volume médio-alto e concorrência baixa

Ferramentas: AppFollow, Sensor Tower, AppTweak
```

**Descrição:**
```
Primeiras 3 linhas: mais importantes (antes do "Ver mais")
→ Benefício principal + prova social + call to action

Estrutura:
1. Hook (dor do usuário ou benefício)
2. Features principais em bullets (3-5)
3. Prova social ("Usado por 500k empresas no Brasil")
4. Call to action sutil
```

### Screenshots — maior impacto na CVR

```
Orientação: screenshots em portrait convertem melhor para maioria dos apps
             landscape para jogos e apps de vídeo

Primeiro screenshot: mais importante — deve comunicar o valor em < 2s

Padrão efetivo:
1. Tela principal do app + headline do benefício
2. Feature mais diferencial + headline
3. Feature de social proof / comunidade
4. Feature de personalização
5. Call to action sutil ("Comece grátis")

Boas práticas:
- Texto mínimo, grande, legível em thumbnail
- Consistência visual (same design system)
- Mostrar a UI real, não mock inventado
- Testar com usuários reais antes de publicar (5-second test)
```

### A/B Testing de assets na store

**App Store Connect — Product Page Optimization:**
```
Testar: ícone, screenshots, vídeo de preview
Alocação: até 90% da audiência para variantes, 10% para controle
Duração: mínimo 7 dias (90 dias de validade)
Métrica: install conversion rate
```

**Google Play Console — Store listing experiments:**
```
Testar: ícone, screenshots (curtos e longos), feature graphic
Alocação: 50/50 recomendado
Duração: mínimo 7 dias para significância estatística
```

```typescript
// Integração com analytics para correlacionar store variant com comportamento pós-install
// Após install, o variant da store fica acessível via SKAdNetwork (iOS) ou Google Play (Android)

// iOS — verificar variante da campanha
import StoreKit

func getStoreVariant() async -> String? {
  // Disponível via SKAdNetwork 4.0+
  return nil // implementar conforme documentação da Apple
}

// Google Play — obter referral
// Via referrer broadcast ou Google Play Install Referrer API
```

### Gestão de Reviews — estratégia

```
Pedir review no momento certo:
✓ Após completar ação de valor (primeiro pedido entregue, primeiro workout concluído)
✓ Após interação positiva (usuário usou feature premium pela 3a vez)
✓ D3-D7 após install (engajamento confirmado)

Não pedir review:
✗ Na abertura do app
✗ Após erro ou loading lento
✗ Durante onboarding
✗ Mais de 3x por ano (iOS limita a SKStoreReviewRequest.requestReview a 3x/365 dias)
```

```swift
// iOS — solicitar review no momento certo
import StoreKit

func requestReviewIfAppropriate() {
  guard shouldShowReviewPrompt() else { return }

  if let scene = UIApplication.shared.connectedScenes.first as? UIWindowScene {
    SKStoreReviewController.requestReview(in: scene)
    markReviewRequested()
  }
}

func shouldShowReviewPrompt() -> Bool {
  let installDate = UserDefaults.standard.object(forKey: "install_date") as? Date ?? Date()
  let daysSinceInstall = Calendar.current.dateComponents([.day], from: installDate, to: Date()).day ?? 0
  let completedActions = UserDefaults.standard.integer(forKey: "completed_actions_count")
  let lastReviewRequest = UserDefaults.standard.object(forKey: "last_review_request") as? Date

  // Condições: D3+, 3+ ações completadas, não pediu nos últimos 90 dias
  return daysSinceInstall >= 3
    && completedActions >= 3
    && (lastReviewRequest == nil || Calendar.current.dateComponents([.day], from: lastReviewRequest!, to: Date()).day ?? 0 >= 90)
}
```

```kotlin
// Android — In-App Review API
class ReviewManager(private val activity: Activity) {
  private val manager = ReviewManagerFactory.create(activity)

  fun requestReviewIfAppropriate() {
    if (!shouldShowReview()) return

    manager.requestReviewFlow().addOnCompleteListener { request ->
      if (request.isSuccessful) {
        manager.launchReviewFlow(activity, request.result).addOnCompleteListener {
          markReviewRequested()
        }
      }
    }
  }
}
```

**Responder reviews negativos:**
```
Fórmula: Agradecer → Reconhecer problema → Solução ou caminho → Contato direto

Exemplo:
"Olá [Nome], obrigado pelo feedback! Entendemos sua frustração com [problema].
Lançamos a correção na versão 2.3.1 — atualize e o problema estará resolvido.
Se o problema persistir, entre em contato direto pelo suporte@yourapp.com.
Agradecemos sua paciência!"
```

### Estratégia de lançamento

```
Soft launch (4-6 semanas antes do launch global):
→ Publicar em 2-3 países menores (similar ao target mas sem saturar o mercado)
→ Objetivos: estabilidade, ASO inicial, early reviews
→ Markets sugeridos: Portugal (iOS), Canadá (EN), Austrália (EN)

Launch day:
→ Assets de store finalizados e testados
→ Press kit pronto (screenshots, vídeo, press release)
→ Email list / comunidade notificada com link de download
→ ProductHunt, blogs do nicho, influenciadores do segmento
→ Monitorar crash rate nas primeiras 4h

Pós-launch:
→ Responder todos os reviews das primeiras 2 semanas
→ Monitorar ASO metrics semanalmente (install rate, keyword rankings)
→ A/B test de screenshots no mês 2
→ Push para press/blogs no mês 3 (já tem reviews orgânicos para mostrar)
```

## Trade-offs

| Elemento | Impacto no CTR | Impacto no CVR | Esforço de otimização |
|---|---|---|---|
| Ícone | Alto | Médio | Médio |
| Screenshots | Baixo | Muito alto | Alto |
| Rating/reviews | Alto | Alto | Contínuo |
| Nome/keywords | Alto (ranking) | Baixo | Baixo |
| Vídeo de preview | Baixo | Alto (quando bem feito) | Alto |

## Quando Usar / Quando Evitar

**Invista em screenshots antes do lançamento** — é o elemento com maior impacto no CVR e o mais ignorado por devs.

**Soft launch sempre** — descobrir crash em 100% dos usuários vs 5% de um país menor é a diferença entre uma crise e um hotfix silencioso.

**Não peça reviews antes de D3** — usuários que não ativaram o app darão 1 estrela.

**Responda TODOS os reviews negativos** — 80% dos usuários leem as respostas antes de instalar.

## Conceitos Relacionados
[[mobile-cicd]] · [[mobile-feature-flags]] · [[mobile-monitoramento]] · [[mobile-monetizacao]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
