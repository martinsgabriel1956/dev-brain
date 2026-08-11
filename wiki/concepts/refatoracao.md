---
type: concept
title: "Refatoração"
aliases: ["refactoring", "refatorar"]
date_created: 2026-07-15
date_updated: 2026-08-11
source_count: 5
tags: [refactoring, clean-code, craftsmanship, design-de-software, tech-debt]
skill: tech-mentor-backend
status: draft
---

# Refatoração

Processo de modificar a estrutura interna de um sistema de software **sem alterar seu comportamento externo**. Não é sinônimo de "reescrever" nem de "corrigir bug" — é melhorar o design do código depois que ele já foi escrito, preservando exatamente o que o sistema faz por fora.

## Dois pilares da definição

1. **Comportamento externo intacto.** Uma refatoração nunca deve ser feita ao mesmo tempo que se adiciona ou altera uma funcionalidade — ver [[wiki/concepts/dois-chapeus-kent-beck]].
2. **Estrutura interna livre para mudar** — às vezes drasticamente — desde que o resultado observável (inputs/outputs, efeitos colaterais) permaneça o mesmo.

## Por que o design degrada com o tempo

Todo sistema tende a começar organizado. A cada nova feature, cada hotfix sob pressão de prazo, o design bem pensado vai sendo "atropelado" — um `if` aqui, uma regra ali, até uma classe que começou coesa virar um [[wiki/concepts/god-object]] que ninguém tem coragem de tocar. Um compilador não se importa se o código está feio; o humano sim — código com design ruim é difícil de entender, difícil de saber tudo que precisa mudar, e por isso mais propenso a bugs. Ver [[wiki/concepts/entropia-de-software]].

### A analogia da jardinagem (Pragmatic Programmer)

[[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] registra uma analogia do *Pragmatic Programmer*: desenvolvimento de software é comparado com mais frequência a construção civil, mas essa analogia é enganosa — um prédio pronto não continua "vivo". Uma analogia mais adequada é a de jardinagem: plantas daninhas crescem, galhos saem em excesso, e é preciso podar continuamente para manter o jardim saudável. Refatoração é essa poda — uma atividade de rotina (como cortar grama), não um projeto esporádico.

### Refatoração como mudança mínima, isolada

A mesma fonte reforça a definição de Fowler com um exemplo concreto: renomear uma variável já é uma refatoração completa — muda a estrutura, não o comportamento. Isoladamente, uma única refatoração desse tipo pode parecer pequena demais para valer o esforço; o valor aparece na soma de muitas pequenas alterações feitas com frequência, não numa refatoração isolada e grande.

## Como não piorar o código refatorando

A garantia central é **cobertura de testes automatizados** — de preferência barata e rápida de rodar (base da [[wiki/concepts/piramide-de-testes]], não testes E2E). Se a funcionalidade a ser refatorada não tem testes, o primeiro passo é escrevê-los só para aquele escopo, para mapear o comportamento real antes de mexer na estrutura.

A refatoração deve avançar em **passos pequenos**, nunca reescrevendo um módulo inteiro de uma vez numa branch isolada — o risco é terminar com um estado que não entrega nem a refatoração nem funcionalidade nova, e um merge quase impossível. O processo deve permitir parar a qualquer momento sem deixar o comportamento externo do sistema quebrado; se a refatoração deixa o sistema quebrado por horas ou dias, é sinal de alerta.

### Bugs encontrados durante a refatoração

Segundo [[wiki/entities/martin-fowler]] (*Refactoring: Improving the Design of Existing Code*): um bug **já conhecido e priorizado** deve ser deixado como está — o objetivo é reproduzir exatamente o comportamento externo que existia antes da refatoração começar. Um bug **novo, ainda não mapeado**, pode ser corrigido no mesmo momento, mas só com certeza absoluta de que é de fato um bug real — senão a refatoração se mistura com mudança de comportamento.

## Quando refatorar é uma boa ideia

- **Refatoração oportunista** (a mais comum e recomendada): imediatamente antes de adicionar uma funcionalidade nova muito parecida com um comportamento já existente. A alternativa ruim é duplicar o método/código, o que obriga a alterar em múltiplos lugares sempre que a regra compartilhada mudar no futuro.
- Quando o código está difícil de entender (lógica confusa, duplicação) e é preciso se embrenhar nele de qualquer forma para dar manutenção.
- Se a refatoração necessária ultrapassa horas/dias de esforço, o caminho é registrá-la como [[wiki/concepts/tech-debt-como-ferramenta|débito técnico]] para um momento mais oportuno, em vez de insistir ali.

Existem também **refatorações planejadas** (revisões de código dedicadas), mais raras que as oportunistas.

### As duas motivações de Fowler

Segundo [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]], Fowler resume as motivações para refatorar em duas: (1) você entendeu melhor o código e quer refletir esse entendimento na estrutura; (2) uma alteração planejada seria difícil de fazer no estado atual do código, e refatorar facilita essa mudança. A recomendação é alternar continuamente entre adicionar funcionalidade e refatorar, nunca parar de fazer as duas ao longo da vida do sistema.

