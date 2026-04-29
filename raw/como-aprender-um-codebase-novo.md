# Como Aprender um Codebase Novo

> Transcrição adaptada de vídeo sobre o método de aprender codebases desconhecidos.
> Demonstração prática usando o Excalidraw (React + TypeScript, open source).

---

## Contexto

Aprender codebases novos é algo que acontece o tempo todo — seja você um dev júnior entrando num emprego, um dev experiente trocando de time ou empresa, ou um contribuidor de open source tentando entender o projeto antes de contribuir. Antes era uma das partes mais difíceis do trabalho. Com um método, vira algo que você passa a gostar.

---

## O Método — Visão Geral

1. Leia a documentação
2. Use o software como usuário final
3. Explore o código com intenção
4. Complete tarefas reais (atribuídas por colegas ou auto-atribuídas)
5. Faça pair programming
6. Anote tudo e ensine o que aprendeu
7. Repita — cada ciclo aprofunda a compreensão

---

## 1. Leia a Documentação

Leia tudo que estiver disponível:

- README
- Docs de contribuição (CONTRIBUTING.md)
- Guias de arquitetura
- JSON schema, atributos e valores de configuração
- Convenções de nomenclatura e prefixos semânticos de commit

**Por que ler mesmo sem entender tudo?**

É como ler o próximo capítulo antes da aula. Você não vai entender tudo, mas o conteúdo fica na sua cabeça. Quando o professor (ou o código) apresentar aquilo de novo, você vai ter um momento de *"ah, lembro disso"* — e vai conseguir fazer perguntas mais inteligentes. Cada exposição ao mesmo conceito aprofunda o aprendizado.

**Na prática:**

```bash
# Clone o repo
git clone <url>

# Instale as dependências
yarn install  # ou npm install

# Suba o servidor
yarn start

# Rode os testes para ver o estado atual
yarn test

# Reformate os arquivos (se disponível)
yarn prettier
```

Execute cada comando disponível no package.json ou Makefile. Veja o que cada um faz.

---

## 2. Use o Software Como Usuário Final

Antes de entrar no código, use o produto. Entenda o que ele faz do ponto de vista de quem usa.

No caso do Excalidraw: desenhe, apague, redimensione, mude tema, ative o modo zen, troque fontes, faça upload de imagem.

**Por que isso importa?**

Quando você voltar ao código, vai conseguir mapear ações do usuário a fluxos de código. Vai visualizar o que cada função está fazendo. Isso constrói um modelo mental muito mais sólido do que só ler código no vácuo.

---

## 3. Explore o Código com Intenção

Não fique vagando pelo código sem objetivo. Explore com uma pergunta específica em mente.

**Exemplo de pergunta com intenção:**

> *"Quando eu desenho um retângulo no Excalidraw, qual código roda no mouse down? Onde o shape é adicionado ao estado? Quais componentes re-renderizam? Onde o undo é acionado?"*

Com essa pergunta, você vai descobrir:
- `onPointerDown` em `app.tsx` — evento principal de mouse down
- `createGenericElement` — cria o novo elemento retângulo
- Estado atualizado em `onMouseMove` conforme você arrasta para dimensionar
- Undo controlado pelo histórico de estado

Esse tipo de rastreamento te dá um **modelo mental claro do fluxo de dados** — como a informação entra, por onde passa e onde termina.

**Dica:** combine exploração do código com o uso do app ao mesmo tempo. Use o app, observe o que acontece, depois vá ao código ver como aquilo funciona.

---

## 4. Complete Tarefas Reais

Esse passo é o que mais acelera o aprendizado. Peça a um colega de time uma tarefa que sirva como **bom ponto de entrada** no codebase — algo que toque componentes-chave, não só periféricos.

Se você não tem colega (open source, por exemplo), pergunte aos maintainers ou contributors: *"Quero aprender o codebase e contribuir. Qual seria a melhor primeira tarefa?"*

Se não tiver ninguém para perguntar, **invente uma tarefa** com essa mesma lógica:

> *"Adicionar opção de retângulo com bordas arredondadas à ferramenta de retângulo."*

Isso vai te obrigar a entender exatamente quais arquivos precisam ser tocados, como as ferramentas são registradas, como o estado é atualizado — tudo que importa.

**Escrever testes** também é uma forma excelente de aprender. Verificar seu entendimento do código escrevendo testes para ele, e se você quebrar algo, ainda melhor — você vai aprender por que quebrou.

---

## 5. Pair Programming

Pair programming é um dos melhores aceleradores para aprender um codebase.

**Como fazer:**

1. **Primeiro:** olhe sobre o ombro de alguém que já conhece o codebase. Observe como ela navega, como usa o app enquanto programa, quais testes escreve, como busca o que precisa.
2. **Depois:** faça pair programming de verdade, contribuindo ativamente.

Não tem nada a ver com parecer esperto. Tem tudo a ver com **ficar esperto o mais rápido possível**. Admitir que não sabe X ou Y é exatamente como você aprende X e Y.

---

## 6. Anote Tudo e Ensine o que Aprendeu

Enquanto você faz tudo isso:

- Anote dúvidas, coisas que não entende, e coisas que **acha que entende**
- Explique seu entendimento para um colega e peça que ele corrija onde você está errado
- Ensinar é a forma mais eficaz de identificar onde estão seus gaps

**Aprender o codebase não é algo que acontece passivamente ao longo de meses.** Com esforço concentrado nas primeiras semanas, você consegue um head start enorme. Seis meses depois, a diferença vai ser significativa.

---

## 7. Repita

Leia a documentação de novo. Agora você vai entender muito mais.

Use o app de novo. Agora você vai conseguir visualizar o código rodando enquanto interage.

E quando se sentir confortável, **contribua com a própria documentação**: adicione diagramas, fluxogramas, guias internos — o que teria te ajudado quando você chegou. Isso ajuda o próximo dev que vai estar exatamente onde você estava.

---

## Bônus: Entenda o Domínio

Software é construído para resolver algo. Entenda o quê.

- Construindo para designers? Aprenda como designers trabalham.
- Construindo uma plataforma de trading? Aprenda o básico de mercados financeiros.
- Construindo para médicos? Entenda o fluxo clínico.

Entender o domínio te ajuda a entender **o porquê** das decisões técnicas — e te torna muito melhor em tomar decisões arquiteturais no futuro.

---

## Resumo do Método

| Passo | O que fazer |
|---|---|
| 1 | Leia toda a documentação disponível |
| 2 | Use o software como usuário final |
| 3 | Explore o código com perguntas específicas e intencionais |
| 4 | Complete tarefas reais (ou auto-atribuídas) — escreva testes |
| 5 | Pair programming — observe, depois contribua |
| 6 | Anote tudo, ensine o que aprendeu, corrija os gaps |
| 7 | Repita — cada ciclo aprofunda o modelo mental |
| + | Entenda o domínio do negócio por trás do software |
