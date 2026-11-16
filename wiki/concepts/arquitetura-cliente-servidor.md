---
type: concept
title: "Arquitetura Cliente-Servidor"
aliases: ["client-server", "cliente servidor", "browser e servidor", "arquitetura web básica"]
date_created: 2026-09-28
date_updated: 2026-11-16
source_count: 8
tags: [fundamentos, http, rede, backend, iniciante]
skill: tech-mentor-leadership
status: stub
---

# Arquitetura Cliente-Servidor

## TL;DR

Segundo [[wiki/entities/andre-casciotti]], entender a dinâmica cliente-servidor — como o **browser** se encaixa numa aplicação web, como funciona o protocolo **HTTP** (verbos GET/POST/PUT/DELETE, códigos de status como 200 e 404) e onde termina o código que roda no cliente e começa o que roda no servidor — é um fundamento que faz falta mesmo para devs experientes que só "entregam código" sem entender por que ele funciona onde funciona.

## O ponto de dor descrito pelo autor

O autor relata dificuldade pessoal no início da carreira: código JavaScript não funcionava como esperado porque ele tinha um processamento rodando do lado do servidor (ASP 3, à época) e não entendia a fronteira entre o que já tinha acontecido no servidor e o que ainda precisava acontecer no navegador. Esse tipo de confusão é comum em quem nunca parou para mapear explicitamente onde cada parte do sistema roda.

## Por que isso é mais amplo que aprender uma linguagem

Aplicações do tipo cliente-servidor não são exclusivas da web — jogos com launcher (Steam, Epic Games, Xbox) também são clientes locais conversando com um servidor remoto, com um protocolo próprio (não necessariamente HTTP). O conceito central (uma parte roda perto do usuário, outra parte roda remotamente, e existe um protocolo de comunicação entre elas) generaliza.

## Relação com fundamentos de rede

Andar de mãos dadas com o básico de rede: o que é IP, o que é DNS, por que as coisas "têm nome" na rede — sem aprofundar, mas sabendo que existe, o suficiente para não ficar perdido quando "localhost" deixa de ser a resposta padrão (a aplicação passa a rodar num servidor real, às vezes Linux em vez de Windows, atrás de um load balancer).

## Relação com outros conceitos

- [[wiki/concepts/http-vs-https]] — protocolo específico usado na maioria das arquiteturas cliente-servidor web
- [[wiki/concepts/sessoes-http-cookies]] — mecanismo concreto de manter estado entre requisições cliente-servidor
- [[wiki/concepts/aprender-com-foco-no-problema]] — entender a fronteira cliente-servidor é pré-requisito para "caçar problemas" como autenticação e permissões

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] explica para iniciantes com um restaurante: você pede ao garçom, ele leva ao cozinheiro e volta com a comida. "Cliente é você"; "tudo que for do garçom pra lá" é o servidor, que responde mesmo que seja "não tenho". Front-end é o que pede e mostra; back-end, o que devolve (o arquivo do download está "lá no back-end").

## Na NLW #1, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] retoma o restaurante do dia 1, agora com o cozinheiro como back-end: "receber os pedidos do cliente", aplicar "regras de negócio" (no login, validar o CPF e conferir a senha), guardar os dados e "enviar as respostas". O mesmo JavaScript roda nos dois lados.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: um back-end (Node) e vários clientes (React, React Native, Angular, Vue). O back-end decide "como que a nossa aplicação se comporta", e o front-end é "a parte visual".

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], a mesma analogia do restaurante: front-end é o cliente que pede, o garçom leva, o back-end é "aquela parte da cozinha". Clicar num vídeo do YouTube é pedir e receber: "tá rolando uma troca de dados".

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], o back-end tem a responsabilidade de "receber os pedidos do cliente", prepará-los e devolver; o front-end é o cliente. A aula cria o primeiro servidor do Proffy e mostra que, rodando no Git Bash, ele funciona com o editor fechado: "meu servidor, nesse caso, é a minha própria máquina".

## No JStack, aula 02

Em [[wiki/sources/jstack-http-e-apis-rest]], uma API é "alguém ali no meio" que liga web, mobile, desktop e outras APIs à "mesma fonte de dados"; o HTTP é a troca de mensagens em que "o cliente pede e o servidor responde de volta".

## Key Sources

- [[wiki/sources/o-que-estudar-guia-para-iniciantes-andre-casciotti]]
- [[wiki/sources/isomorfismo-institucional-gaiola-de-ferro-ia-e-mimetismo]] — o movimento de mercado "cliente-servidor" dos anos 90 (downsizing) como onda de modernização — ver [[wiki/concepts/cliente-servidor-como-onda-de-modernizacao]]
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: restaurante, front-end x back-end para iniciantes
- [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta]]: cozinheiro = back-end; regras de negócio no login
- [[wiki/sources/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native]]: um back-end, vários clientes
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: restaurante e troca de dados
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: responsabilidades do back-end
- [[wiki/sources/jstack-http-e-apis-rest]]: API no meio de vários clientes; HTTP como troca de mensagens
