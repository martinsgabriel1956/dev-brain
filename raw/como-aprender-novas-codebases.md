# Como Aprender Novas Codebases

> Transcrição traduzida do vídeo — autor não identificado (canal focado em desenvolvimento de software)

---

Preciso aprender novas codebases com bastante frequência — na verdade muito. Eu entro em novas codebases mais do que faço cortes de cabelo. E costumava ser uma das partes mais difíceis do trabalho, mas agora que tenho um método, eu realmente gosto disso. Pode me chamar de louco, mas independente do tipo de desenvolvedor que você seja, em algum momento você vai precisar aprender uma codebase existente. Pode ser um dev iniciante entrando em um emprego, um desenvolvedor experiente mudando de time ou empresa, ou um contribuidor open source tentando entender o projeto antes de contribuir.

Neste vídeo quero mostrar como aprendo novas codebases usando o **Excalidraw** como exemplo — um projeto React + TypeScript, interativo e divertido de explorar.

---

## 1. Leia a Documentação

O primeiro passo é ler a documentação da codebase. Clone o repositório, instale as dependências, inicie o servidor e leia tudo que estiver disponível: guia de contribuição, convenções de nomenclatura, prefixos semânticos para commits, schema JSON, atributos e valores.

Você pode não entender tudo de primeira — e tá ótimo. Pense como quando um professor manda ler o capítulo antes da aula: você tem uma primeira impressão do conteúdo. Quando depois você começa a codar e explorar, vêm os momentos de "ah, lembro de ter lido sobre isso!". A cada nova exposição ao mesmo conceito, a compreensão se aprofunda. Quanto mais impressões com a codebase, melhor.

---

## 2. Use o Software Como Usuário Final

Antes de mergulhar no código, use a aplicação como usuário final. No caso do Excalidraw: desenhe, apague, mude o tema, explore os modos. Isso dá contexto para tudo que você vai ver no código depois.

---

## 3. Explore o Código com Intenção

Não fique navegando aimlessly pelo código. Explore com propósito. Por exemplo:

- Você usou o apagador na aplicação → vá ao código e encontre onde o apagador é tratado.
- Encontrou `appstate.activeTool.type === 'eraser'` → siga o fio para entender o fluxo.

Perguntas úteis para guiar a exploração:
- Quando desenho um retângulo, qual código é acionado no `mouseDown`?
- Onde o elemento é adicionado ao estado?
- Quais componentes re-renderizam?
- Onde o undo é disparado?

Depois responda indo até os arquivos reais. Isso cria um **modelo mental claro do fluxo de dados** — algo que ajuda muito a visualizar o funcionamento interno enquanto você usa a aplicação.

---

## 4. Complete Tarefas Reais

Peça ao seu time uma tarefa como ponto de entrada na codebase — algo que toque componentes centrais, não periféricos. Isso te faz contribuir de verdade enquanto aprende as partes mais importantes.

Se for contribuidor open source, pergunte aos mantenedores qual seria uma boa primeira issue. Se estiver aprendendo sozinho, invente uma tarefa com esse critério:

> "Qual feature pequena toca o core da aplicação e me força a entender o fluxo principal?"

Exemplo do vídeo: adicionar uma opção de retângulo com bordas arredondadas — isso força o desenvolvedor a entender como formas são criadas, adicionadas ao estado e renderizadas.

---

## 5. Escreva Testes

Escrever testes é uma das melhores formas de aprender uma codebase. Você precisa entender o comportamento esperado do código para testar corretamente — e quando algo quebra, você aprende ainda mais.

---

## 6. Pair Programming

- Assista como colegas que conhecem a codebase trabalham: como navegam, quais ferramentas usam, quais testes escrevem.
- Depois faça pair programming ativo com eles.
- Não tenha medo de parecer iniciante. O objetivo não é parecer inteligente — é ficar inteligente o mais rápido possível.

---

## 7. Anote Tudo

Enquanto explora, anote:
- Dúvidas que surgirem.
- Coisas que acha que entendeu (para verificar depois).
- Gaps de entendimento.

Depois pergunte a um colega ou **explique o que você entendeu para ele e peça para te testar**. Ensinar é uma das formas mais eficazes de consolidar conhecimento.

---

## 8. Entenda o Domínio

Software é construído para algum propósito. Entenda esse propósito:
- Construindo para designers? Aprenda como designers trabalham.
- Plataforma de trading? Estude os fundamentos de mercados financeiros.

Entenda também o **"por quê"** por trás das tarefas que você recebe — o contexto de negócio e a decisão técnica. Isso melhora suas decisões arquiteturais e acelera o problem-solving no futuro.

---

## 9. Repita o Ciclo

Depois de passar por tudo isso, recomece:
- Releia a docs — agora você vai entender muito mais.
- Use o app de novo — vai enxergar o código por trás de cada interação.
- Explore o código com mais contexto.
- Continue contribuindo.

Com o tempo, ao usar a aplicação, você vai **visualizar naturalmente o código que está rodando por baixo**. Isso é quando a codebase começa a fazer sentido de forma profunda.

---

## 10. Contribua com a Documentação

Quando se sentir confortável, contribua de volta:
- Adicione diagramas ou fluxogramas que te ajudaram.
- Escreva guias internos.
- Documente o que estava faltando quando você chegou — para facilitar a vida do próximo.

---

## Resumo do Método

| Etapa | Ação |
|-------|------|
| 1 | Leia toda a documentação disponível |
| 2 | Use o software como usuário final |
| 3 | Explore o código com intenção (siga o fio de features específicas) |
| 4 | Complete tarefas reais que toquem o core |
| 5 | Escreva testes para verificar sua compreensão |
| 6 | Faça pair programming (observe primeiro, depois participe) |
| 7 | Anote dúvidas e ensine o que aprendeu |
| 8 | Entenda o domínio do negócio |
| 9 | Repita o ciclo com mais profundidade a cada volta |
| 10 | Contribua com a documentação |

> A meta não é aprender passivamente ao longo de meses. É dar o melhor ponto de partida possível nas primeiras semanas — porque isso define a qualidade do seu trabalho nos meses seguintes.
