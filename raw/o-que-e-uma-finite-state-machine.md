---
title: "O que é uma Finite State Machine?"
author: Felipe Costa
source_url: https://medium.com/@felipecoast/o-que-é-uma-finite-state-machine-0592d7213f21
date_published: 2023-12-07
---

**_Finite State Machine_** (FSM) ou Máquina de Estado Finita é uma técnica que modela a representação de um fluxo entre diferentes comportamentos em um jogo. Ela permite que sejam realizadas transições de estados que são acionadas por ações ou eventos específicos.

Digamos que ela seja o "cérebro" de um inimigo, por exemplo. Este inimigo poderá realizar ações diferentes através da FSM, como "atacar" ou "correr" (a depender dos eventos ocasionados pelo jogador).

Um ponto interessante a ser mencionado, é que a utilização da FSM era muito mais frequente no passado, onde ela sempre foi considerada uma das possíveis formas de Inteligência Artificial (IA). Com o salto na evolução das IAs, hoje em dia, a FSM pode não ser mais considerada uma das principais inteligências artificiais se levarmos em conta os modelos que temos disponíveis atualmente. Elas não foram as precursoras das IAs em games, mas foram uma abordagem inicial e seguem sendo utilizadas até hoje.

Agora vem comigo que te explico como ela age através de exemplos práticos.

## Exemplo 1: Finite State Machine em Pac-Man

Em _Pac-Man_, a movimentação dos fantasmas foi toda feita através de FSMs.

A FSM de _Pac-Man_ é mais complexa do que isso, mas para deixar de maneira clara como ela funciona, sigamos dessa forma. Note que temos 2 estados distintos: um é perseguir, e o outro é fugir. Não é possível que ambos os estados estejam ativos ao mesmo tempo, ou seja, a depender da situação, ou o fantasma estará te perseguindo, ou então estará fugindo de você.

A transição entre perseguir e fugir ocorre de acordo com o resultado do que é feito pelo jogador. Os fantasmas, por padrão, perseguem o jogador para fazer com que ele perca vidas ao encostarem nele, por outro lado, uma vez que o _Pac-Man_ come uma pílula, a situação é a oposta, pois agora os fantasmas é quem deverão fugir do personagem principal.

No exemplo visto, temos um caso onde ambos os estados só serão ativados a depender de uma situação visualmente clara de entender (o personagem principal comeu a pílula ou não). Mas também existem maneiras não tão visuais para que uma transição de estado seja realizada.

O Game Designer pode definir certas "regras" de ativação de acordo com o que achar válido. Por exemplo, os inimigos só deverão fazer uma transição entre os estados de "patrulhar" e "atacar", apenas se o jogador chegar a exatos 3 metros de distância deles, caso contrário, os inimigos continuarão a patrulhar a área como se nada tivesse acontecido. Estas ativações também podem ocorrer de formas diferentes, como quando o jogador faz algum barulho que pode chamar a atenção de um guarda e então colocá-lo em estado de alerta.

## Exemplo 2: Funcionamento de uma Turret com a Finite State Machine

A imagem trata-se de uma FSM referente a uma _turret_ pensada para um jogo em desenvolvimento.

Diferentemente do que vimos em _Pac-Man_, aqui a mudança de estados da _turret_ não é algo tão visual. Ela acontece apenas quando o jogador entra no alcance da mesma (e cabe ao _Game Designer_ definir qual alcance é esse).

Note que, quando o jogador estiver sem vida (HP), o jogo vai checar se ele possui um item de _revive_ e, caso tenha, o estado de patrulhar é ativado novamente e a **_Finite State Machine_** é reiniciada. Caso não tenham mais _revives_ restando, o personagem é eliminado e o jogo termina.

## Easter Egg: Hierarchical Finite State Machine

Além do que já vimos até aqui, também temos a **_Hierarchical Finite State Machine_** (HFSM), que pode ser considerada uma extensão da FSM.

As principais diferenças entre uma FSM e uma HFSM estão em suas organizações e estruturas. Além dos estados normais de uma FSM, uma HFSM pode ter subestados que podem dar acesso à outros conjuntos de transições. Esse modelo serve para aumentar a complexidade de comportamentos e também deixá-los, de certa forma, mais flexíveis e naturais.

Como forma de exemplo, vamos levar ainda em consideração o modelo que vimos do _Pac-Man_. Os fantasmas ainda podem persegui-lo ou então fugir de você, mas cada um desses estados agora podem ser divididos em partes menores. Por exemplo, quando o fantasma está te perseguindo, ele pode ter um estado para "atravessar paredes" e outro para "ficar invisível".

Dessa maneira, é possível entender o HFSM como uma forma de organização de estados em níveis diferentes, onde um comportamento pode ser colocado dentro de um outro comportamento maior.

Chegamos ao fim deste artigo! Agradeço pelo seu tempo com esta leitura, e espero ter deixado um pouco mais claro na sua cabeça do que se tratam as **_Finite State Machines_** em _Game Design_.
