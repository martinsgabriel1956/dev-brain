---
type: concept
title: "Arquitetura Cliente-Servidor"
aliases: ["client-server", "cliente servidor", "browser e servidor", "arquitetura web básica"]
date_created: 2026-09-28
date_updated: 2026-09-28
source_count: 1
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

## Key Sources

- [[wiki/sources/o-que-estudar-guia-para-iniciantes-andre-casciotti]]
