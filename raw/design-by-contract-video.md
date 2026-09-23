# Design by Contract

> Transcrição de vídeo em português (canal não identificado com certeza — a transcrição automática grafa "design by countrykitty" onde o áudio diz "design by contract"). Texto limpo e estruturado em seções a partir do áudio transcrito automaticamente. Vários termos foram distorcidos pelo reconhecimento de voz e foram corrigidos pelo contexto, listados abaixo; o restante foi mantido fiel ao conteúdo original.
>
> **Correções de transcrição aplicadas:** "design by countrykitty / country" → *design by contract*; "bertrand meyer / breadwinner / transmer" → *Bertrand Meyer*; "alfeu / wi-fi" → *Eiffel*; "closer" → *Clojure*; "a operar" → *OpenAPI*; "própria que base teste" → *property-based testing*; "assim variantes" → *invariantes*; "poças condições" → *pós-condições*; "gerente eo amante" → *gerente e o montante*.
>
> **Trechos incertos:** a passagem sobre a carreira acadêmica de Meyer veio muito corrompida ("júri é composto por 15 anos", "steffler", "universo de aquela forma em santa bárbara"); a leitura mais provável é: trabalhou ~15 anos no ETH Zurich, foi professor na UC Santa Barbara e hoje está numa universidade em Milão. Tratar como inferência. O trecho sobre o exemplo em Clojure (`deposito`) também é confuso no áudio; foi reconstruído pelo sentido geral.

## Introdução

É muito difícil lidar com a máquina, mas mais difícil do que lidar com a máquina é lidar com pessoas. Entretanto, a humanidade teve tempo de encontrar maneiras de melhorar as relações humanas. Uma das melhores soluções criadas para negociação justa entre duas pessoas é o **contrato**. Um contrato define direitos e responsabilidades seus e da outra parte. Provavelmente você tem um contrato de emprego que diz quantas horas você tem que trabalhar e quanto o empregador vai te pagar por essas horas. Quando as duas partes realizam o que está definido no contrato, todo mundo se beneficia. A ideia de contrato é utilizada no mundo todo.

Será que a gente não pode utilizar a mesma ideia para as interações entre módulos de software? A resposta é sim.

## Origem: Bertrand Meyer

Bertrand Meyer é um cientista da computação francês, já mencionado antes no canal. Trabalhou em vários lugares (a transcrição menciona ETH Zurich, UC Santa Barbara e hoje uma universidade em Milão — ver nota de incerteza acima). Ele é o autor do **Open/Closed Principle**, o "O" do SOLID, os cinco princípios de projeto orientado a objetos. Meyer também criou a linguagem de programação **Eiffel**, e dentro do Eiffel criou a ideia de **Design by Contract** (projeto por contrato).

## A ideia

A ideia do Design by Contract é simples: é focada na **documentação e na aceitação dos direitos e responsabilidades dos módulos de software**, e com isso você aumenta a confiança na corretude do programa.

O que seria um programa correto no Design by Contract? É um programa que **não faz nada a mais nem a menos do que aquilo que foi concordado no contrato**. Todo método ou função do programa tem que fazer alguma coisa; para fazer essa coisa, ele tem expectativas sobre o estado do mundo antes de realizá-la.

## As três partes do contrato

O contrato, em geral, é composto de três partes: pré-condições, pós-condições e invariantes.

- **Pré-condições:** o que deve ser verdade para que a rotina seja chamada — são os requisitos da rotina. A rotina nunca deve ser chamada se as suas pré-condições são violadas. É responsabilidade da rotina **chamadora** passar bons dados para a rotina chamada.
- **Pós-condições:** o que a rotina **garante** fazer — o estado do mundo depois que a rotina executa. O fato de a rotina ter pós-condições também implica que ela sempre vai concluir; ou seja, laços infinitos não são permitidos.
- **Invariantes:** condições que são sempre verdadeiras da perspectiva do chamador. As invariantes podem ser desrespeitadas durante a execução da rotina, mas, depois da execução, têm que estar verdadeiras de novo.

Resumindo: o contrato estabelece pré-condições, pós-condições e invariantes; e se alguma das partes falha em seguir o contrato, algum **remédio** é invocado, conforme o que foi concordado entre as partes.

## Como fica no código

Algumas linguagens oferecem suporte ao Design by Contract; outras têm suporte parcial ou nenhum.

### Clojure — suporte a pré e pós-condições

Clojure é uma linguagem que apoia pré-condições e pós-condições. O exemplo é uma função `deposito` que recebe uma conta e uma quantia a ser depositada nessa conta:

- **Pré-condição:** a quantia tem que ser maior que zero, e a conta tem que estar aberta. Se ambas valem, a função realiza o depósito. Se a função for chamada com quantia menor ou igual a zero, é lançada uma exceção — a asserção falhou. Mesma coisa se for chamada com a conta fechada.
- **Pós-condição:** se o depósito foi realizado, a transação deve estar registrada no sistema.

### Linguagens sem suporte nativo — cláusulas condicionais

Outras linguagens não têm suporte ao Design by Contract, mas suportam outros tipos de cláusulas que podem ser usadas de forma equivalente. No exemplo de depósito:

- se a quantia é maior que 100 mil, faz-se uma coisa diferente (por exemplo, exigir tratamento especial);
- se a quantia é maior que 10 mil, chama-se o gerente;
- se a quantia é maior que zero mas não excede nem 10 mil nem 100 mil, faz-se o processamento normal do depósito;
- se a quantia é menor ou igual a zero, a função não executa e um erro é lançado.

## Vale a pena pensar em contratos mesmo sem automação

Mesmo que a linguagem ou a tecnologia não dê apoio completo ao Design by Contract, vale a pena pensar em contratos. Você pode não automatizar a checagem, mas pode, por exemplo, escrever em **comentário antes de um método** quais são as pré-condições, as pós-condições e as invariantes. Isso já ajuda quem for utilizar aquele método: pode olhar a documentação e ver o que é esperado e o que é garantido.

## Não confundir com contrato de API

Esse tipo de contrato não deve ser confundido com o contrato feito para APIs, por exemplo usando a especificação **OpenAPI**. Esse tipo de contrato de API (por exemplo, HTTP) descreve a API; até onde o autor pôde ver, não existem pré-condições e pós-condições nesse tipo de contrato. É um outro tipo de contrato, muito interessante, sobre o qual talvez ele fale em outro vídeo.

## Fechamento

Mais uma ferramenta para o arsenal do desenvolvedor: vale a pena estudar, e se puder utilizar o Design by Contract, é muito poderoso. Existe ainda uma outra técnica de teste, o **property-based testing**, bem relacionada com o Design by Contract, que o autor pretende abordar no canal mais para frente.
