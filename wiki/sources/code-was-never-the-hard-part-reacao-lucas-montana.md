---
type: source
title: "Code Was Never the Hard Part — Reação ao Artigo (Lucas Montana)"
aliases: ["code was never the hard part", "reação lucas montana ia programação", "programar é fácil o difícil é decidir o que programar"]
date_created: 2026-08-27
date_updated: 2026-08-27
source_count: 0
tags: [tech-mentor-leadership, ia-e-programacao, identidade-profissional, abstracao, quality-gate, mercado-de-trabalho, dario-amodei, leetcode, burnout]
skill: tech-mentor-leadership
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/code-was-never-the-hard-part-reacao-lucas-montana.md
source_url:
author: Lucas Montana (canal de YouTube)
date_published:
date_ingested: 2026-08-27
---

# Code Was Never the Hard Part — Reação ao Artigo (Lucas Montana)

## TL;DR

Lucas Montana reage ao artigo em inglês "Code Was Never the Hard Part — It's an Insult to All Programmers", que argumenta que programar sempre foi a parte fácil e que descobrir o que construir/entender o cliente é o trabalho difícil. Montana concorda em parte, mas usa o artigo como fio condutor pra um argumento maior: a profissão já passou por transformações de abstração antes (assembly → C → bytecode/JVM), e o que a IA generativa adiciona é só mais uma camada — linguagem natural (inglês/português) como interface pra gerar código — não algo qualitativamente disruptivo, até que a IA comece a falar direto com o hardware. Contrapõe cada provocação do artigo (Clean Code é inútil? bootcamps não fazem sentido?) argumentando que esse conhecimento migrou de "escrever à mão" para "quality gates automatizados que revisam código gerado por IA". Fecha com observações de mercado (Dario Amodei errou a previsão de "6 meses sem código manual" por ~10-12 meses, não pela tese em si), burnout ligado a medição de produtividade via OKR, e defesa de que LeetCode/estruturas de dados continuam relevantes via a heurística dos "três níveis de profundidade".

## Key Claims

1. **Cada geração de linguagem já foi uma "perda de controle íntimo" sobre a máquina** — um engenheiro citado (nome não identificado no áudio original, ASR garbled) descreve a transição de 15 anos em assembly (conhecia cada bit, cada flag) para C: abandonar o conhecimento íntimo da máquina e confiar num compilador "caixa mágica" que traduz a intenção pra linguagem de máquina — inclusive tendo que escrever código pra verificar a qualidade do assembly gerado, porque compiladores da época eram pouco confiáveis.
2. **Java/Kotlin não são "a linguagem que fala com a máquina"** — Java vira bytecode, que roda numa JVM interpretada, que usa registradores por baixo; achar que a linguagem de alto nível é conhecimento suficiente sobre a máquina é ilusório. LLMs geradoras de código (a partir de prompt em inglês/português) são só mais uma camada em cima dessa mesma cadeia de abstração (linguagem natural → código-fonte → compilador/interpretador → bytecode/máquina virtual → linguagem de máquina).
3. **O limiar de preocupação do autor é a IA falar direto com o hardware** — enquanto GPT/Claude geram código-fonte (Python etc.) que ainda passa por compilador/interpretador convencional, a mudança não é disruptiva; seria disruptivo se a IA gerasse binário/linguagem de máquina diretamente, sem essa camada intermediária revisável.
4. **"Programar é fácil, o difícil é decidir o que programar" tem uma verdade parcial** — hoje quase qualquer pessoa consegue gerar código funcional via IA (leigos, "tua tia", "o padeiro"), mas isso revelou que nem todo mundo *quer* programar nem consegue pensar sistematicamente/decompor problemas — a barreira nunca foi só sintaxe.
5. **Clean Code não morreu — migrou de disciplina manual pra [[wiki/concepts/quality-gate|quality gate]] automatizado** — contra-argumento direto ao artigo: livros como Clean Code continuam relevantes porque seus princípios viram regras verificáveis estaticamente (SonarQube, microbenchmarks, análise determinística) que revisam código gerado por IA antes do merge — não é "IA revisando IA", é o dev escrevendo o gate que audita a IA.
6. **Identidade profissional e defesa de ego se ativam quando a ferramenta amada é criticada** — brincadeiras sobre Flutter/React Native/Xamarin geram reações de ofensa pessoal, não debate técnico, porque tempo investido em especialização se converte em identidade; questionar a ferramenta é lido como invalidar as horas/noites de dedicação — mecanismo análogo à [[wiki/concepts/falacia-do-custo-afundado|falácia do custo afundado]].
7. **Observação de mercado: em times de ponta, código manual praticamente desapareceu** — relatos de staff engineers/tech leads/sêniors em grandes empresas que não escrevem código manualmente há meses, times liberando milhares de dólares/dia de uso de IA, 20-25 PRs por semana, e revisão de código deixando de ser leitura humana linha a linha pra virar estrutura de verificação automatizada.
8. **A previsão do Dario Amodei ("6 meses sem código manual") errou o prazo, não a tese** — a previsão feita ~2 anos antes do vídeo (motivo de piada na época: "estamos a um mês de seis meses de não precisar mais escrever código") demorou cerca de 8-12 meses a mais que o anunciado para se concretizar; hipótese do autor: labs como a Anthropic já tinham acesso interno a modelos mais avançados (ex.: geração Opus 4.7/4.8) antes do público, o que explica o otimismo aparentemente exagerado da previsão original.
9. **Devs estão absorvendo trabalho de produto/gestão à medida que cargos de PM/EM são cortados** — layoffs em funções de produto e engineering management empurram a comunicação com design/produto e o alinhamento a OKRs pra cima de sêniors/tech leads, que viram squad leads fazendo esse trabalho além do técnico.
10. **Medição de produtividade via IA tende a intensificar trabalho, não just mostrar ganho de eficiência** — cruzar throughput de tickets (dobrado via IA) com OKRs de negócio é apontado como mecanismo real por trás do burnout observado, mais que "a IA aumentou minha produtividade" isoladamente.
11. **A heurística dos "três níveis de profundidade" continua justificando LeetCode/estruturas de dados** — usar `Map` em JavaScript exige saber (nível 1) que é uma abstração, (nível 2) que por baixo há uma hash table, e (nível 3) como essa hash table resolve colisão de hash — conhecimento que não é substituído por delegar a implementação a uma IA.

