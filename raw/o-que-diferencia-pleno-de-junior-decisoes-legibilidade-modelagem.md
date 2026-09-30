# O Que Diferencia um Dev Pleno de um Júnior — Decisões, Legibilidade e Modelagem (Java)

> Transcrição de vídeo em português (professor de Java, canal não identificado) respondendo à pergunta "o que preciso aprender para me tornar pleno?". Texto limpo e estruturado em seções a partir do áudio transcrito automaticamente; conteúdo mantido fiel ao original. Já estava em português — sem tradução.
>
> **Correções de transcrição aplicadas pelo contexto:** "Springboot" → Spring Boot; "Cafkaa" → Kafka; "Kubernets" → Kubernetes; "chat EPT" → ChatGPT; "extrem dupla" → (programação) em dupla; "desenvolvedor VIP" → cliente VIP; "ifzão is vip" → `if (pedido.isVip())`; "elsces" → elses; "RP" → ERP; "intque" → int quantidade/estoque; "site preço" → `setPreco`; "setoque" → `setEstoque`; "double D" → `double d`; "virtual trades" → virtual threads; "no meu preciso" → trecho incompreensível (sobre novos integrantes herdando o código).
>
> **Trechos incertos:** o vídeo é apresentado com código na tela (método `calcularDesconto` e classe `Produto`) que não aparece na transcrição; a descrição abaixo reflete apenas o que o autor narra. O nome do canal e do autor não constam.

## Introdução: a pergunta recorrente

Pergunta frequente dos alunos: "o que preciso aprender para virar pleno? Estou há 3 anos na empresa e ela não me nota" — situação mais comum do que parece. A resposta típica da internet (ChatGPT, YouTube, influenciadores) é uma lista de tecnologias: Spring Boot, Docker, Kafka, Kubernetes, microsserviços, testes automatizados. O autor concorda que são importantes, mas nenhuma delas transforma o júnior em pleno: frameworks, bibliotecas e ferramentas são **meios** para resolver problemas. O que diferencia o profissional não é a quantidade de tecnologias, e sim **a maneira como toma decisões durante o desenvolvimento**.

## Mesmo time, mesma stack, códigos diferentes

- Em times com mais de um dev, todos usam o mesmo framework, linguagem, biblioteca e até os mesmos requisitos. É comum trabalhar em dupla no mesmo ticket (pleno com júnior, sênior com pleno) para que um supra o outro.
- Quando dois devs da mesma stack entregam, um, um código simples, funcional e de fácil compreensão; o outro, um código com biblioteca de terceiros cheio de problemas, percebe-se a falta de alguma noção: **ambos dominam a sintaxe**, mas a forma de pensar e escrever é diferente.

## Exemplo 1 — `calcularDesconto`

Cenário: plataforma de e-commerce; o gestor/cliente pede que clientes VIP ganhem 15% de desconto no valor final do pedido e todos os demais, 5%.

- **Versão júnior:** método `calcularDesconto(pedido)` retornando `double` (poderia ser `BigDecimal`) com um `if (pedido.isVip())` → `valor * 0.15`, senão `valor * 0.05`. Funciona, é simples, é fácil de manter.
- **O que muda no pleno:** ele já pensa à frente — em alguns meses ou um ano a regra muda. Hoje há cliente VIP; amanhã pode haver cliente **ouro**, **prata**, variação de desconto por **sazonalidade** do produto (exemplo: paçoca vende muito mais em festa junina e deixa de vender em outras épocas). Quando outras regras entram, o método simples vira uma cascata de `else`/`if`. Por isso o pleno **modela o método de outra maneira** desde o início.

## Frase-chave: "o código será muito mais vezes lido do que escrito"

- Projetos tendem a durar anos: talvez você trabalhe numa Netflix (15 anos de mercado) ou num ERP (20 anos). Há transição de pessoas; novos integrantes vão ler o código que você escreveu.
- O júnior pode escrever de forma mais simples, mas precisa tomar certos cuidados; o pleno já percebe isso na forma como escreve.

## Exemplo 2 — nome de variável

- `double d = pedido.getValorTotal() * 0.15;` vs. a mesma linha com nome legível (`valorDesconto`, melhor ainda `valorDescontoPedido`).
- Em um método de 6 linhas, tanto faz. Mas se o método tiver 500 ou 1000 linhas (o que "já estaria errado"), estar na linha 533 com uma variável `d` — cuja declaração ficou longe e que é modificada n vezes — é muito pior do que ver uma variável cujo nome diz o que ela faz. **Nome correto de variável é o que diferencia a forma como as pessoas leem seu código.**

## Exemplo 3 — classe `Produto` e o estado inválido

- Dev menos experiente modela `Produto` com `String nome`, `double preco`, `int estoque`. Compila e funciona.
- Mas a classe dá margem a outro dev do time chamar `setPreco(-30)` (preço negativo) ou `setEstoque(-30)` se houver getters e setters no escopo da classe — algo errado para o negócio.
- Mudança de mentalidade: no início se pensa nas classes **apenas como estruturas de dados**; com o tempo é preciso perceber que elas **representam conceitos do mundo real**. A classe `Produto` parece aceitável à primeira vista, mas do ponto de vista do negócio **aquele objeto (preço negativo) nunca deveria existir**. O dev precisa começar a notar e anotar essas situações.

## Conhecer novidades da linguagem não basta

- Não adianta conhecer todas as novidades da linguagem: isso não transforma ninguém em bom engenheiro. Devs plenos usam os recursos novos **porque entendem qual problema resolvem e quais são as limitações**.
- O autor não diz que não se deva aprender APIs, streams, generics, `Optional`, virtual threads (novidade do Java 25) — diz que é preciso conhecer, mas **a quantidade de tecnologias não destaca ninguém; o raciocínio destaca** — o que fazer para construir código mais legível para quem vai ler.

## Conclusão

- A transição de júnior para pleno **não acontece ao aprender um framework ou adicionar uma tecnologia ao currículo**; acontece quando a **forma de pensar muda**: quando se deixa de escrever código só para resolver o problema atual e se passa a considerar a **evolução maior do sistema** e o fato de que **outras pessoas precisarão entender** o que foi escrito.
- Fechamento: "faça o código direito, não seja preguiçoso, valide, pesquise, entenda a regra de negócio".
- Sobre IA: hoje é comum pedir à IA, receber o código e copiar/colar; não há problema, **desde que você entenda o que ela gera e entenda a regra de negócio do produto**.
- Última lembrança: "o código será muito mais vezes lido do que escrito".
