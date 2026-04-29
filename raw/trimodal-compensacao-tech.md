# A Natureza Trimodal da Compensação em Tech — Revisitada

> Artigo original: [The Trimodal Nature of Tech Compensation Revisited](https://newsletter.pragmaticengineer.com/p/trimodal-nature-of-tech-compensation)
> Autor: Gergely Orosz (The Pragmatic Engineer) | Publicado: julho 2024
> Parte 2 de uma série de 3 artigos sobre compensação trimodal em tech.

---

## A Pergunta Central

Por que a mesma posição pode oferecer **2 a 4x mais compensação** no mesmo mercado?

A resposta está no modelo trimodal: o mercado de tech não tem uma distribuição salarial uniforme — tem **três distribuições distintas**, cada uma com seu próprio centro de gravidade.

---

## O Modelo Trimodal

### Origem

Em 2021, Gergely Orosz estava pesquisando a diferença entre os salários reportados em sites de benchmark (Payscale, Honeypot, etc.) e o que a Uber oferecia para engenheiros em Amsterdã. Os números não batiam — havia um gap invisível.

Ao plotar os dados, o gráfico tinha **três picos locais** — não uma curva normal. Isso indicava três distribuições separadas, não uma única.

### Os Três Tiers

| Tier | Tipo de Empresa | Benchmark |
|---|---|---|
| **Tier 1** | Empresas locais tradicionais | Salários de sites públicos (Payscale, Glassdoor) — próximo a salários de posições governamentais |
| **Tier 2** | Startups e scaleups ambiciosas | Acima do mercado local — querem contratar e reter os melhores talentos locais |
| **Tier 3** | Big Tech, hedge funds, scaleups que competem globalmente | Benchmark regional/global — competem com outras Big Techs por talento |

### Por que Sites de Salário Mostram Números Errados

Três razões pelas quais benchmarks públicos subestimam a compensação real de Tier 3:

1. **Volume baixo:** pacotes Tier 3 são minoria — ficam fora da mediana, média e até do percentil 75
2. **Sem incentivo para compartilhar:** quem ganha muito sabe que está acima da mediana e não compartilha
3. **Equity não é capturado:** a maioria dos sites não coleta dados de equity — que é geralmente o maior diferencial de compensação de Tier 3

**Equity é o segredo.** Muitos outliers de compensação muito alta são pessoas que receberam um grant que apreciou 5–10x desde a emissão.

### Fontes Confiáveis para Dados de Tier 3

- **[Levels.fyi](https://www.levels.fyi)** — cobre praticamente todas as Tier 3 nos EUA
- **[The European Engineer](https://www.theeuropeanengineer.com)** — top tier companies por cidade europeia
- **[Blind](https://www.teamblind.com)** — rede social anônima onde usuários compartilham TC (total compensation)
- **Reddit** (r/ExperiencedDevs, r/cscareerquestions)

---

## Aplicabilidade Global

O modelo foi originalmente desenvolvido para a Holanda, mas se mostrou válido internacionalmente — só os números mudam, a estrutura trimodal se mantém.

**Por que a Holanda foi um bom laboratório:**
- Big Tech americana crescendo: Amazon AWS, Google Cloud, Meta, Uber
- Empresas VC-funded internacionais contratando localmente: Databricks, Stripe, Personio, Linear
- Hedge funds: Optiver, Flow Traders, IMC Trading
- Empresas locais VC-funded: Mollie, Adyen, Messagebird
- Maioria dos devs ainda contratados por empresas "locais" (Tier 1)

**Confirmações internacionais:**

> "O modelo trimodal se aplica aos EUA também. É o que tenho visto na minha experiência e em conversas com ICs e managers nos três tipos de empresa." — VP de Engenharia, Rick Luevanos

> "Ignore os números absolutos se não estiver na Europa. As tendências são as mesmas nos EUA." — Engenheiro de software, Reddit

---

## Validação com Dados (2024)

Orosz analisou mais de **1.000 data points**, tagueou manualmente o tier de cada empresa, e plotou a distribuição. O resultado confirmou a premissa trimodal — três agrupamentos claros e distintos.

**Distribuição de posições por tier:**
- Tier 1 tem a **maioria** das posições
- Tier 2 tem posições significativas, mas menos que Tier 1
- Tier 3 tem a **menor quantidade** de posições absolutas

---

## Números de Compensação (Holanda, referência)

Dados ilustrativos para entender a escala das diferenças entre tiers. Os valores específicos variam por ano e mercado, mas a **proporção** entre tiers é o que importa:

| Nível | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Mid-level | Base baixa, sem equity | Base média, equity pequeno | Base alta + equity significativo |
| Senior | ~mercado local | 1,5–2x Tier 1 | 2–4x Tier 1 |
| Staff+ | Raro | Existe, equity relevante | Comum, equity majoritário |
| EM | Próximo de IC senior | Acima de IC senior | Muito acima, bônus + equity |
| Exec | Raro, baixo | Existe | Alto, equity é componente dominante |

---

## Empresas por Tier

### Tier 3 (top-paying)
- **Big Tech:** Google, Meta, Amazon, Apple, Microsoft, Netflix
- **Hedge funds e HFT:** Jane Street, Two Sigma, Citadel, DE Shaw, Optiver, IMC Trading
- **Scaleups de destaque:** Stripe, Databricks, alguns unicórnios VC-funded

### Tier 2 (mid-paying)
- Startups e scaleups VC-funded (maioria)
- Empresas full-remote (tendência)
- Empresas bootstrapped ambiciosas

### Tier 1 (local baseline)
- Maioria das empresas tradicionais
- Empresas sem pressão de competição global por talento
- Compensação próxima de benchmarks de sites públicos

---

## Realidades de Tier 2 e Tier 3

Tier 2 e Tier 3 não diferem muito em **expectativas, cultura e nível de exigência**. A diferença principal é a compensação — especialmente a composição:

- **Tier 1:** salário base, talvez bônus pequeno, sem equity
- **Tier 2:** salário base acima do mercado, bônus, equity em startups
- **Tier 3:** salário base alto, bônus relevante, RSUs/equity com vesting — equity é o maior componente

**Implicação prática:** passar de Tier 1 para Tier 2 ou 3 não necessariamente significa trabalhar mais ou em condições piores. Significa estar numa empresa que compete globalmente por talento.

---

## Por que o Modelo Importa para a Carreira

1. **Salary sites mentem por omissão** — reportam a mediana do Tier 1, mas essa não é a realidade do mercado todo

2. **A decisão de empresa importa mais que a de cargo** — um Sênior em Tier 3 ganha mais que um Staff em Tier 1

3. **Equity é o diferencial invisível** — quem não entende equity subestima sistematicamente a compensação de Tier 3

4. **O modelo é global** — com ajuste de números, a estrutura trimodal se aplica a EUA, Canadá, Reino Unido, Europa e além

5. **Tier 3 não é inacessível** — exige preparação e esforço, mas não é reservado a um grupo fechado

---

## Fontes e Série Completa

- **Parte 1 (2021):** [The trimodal nature of software engineering salaries in the Netherlands and Europe](https://blog.pragmaticengineer.com/software-engineering-salaries-in-the-netherlands-and-europe/)
- **Parte 2 (2024):** [The trimodal nature of tech compensation revisited](https://newsletter.pragmaticengineer.com/p/trimodal-nature-of-tech-compensation) ← este artigo
- **Parte 3 (2025):** [The trimodal nature of tech compensation in the US, UK and India](https://newsletter.pragmaticengineer.com/p/trimodal)
