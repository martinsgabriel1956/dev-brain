# Ninguém Mais Revisa o Código da IA — Como Migrar de "Eu Reviso" para "Eu Não Reviso"

> Transcrição de vídeo (Augusto Galego, "Galego"), reação a um tweet de Uncle Bob e a argumentos de Boris (criador do Claude Code) e Lucas Montano. Limpa e organizada a partir do áudio original em português.

## Abertura: o tweet controverso de 2026

"Quais métricas você está utilizando para medir o sucesso desse approach?" — "I read the code." "Eu leio o código." Esse tweet foi controverso em 2026, e vale a pena falar sobre ele.

Em 2026, ninguém mais revisa o código da IA. Na verdade, algumas pessoas revisam — mas o fenômeno é o seguinte: temos o nosso queridinho **Fable 5** e amigos (Fable 5 e similares, ou GPT 5.6 Sol, Química 3), e dá para dizer sem medo de ser polêmico que esses modelos são de fato melhores do que a maioria dos engenheiros.

Se você me dá uma tarefa, ou dá a mesma tarefa pro Fable, na relação entre qualidade e velocidade o Fable vai ser mais rápido que eu. Talvez eu entregue com mais qualidade, com mais carinho — mas o Fable vai entregar muito mais feature, muito mais rápido, e provavelmente com qualidade adequada. O mesmo vale pro GPT Sol e pro Química 3.

O resultado prático: isso gera uma quantidade **enorme** de código. Tão grande que as pessoas não têm tempo sequer de revisar tudo. E o desfecho óbvio é a nossa manchete: ninguém mais está revisando o código da IA. O código está sendo mergeado sem revisão.

## A exceção: quando o dinheiro está em jogo

Pessoalmente, na empresa em que trabalhei nos últimos meses, era muito verdadeira a frase "quem tem alguma coisa tem medo" — a gente revisava todo o código. Mas o cenário era específico: uma empresa de pagamentos, que mexe muito com dinheiro e pouco com features.

O que a gente precisava oferecer era **velocidade, robustez e usabilidade simples**. Não fazia sentido gerar tanto código, tanta feature — robustez era muito mais importante. E quando você tem potencial de causar prejuízos multimilionários no cliente, você toma muito cuidado com todo merge. Por isso a gente revisava todo o código do core business, sempre.

Mas o meu caso não é o caso de todo mundo. O caso da maioria está muito mais próximo do Uncle Bob: "eu não reviso o código escrito por agentes."

## Se ninguém revisa código, o que a gente faz no lugar?

Uncle Bob propõe avaliar, no lugar da leitura linha a linha:

- **Cobertura de testes** (code coverage)
- **Estrutura das dependências**
- **Complexidade ciclomática**
- **Tamanho dos módulos**
- **Testes de mutação** (mutation testing)

A partir dessas métricas, ele deixa o código pra IA, porque julga que a IA é mais rápida que os humanos — e de fato é, escrever código é muito mais rápido.

O argumento é uma mudança de metáfora: antes a gente via código como cultivar um **jardinzinho**, olhando planta por planta. Hoje a gente vê como uma **fazenda industrial** — não olhamos cada planta individualmente; medimos a qualidade do solo, do ar, do adubo. As plantas crescem, e depois a gente colhe com trator.

### O que eu acrescentaria à lista

Além de coverage e mutation testing:

- **Testes para prevenir regressão**
- **Testes end-to-end**

Esses "modelos" não existem como categorias fixas — a ideia é ter testes que meçam cobertura, façam mutação, previnam regressão e validem o funcionamento ponta a ponta.

### Por que essas métricas: elas são objetivas

Todas têm **algum grau de objetividade**, dá pra mensurar:

- **Testes** — ou passam, ou não passam; ou executam uma linha, ou não executam. Critério numérico.
- **Estrutura de dependências** — objetivo: dá pra plotar num grafo e ver dependência circular, ver se a injeção faz sentido.
- **Tamanho dos módulos** — objetivo: número de linhas. Talvez não seja a melhor métrica, mas é objetiva.
- **Complexidade ciclomática** — parece um grafo; quanto mais fluxos, mais poluído, pior. Perfeitamente mensurável, dá pra dizer "nunca faça função com CCN acima de X". 100% objetivo.

A partir disso, a gente **infere** a qualidade do código.

## O limite: métrica boa não garante código bom

Você vai dizer: "Galego, dá pra mensurar tudo isso, mas isso não quer dizer que o código está bom." Concordo. Você tem uma **probabilidade** de o código estar bom — mas pode ser que esteja uma porcaria mesmo com todas as métricas verdes.

Por isso o tweet do Uncle Bob é bom, mas **não é suficiente por si só**.

A melhor maneira de saber se o código está bom ainda é ler o código. "I read the code." Supondo que você seja um humano com boa capacidade de comunicação e interpretação, você consegue ler um código e me explicar por que ele não está bom. E se consegue explicar, consegue **escrever** essa explicação. E se consegue escrever, consegue colocá-la num `CLAUDE.md`, num `review.md`.

## Boris (criador do Claude Code): documentação como o novo trabalho

É o que Boris argumenta: **todos os times deveriam estar escrevendo `CLAUDE.md`, `review.md`, skills e docs** que permitam que agentes trabalhem produtivamente na code base com zero contexto adicional de quem está promptando.

Estamos vendo uma migração — há muita resistência, mas eu enxergo que esse é o caminho do futuro. Não importa se eu gosto ou acho certo; acho que é o futuro. Posso estar errado — ninguém é expert nisso. Esses desenvolvimentos são tão recentes que é impossível ter um expert: expertise leva anos, e isso é um acontecimento de 2026. Existem experts em controle de qualidade de código, e experts em criar IA, mas quase ninguém fez as duas coisas juntas por muitos anos.

Outro ponto de Boris: no passado, os melhores engenheiros passavam muito tempo **automatizando** a forma como trabalham — automatizar é criar processos repetíveis, que vivem em regras de lint, regras de CI, rotinas. Agora ficou muito mais barato automatizar vários tipos de coisa. Definir regras, definir padrões, escrever documentação, analisar dependências / complexidade ciclomática / limites entre serviços — tudo isso se torna parte mais relevante do trabalho.

## Lucas Montano: o Quality Gate

Isso vai ao encontro do que o Lucas Montano falou. Para resolver todas as conversas de um PR depois de endereçar os comentários (acompanhar no GitHub quais comentários já foram implementados), ele criou o **Quality Gate**: a IA fica automaticamente corrigindo e corrigindo.

Ele tem vários **baselines** — a base que serve de referência de melhorias no momento em que você coloca um quality gate num projeto que nunca teve controle de qualidade. Você mensura, constrói o ferramental, constrói a skill, e coloca um agente em loop fazendo **babysitting** do pull request. O PR só pode ser mergeado se preencher uma série de pré-requisitos objetivos e descritíveis.

Você pode inclusive ter um **revisor que usa o seu `CLAUDE.md` e o seu `review.md`** para ver se o PR se adequa às estruturas e instruções. Nunca terá 100% de assertividade na IA — mas também nunca terá 100% num humano. Então dá pra usar `CLAUDE.md` + `review.md` como input de um review automático do PR, com uma IA vestindo o papel de revisor: "isso aqui está legal, isso não está, corrige." Assim você cria sua fazenda automatizada de código.

## Paulo Tarso: colocando em prática

É um movimento crescente nas empresas, com vários artigos surgindo. Tem o artigo do **Paulo Tarso** (brasileiro, publicado em inglês e português) que detalha tecnicamente: métrica de cobertura, complexidade ciclomática, tamanho de módulos, teste de mutação — e como implementar cada uma. É claramente baseado no tweet do Uncle Bob, mas mostra gente colocando isso em prática.