## Entidades Mencionadas

- [[wiki/entities/anthropic]] — previsão de Dario Amodei sobre fim do código escrito manualmente em ~6 meses, e hipótese de acesso antecipado a modelos mais avançados
- [[wiki/entities/leetcode]] — plataforma citada como ainda relevante pra prática de estruturas de dados/algoritmos, mesmo na era de geração de código por IA
- [[wiki/entities/uncle-bob|Uncle Bob (Robert C. Martin)]] — citado indiretamente via referência ao livro Clean Code como um dos "livros volumosos" mencionados pelo artigo original

## Conceitos Tocados

- [[wiki/concepts/abstracao]]
- [[wiki/concepts/compilador]]
- [[wiki/concepts/vibe-coding]]
- [[wiki/concepts/quality-gate]]
- [[wiki/concepts/engenheiro-vs-programador]]
- [[wiki/concepts/falacia-do-custo-afundado]]
- [[wiki/concepts/burnout-dev]]
- [[wiki/concepts/ciclo-de-mercado-tech]]
- [[wiki/concepts/hashmap]]
- [[wiki/concepts/hashing]]
- [[wiki/concepts/entrevista-tecnica-coding]]
- [[wiki/concepts/linguagem-natural-como-camada-de-abstracao]]

## Open Questions

- **Engenheiro citado no clipe de assembly→C não foi identificado com segurança** — nome ficou incompreensível no ASR original ("Anco Bob" ou similar); marcado como não identificado até confirmação por fonte primária. Se o usuário reconhecer a entrevista, vale corrigir e criar página de entidade própria.
- **"Karm" citado como possível exemplo de "estar no lugar certo na hora certa"** — nome também garbled no áudio (possivelmente uma referência que não chegou limpa no ASR); não foi possível identificar a quem se refere, então não foi promovido a entidade.
- Sem verificação independente da tese de que Anthropic já tinha acesso interno a "Opus 4.7/4.8" meses antes do público — tratado como especulação do autor, marcado como não verificado em [[wiki/entities/anthropic]].
- Fonte não cita o autor nem a publicação original do artigo em inglês, só o título — impossível linkar a fonte primária sem o texto completo.

## Raw Quotes

> "15 years, so I knew assembly language and I knew the machine, and I knew every bit in the machine. [...] going to C you have to give that up — this intimate knowledge of the machine you have to give up. You have to back away one little step and treat the language as if talking to some abstract machine."

> "Atualmente a gente ainda tá adicionando um nível de abstração em cima do que a gente já faz — isso não é disruptivo. Eu vou me preocupar quando a IA gerar direto linguagem de máquina ou gerar o binário."

> "Eu não tô nem falando aqui de IA revisando IA — tô falando de eu escrever um código que vai revisar o código da IA pra fazer isso. Pra isso tu precisa entender de Clean Code."

> "Tu ofendeu a minha pessoa — isso acontece porque tu investiu tantas horas se especializando naquilo, com dor e sofrimento, e quando alguém fala que o que tu gastou anos da tua vida fazendo não é bom suficiente, tu sente que tá te dizendo que todas aquelas horas e noites codando foram em vão."

> "O Dario errou ali por uns 8, 10, 12 meses — foi o que ele errou. Hoje ninguém mais tá escrevendo código manualmente."

> "Implementei algo com Map, tá — mas qual Map? Ah, lá por baixo tava usando uma hash table — tá, então o que é o hash da hash table, e como tu faz pra evitar colisão de hashes? Três níveis."
