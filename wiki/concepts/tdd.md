---
type: concept
title: "TDD — Test-Driven Development"
aliases: ["test driven development", "red green refactor", "desenvolvimento guiado por testes"]
date_created: 2026-04-22
date_updated: 2026-07-28
source_count: 12
tags: [testes, tdd, design, red-green-refactor, qualidade, dora]
skill: tech-mentor-testing
status: stable
---

# TDD — Test-Driven Development

Prática onde o **teste é escrito antes do código de produção**. O benefício central não é cobertura — é **sentir o acoplamento antes de criá-lo**. Código difícil de testar é código com problemas de design.

## Ciclo obrigatório

```
RED → GREEN → REFACTOR → RED → GREEN → REFACTOR → ...
```

- **RED**: escreva um teste que falha — o comportamento ainda não existe
- **GREEN**: escreva o *mínimo* de código para o teste passar — sem over-engineering
- **REFACTOR**: melhore sem quebrar os testes

Sem o Refactor, TDD é apenas "testes primeiro" — acumula débito técnico com os testes.

[[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] liga explicitamente a primeira das três dicas de Fowler para refatorar com segurança — nunca misturar adicionar funcionalidade com refatorar — ao mesmo ciclo RED-GREEN-REFACTOR: primeiro faz funcionar (RED → GREEN), depois refatora (REFACTOR), nunca as duas coisas ao mesmo tempo. Ver [[wiki/concepts/dois-chapeus-kent-beck]].

## Armadilha: testar implementação, não comportamento

```typescript
// ❌ Frágil — quebra se renomear método interno
it("should call calculateSubtotal", () => {
  const spy = jest.spyOn(order, "calculateSubtotal");
  order.totalWithDiscount(0.1);
  expect(spy).toHaveBeenCalled();
});

// ✅ Robusto — testa o resultado observável
it("should return correct total with 10% discount", () => {
  expect(order.totalWithDiscount(0.1)).toBe(225);
});
```

## As duas escolas

### Detroit (Inside-Out / Classicist)
Começa pelas unidades internas do domínio. Usa objetos reais, mocka apenas I/O externo real (DB, HTTP). Integração validada mais cedo nas unidades.

### London (Outside-In / Mockist)
Começa pelo comportamento externo. Mocka todos os colaboradores ainda não existentes — o design emerge das interfaces que o teste exige. Risco: mocks podem mascarar integração quebrada.

Essas duas escolas mapeiam quase diretamente para a distinção de Fowler entre [[unit-test-solitario-vs-sociavel|unit test solitário (London) e sociável (Detroit)]].

## Origem: do framework caseiro em Smalltalk ao JUnit

Antes do TDD ser formalizado, [[wiki/entities/kent-beck]] já construía frameworks de teste caseiros em Smalltalk para rodar testes rapidamente dentro do ciclo de edição — usados no projeto [[wiki/entities/c3-project|C3]], o "projeto de nascimento" da Extreme Programming. Em 1997, Beck e Erich Gamma ([[wiki/entities/gang-of-four|Gang of Four]]) criaram o [[wiki/entities/junit]] num voo para a OOPSLA — o framework que, segundo [[wiki/entities/martin-fowler]], foi essencial para sustentar o crescimento de XP e TDD na indústria, ao ser simples o suficiente para encorajar adoção em massa. Ver [[wiki/sources/xunit-martin-fowler]].

## Quando usar / evitar

**Use:** lógica de negócio com múltiplos caminhos, refatorando legado (testes antes de mudar qualquer linha), algoritmos com comportamento claro antes da implementação.

**Evite:** exploração de APIs desconhecidas (spike primeiro), protótipos descartáveis, UI visual, IaC.

## Ver também

- [[bdd]] — extensão do TDD para linguagem de negócio
- [[test-doubles]] — como isolar dependências no ciclo TDD
- [[piramide-de-testes]] — onde TDD vive na estratégia de testes
- [[testar-proprio-codigo]] — hábito relacionado

## TDD com IA

Na [[era-agentica]], TDD via IA é mais poderoso do que nunca — e mais necessário. A IA gera testes em volume rapidamente, mas tende a criar testes que apenas executam o código sem validar o comportamento real. TDD inverte esse problema: o teste é escrito primeiro (por você ou pela IA), e o código só existe para passar no teste.

Forçar TDD via [[harness-de-qualidade]]:
- Pipeline rejeita código sem cobertura de teste adequada
- [[teste-de-mutacao]] valida que os testes gerados pela IA realmente testam comportamento
- O ciclo red-green-refactor garante que o código é testável por design

> *"Manda a IA fazer TDD. Ela consegue fazer isso. Configura os linters com boas regras. Ela vai seguir."*

### Não deixe a IA deletar testes que falham

Padrão de falha comum: a IA implementa uma feature, o teste continua falhando, e em vez de corrigir o código ela deleta ou enfraquece o teste para "fazer passar". Isso precisa ser proibido explicitamente na instrução — ver [[gaming-de-testes-por-ia]].

### "Outrunning your headlights" — por que a IA precisa de TDD mais que o humano

[[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] aplica um termo do Pragmatic Programmer ("outrunning your headlights" — dirigir mais rápido do que o alcance dos faróis permite enxergar) ao comportamento padrão de LLMs: mesmo com type-checking, acesso ao browser e testes automatizados disponíveis, a IA tende a gerar uma quantidade grande de código de uma vez, e só depois checa tipos ou roda testes — o oposto do ciclo RED-GREEN-REFACTOR. A taxa de feedback é o "limite de velocidade"; TDD força a IA a andar nesse limite, em passos pequenos e deliberados, em vez de acumular risco antes de qualquer verificação.

### TDD depende de módulos testáveis

A mesma fonte argumenta que testar é intrinsecamente difícil (decidir tamanho da unidade, o que mockar, quais comportamentos testar) e que **[[wiki/concepts/modulo-profundo|módulos profundos]]** — poucos módulos grandes com interface simples — são o que torna uma base de código genuinamente testável: a fronteira de teste é a própria interface do módulo, sem precisar mockar uma teia de dependências internas. Uma base de código cheia de módulos rasos gera testes flaky ou excessivamente mockados, prejudicando o próprio loop de feedback que o TDD depende.

## TDD não é o que atrasa a entrega

Contraintuitivamente, aplicar TDD não torna a entrega mais lenta — a pesquisa [[dora-metrics|DORA]] (*Accelerate*) mostra que equipes com melhores práticas de engenharia (incluindo testes automatizados como pré-condição para deploy contínuo) entregam com mais frequência e menor lead time, não menos. TDD é parte do que torna um sistema seguro de mudar rapidamente — sem ele, cada mudança exige validação manual, que é o gargalo real. Ver [[over-engineering]] para a discussão mais ampla dessa correlação.

## Testes Como Condição de Parada de um Loop Agêntico

[[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] observa que testes escritos antes do código não são só verificação — são a **condição de parada objetiva** que um [[wiki/concepts/loop-engineering|loop agêntico]] precisa para rodar sem supervisão ("roda até os testes passarem" só funciona se os testes já existirem antes do código). Quem já pratica TDD já satisfaz o pré-requisito do nível "goal-based" na escada de autonomia de loop do guia da Anthropic — falta só disparar o loop.

## Mapear entrada/processamento/saída antes do primeiro teste

O ciclo RED-GREEN-REFACTOR pressupõe saber o que testar primeiro — na prática, o passo que precede o RED é decompor a tarefa em casos discretos. [[wiki/concepts/mapear-entrada-processamento-saida]] descreve essa técnica: três campos-guia (entrada, processamento, saída) preenchidos progressivamente conforme a especificação e as regras de negócio ficam claras, combinados com sentenças dado/quando/então, cada uma virando diretamente um teste anotado antes de qualquer implementação. Complementado por [[wiki/concepts/setup-live-reload-debug-testes]] — live reload, `--inspect` e `node --test` integrados via `launch.json`, fazendo cada `Ctrl+S` rodar os testes com o debugger já conectado, sem sair do editor.

## 100% de cobertura não é o objetivo

Cobertura alta prova que uma linha foi executada, não que ela foi exercitada com os valores certos — não existe forma de testar (via TDD ou não) um bug que ninguém pensou em cobrir. Ver [[criterios-de-bom-teste]] para os cinco critérios (determinístico, conciso, relevante, compreensível, durável) usados para julgar se um teste feito sob TDD realmente vale o ciclo red-green-refactor.

## Importar Testes de uma Implementação de Referência como Oráculo

Quando a interface, o input e o output já são conhecidos por uma especificação externa (RFC, protocolo, formato de arquivo), é possível pular a etapa de escrever os testes do zero e **importar a suite de testes de uma implementação de referência já validada**. [[wiki/sources/algoritmo-decode-utf8-com-tdd]] faz isso ao copiar a suite de testes do pacote `unicode/utf8` da standard library de Go para validar uma implementação própria de decode UTF-8 — os testes cobrem edge cases (sequências de bytes inválidas, overlong encoding, surrogate pairs) que seriam difíceis de antecipar escrevendo do zero. Passar em toda a suite importada é evidência forte de que a implementação está correta e não apenas "parece funcionar" nos casos óbvios. É uma variação do ciclo clássico RED → GREEN → REFACTOR: a primeira rodada dos testes falha propositalmente (a função ainda nem existe), confirmando que os testes de fato exercitam o comportamento esperado antes de qualquer código de produção ser escrito.
## Expectativa que quebra é sinal de bug, não de teste errado

[[wiki/sources/os-3-estagios-de-maturidade-para-testar-codigo]] ilustra o princípio central do RED com um caso concreto de segurança: um teste espera `403` para uma rota sensível de migrations acessada por usuário anônimo, mas o código retorna `200`. A expectativa está certa — o código é que está exposto, sem nenhum middleware de autorização no handler. A fonte estende o mesmo raciocínio à fase de manutenção: meses depois, uma alteração não relacionada (permissão liberada por engano em outro arquivo) faz o mesmo teste voltar a falhar sozinho, em modo watch, pegando a regressão sem qualquer verificação manual — o mesmo teste escrito uma vez continua funcionando como especificação executável indefinidamente. Ver [[wiki/concepts/tres-estagios-maturidade-testes]] para o enquadramento de "teste automatizado com watch mode" como estágio mais maduro de validação de código, depois de clicar manualmente na UI e de usar um cliente HTTP dedicado (Postman).

## TDD como Prevenção de Dívida Técnica

[[wiki/sources/tech-debt-guia-completo-gestao-metricas]] enquadra TDD não como técnica de gestão de dívida técnica já existente, mas como **prevenção** — é difícil escrever lógica confusa e mal desenhada quando é preciso primeiro passar num teste limpo e simples (fase GREEN). Nesse enquadramento, a fase de REFACTOR do ciclo é onde a [[wiki/concepts/boy-scout-rule]] acontece de forma estruturada e obrigatória, em vez de depender da disciplina individual do dev de limpar o código depois. Ver [[wiki/concepts/tech-debt-como-ferramenta]] para as outras práticas de prevenção citadas na mesma fonte (pair programming, CI/CD com quality gates).

## Key Sources

- [[wiki/sources/tdd]]
- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
- [[wiki/sources/tdd-sdd-bdd-era-ia]]
- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]]
- [[wiki/sources/como-evitar-over-engineering-david-farley]]
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — cobertura alta ≠ ausência de bugs
- [[wiki/sources/xunit-martin-fowler]] — origem histórica do JUnit e da família Xunit
- [[wiki/sources/3-pilares-testes-automatizados-produtividade]] — decomposição de tarefa em entrada/processamento/saída como passo pré-RED; setup de live reload/debug/testes integrados via `node --test` + `--inspect` + `launch.json`
- [[wiki/sources/algoritmo-decode-utf8-com-tdd]] — importar a suite de testes de uma implementação de referência (stdlib de Go) como oráculo de corretude
- [[wiki/sources/os-3-estagios-de-maturidade-para-testar-codigo]] — expectativa que quebra expõe bug de autorização real; teste como rede de segurança contra regressão futura não relacionada
- [[wiki/sources/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao]] — liga a regra "não misturar feature e refatoração" de Fowler ao ciclo RED-GREEN-REFACTOR
- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — testes escritos antes do código como condição de parada objetiva de um loop agêntico goal-based
- [[wiki/sources/tech-debt-guia-completo-gestao-metricas]] — TDD como prática de prevenção de dívida técnica, não gestão; fase REFACTOR do ciclo como Boy Scout Rule estruturada
