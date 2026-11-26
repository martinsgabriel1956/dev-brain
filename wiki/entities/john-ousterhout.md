---
type: entity
title: "John Ousterhout"
aliases: ["ousterhout", "philosophy of software design"]
date_created: 2026-07-09
date_updated: 2026-11-26
source_count: 11
tags: [autor, complexidade, arquitetura, deep-modules, professor]
skill: tech-mentor-backend
status: draft
---

## Quem É

Professor de ciência da computação em Stanford, criador da linguagem Tcl, e autor de *A Philosophy of Software Design* (2018) — livro que define complexidade de software e propõe módulos profundos como estratégia central de design.

## Contribuições relevantes para o wiki

**Definição de complexidade:** "qualquer coisa relacionada à estrutura de um sistema de software que dificulta entender e modificar o sistema". Uma base de código ruim, por essa definição, é simplesmente uma base de código difícil de mudar sem causar bugs.

**Módulos profundos (deep modules) vs. módulos rasos (shallow modules):** módulos profundos escondem muita funcionalidade atrás de uma interface simples — a complexidade fica encapsulada, o consumidor não precisa (mas pode) olhar por dentro. Módulos rasos expõem pouca funcionalidade atrás de uma interface relativamente complexa — multiplicam o número de peças que quem lê o código precisa rastrear. Ver [[wiki/concepts/modulo-profundo]].

## Relevância na era da IA

Citado em [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] como base teórica para dois problemas de agentes de IA: (1) LLMs tendem a produzir código com módulos rasos por padrão, o que dificulta a própria IA explorar e entender a base de código depois; (2) módulos profundos permitem tratar a implementação como "caixa cinza" — o humano projeta e revisa a interface, delega a implementação à IA, sem precisar acompanhar cada linha.

## Do capítulo introdutório (fonte primária)

[[wiki/sources/filosofia-do-design-de-software-introducao]] é a primeira citação de primeira mão do próprio livro no wiki (as anteriores vinham de uma palestra de Matt Pocock citando o autor). Nela, Ousterhout enquadra as duas estratégias gerais contra complexidade — eliminar (código mais simples e óbvio) e encapsular ([[wiki/concepts/modulo-profundo|design modular]]) — e argumenta que design de software é processo contínuo, nunca uma fase única: ver [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]]. Também introduz o método de trabalho do livro inteiro: reconhecer [[wiki/concepts/red-flags-de-design]] via [[wiki/concepts/code-review]], já que é mais fácil ver problemas de design no código de outra pessoa do que no próprio.

## Livro completo (2026-07-29)

[[wiki/sources/filosofia-do-design-de-software-livro-completo]] cobre os 22 capítulos do livro. Além dos temas já registrados acima, o autor discorda explicitamente de Robert Martin (*Clean Code*) em três pontos nomeados — tamanho de método vs. profundidade ([[wiki/concepts/red-flags-de-design]]), motivo dos comentários existirem ([[wiki/concepts/comentarios-como-ferramenta-de-design]]) — e do guia de estilo de nomenclatura do Go ([[wiki/concepts/naming]]). Também formula, com vocabulário próprio, a distinção entre [[wiki/concepts/tech-debt-como-ferramenta|programação tática e estratégica]] (Cap. 3) e o conceito de [[wiki/concepts/ocultamento-de-informacao|ocultamento de informação]] de David Parnas (Cap. 5), central para módulos profundos.

## Debate Histórico com Uncle Bob, e o Primeiro Dado Empírico

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] recupera o debate público — travado por anos, sem acordo — entre Ousterhout e [[wiki/entities/uncle-bob]] sobre função pequena (*Clean Code*) vs. módulo profundo. A fonte argumenta que, com agentes de IA como novo "leitor" mensurável, esse debate ganha pela primeira vez um jeito de ser medido empiricamente. Num estudo controlado citado (sem nome/link, tratar como direcional): quebrar métodos e classes densos em helpers menores, isoladamente, deu **empate** — a explicação apontada foi que extração de código redistribui complexidade em vez de eliminá-la, reforçando o argumento central de Ousterhout de que módulo profundo, não tamanho de função, é o que importa. Ver [[wiki/concepts/modulo-profundo]] e [[wiki/concepts/codigo-grepavel]] para a exceção onde a quebra em funções menores ajudou (por buscabilidade, não por profundidade).

## Discutido em Bate-Papo entre Praticantes (Não é Fonte Primária do Livro)

