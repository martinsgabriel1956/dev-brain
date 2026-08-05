---
date: 2026-08-04
tags: [clean-code, uncle-bob, agentes-ia, code-review, tdd, bdd, mutation-testing, module-profundo, arquitetura-de-arquivos, harness]
skill: tech-mentor-ai
type: transcript
---

# O Direito de Não Ler Código (Uncle Bob na Era dos Agentes)

> Transcrição de vídeo de reação a um post no Twitter/X de Robert C. Martin (Uncle Bob), autor de *Clean Code*, sobre não ler mais nenhuma linha de código escrita pelos seus agentes de IA. Transcrição bruta já estava em português — limpa, pontuada e estruturada em markdown, sem necessidade de tradução. Trecho de chamada promocional de workshop (meio do vídeo) mantido resumido, não verbatim.

---

## Introdução: o paradoxo do autor de Clean Code

Robert C. Martin — Uncle Bob, autor de *Clean Code*, o livro que defende que a gente lê muito mais código do que escreve e que por isso ele deve ser extremamente legível — postou na semana passada que não lê mais nenhuma linha de código que os agentes dele escrevem.

Só que tem alguém que ainda lê cada linha, toda vez: o próprio agente. O leitor mudou, mas a gente segue aplicando as mesmas regras que aplicava para leitores humanos. Este vídeo cruza as regras do Clean Code — principalmente a mais famosa, a de código pequeno — com estudos controlados recentes sobre como agentes de IA realmente leem e navegam código. Na segunda metade, o vídeo mostra o que Uncle Bob faz *de verdade* para não precisar ler código e ainda assim confiar nele — e por que os fundamentos que ele defende continuam importantes na era dos agentes.

## Função pequena vs. módulo profundo: um debate antigo que agora tem dados

A regra mais famosa de *Clean Code*: função pequena, faz uma coisa só, idealmente poucas linhas.

John Ousterhout, autor de *A Philosophy of Software Design*, discorda dessa regra desde 2018. O conceito central dele é o de **módulo profundo**: uma interface pequena com muita implementação escondida atrás dela. O oposto é o **módulo raso** — uma função de quatro linhas que, ao ser aberta, não esconde nada; ela só criou mais um lugar para o leitor precisar olhar.

Ousterhout e Uncle Bob debateram isso publicamente por anos, sem chegar a nenhum acordo. A diferença agora é que existe forma de medir isso empiricamente, porque o leitor mudou — é um agente, e o comportamento dele é observável e mensurável.

## Estudo 1: extrair funções pequenas não elimina complexidade, redistribui ela

Em tarefas com código denso — métodos e classes gigantes — quebrar aquele código em helpers menores, no primeiro estudo analisado, deu **empate**. Não mudou o resultado.

A explicação dos próprios autores do estudo: extração de código redistribui a complexidade em vez de eliminá-la. A lógica continua a mesma, só que agora espalhada em vários lugares. Como o agente lê o arquivo inteiro de qualquer forma, essa quebra em si não muda nada para ele.

### Mas houve um caso onde a limpeza ganhou com muita vantagem: 35% menos tokens

A razão não foi o código dentro da função em si — foi o fato de o código ter ficado **grepável**. Quando um bloco grande é quebrado em funções menores e nomeadas, e o agente está fazendo uma busca (por exemplo, planejando uma tarefa e precisando localizar algo relacionado em outros arquivos), ele consegue fazer grep e achar a função mais facilmente.

A vantagem real de refatorar um bloco grande em funções menores dentro do mesmo arquivo, então, não é legibilidade linear — é tornar aquelas funções **acháveis de fora** para o agente, algo que o ser humano lendo sequencialmente não precisava tanto.

## Tamanho de arquivo, separação de responsabilidade e o custo por tool call

Aqui entra uma regra ainda mais interessante: tamanho de arquivo e responsabilidade única.

O agente lê um arquivo por tool call e navega por texto.

- Um arquivo de 1000 linhas com **um assunto só** é uma leitura, e o assunto inteiro está ali.
- O mesmo assunto picado em 10 arquivos são 10 idas e voltas — e cada salto é uma chance do agente perder a linha (o fio da meada).
- Já 1000 linhas com **cinco assuntos diferentes** é uma leitura onde ~80% daquele arquivo é lixo para a tarefa em questão — o agente paga o custo de ler tudo para aproveitar só uma parte.

