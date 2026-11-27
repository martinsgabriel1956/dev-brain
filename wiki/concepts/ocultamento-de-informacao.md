---
type: concept
title: "Ocultamento de Informação (Information Hiding)"
aliases: ["information hiding", "ocultação de informação", "information leakage", "vazamento de informação", "back-door leakage", "vazamento pela porta dos fundos"]
date_created: 2026-07-29
date_updated: 2026-11-27
source_count: 6
tags: [arquitetura, complexidade, design, ousterhout, information-hiding, parnas]
skill: tech-mentor-backend
status: stable
---

# Ocultamento de Informação (Information Hiding)

## TL;DR

Técnica central (David Parnas, 1972) para produzir [[wiki/concepts/modulo-profundo|módulos profundos]]: cada módulo deve encapsular uma ou poucas decisões de design (algoritmo, estrutura de dados, formato de arquivo, suposição sobre o domínio), de forma que essa informação fique invisível para o resto do sistema. O oposto — **vazamento de informação** — ocorre quando a mesma decisão se reflete em múltiplos módulos, criando uma dependência entre eles mesmo que nenhum dos dois a exponha publicamente na interface ("back-door leakage").

## Como reduz complexidade

Duas vias, segundo [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, Cap. 5): (1) simplifica a interface — quem usa uma árvore-B não precisa saber o fanout ideal dos nós; (2) facilita evolução — se uma informação está escondida, não há dependências fora do módulo que a contém, então uma mudança de design relacionada a ela afeta só aquele módulo.

**Importante:** declarar uma variável/método como `private` não é a mesma coisa que ocultar informação. Getters e setters expõem a natureza e o uso da variável tão publicamente quanto se ela fosse `public` — o encapsulamento sintático (privado) não implica encapsulamento semântico (informação escondida).

## Vazamento de informação (Information Leakage)

Ocorre quando uma decisão de design se reflete em mais de um módulo. Exemplo do livro: duas classes que ambas entendem o formato de um mesmo tipo de arquivo (uma lê, outra escreve) — mesmo que nenhuma exponha isso na interface pública, mudar o formato exige mudar as duas. Esse tipo de vazamento "por trás" é mais perigoso que vazamento via interface porque não é óbvio.

## Decomposição temporal: uma causa comum de vazamento

Estruturar os módulos pela ordem de execução ("primeiro lemos, depois analisamos") em vez do conhecimento de cada tarefa. O livro a chama de "uma causa comum" do vazamento, não "a mais comum". Exemplo canônico: o servidor HTTP com uma classe para ler a requisição e outra para analisá-la; como o `Content-Length` precisa ser analisado para saber onde a requisição termina, as duas entendiam o formato. O livro diz que "teria sido melhor" fundi-las. Página própria: [[wiki/concepts/decomposicao-temporal]].

## Como corrigir um vazamento (cap. 5.2)

Pergunte como reorganizar as classes para que o conhecimento afete uma só. Duas saídas: **fundir** as classes, se forem pequenas e muito ligadas à informação; ou **extrair** a informação para uma classe nova. A extração só funciona com uma interface simples. Uma classe nova que expõe quase tudo só troca o vazamento pela porta dos fundos por um vazamento pela interface ([[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]]).

## Os exemplos HTTP do cap. 5

- **Bom:** esconder se o parâmetro veio da linha inicial ou do corpo, e decodificar o *URL encoding* antes de devolver o valor.
- **Ruim:** `getParams()` devolvendo o `Map<String, String>` interno. Expõe a representação, dá mais trabalho ao chamador e deixa ele alterar o estado interno sem querer. Melhor: `getParameter(name)` e `getIntParameter(name)`.
- **Ruim:** exigir que o chamador informe a versão HTTP da resposta, que já é a da requisição. A biblioteca deve preencher sozinha, assim como o cabeçalho `Date`.

## Ocultação parcial e valores padrão

Esconder tudo é o melhor caso, mas esconder em parte também vale. Um recurso que só alguns usuários precisam, acessado por métodos separados, quase não cria dependência. Valores padrão são o exemplo típico: no caso normal o chamador nem sabe que o item existe. O red flag correspondente é a **superexposição**: a API de um recurso comum obriga o usuário a aprender recursos raros ([[wiki/concepts/red-flags-de-design]]).

## Dentro de uma classe e o limite (5.8 e 5.9)

O mesmo vale entre os métodos privados de uma classe: cada um deve esconder algo do resto, e cada variável de instância deve aparecer no menor número possível de lugares. O limite: não se esconde o que é necessário fora do módulo. Parâmetros que usos diferentes precisam ajustar vão para a interface. Ajustar sozinho é melhor que expor, mas o que é necessário tem de ser exposto.

## Ocultamento não é `private` nem sinônimo de encapsulamento