Mentalidade a fixar: **"eu estou cultivando um ambiente que vai produzir código bom"**. É diferente de "eu produzo código bom" — a meta é cultivar um ambiente em que código bom é a única possibilidade.

O nome disso é **engenharia de software**. O livro que descreve várias dessas coisas é *Extreme Programming* (por volta de 1999–2001). Faz 25 anos que esses conceitos existem — e a prova viva de que são bons é que agora, com código barato/rápido/fácil de produzir em grande quantidade, todo mundo está falando deles de novo.

## Guidelines para o período de transição

Não é sensacionalismo: ninguém vai parar de revisar código do dia pra noite, nem implementar tudo isso "do dia zero". As empresas não podem adotar isso na correria. "Quem tem coisa tem medo" — e você deve ter medo, isso é bom. A melhor forma de errar é errar quando o erro é pequeno e inconsequente. Não faça isso na empresa inteira de um dia pro outro.

Se hoje você revisa 100% do código e quer transicionar, comece avaliando **duas coisas: risco e dificuldade/complexidade**.

### Matriz de risco × dificuldade

1. **Baixo risco + baixa dificuldade** → alta probabilidade de a IA acertar, e se der errado não há problema grande. Esse é o **primeiro tipo de PR** a permitir **merge automático sem revisar o código** — *desde que* exista um teste garantindo que os fluxos com que esse código interage estão funcionando. Sem esse teste, esqueça o merge automático.

2. **Risco médio + complexidade média** → use **amostragem (sampling)**. Pegue amostras do código; olhe principalmente **testes e docs**, porque teste e doc dizem a intenção, e a IA vai seguir quase à risca a intenção (com alguns errinhos aqui e ali). Olhe trechos do código e use isso para informar melhorias no seu `CLAUDE.md` / `review.md`. (Falo `CLAUDE.md` por hábito — a Anthropic prefere `AGENTS.md`.)

3. **Alto risco** → **revise manualmente**, em pares, em duas/três/cinco pessoas. O que é alto risco: autorização, autenticação, pagamentos, senhas, migração de banco de dados, mudanças de infraestrutura, permissões. Hoje, a maioria das empresas e pessoas **não tem maturidade** — não no sentido de ser adulto, mas de sofisticação do ferramental — para se dar o luxo de não revisar isso.

Aos poucos você vai migrando para esse futuro.

## Fechamento: calma com o hype

A IA faz a gente acreditar que todo mundo está correndo, produzindo as novas empresas multibilionárias com IA. Mas uma coisa eu ainda **não vi**: nenhuma empresa multibilionária feita só com Fable, rodando 300 milhões de agentes em paralelo.

Se 300 milhões de agentes em paralelo conseguissem produzir o que 300 milhões de desenvolvedores produzem em 10 anos — cadê o Figma 2? Cadê o Photoshop 2? Cadê a empresa multibilionária inteiramente construída em cima de IA? Ela não está aqui hoje. E se não está, vamos com calma.

---

## Bloco patrocinado (Abacus AI)

Mencionado como patrocinador: Abacus AI. Na mesma subscription: Fable 5, família GPT (5.6 Sol, Terra, Luna), família Nano Banana (geração de imagem), Química 3 — utilizáveis via API. Permite criar um **Custom Router** (create custom router): a própria API decide quais modelos usar (ex.: Fable para problemas muito difíceis; GPT 5.5 se precisa ser rápido; Gemini 3.5 balanceado; Química 2.7). Plugável no Claude Code / OpenCode, com a harness que quiser. Também citados: "supercuter" rodando Hermes ou open claw; "wed sessions" para rodar vários agentes em paralelo e hospedar o projeto. Recomendação: bom custo-benefício pela quantidade de ferramentas e centralização de várias subscriptions de IA.