Isso volta ao módulo profundo de Ousterhout: um arquivo com um ponto de entrada só e uma responsabilidade só é melhor do que vários arquivos separados somados. Combinado com o que já foi visto de Clean Code — métodos nomeados dentro de um arquivo são melhores do que código agrupado sem nenhuma explicação.

Tamanho de arquivo importa, mas por um motivo que não tem a ver com estilo: o `Read` do Claude Code, por exemplo, lê no máximo ~2000 linhas por vez. Na prática, por volta de **1000 linhas é seguro**, **2000 é risco**. Isso não significa otimizar para ter só 50 linhas por arquivo — se há uma responsabilidade só, o que precisa estar ali faz sentido, e o arquivo tem 1000 linhas, está OK.

*(Bloco promocional no vídeo original: chamada para a terceira edição de um workshop avançado de engenharia de software com IA, com convidados de PayPal, iFood e Langwatch, voltado a devs com 3+ anos de experiência — omitido aqui por não ser conteúdo técnico da transcrição.)*

## Estrutura de pastas também tem custo: o Navigation Paradox

Quanto mais arquivos, maior o custo. Seguindo essa linha, estrutura em camadas também custa — e há um segundo paper deste ano, o **Navigation Paradox**, que mediu esse custo do jeito mais direto possível.

Em resumo: uma estrutura com várias camadas que o agente precisa atravessar para implementar uma funcionalidade (múltiplos arquivos — mappers, DTOs, etc.) é muito custosa, e o agente provavelmente vai deixar arquivos para trás no processo. Uma estrutura mais flat é bem melhor, e uma estrutura de **vertical slice por feature** (como o padrão *package by feature* do Go) é ainda melhor, porque é muito mais óbvia tanto para o agente quanto para o ser humano — e é uma estrutura que tem crescido bastante em adoção.

## A parte que ninguém leu no tweet: o que Uncle Bob faz no lugar de ler

A parte que mais importa do tweet do Uncle Bob é a segunda metade, onde ele lista o que faz *no lugar* de ler o código primeiro:

- Teste unitário
- Teste Gherkin
- Procedimento de QA
- Métrica de qualidade
- Mutation test
- "Vários outros"

Parece uma lista de coisas jogadas ali, mas não é: cada item pega um tipo de erro que os outros deixam passar. Isso é harness puro. Item por item:

- **Teste unitário** pega erro de lógica de negócio — principalmente, se o código faz o que diz que faz.
- **Cobertura** pega o buraco: código que nenhum teste encostou.
- **Mutation testing** pega a variação — se o código está otimizado só para um caminho feliz (RPF) ou se ele de fato suporta mudanças de parâmetros.
- **Gherkin/BDD** pega o pior erro de todos: construir a coisa errada, mesmo que construída certo. Não basta construir certo — é preciso garantir que se construiu a coisa certa, do jeito certo.
- **Métrica de qualidade** é o que permite saber se o sistema está piorando ou melhorando ao longo do tempo.

### Gherkin como equivalente da spec em Spec-Driven Development

Para quem usa Spec-Driven Development, Gherkin é muito similar à spec: as regras ficam ali, de forma parecida com o que Uncle Bob faz. Isso permite validar tanto a implementação quanto os testes contra a fonte da verdade que está na spec ou no arquivo Gherkin.

O ponto central não é o formato — é o momento: escrever *antes*. Essa é a única peça do sistema que o agente não derivou da própria cabeça; foi o humano, na própria pesquisa, que colocou ali algo imutável, que o agente tem que seguir. Serve para validar se o harness foi implementado do jeito certo.

## Fechamento: o direito de não ler código é conquistado, não copiado

O direito de não ler código é **conquistado**, não copiado. Pelas próprias palavras de Uncle Bob no Twitch, ele programa desde os anos 60 — trabalha essas coisas há muito tempo, o que permite acelerar bastante esse processo. Não dá para copiar isso da noite para o dia; é preciso fazer mais coisas no próprio código para chegar lá.

### A regra operacional prática

1. Não parar de ler todo o código de uma vez — ir por **classes de mudança**, categorias que vão ficando seguras aos poucos.
2. Escolher uma categoria (por exemplo, um CRUD de admin).
3. Ler todo o PR daquela categoria.
4. Quando acumular ~30 PRs sem quase nenhum feedback a dar, e com harness confiável, marcar aquela categoria como pronta.
5. Ir para a próxima categoria, até que todo o codebase esteja coberto por confiança.
6. Continuar melhorando o harness e o code review ao longo de todo o processo.
7. Durante tudo isso, usar um bom agente de code review para ajudar.
