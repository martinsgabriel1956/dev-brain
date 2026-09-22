---
type: entity
title: "Kent Beck"
aliases: ["kent beck"]
date_created: 2026-07-09
date_updated: 2026-09-21
source_count: 14
tags: [autor, tdd, extreme-programming, design-incremental, junit, xunit, yagni]
skill: tech-mentor-testing
status: stub
---

## Quem É

Criador do TDD (Test-Driven Development) moderno e da Extreme Programming (XP), coautor do Manifesto Ágil. Autor de *Test Driven Development: By Example* e *Tidy First?*.

## Criador do framework original e coautor do JUnit

Antes do TDD ser formalizado como prática, Beck já construía frameworks de teste caseiros em Smalltalk — usados por ele e clientes num ciclo de edição-e-teste rápido dentro da própria IDE. Preferia que cada time reconstruísse o próprio framework (levava poucas horas) em vez de compartilhar um único — um exemplo do que Fowler chamaria de [[wiki/concepts/seedwork|Seedwork]]. Esse framework foi usado no projeto [[wiki/entities/c3-project|C3]] (Chrysler, 1996), o "projeto de nascimento" da Extreme Programming, onde Ron Jeffries também foi apresentado a ele. [[wiki/sources/xunit-xunitpatterns]] é a primeira fonte primária a dar nome próprio a esse framework: **[[wiki/entities/sunit|SUnit]]**, citado ao lado do JUnit como um dos dois padrões de referência que definem formalmente o que é um framework "xUnit".

## Relatou o primeiro caso de "Very Low Defect Project" a Fowler

Segundo [[wiki/sources/very-low-defect-project-martin-fowler]], foi Beck quem descreveu a Fowler o primeiro exemplo do que este batizaria de [[wiki/concepts/very-low-defect-project|VeryLowDefectProject]]: uma fabricante de máquinas de classificação de alimentos (esteiras, câmeras e sensores, rodando em Smalltalk) que caiu de ~100 bugs abertos simultaneamente para cerca de um a cada dois meses depois de adotar XP.

## Liderança do recomeço do C3 (1996)

Segundo [[wiki/sources/c3-martin-fowler]], Beck assumiu a liderança do C3 em 1996, num recomeço motivado por problemas de estabilidade do desenvolvimento original em Smalltalk (iniciado em 1995). Foi nesse recomeço, não no início do projeto, que as práticas hoje conhecidas como [[wiki/concepts/extreme-programming|Extreme Programming]] foram reunidas de forma coesa pela primeira vez.

Em 1997, num voo de Zurique para a OOPSLA em Atlanta, Beck programou em par com [[wiki/entities/gang-of-four|Erich Gamma]] a primeira versão do [[wiki/entities/junit]] — feita test-first. JUnit se tornou o membro fundador da família de frameworks "Xunit" e, segundo Fowler, foi essencial para sustentar o crescimento de XP e TDD na indústria. Ver [[wiki/sources/xunit-martin-fowler]].

## Contribuições relevantes para o wiki

**TDD (RED-GREEN-REFACTOR):** ver [[wiki/concepts/tdd]] — a prática de escrever o teste antes do código de produção, com foco em sentir o acoplamento antes de criá-lo, não em cobertura.

**"Invest in the design of the system every day"** — citação usada em [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] para argumentar contra o movimento spec-driven ("specs to code") que trata o código como descartável: cada mudança deveria melhorar (ou ao menos preservar) o design do sistema, nunca só resolver o problema local ignorando a estrutura.

**Metáfora dos dois chapéus:** ver [[wiki/concepts/dois-chapeus-kent-beck]] — adicionar funcionalidade e refatorar são atividades mutuamente exclusivas no tempo, cada uma com sua própria disciplina de validação (testes passando vs. comportamento externo intacto). Citado em [[wiki/sources/o-que-e-refatoracao-quando-usar]] como o argumento central para nunca refatorar e mudar comportamento ao mesmo tempo.

## Autor de *Extreme Programming Explained* (1999) — origem do YAGNI

Beck é o autor do livro fundador da Extreme Programming, onde [[wiki/concepts/yagni]] foi apresentado. [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] atribui esse livro a Ron Jeffries — provável imprecisão da fonte, registrada como nota de verificação em [[wiki/concepts/yagni]]. Jeffries é cocriador da XP junto com Beck no [[wiki/entities/c3-project|projeto C3]], mas não é o autor do livro em questão.

## "Make the hard change easy" — Tidy First?

