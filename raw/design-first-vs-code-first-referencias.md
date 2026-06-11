# Design First vs Code First — Abordagens e Referências de Design para Devs

> **Fonte:** Transcrição de vídeo — Canal Rocket City (Eduarda)  
> **Domínio:** Frontend, Design Engineering, UX

---

## 1. As Duas Abordagens

### Code First

Começar pelo código usando bibliotecas de componentes pré-estilizados sem criar um layout antes.

**Exemplos de ferramentas:** Shadcn/UI, Radix UI, Vercel AI Elements, Cos Hey UI.

**Vantagens:**
- Velocidade de desenvolvimento
- Não exige criatividade de design

**Problemas:**
- Componentes são isolados e não têm contexto da aplicação
- Sem visão de design, o resultado tende a ser um "Frankenstein" — partes que não conversam entre si
- Funciona bem apenas quando a aplicação é muito semelhante a outras existentes que serviram de referência

---

### Design First

Criar o layout completo antes de escrever código. Abordagem padrão em grandes empresas.

**Ferramenta principal:** Figma

**Vantagens:**
- Maior padronização
- Visão coesa da aplicação antes da implementação

**Problemas:**
- Em times pequenos (1-3 pessoas que fazem design e código), o Figma fica rapidamente desatualizado à medida que o código evolui
- Funciona bem quando há **separação clara** entre designers e desenvolvedores frontend

---

### O Design Engineer — O Cargo do Meio

Quando a mesma pessoa (ou pequeno time) faz design e código, surge o papel do **Design Engineer**: profissional com conhecimentos de design que aplica esses conhecimentos diretamente no código.

- As experimentações de layout acontecem no código, não no Figma
- O Figma vira ferramenta de testes e referência, não a fonte da verdade
- Outras ferramentas usadas: Hive (animações), entre outras

> É o cargo "queridinho" do Vale do Silício no momento — uma resposta prática ao problema de manter Figma e código sincronizados.

---

## 2. O Que Realmente é Design

Design não é só criar layouts bonitos. Design é:

- **Usabilidade** — o quão fácil e prazerosa é a interação
- **Onboarding** — a primeira impressão do usuário
- **Animações e micro-interações** — o que diferencia um produto "gostoso" de usar
- **Conhecer o público** — criar algo direcionado a quem vai usar

**Exemplo concreto — Fake Delay:**

```
Problema: ação executa em 50ms, muito rápido para o usuário perceber feedback
Solução:  aplicar delay mínimo de 300ms antes de mostrar o spinner

const MIN_DELAY = 300
await Promise.all([fetchData(), sleep(MIN_DELAY)])
```

O usuário não percebe a diferença entre 50ms e 300ms, mas percebe a ausência do feedback visual. O delay artificial cria uma sensação mais prazerosa de interação — isso é design.

> Design se manifesta no momento da interação, não na primeira visualização.

---

## 3. Referências para Seguir (X / Twitter)

### RA — Staff Design Engineer na Vercel
- Tem um site ("Craft") com mini-experimentações de design + usabilidade implementadas em código
- Mostra o detalhismo, as animações e o cuidado de implementação que definem o nível de Design Engineer

### Stephen — Founder da Paper
- **Paper**: ferramenta nova que se propõe a ser um Figma focado em Design Engineers e devs — permite ver e modificar componentes reais da aplicação diretamente no editor (o que o Dreamweaver tentou fazer nos anos 2000, com abordagem moderna)
- Posta bastante sobre design e experimentações

### Pedro Duarte — Co-fundador da Radix UI / Stitches
- Brasileiro
- Radix e Stitches foram adquiridos pela WorkOS; hoje trabalha na Raycast
- Posta sobre design com foco em usabilidade e experiência, não só estética
- Entrevistado no canal Rocket City (2019)

### Paul McGregor — Designer no Linear
- Participou da concepção do Linear
- **Linear** é referência obrigatória de design para frontend: aplicação rápida, acessível, com design de altíssima qualidade
- Referência em "por que clicar num botão aqui é mais prazeroso do que em outros lugares"

### Dev no Architect (21 anos) — Referência Técnica
- Traz conteúdo mais técnico sobre UX e micro-interações
- Conhecido pelo post sobre **fake delays** — técnica de aplicar delay mínimo (300ms) em interações para garantir feedback visual adequado

### Gavin — Designer na OpenAI
- Um dos principais designers nos produtos da OpenAI
- Abordagem mais "purista" de design, menos focada em web especificamente
- Relevante para quem quer aprofundar além de UI/UX web

### Ned — Founder do Lovable
- Lovable: principal ferramenta para pessoas não técnicas construírem produtos técnicos em 2025/2026
- O sucesso do Lovable não é só tecnologia — é resultado de muito trabalho de design para tornar o produto acessível ao público não técnico
- Exemplo de que design é sobre conhecer e servir o seu público

---

## 4. Ferramentas de Referência Visual

### Dribbble
- Principal fonte de referências visuais de design para o autor
- Uso prático: pesquisar pelo componente que está sendo construído (ex: "table design") e filtrar por "web"
- Não para copiar, mas para capturar referências e direções visuais

---

## 5. Resumo das Abordagens

| | Code First | Design First | Design Engineer |
|---|---|---|---|
| Ponto de partida | Componentes pré-prontos | Layout no Figma | Código direto |
| Velocidade inicial | Alta | Média | Alta |
| Risco principal | Frankenstein visual | Figma desatualizado | Requer conhecimento de design |
| Melhor contexto | Protótipos rápidos | Times grandes com designers dedicados | Times pequenos / solo devs |
| Ferramenta principal | Shadcn, Radix, etc | Figma | Código + Figma como referência |

---

## 6. A Regra de Ouro

Estudar design apenas pela prática (combinação de cores, espaçamentos) pode levar a criar coisas bonitas, mas sem utilidade real. O passo fundamental é **entender o público** — design sem audiência definida é decoração.
