---
type: source
title: "Golang Profissional: Por Que 'Código Fofo' Não Existe em Go"
aliases: ["código fofo no go tá perdido", "3 dicas realidade go profissional", "go não é pra código fofo"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 0
tags: [go, golang, standard-library, frameworks, filosofia-de-linguagem, generics, carreira]
skill: lang-systems
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/golang-profissional-sem-grandes-frameworks.md"
source_url: ""
author: "Lucas Badico"
date_published: ""
date_ingested: "2026-07-31"
---

## TL;DR

Lucas Badico ([[wiki/entities/lucas-badico]]), programando em Go profissionalmente há ~5 anos (últimos 3 meses full-time, sem cargo de liderança), argumenta que Go é hostil a quem busca "código fofo" — soluções prontas via grande framework. Três dicas: (1) não existe um framework dominante em Go (nenhum equivalente a Rails/Express) — a comunidade prefere repetir código a acoplar a uma grande lib; (2) ~80% das dependências de um projeto Go real vêm da standard library, o resto sendo pacotes pequenos e bem estabelecidos (gRPC, drivers de banco) — tudo o resto (auth, logging) é escrito à mão como aprendizado; (3) mesmo com generics disponíveis desde 1.18, a filosofia de "escrever bastante" continua enraizada — generics resolvem casos pequenos e específicos, não abstrações grandes e "inteligentes", porque a comunidade prefere repetição estável a abstração frágil. Fecha com chamada para o próprio curso de Go (25–29/11).

---

## Reivindicações Principais

**Claim:** Não existe um framework dominante para Go equivalente ao Rails (Ruby) ou Express (Node) — a comunidade opera por recomendações e boas práticas, não por um padrão definitivo, e empresas diferentes adotam combinações diferentes de ferramentas.
**Evidência:** Comparação direta com Rails/Express; observação pessoal do autor a partir de lives de construção de sistema próprio, sem framework central.
**Confiança:** Alta — consistente com [[wiki/concepts/go-ecossistema]], que já documenta Chi como "wrapper fino" (não framework completo) e a escolha explícita da comunidade Go por libs que estendem a stdlib em vez de substituí-la.

**Claim:** "É melhor repetir um pouco de código do que acoplar a uma grande biblioteca" — ditado da comunidade Go que orienta a filosofia geral de dependências da linguagem.
**Evidência:** Citação de ditado da comunidade, sem fonte formal citada; reforçada pela prática pessoal do autor.
**Confiança:** Média-alta — plausível e citado como ditado real e amplamente conhecido na comunidade Go, mas apresentado sem link ou atribuição de origem.

**Claim:** ~80% das dependências de um projeto Go profissional vêm da standard library; os ~20% restantes de fora dela tendem a ser pacotes pequenos e bem estabelecidos (ex.: gRPC, drivers de banco de dados) — código de autenticação, logging etc. é escrito à mão em vez de importado.
**Evidência:** Observação pessoal/percentual estimado pelo autor a partir da própria experiência profissional, sem estudo ou survey citado.
**Confiança:** Média — número específico (80%) é estimativa anedótica, não dado verificado, mas a direção geral é altamente consistente com [[wiki/concepts/go-stdlib]] e [[wiki/concepts/go-ecossistema]] (stdlib como base, ecossistema como complemento pontual).

**Claim:** O pacote `net/http` (com o multiplexer nativo desde Go 1.22) eliminou a necessidade da maioria dos pacotes de "HTTP server" de terceiros que existiam antes — reduzindo a dependência de algo equivalente a Express.
**Evidência:** Argumento técnico direto sobre a evolução da stdlib; alinhado ao histórico real de `http.ServeMux` ganhar roteamento por método/path em Go 1.22.
**Confiança:** Alta — verificável e coerente com [[wiki/concepts/go-stdlib]], que já documenta o exemplo de `http.NewServeMux()` com `r.PathValue("id")` (Go 1.22+) como capaz de cobrir APIs simples sem framework.

**Claim:** Mesmo com generics disponíveis (desde Go 1.18), a filosofia de "escrever bastante em vez de abstrair" permanece dominante na comunidade — generics são usados para casos pequenos e pontuais (trocar tipo em uma peça isolada), não para abstrações grandes e "inteligentes" como um mapper genérico universal; handlers repetitivos são considerados normais e até preferíveis, porque uma abstração genérica "quebra tudo" se algo mudar.
**Evidência:** Exemplo do próprio autor (handlers repetitivos no seu projeto); argumento de estabilidade (abstração genérica grande como ponto único de falha).
**Confiança:** Média-alta — o argumento de risco de acoplamento é coerente com a filosofia geral de Go documentada em [[wiki/concepts/go-fundamentos]] (pragmatismo > expressividade), mas a afirmação de que isso é consenso da comunidade, e não só preferência pessoal do autor, não é sustentada por dado externo.

**Claim:** A remoção da "engenharia" excessiva da programação (via ausência de frameworks e abstrações mágicas) torna a programação de grandes sistemas em Go mais simples e "divertida" — sem nada mágico ou escondido, cada hora codando é aprendizado real, o que atrai quem quer previsibilidade e afasta quem busca algo "mágico" (ex.: Elixir, Ruby on Rails, Laravel).
**Evidência:** Argumento normativo/experiencial do autor, sem estudo citado, mas alinhado à sua trajetória pessoal (5 anos de Go profissional, atualmente full-time codando).
**Confiança:** Média — opinião de carreira bem fundamentada na experiência do autor, mas não um dado objetivo; vale como reforço qualitativo de [[wiki/concepts/go-fundamentos]] (pragmatismo de Go vs. expressividade de outras linguagens).

---

## Entidades

- [[wiki/entities/lucas-badico]] — autor; `source_count` atualizado

## Conceitos

- [[wiki/concepts/go-stdlib]]
- [[wiki/concepts/go-ecossistema]]
- [[wiki/concepts/go-fundamentos]]
- [[wiki/concepts/go-avancado]] (generics)
- [[wiki/concepts/cargo-cult-tecnologico]]

## Questões em Aberto

- O número "80% das dependências vêm da stdlib" é estimativa pessoal do autor, sem survey ou medição de projeto real citados — tratar como ordem de grandeza plausível, não dado verificado.
- O vídeo trata a preferência por repetição em vez de generics como consenso da comunidade Go, mas não cita nenhuma fonte externa (RFC, blog oficial do Go team, survey) que confirme isso como posição institucional — é a leitura pessoal do autor sobre a cultura da comunidade.
- Vídeo é majoritariamente promocional (chamada recorrente para curso próprio de Go, 25–29/11) — as afirmações técnicas centrais (stdlib, ausência de framework, generics) são, porém, independentes do CTA e verificáveis contra o próprio ecossistema Go.

## Contradições com a Wiki

Nenhuma contradição — a fonte reforça e adiciona textura qualitativa (percepção de "código fofo" vs. realidade profissional, ditado da comunidade sobre repetição vs. acoplamento) a claims já documentadas em [[wiki/concepts/go-stdlib]] e [[wiki/concepts/go-ecossistema]] a partir de [[wiki/sources/go-stdlib]] e [[wiki/sources/go-ecossistema]]. Converge também com a filosofia de pragmatismo de [[wiki/concepts/go-fundamentos]] (a partir de [[wiki/entities/lucas-badico]] já citado ali), sem introduzir tensão.

## Citações Preservadas

> "A real é que código fofo no Go tá perdido."

> "Não existe um grande framework para Golang. A verdade é que Go desestimula grandes frameworks. Existe um ditado que diz que é melhor repetir um pouquinho de código do que acoplar a uma grande biblioteca."

> "80% das suas dependências vão ser a standard library."

> "Não tem um framework na standard library. Não existe um framework — existem várias ferramentas, pedaços do que o seu sistema precisa, que você vai juntar."

> "A gente prefere escrever do que ter algo genérico muito inteligente que pode quebrar se algo mudar — quebra tudo."

> "Você não vai ter nada mágico com Go. [...] É muita repetição, e isso é algo muito bom: faz com que a sua carreira seja tranquila se você se dedicar."