### Seis situações do Pragmatic Programmer

A mesma fonte lista seis gatilhos concretos do *Pragmatic Programmer* para decidir refatorar:

1. **Duplicação** — viola DRY (*don't repeat yourself*).
2. **Falta de ortogonalidade** — código muito acoplado, que pede desacoplamento.
3. **Conhecimento desatualizado** — você aprendeu algo novo sobre requisitos ou domínio que o código ainda não reflete.
4. **Mudança de prioridades no uso real** — usuários reais revelam que partes tidas como importantes não são, e vice-versa.
5. **Oportunidade de melhoria de performance** — refatorar mantendo o comportamento, mas com melhor desempenho.
6. **Quando um teste está passando** — contraintuitivo, mas é o momento de maior segurança para alterar: o teste de regressão avisa se o comportamento quebrou.

## Quando NÃO refatorar

- Algoritmo complicado (às vezes proprietário) que funciona desde a primeira versão e não precisa ser entendido/alterado agora — refatorar só compensa se for necessário mexer internamente naquele código.
- Quando reescrever do zero é mais barato que refatorar — decisão arriscada, pois só dá para saber que algo é "difícil de refatorar" depois de já ter se debruçado sobre o código por um tempo.

## Benefícios (por que vale o esforço)

1. Freia a degradação contínua do design.
2. Aumenta a manutenibilidade — código refatorado é mais legível para quem for mexer nele depois (frequentemente você mesmo).
3. Ajuda a encontrar bugs e comportamentos inesperados, como efeito colateral de entender melhor a estrutura interna.
4. Contraintuitivamente, **acelera** a entrega: segundo Fowler, investir no design interno reduz o tempo de entrega de features futuras, porque adicionar comportamento a um código bem desenhado é mais rápido que a um código degradado.

## Gestão e o hábito da refatoração

Refatoração idealmente não é um "projeto" à parte que precisa de aprovação — é incorporada no tempo normal de desenvolvimento de uma feature, do mesmo jeito que se reserva tempo para escrever testes. Com gestão pouco técnica, a recomendação prática é simplesmente não pedir permissão para esse tempo embutido. Com gestão técnica, vale abrir a discussão sobre quando uma refatoração deixa de ser oportunista e deve virar item priorizado de débito técnico.

## "Ficar estratégico" ao modificar código existente (Ousterhout)

[[wiki/sources/filosofia-do-design-de-software-livro-completo]] (Cap. 16) discute manutenção contínua sob a mesma régua tática/estratégica do Cap. 3 (ver [[wiki/concepts/tech-debt-como-ferramenta]]): ao corrigir bug ou adicionar feature em código existente, o objetivo estratégico não é "a menor mudança possível que funcione" — é deixar o sistema com a estrutura que teria se tivesse sido projetado desde o início considerando aquela mudança. Regras práticas complementares para manter a refatoração e a documentação sustentáveis ao longo do tempo:

- **Comentários perto do código, não em arquivo de cabeçalho distante** — a chance de um comentário ser atualizado cai com a distância até o código que ele descreve.
- **Documentação no código, não na mensagem de commit** — um desenvolvedor futuro raramente vai vasculhar o log do git para entender uma decisão; se a informação importa depois, ela precisa estar no código.
- **Evitar duplicação de documentação** — se não há um lugar óbvio único para uma decisão cross-module, o autor recomenda um arquivo central `designNotes` com referências curtas a partir de cada ponto do código afetado (exemplo real: o tratamento de "zombie servers" no sistema RAMCloud).
- **Revisar o diff antes de commitar** — checagem manual de que cada mudança de código tem a documentação correspondente atualizada.

## Relacionado

[[wiki/concepts/dois-chapeus-kent-beck]] · [[wiki/concepts/tech-debt-como-ferramenta]] · [[wiki/concepts/boy-scout-rule]] · [[wiki/concepts/piramide-de-testes]] · [[wiki/concepts/god-object]] · [[wiki/concepts/entropia-de-software]] · [[wiki/concepts/essential-complexity]] · [[wiki/concepts/accidental-complexity]] · [[wiki/entities/martin-fowler]] · [[wiki/entities/kent-beck]] · [[wiki/concepts/comentarios-como-ferramenta-de-design]]

## Key Sources

- [[wiki/sources/arquitetura-de-sacrificio]] — substituir *módulos individuais* (com boas fronteiras) é a alternativa incremental ao descarte total do sistema
- [[wiki/sources/o-que-e-refatoracao-quando-usar]]
- [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — "ficar estratégico" ao modificar código existente; regras de manutenção de comentários (Cap. 16)
- [[wiki/sources/extrair-melhor-codigo-de-agentes-ia-planejamento-plan-mode-skills]] — refatoração conduzida por IA com [[wiki/concepts/plan-mode|plan mode]] e [[wiki/concepts/strategy-pattern|Strategy]]; comportamento externo (interface do front end) preservado — mas a validação do resultado é visual/estrutural, sem os testes automatizados que esta página exige como garantia
