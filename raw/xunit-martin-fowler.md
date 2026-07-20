---
title: "Xunit"
author: "Martin Fowler"
source_url: "https://martinfowler.com/bliki/Xunit.html"
date_published: 2006-01-17
date_ingested: 2026-07-19
note: "Tradução para PT-BR do artigo original (bliki entry, texto curto). Buscado via curl direto no HTML (não via resumo de modelo) para preservar o texto exato. Para o texto exato em inglês, consultar a source_url."
---

# Xunit

XUnit é o nome de família dado a um grupo de frameworks de teste que se tornaram amplamente conhecidos entre desenvolvedores de software. O nome é uma derivação de [JUnit](http://junit.org), o primeiro deles a ficar amplamente conhecido.

As origens desses frameworks começaram, na verdade, no Smalltalk. Kent Beck era um grande entusiasta de testes automatizados no centro do desenvolvimento de software. Para ajudar a si mesmo, e a seus clientes, a fazer isso, ele construía um framework simples para organizar e rodar testes unitários. O foco era facilitar para os programadores definirem os testes usando seu ambiente Smalltalk normal, e então rodar um subconjunto ou o conjunto completo de testes rapidamente. Kent e seus seguidores rodavam os testes unitários depois de cada mudança no sistema, passando por um ciclo rápido de edição e teste na IDE do Smalltalk.

Fowler encontrou Kent nessa época. Ele já tinha feito algo parecido por conta própria, mas o framework de Kent tinha uma combinação boa de simplicidade absurda e exatamente os recursos certos para ele. Basicamente, Kent fez um trabalho melhor do que o dele, então ele simplesmente passou a usar o de Kent. Em particular, usaram o framework no [C3](https://martinfowler.com/bliki/C3.html), onde Ron Jeffries também foi apresentado a ele.

Fowler diz "ele" (o framework), mas isso é, na verdade, um equívoco de nomenclatura. Não havia um único framework kent-beck-smalltalk-de-testes-unitários. Kent queria que as pessoas controlassem seu próprio ambiente, então gostava que cada time construísse o framework por conta própria (levava só um par de horas), assim eles se sentiriam à vontade para mudá-lo conforme suas circunstâncias particulares — essencialmente, era de fato um [Seedwork](https://martinfowler.com/bliki/Seedwork.html).

Isso ainda era desconhecido fora da comunidade Smalltalk, então é justo dar a JUnit o crédito por espalhar a ideia mais amplamente. JUnit nasceu num voo de Zurique para a OOPSLA de 1997, em Atlanta. Kent estava voando com Erich Gamma, e o que mais dois geeks fariam num voo longo senão programar? A primeira versão de JUnit foi construída ali, em par, e feita test-first (uma forma agradável de geek-ice meta-circular). Fowler ouviu falar disso e exigiu uma cópia, o que o torna um dos primeiros usuários alfa. Ele se sentiu livre para mudar coisas de que não gostava, mandando algumas contribuições de volta para Kent e Erich. Se alguém estiver se perguntando de quem é a culpa pelo fato de as mensagens de assert serem o primeiro argumento em vez de seguir a convenção Java de colocar argumentos opcionais no final...

JUnit também introduziu o indicador de progresso em barra vermelha/verde. No C3, a equipe costumava colorir a janela inteira de vermelho assim que um teste falhasse, e de verde se todos passassem. Era fácil ver a janela na máquina de build central quando você estava integrando. JUnit introduziu isso como uma barra de progresso, e assim adicionou um novo vocabulário aos desenvolvedores de software.

JUnit decolou como um foguete — e foi essencial para sustentar o movimento crescente de Extreme Programming e Test-Driven Development. Fowler viu uma mudança enorme de atitude em relação a testes na última década, e acha que JUnit teve um papel importante nisso. Por ser pequeno e simples, encorajou as pessoas a aprender e usar. Também se mostrou fácil de outros estenderem e integrarem a ferramentas. (Embora Fowler gostasse que a Sun simplesmente empacotasse a coisa toda no JDK.)

Conforme JUnit ficou mais popular, outras linguagens quiseram ter o seu também. Fowler lembra de Michael Feathers montando o CppUnit para C++, que pode ter sido o primeiro port. Muitos seguiram — praticamente toda linguagem tem pelo menos um port de JUnit. Fowler supõe que era inevitável que ele também fosse "portado" de volta para Smalltalk como um framework de verdade.

Os ports variam. Alguns são reescritas linha a linha do JUnit original, com pouca concessão à linguagem-alvo. A primeira versão do [NUnit](http://nunit.org) chegou a ter um método "isVAforJava", que se originou de um tratamento especial para o Visual Age for Java. Outros foram mais sofisticados: o NUnit 2.0 foi elogiado por Anders Hejlsberg por seu uso de atributos em C# — experiência que voltou para a comunidade Java e para o próprio JUnit conforme o Java desenvolveu as annotations.

## Metadados do artigo

- Publicado em 17 de janeiro de 2006 — mesma data de publicação do bliki entry "Test Double" (ver [[wiki/sources/test-double-martin-fowler]]).
- Entidades centrais citadas: Kent Beck (criador do framework original em Smalltalk e do JUnit), Erich Gamma (coautor do JUnit, também um dos autores do Gang of Four), Ron Jeffries (apresentado ao framework no projeto C3), Michael Feathers (autor do primeiro port, CppUnit), Anders Hejlsberg (elogiou o uso de atributos do NUnit 2.0).
- Termos/artigos relacionados citados por Fowler: `C3` (bliki, projeto onde o framework de Beck foi usado — origem histórica da Extreme Programming), `Seedwork` (bliki, padrão de framework mínimo que cada time reconstrói por conta própria).
