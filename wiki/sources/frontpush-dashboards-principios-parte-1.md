---
type: source
title: "Princípios de dashboards, parte 1: hierarquia visual, fluxos definidos, gráficos coerentes e pesquisa com o usuário (FrontPUSH)"
aliases: ["FrontPUSH dashboards aula 04", "DashClass aula 04", "04: Princípios pt.1", "princípios de dashboard parte 1", "o que considerar em dashboards"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [dashboard, ui-design, ux-design, hierarquia-visual, contraste, posicionamento, escala, fluxos, caminho-feliz, foco, wizard, stepper, login, recuperacao-de-senha, login-social, graficos, visualizacao-de-dados, grafico-de-pizza, grafico-de-linha, grafico-de-barras, filtros, pesquisa-com-usuario, levantamento-de-requisitos, material-design]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-dashboards-principios-parte-1.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-24
---

# Princípios de dashboards, parte 1: hierarquia visual, fluxos definidos, gráficos coerentes e pesquisa com o usuário (FrontPUSH)

## TL;DR

Quarta aula (cerca de 18 min) do módulo de dashboards do [[wiki/entities/frontpush|FrontPUSH]], desenhada à mão num iPad. A pergunta é "o que considerar em dashboards?", e a resposta parte de um problema: dashboards "são muito cheios de [...] informações", e "um dos principais exemplos de bad UX [...] é quando você tem muitas informações na sua tela". No quadro, quatro itens apontam para "informações":

- **Hierarquia visual:** o mais importante, definido "com o usuário", ganha mais [[wiki/concepts/contraste]], fica "o mais alto possível e mais à esquerda possível" e num card maior. A home de um dashboard é o lugar dos resumos ([[wiki/concepts/hierarquia-visual]]).
- **Fluxos definidos e uma tela para cada:** "não colocar tudo para resolver em uma tela só". Cada fluxo tem um objetivo, "uma ação no centro da tela", "step by step", dizendo "são tantos passos" e em qual o usuário está. Uma tela cheia de ações é "template de resumo, não é um fluxo" ([[wiki/concepts/fluxos-bem-definidos]]).
- **O exemplo do login:** a tela inicial abre vários fluxos: sucesso ("o usuário não fez nada de errado"), senha errada, esqueci a senha, criar conta, entrar com Google, GitHub ou Facebook. No [[wiki/entities/dash-class|DashClass]], "passo 1 de 3, recuperar senha", por e-mail ou telefone, com código e nova senha ([[wiki/concepts/caminho-feliz]]).
- **Gráficos coerentes:** "cada gráfico [...] vai servir para poder comparar uma informação determinada": pizza para porcentagem, linha para meses, linhas sobrepostas com contraste para comparar, e filtros para decidir. Promete um documento do [[wiki/entities/material-design|Material Design]] sobre isso ([[wiki/concepts/escolha-de-grafico]]).
- **Pesquisa com o usuário:** "inerente a todo esse processo": no levantamento de requisitos, perguntar "qual que é o aspecto mais importante para você?", mostrar o fluxo "em sucessivas reuniões" e entender o dia a dia ([[wiki/concepts/pesquisa-com-usuario]]).

## Key Claims

### O problema: informação demais

- "Dashboards são muito cheios de [...] informações. E um dos principais exemplos de bad UX [...] é quando você tem muitas informações na sua tela." Exemplo: "dashboards mais antigos [...] de vendas", sistemas genéricos vendidos ou gratuitos para controlar finanças e fluxo de caixa ([[wiki/concepts/densidade-de-informacao]], [[wiki/concepts/carga-cognitiva]]).
- Ele vai mostrar, além do desenho, "alguns artigos que eu deixo aí no Notion" e a prática no DashClass.
- Quadro: "O que considerar em dashboards? Hierarquia visual; gráficos coerentes; fluxos definidos e uma tela p/ cada; pesquisa c/ usuário", tudo ligado por setas a "informações".

### Hierarquia visual

- "Você tem que se lembrar bem de quais são os princípios de uma hierarquia visual." O primeiro é o contraste: "aquilo que é mais importante, você define com o usuário", a informação que "ele tá sempre utilizando com mais frequência", e "você vai colocar essa informação com mais contraste" ([[wiki/concepts/contraste]]).
- Além da cor: **posição**. "Eu sempre vou tentar deixar essa informação [...] o mais alto possível e mais à esquerda possível", "porque eu sempre vou ler as informações de cima para baixo e da esquerda para direita."
- **Tamanho**: "aquilo que é maior eu enxergo primeiro"; "se eu quero dar mais contraste para uma determinada informação, eu vou colocar ela num card maior do que os outros". O card no alto, à esquerda e maior "tem um grau de hierarquia maior" ([[wiki/concepts/hierarquia-visual]]).
- O que vai em destaque: "o CEO de uma determinada empresa, quais são os principais dados que eles utilizam [...] para poder fazer a tomada dessas decisões? Eu tenho que deixar isso mais destacado possível."
- "A home dentro de dashboard, geralmente, é um lugar onde a gente coloca os resumos [...] um resumo geral dos gráficos, uma visão geral" ([[wiki/concepts/dashboard]]).
- Em landing page já se usava hierarquia; aqui, "com números, com gráficos, [...] com fluxo de caixa, com 300 coisas na tela do usuário", ela precisa ser "bem mais aprimorada".

### Fluxos bem definidos

- "Basicamente, é você não colocar tudo para resolver em uma tela só." Mesmo com hierarquia "maravilhosa" (escala, cor, posição), "se você não colocar fluxos definidos, você também vai confundir o usuário" ([[wiki/concepts/fluxos-bem-definidos]]).
- Na tela de login, imaginar "o que que esse usuário [...] vai fazer": e-mail ou user e senha. "Tem o fluxo do sucesso, que eu sempre digo assim, que o usuário não fez nada de errado" ([[wiki/concepts/caminho-feliz]]). Outros: esqueci minha senha; logar com Google, GitHub, Facebook. "Você tem que tentar imaginar quais são todos esses fluxos. E dividir eles da melhor maneira possível."
- "Quando você define, você isola mais e você dá uma característica para a tela, que é o famigerado foco."

### Foco: uma bolinha ou várias

- Uma tela com uma bolinha azul: "você vai olhar para essa bolinha". Com várias bolinhas de tamanhos e hachuras diferentes, "você já confundiu o usuário": cada bolinha "é uma ação, nessa aqui é outra, nessa aqui é outra".
- "Esse template que eu desenhei para vocês, geralmente é um template de resumo, não é um fluxo. É simplesmente uma tela inicial para iniciar um fluxo."

### Uma ação por fluxo, passo a passo

- "Fluxo, a gente detém de uma ação só." Esqueci minha senha "tem todo um fluxo e ele é todo direcionado, sempre com uma ação no centro da tela [...] step by step".
- Dizer o total e a posição: "step 1", "são quantos passos ao total? São 5. Eu já digo para ele quantos passos são." Exemplos: três passos para o login com conta pessoal, dois com o Google, cinco para o cadastro ([[wiki/concepts/poder-da-barra-de-progresso-e-do-check]]).
- Fim do fluxo: "Você concluiu. Tudo certo. Cadastrado." Ou: "deu um erro. Qual que é o erro? Procure o administrador, tenha tal contato, verifique seu e-mail, verifique o SMS" ([[wiki/concepts/feedback-do-sistema]]).

### O fluxo de login no DashClass

- A tela de login "é uma tela inicial, que pode iniciar o fluxo para diversos jeitos": sucesso, senha errada, esquecer a senha, criar conta, Google, Facebook, "e dentro de cada um desses pode ter subfluxos". Em todos, "é uma ação centralizada".
- Recuperar senha: "Passo 1 de 3"; dois subfluxos, e-mail ou telefone; código de verificação por e-mail ou SMS; "você pode cancelar, você pode voltar"; nova senha com conferência; "criada a nova senha e eu redireciono ele para a página inicial".
- "Esse é um fluxo, você tem que pensar em todos os outros fluxos."

### Gráficos coerentes

- Ele vai mostrar "um documento do Material Design em que, de acordo com o número, da escala do número, do que que você está apresentando, o gráfico muda" ([[wiki/entities/material-design]]).
- "Nós temos gráfico de barra, [...] de pizza, [...] de linha [...] Cada gráfico, ele vai servir para poder comparar uma informação determinada" ([[wiki/concepts/escolha-de-grafico]]).
- Pizza para porcentagem: "tantos por cento das nossas vendas são destinadas a tal setor", para ver "onde é que está concentrada a maior parte das minhas vendas" e decidir onde investir. "Faria pouco sentido eu, talvez, mostrar esse tipo de gráfico em barras" (ver Precisões).
- Linha para meses: picos e quedas ("por que que em fevereiro caiu em relação a janeiro?"), cruzando com datas comemorativas ("por que que no dia das mães a minha empresa vende mais?").
- "Um ponto que é muito importante para poder a gente realizar tomada de decisão é aplicar filtros nos gráficos." Uma segunda linha sobreposta, nos mesmos meses, exige "estabelecer contraste entre eles dois para poder conseguir visualizar e ter parâmetros para poder comparar".

### Pesquisa com o usuário

- "Inerente a todo esse processo": no levantamento de requisitos de um dashboard, "sempre pergunte ao usuário, qual que é o aspecto mais importante para você?" ([[wiki/concepts/pesquisa-com-usuario]], [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]).
- "Em sucessivas reuniões, é interessante você mostrar, perguntar a opinião dele e, literalmente, qual o dia a dia seu, o que você mais faz", para "definir o posicionamento daquilo que você está querendo construir" com hierarquia, gráficos coerentes e fluxos definidos ([[wiki/concepts/briefing]]).
- Outros princípios ficam para as próximas aulas.

## Precisões e ressalvas

1. **Pizza não ganha de barras.** `[skill: ux-ui-mentor]` Pelo ranking de Cleveland & McGill (1984), que a referência `dados-dashboards.md` reproduz, posição em escala comum (barras) é lida com mais precisão que ângulo (pizza); "substituir um gráfico de pizza por barras quase sempre melhora a precisão de leitura", e pizza só vale para 2 ou 3 categorias com diferenças claras (máx. 5 fatias). A tabela da skill admite pizza, donut ou barra empilhada para "composição de um todo". Então pizza para porcentagem é aceitável, mas "faria pouco sentido [...] em barras" está invertido: barras costumam ser a escolha mais segura. O próprio painel do DashClass mostra vendas por categoria em barras (alta).
2. **Linhas sobrepostas têm limite.** `[skill: ux-ui-mentor]` Duas linhas com contraste funcionam; com muitas, a referência sugere *small multiples* (Tufte): um gráfico pequeno por série. Também evitar dois eixos Y e eixo Y que não começa em zero quando a comparação é de grandeza (alta).
3. **"Alto e à esquerda" é leitura ocidental.** Vale para línguas LTR; em árabe ou hebraico, o ponto de entrada é o canto superior direito. A mentoria de UI Design já tratava disso com a leitura em Z e em F ([[wiki/concepts/hierarquia-visual]]) (alta).
4. **Hierarquia não é só contraste de cor.** A fala diz "e é só contraste na cor", mas o resto do trecho ("além disso, tem outras formas") lista posição e tamanho; provavelmente faltou um "não". O texto em `raw/` ficou literal.
5. **Uma tela para cada fluxo, não para cada passo.** `[skill: ux-ui-mentor]` A referência `formularios.md` recomenda wizard só para formulário longo ou com etapas naturais, sempre com "Etapa 2 de 4", voltar sem perder dados e indicador de progresso. Para formulário curto, uma tela basta. O "passo 1 de 3" do DashClass segue isso; o "cinco passos para o cadastro" pode ser demais se cada passo tiver um campo só (inferência, média).
6. **Entrar com Google é OpenID Connect.** O "logar com o Google, GitHub, Facebook" é login social: autenticação por [[wiki/concepts/openid-connect]], que roda sobre [[wiki/concepts/oauth2]]. O "dois passos" é a parte visível; o resto acontece no provedor (alta).
7. **Erro com saída.** O fim do fluxo com "procure o administrador [...] verifique o SMS" segue a heurística de Nielsen de ajudar a reconhecer e recuperar erros: dizer o que aconteceu e o que fazer (alta).
8. **Nomes reconstruídos da legenda:** "Dash Class" → DashClass, "rachurada" → hachurada (5×), "Recuperar 100" → recuperar senha (média-alta), "prosta" → proposta. Ficaram literais: "Do, vem pra mais tarde", "O que que mais a parte do topo, o CEO", "e é só contraste na cor".

## Entities

- [[wiki/entities/nasser]]: instrutor; aula desenhada no iPad (o quadro mostra o Procreate com a paleta "FrontPUSH 2.0").
- [[wiki/entities/dash-class]]: fluxo de recuperação de senha como exemplo.
- [[wiki/entities/material-design]]: documento de gráficos prometido.
- [[wiki/entities/frontpush]]
- Sem página própria: Google, GitHub e Facebook (como provedores de login), Notion.

## Concepts

- [[wiki/concepts/fluxos-bem-definidos]] (novo), [[wiki/concepts/escolha-de-grafico]] (novo), [[wiki/concepts/pesquisa-com-usuario]] (novo)
- [[wiki/concepts/hierarquia-visual]], [[wiki/concepts/contraste]], [[wiki/concepts/densidade-de-informacao]], [[wiki/concepts/carga-cognitiva]]
- [[wiki/concepts/caminho-feliz]], [[wiki/concepts/poder-da-barra-de-progresso-e-do-check]], [[wiki/concepts/feedback-do-sistema]]
- [[wiki/concepts/openid-connect]], [[wiki/concepts/oauth2]]
- [[wiki/concepts/dashboard]], [[wiki/concepts/patterns-de-dashboard]]
- [[wiki/concepts/briefing]], [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]

## Open Questions

- Qual é o documento do Material Design sobre gráficos? Provavelmente a seção de data visualization do Material 2; fica para a aula em que ele o mostrar.
- Quais são os "artigos" sobre dashboards deixados no Notion?
- O quadro diz "uma tela p/ cada" fluxo; isso vale também para os fluxos internos do painel administrativo (adicionar usuário, novo curso)?

## Raw Quotes

- "Um dos principais exemplos de bad UX [...] é quando você tem muitas informações na sua tela."
- "Basicamente, é você não colocar tudo para resolver em uma tela só."
- "Esse template [...] geralmente é um template de resumo, não é um fluxo."
- "Fluxo, a gente detém de uma ação só."
- "Qual que é o aspecto mais importante para você?"
