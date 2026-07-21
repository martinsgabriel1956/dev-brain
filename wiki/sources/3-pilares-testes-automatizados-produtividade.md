---
type: source
title: "3 Pilares para Testes Automatizados e Produtividade no Dia a Dia"
aliases: ["3 pilares testes automatizados", "método TJS", "entender antes de codificar"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/3-pilares-testes-automatizados-produtividade.md
source_url: ""
author: "Erick Wendel"
date_published: ""
date_ingested: 2026-07-21
source_count: 0
tags: [testes, tdd, node-js, produtividade, comunicacao-tecnica, debugging, jsdoc, live-reload, tarefas]
skill: tech-mentor-testing
status: stable
---

# 3 Pilares para Testes Automatizados e Produtividade no Dia a Dia

## TL;DR

Erick Wendel descreve o próprio método de trabalho em três pilares: (1) nunca cair para implementação sem ter certeza do que precisa ser feito — usando uma técnica de repetir de volta o entendimento até ser confirmado por quem pediu a tarefa; (2) todo projeto deve ter live reload, modo de depuração (`--inspect`) e testes automatizados (`node --test`) integrados desde o início, ligados ao debugger do VS Code via `launch.json`, eliminando o ciclo lento de `console.log` → reiniciar servidor → verificar manualmente; e (3) toda tarefa deve ser decomposta em casos de teste usando três campos guia — entrada, processamento, saída — combinados com sentenças no formato dado/quando/então (Given/When/Then), exemplificado com o desafio open source "Rinha de Backend". Também demonstra tipagem forte em JavaScript puro via JSDoc (`@typedef`, `@param`, `@returns`), sem precisar de TypeScript.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Implementar sem ter certeza do que foi pedido causa retrabalho e perda de tempo | Experiência pessoal do autor com times de produto que corrigem escopo depois da entrega | experiência pessoal | alta (mas subjetiva, sem dado quantitativo) |
| Repetir de volta o entendimento da tarefa antes de implementar reduz retrabalho e aumenta respeito no time | Técnica pessoal descrita em detalhe (peça para explicar, deixe terminar, corrija depois) | experiência pessoal, sem estudo formal citado | média |
| Live reload + modo debug + testes automatizados integrados no editor eliminam o ciclo lento de validação manual (console.log + restart manual) | Demonstração prática ao vivo no vídeo, com configuração completa de `package.json` e `launch.json` | demonstração técnica reproduzível | alta (mecanismo verificável, comportamento do Node.js/VS Code documentado) |
| `--experimental-test-coverage` do Node.js não funciona corretamente em conjunto com `--inspect` (modo debug) no ambiente demonstrado | Observado ao vivo durante a demonstração — coverage não aparecia com debug ativo | observação direta, não documentada oficialmente pela fonte | média (comportamento pode mudar entre versões do Node.js; sinalizado como experimental pelo próprio autor) |
| Decompor uma tarefa em entrada/processamento/saída + Given/When/Then antes de implementar torna a tarefa diretamente traduzível em testes automatizados | Exemplo passo a passo com a especificação da "Rinha de Backend" | exemplo prático guiado, sem estudo formal | média-alta (mecanismo claro e reproduzível, mas é opinião de método, não pesquisa) |
| JSDoc (`@typedef`, `@param`, `@returns`) dá autocomplete e alguma validação de tipo em JavaScript puro, sem precisar de TypeScript | Demonstração ao vivo no VS Code, com autocomplete de propriedades funcionando | demonstração técnica reproduzível (comportamento do VS Code/TS Language Server documentado) | alta |

---

## Key Claims

### 1. Entender antes de implementar — o pilar que evita retrabalho
O maior desafio em desenvolvimento não é lidar com código — é comunicação: entender e ser entendido. Times de produto frequentemente passam tarefas de forma incompleta, e só depois da entrega aparece algo "que não estava previsto", forçando retrabalho total. Conecta diretamente com [[wiki/concepts/comunicacao-tecnica]] — a responsabilidade de garantir entendimento é de quem recebe a tarefa, na prática, tanto quanto de quem a passa.

### 2. Loop de confirmação de entendimento
Técnica específica: perguntar o que precisa ser feito, anotar, e então — em vez de interromper com perguntas pontuais — dizer de volta "o que eu entendi foi X", pedindo para a pessoa aguardar até o fim da explicação para corrigir ou complementar. Repetir esse loop até ter certeza real do entendimento. Isso demonstra maturidade, faz quem está explicando repensar a própria proposta, e — com prática — passa a permitir antecipar problemas durante a própria explicação (ex.: perceber que "atualizar data de acesso no login" não cobre o caso de logout implícito por fechamento de página). Ver [[wiki/concepts/loop-de-confirmacao-de-entendimento]].

### 3. Setup de ferramental antes de codificar: live reload, debug e testes integrados
Gastar as primeiras horas de um projeto (novo ou legado) configurando o ambiente de desenvolvimento paga-se no resto do projeto. Três camadas, cada uma resolvendo uma dor específica do ciclo de validação manual (alterar código → rodar manualmente → `console.log` → verificar → repetir):
- **Live reload**: `node --watch` (ou Browser Sync para projetos de navegador) reinicia o servidor a cada alteração salva, sem precisar descer ao terminal.
- **Modo de depuração**: `node --inspect` abre uma porta de debug que o VS Code (ou Chrome DevTools) pode conectar, permitindo breakpoints direto no editor.
- **Testes automatizados integrados**: `node --test` (test runner nativo do Node.js) combinado com `--watch` e `--inspect` faz os testes rodarem automaticamente a cada `Ctrl+S`, com o debugger já conectado — eliminando a necessidade de sair do editor para validar qualquer mudança.

A peça final é o `launch.json` do VS Code, que aponta para o script do `package.json` (não direto para o Node.js) — garantindo que qualquer pessoa do time, independente do editor, rode o mesmo comando subjacente. Ver [[wiki/concepts/setup-live-reload-debug-testes]].

### 4. Tipagem forte em JavaScript puro via JSDoc
Sem precisar de TypeScript, é possível ter autocomplete e alguma validação de tipos usando comentários JSDoc: um arquivo `types.js` define `@typedef` para os formatos de entrada e saída de uma função, e a função os referencia via `@param` e `@returns`. O VS Code (via TS Language Server rodando sobre JS) passa a oferecer autocomplete de propriedades e alertar sobre incompatibilidades de tipo, tanto no código de produção quanto no teste. Ver [[wiki/concepts/tipagem-com-jsdoc]].

### 5. Decompor uma tarefa em entrada/processamento/saída + Given/When/Then
Depois de entender o problema (pilar 1) e montar o setup (pilar 3), o passo central é dividir a tarefa em casos de teste concretos usando três campos-guia — **entrada**, **processamento**, **saída** — preenchidos progressivamente à medida que a especificação e as regras de negócio ficam claras. Quando o processamento ainda não está claro, o campo fica em branco propositalmente, sinalizando o que falta perguntar. Combinado com sentenças no formato **dado/quando/então** (mesma estrutura do Given/When/Then usado em [[wiki/concepts/bdd]], mas aqui usada como ferramenta pessoal de planejamento, não como spec formal compartilhada com o negócio), cada caso vira diretamente um teste anotado (`it(...)` pendente) antes de qualquer linha de implementação real ser escrita. Exemplo completo usando a especificação pública do desafio [[wiki/entities/rinha-de-backend]] (transações de crédito/débito com validação de limite). Ver [[wiki/concepts/mapear-entrada-processamento-saida]].

---

## Entidades Mencionadas

- [[wiki/entities/erick-wendel]] — autor do vídeo, criador de conteúdo sobre Node.js e testes automatizados; menciona treinamento próprio ("Método TJS"/"Método TDD") de ~4h
- [[wiki/entities/rinha-de-backend]] — desafio open source usado como exemplo prático de decomposição de tarefa em casos de teste

## Conceitos Tocados

- [[wiki/concepts/loop-de-confirmacao-de-entendimento]] (novo)
- [[wiki/concepts/setup-live-reload-debug-testes]] (novo)
- [[wiki/concepts/tipagem-com-jsdoc]] (novo)
- [[wiki/concepts/mapear-entrada-processamento-saida]] (novo)
- [[wiki/concepts/comunicacao-tecnica]]
- [[wiki/concepts/pensamento-estruturado]]
- [[wiki/concepts/tdd]]
- [[wiki/concepts/bdd]]
- [[wiki/concepts/debugging]]
- [[wiki/concepts/testar-proprio-codigo]]

---

## Questões Abertas

- Nenhum estudo formal é citado para as duas técnicas de comunicação e decomposição de tarefa — são práticas pessoais do autor, tratadas como opinião qualificada, consistente com o tratamento dado a fontes similares já ingeridas na wiki (ex.: [[wiki/concepts/pensamento-estruturado]]).
- O comportamento observado de `--experimental-test-coverage` não funcionar junto com `--inspect` é específico da versão do Node.js usada na gravação (Node.js 20) e da flag ainda ser experimental — pode já ter mudado em versões mais recentes; vale reverificar em uma ingestão futura sobre Node.js test runner se a fonte aparecer.
- O "Método TJS"/"Método TDD" citado como treinamento pago do autor não é detalhado além do nome e duração — não há conteúdo técnico adicional a extrair daí, é citação promocional.

---

## Citações Relevantes

> "Lidar com código é o menor dos problemas — entender e ser entendido é o maior desafio."

> "Calma aí, eu vou te explicar o que eu entendi, e depois que eu terminar de falar você me diz o que tá errado e o que faltou."

> "Antes você poderia inicializar o servidor, colocar um console.log, e em alguma ferramenta externa verificar os valores — e aí manualmente reiniciar o servidor e repetir o processo inteiro até resolver o problema. Agora você dá um F5, as validações rodam, você consegue parar nas linhas sem ter que se distrair saindo da ferramenta."

> "Você sabe exatamente o que precisa ser validado — usa as configurações de live reload, debug e automação dos testes direto do seu editor. Errou alguma regra? É só clicar na linha, inspecionar o problema, e já era."