[[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] é a primeira fonte no wiki que discute o livro *de segunda mão* — dois engenheiros experientes ([[wiki/entities/otavio-santana]] e [[wiki/entities/mauricio-linhares]]) comentando os conceitos a partir de experiência própria, não citando o texto diretamente. Traz vocabulário do Cap. 2 (change amplification, cognitive load, unknown unknowns) ainda não nomeado nas duas ingestões anteriores do livro — ver [[wiki/concepts/sintomas-de-complexidade-ousterhout]] — e exemplos adicionais de má/boa API (Java I/O, cliente HTTP do Go, `file_get_contents` do PHP) complementares aos já registrados em [[wiki/concepts/modulo-profundo]].

## Catálogo aberto por convite do autor

Na seção 1.1 (na versão completa em [[wiki/sources/filosofia-do-design-de-software-cap-01-traducao-revisada]]), Ousterhout pede ao leitor que lhe envie bons exemplos de código e os sinais de alerta que descobrir ("eu adoraria ouvir sobre eles"). Ele trata o próprio catálogo de [[wiki/concepts/red-flags-de-design]] como incompleto e aberto a contribuições, de acordo com o tom de "peça de opinião" que ele mesmo dá ao livro.

## Capítulo 2 em primeira mão (2026-11-25)

[[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]] traz o texto do cap. 2, que até então a wiki só conhecia pelo podcast e por uma citação do livro completo. Ali Ousterhout define complexidade como algo relativo à tarefa ("o que um desenvolvedor vivencia em um determinado momento"), pesa cada parte pelo tempo gasto nela ($C = \sum_p c_p t_p$), nomeia os três [[wiki/concepts/sintomas-de-complexidade-ousterhout|sintomas]] e as duas [[wiki/concepts/causas-de-complexidade-ousterhout|causas]], e defende "tolerância zero" porque a [[wiki/concepts/complexidade-incremental|complexidade é incremental]]. O texto também corrige a leitura do podcast: amplificação de mudanças não exige dependência oculta.

## Capítulo 3 em primeira mão (2026-11-25)

[[wiki/sources/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente]] traz o texto do cap. 3: [[wiki/concepts/programacao-tatica-vs-estrategica]], o [[wiki/concepts/tornado-tatico]], a régua de 10 a 20% e o payback de 6 a 18 meses, que ele marca como opinião sem dados. Corrige um registro antigo da wiki: ele não cunha "dívida técnica", só usa o termo.

## Capítulo 4 em primeira mão (2026-11-25)

[[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] traz o texto do cap. 4. Ousterhout define módulo como qualquer unidade com interface e implementação, inclusive um método, e divide a interface em parte formal e informal ([[wiki/concepts/interface-formal-e-informal]]). Chama de falsa abstração a que omite um detalhe importante ([[wiki/concepts/abstracao]]), mede [[wiki/concepts/modulo-profundo|profundidade]] como custo (interface) contra benefício (funcionalidade) e cunha "classitis" para o excesso de classes pequenas ([[wiki/concepts/classite]]). Os exemplos são a E/S do Unix e o coletor de lixo (profundos), a lista encadeada e um método de uma linha (rasos) e o I/O do Java (classite).

## Capítulo 5 em primeira mão (2026-11-25)

[[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]] traz o texto do cap. 5: [[wiki/concepts/ocultamento-de-informacao]] a partir do artigo de [[wiki/entities/david-parnas]] (1972), vazamento pela interface e pela porta dos fundos, [[wiki/concepts/decomposicao-temporal]] e os exemplos do servidor HTTP dos alunos. Corrige dois registros da wiki: decomposição temporal é "uma causa comum" de vazamento, não "a mais comum", e o livro recomenda fundir as classes de leitura e análise, sem dizer que a equipe fundiu.

## Capítulo 6 em primeira mão (2026-11-26)

[[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]] traz o texto do cap. 6. Ousterhout conta que começou preferindo o uso específico e mudou de ideia revisando projetos de alunos; hoje acha que a superespecialização "talvez seja a maior causa isolada de complexidade". Propõe módulos um tanto de uso geral ([[wiki/concepts/modulo-de-proposito-geral]]), com a classe de texto do editor e a classe `History` de desfazer como exemplos, e [[wiki/concepts/eliminar-casos-especiais]] com a seleção vazia. Corrige um registro da wiki: a classe geral precisa de `findNext` para busca e substituição, não serve "sem alteração".

## Key Sources

- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — debate histórico com Uncle Bob e primeiro estudo controlado medindo função pequena vs. módulo profundo
- [[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] — discussão de segunda mão do livro por dois praticantes, com vocabulário do Cap. 2 e exemplos adicionais de API
- [[wiki/sources/filosofia-do-design-de-software-cap-01-traducao-revisada]] — segunda tradução do cap. 1 e da 1.1, com os apartes do autor em primeira pessoa
- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]] — texto do cap. 2: definição, fórmula, sintomas, causas e complexidade incremental
- [[wiki/sources/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente]]: texto do cap. 3, tática vs. estratégica, tornado tático, 10–20%, Facebook vs. Google/VMware
- [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]]: texto do cap. 4, interface formal e informal, falsa abstração, profundidade como custo-benefício, classite
- [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]]: texto do cap. 5, ocultamento e vazamento, decomposição temporal, exemplos HTTP, valores padrão
- [[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]]: texto do cap. 6, um tanto de uso geral, editor, `History`, casos especiais