[[wiki/sources/cognitive-debt-margaret-storey]] cita Beck (com link para [tidyfirst.substack.com/p/tidy-first-example](https://tidyfirst.substack.com/p/tidy-first-example)) como origem do enquadramento "make the hard change easy, then make the easy change" — ordenar tidying antes de mudanças arriscadas. A autora argumenta que a relutância em fazer esse trabalho preparatório, sob pressão por velocidade com IA, é o que leva à dívida cognitiva. Isso confirma, a favor de *Tidy First?*, a nota de verificação abaixo sobre a citação "invest in the design of the system every day" — mesma obra, mesmo argumento de investir continuamente em preparar o terreno antes de mudar.

## Pai Programador Assembly Migrando Para C — Paralelo Com a IA de Hoje

Segundo [[wiki/sources/ia-paradoxo-de-jevons-camada-de-abstracao-futuro-do-programador]], Beck relatou numa palestra que seu pai era programador assembly e, quando surgiu o C, precisou migrar porque as habilidades que tinha (alocação manual de registradores, conhecimento de layout de memória) perderam valor econômico. A fonte usa essa anedota como paralelo histórico direto para a crise de identidade que devs enfrentam hoje com a geração de código por IA — mesmo mecanismo de desvalorização de habilidade técnica de baixo nível diante de uma nova camada de abstração, ver [[wiki/concepts/linguagem-natural-como-camada-de-abstracao]].

**Nota de confiança:** anedota relatada de segunda mão pelo autor da fonte, sem palestra específica identificada.

## Tweet "90% Desvalorizado, 10% Mil Vezes Mais Valioso"

A mesma fonte cita um tweet famoso de Beck: "O valor econômico de 90% das minhas habilidades praticamente despencou. Já os 10% restantes ficaram 1000 vezes mais valiosos." Usado como evidência central de que conhecimento técnico de implementação (sintaxe, linha a linha) perdeu valor com a IA, mas princípios de engenharia de software, arquitetura e julgamento continuam (e aumentaram) de valor — reforça a tese já registrada em [[wiki/concepts/novo-perfil-dev-ia]] e [[wiki/concepts/ia-como-amplificador]] de que a IA multiplica o julgamento de quem já sabe guiá-la.

**Nota de confiança:** citação amplamente circulada publicamente; a formulação exata das porcentagens vem de memória do autor da fonte, deve ser tratada como aproximada.

## Autor de *Smalltalk Best Practice Patterns* [SBPP] — origem do Pluggable Behavior

[[wiki/sources/pluggable-behavior-xunitpatterns]] parafraseia Beck e seu livro *Smalltalk Best Practice Patterns* [SBPP] como origem do padrão [[wiki/concepts/pluggable-behavior|Pluggable Behavior]] — adicionar uma variável a um objeto para disparar comportamento diferente em runtime, evitando dezenas de subclasses que diferem em um ou dois métodos. É o mesmo padrão, citado sem elaboração em [[wiki/sources/testcase-object-xunitpatterns]], que explica como um [[wiki/concepts/testcase-object|Testcase Object]] sabe qual [[wiki/concepts/test-method|Test Method]] invocar (construtor recebe o nome do método, `run` usa reflection). Reforça a raiz Smalltalk do vocabulário de padrões de teste de Beck, já presente na wiki via [[wiki/entities/sunit|SUnit]].

## Signatário do Manifesto Ágil e Criador do XP com Ward Cunningham

Em [[wiki/sources/agilidade-manifesto-agil-fabio-akita]], citado como um dos 17 signatários do manifesto de 2001 e, junto com [[wiki/entities/ward-cunningham|Ward Cunningham]] (sem página própria ainda nesta wiki), como criador das práticas de Extreme Programming — a fonte recomenda XP, não Scrum, como ponto de partida para iniciantes que querem entender "agilidade" de verdade. Ver [[wiki/concepts/manifesto-agil-como-adjetivo]].

## Nota de verificação

A citação "invest in the design of the system every day" foi atribuída a Beck na palestra-fonte, mas a obra exata não foi identificada durante aquela ingestão — provavelmente de *Tidy First?*, como sugere a citação equivalente em [[wiki/sources/cognitive-debt-margaret-storey]], a confirmar em ingestão futura que leia o livro diretamente.

## Key Sources

- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/o-que-e-refatoracao-quando-usar]] — metáfora dos dois chapéus
- [[wiki/sources/xunit-martin-fowler]] — origem do JUnit e do framework de testes que o antecedeu
- [[wiki/sources/xunit-xunitpatterns]] — nomeia esse framework de testes caseiro como SUnit
- [[wiki/sources/sunit-xunitpatterns]] — verbete próprio do SUnit em si: tagline autodenominada "a mãe de todos os frameworks de teste unitário"
- [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] — verificação de autoria de *Extreme Programming Explained*, origem do YAGNI
- [[wiki/sources/cognitive-debt-margaret-storey]] — "make the hard change easy" (*Tidy First?*) como prevenção de dívida cognitiva
- [[wiki/sources/seedwork-martin-fowler]] — fonte primária que nomeia o padrão do framework de testes caseiro de Beck (reconstruído por cada time) como exemplo de [[wiki/concepts/seedwork]]
- [[wiki/sources/c3-martin-fowler]] — liderança do recomeço do C3 em 1996; consolidação das práticas da Extreme Programming
- [[wiki/sources/very-low-defect-project-martin-fowler]] — relatou a Fowler o caso da fabricante de máquinas de classificação de alimentos
- [[wiki/sources/ia-paradoxo-de-jevons-camada-de-abstracao-futuro-do-programador]] — anedota do pai programador assembly migrando para C; tweet "90% desvalorizado / 10% mil vezes mais valioso"
- [[wiki/sources/agilidade-manifesto-agil-fabio-akita]] — signatário do manifesto de 2001; criador do XP com Ward Cunningham, recomendado como ponto de partida para iniciantes em vez do Scrum
- [[wiki/sources/pluggable-behavior-xunitpatterns]] — autor de *Smalltalk Best Practice Patterns* [SBPP], origem do padrão Pluggable Behavior citado (sem definição) em [[wiki/sources/testcase-object-xunitpatterns]]