`private` impede o acesso direto, mas não esconde a informação se getters e setters públicos a expõem. No Brasil, "encapsulamento" costuma ser usado para o mesmo princípio (N.T. da 5.2); a wiki mantém as duas páginas porque o livro separa o mecanismo (`private`) do objetivo (esconder decisões). Ver [[wiki/concepts/encapsulamento]], que trata o encapsulamento como proteção de invariantes.

## Vazamento de Informação e Change Amplification São o Mesmo Fenômeno, Vistos de Ângulos Diferentes

[[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] descreve, sem citar o termo "information leakage" diretamente, exatamente esse mecanismo pelo ângulo de quem sofre a consequência: uma mudança que parece localizada numa única classe se espalha para dependências desconhecidas — porque a mesma decisão de design estava, sem que ninguém soubesse, replicada em múltiplos lugares do código. Ver [[wiki/concepts/sintomas-de-complexidade-ousterhout]] para o vocabulário completo do Cap. 2 (change amplification, cognitive load, unknown unknowns) que essa fonte introduz na wiki.

## Relação com outros conceitos

- [[wiki/concepts/modulo-profundo]] — ocultamento de informação é a técnica-mãe para produzir módulos profundos; quanto mais se esconde, mais funcional e mais simples a interface tende a ficar.
- [[wiki/concepts/red-flags-de-design]] — Information Leakage, Temporal Decomposition e Overexposure são os três red flags do cap. 5.
- [[wiki/concepts/decomposicao-temporal]] — a causa comum de vazamento, com página própria.
- [[wiki/entities/david-parnas]] — autor do artigo de 1972 que descreveu a técnica.
- [[wiki/concepts/complexidade-acidental]] — vazamento de informação é uma forma estrutural (não do domínio) de complexidade acidental.
- [[wiki/concepts/arquitetura-de-software]] — decisão de onde uma informação deveria "morar" é, em essência, uma decisão de arquitetura.
- [[wiki/concepts/sintomas-de-complexidade-ousterhout]] — change amplification é o sintoma prático (Cap. 2) do qual information leakage é frequentemente a causa estrutural (Cap. 5).

## Nuance do texto do cap. 2

A seção acima segue o podcast, que descreve a amplificação de mudanças como mudança que "se espalha para dependências desconhecidas". No texto do livro ([[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]), a amplificação pura tem dependências conhecidas: a mesma cor escrita em cada página, e todos sabem onde mexer. Quando ninguém sabe que a dependência existe, o livro chama de **incógnita desconhecida**. O vazamento de informação pode causar as duas coisas: amplificação, se o vazamento é visível, e incógnita desconhecida, se não é (o *back-door leakage*).

## O terreno preparado pelo cap. 4

[[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] não usa o termo, mas monta a base do cap. 5. A interface diz **o que** o módulo faz, não **como**; quem usa o módulo não deveria precisar entender a implementação; e uma mudança que não altera a interface não afeta nenhum outro módulo (4.1). O cap. 5 responde à pergunta seguinte: o que deve ficar atrás da interface.

## A generalidade leva a melhor ocultamento (cap. 6)

[[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]] liga o cap. 5 ao cap. 6. A classe de texto especializada, com `backspace` e `deleteSelection`, deixou conceitos da UI dentro da classe de texto: é vazamento, e cada operação nova da UI pedia um método novo lá. A versão geral ([[wiki/concepts/modulo-de-proposito-geral]]) deixa esses detalhes só na UI (6.4). A mesma seção dá o contrapeso: o `backspace` fingia esconder quais caracteres apaga, mas a UI precisa saber disso. "Determinar quem precisa saber o quê, e quando" decide o que esconder; esconder o que o chamador precisa "apenas cria obscuridade". É a 5.9 (não esconder o necessário) vista por outro exemplo.

## Puxar para baixo demais vira vazamento (cap. 8)

[[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]] (8.3) mostra que absorver complexidade no módulo errado é vazamento: o método `backspace` na classe de texto põe conhecimento da UI numa classe que não tem nada a ver com ele, sem simplificar muito o código de cima. Puxar para baixo só vale quando a complexidade é da função da classe ([[wiki/concepts/puxar-complexidade-para-baixo]]).

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — Cap. 5, exemplos de servidor HTTP (leitura+parsing, parâmetros, defaults em respostas)
- [[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] — change amplification descrito como o sintoma prático vivido por quem sofre com informação vazada/duplicada entre módulos
- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]] — corrige a leitura do podcast: amplificação ≠ dependência oculta
- [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]] — texto do cap. 5 em primeira mão: corrige "a causa mais comum" para "uma causa comum" e "a correção foi fundir" para "teria sido melhor fundir"; acrescenta como corrigir, ocultação parcial, getParams, valores padrão, dentro da classe e o limite
- [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]] — 4.1: interface diz o quê, não o como; mudança que não toca a interface não afeta ninguém
- [[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]] — 6.4: generalidade melhora o ocultamento; esconder o que a UI precisa é falsa abstração
- [[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]] — 8.3: `backspace` na classe de texto como vazamento causado por puxar complexidade para baixo demais
