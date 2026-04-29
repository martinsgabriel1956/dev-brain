# Conceitos que Ninguém Ensina em Curso

date: 2026-04-23
tags: [back-pressure, thundering-herd, temporal-coupling, complexidade-acidental, sistemas-distribuídos, fundamentos]
skill: tech-mentor-system-design
level: intermediário

---

Existem conceitos em programação que ninguém coloca em curso, ninguém cobre em bootcamp, e ninguém explica — até você já ter sido demitido.

Não são os conceitos glamourosos. Não são os que geram thumbnail no YouTube ou post no LinkedIn. São os que separam desenvolvedores que **entendem o que está acontecendo** dos que estão só na esperança.

Aqui estão quatro deles.

---

## 1. Back Pressure

Não, não é um termo de CrossFit.

Back pressure é o que acontece quando seu sistema está **produzindo dados mais rápido do que o receptor consegue processar**.

Imagine uma mangueira de incêndio conectada a uma mangueira de jardim. A água não espera educadamente. Ela recua, transborda, e eventualmente algo quebra de um jeito muito difícil de explicar pro seu gestor.

A maioria dos desenvolvedores já enfrentou isso em produção sem saber o nome. A fila continua crescendo. A memória sobe. O sistema crasha de um jeito inexplicável.

Back pressure é por que o fix correto é:
- **Desacelerar o produtor**
- **Bufferizar com inteligência**
- **Descartar dados deliberadamente**

...em vez de deixar o sistema tomar essa decisão por você — travando.

---

## 2. Thundering Herd Problem

Um daqueles conceitos que parece inventado — até derrubarem seu banco de dados inteiro numa terça de manhã.

O cenário: você tem um cache. O cache expira. E no exato momento em que ele expira, **10.000 requisições simultâneas** decidem que precisam daquele dado e vão direto ao banco de uma vez.

Seu banco, que estava lidando tranquilamente com algumas centenas de requisições por segundo, agora recebe 10.000 ao mesmo tempo. Ele não sobrevive a isso com elegância.

O fix:
- **Cache stampede prevention**
- **Probabilistic early expiration** — expirar levemente antes do prazo, de forma aleatória
- **Request coalescing** — um único rebuilder reconstrói o cache enquanto todos os outros esperam

---

## 3. Temporal Coupling

Uma das fontes mais comuns de bugs quase impossíveis de reproduzir — e de alguma forma ainda mais difíceis de explicar em code review.

Temporal coupling é quando duas partes do sistema **precisam acontecer em uma ordem específica**, mas nada no código **impõe essa ordem**.

- Chame `initialize()` antes de `process()`
- Abra a conexão antes de enviar dados

É implícito. Vive num comentário se você tiver sorte. Na cabeça do desenvolvedor original se não. E em lugar nenhum se esse dev saiu há 6 meses.

O bug só aparece quando alguém faz as coisas fora de ordem — o que sempre acontece. E o erro que a pessoa recebe é completamente sem relação com o problema real.

**A solução não é documentar melhor. É projetar uma API que seja impossível de chamar incorretamente** — não apenas documentada para ser chamada corretamente.

---

## 4. Complexidade Acidental vs. Complexidade Essencial

Conceito de Fred Brooks. Um dos modelos mentais mais úteis que já apliquei a uma codebase.

**Complexidade essencial** é inerente ao problema. Construir um sistema de pagamentos significa lidar com transações que falharam, retries e conciliação. Você não pode fazer isso sumir — o problema é genuinamente difícil.

**Complexidade acidental** é tudo o mais:
- A abstração errada
- Três times tomando três decisões que ninguém reconciliou
- A complexidade que vive numa função de 400 linhas que faz 17 coisas — porque era mais fácil adicionar do que refatorar

A maioria das codebases está afogando em complexidade acidental que foi chamada de *tech debt* e nunca foi paga.

---

## O que esses quatro têm em comum

Nenhum é sobre sintaxe. Nenhum é sobre qual framework ou linguagem usar.

São sobre **entender seus sistemas profundamente o suficiente** para que, quando algo der errado — e vai dar errado — você já saiba onde olhar.
