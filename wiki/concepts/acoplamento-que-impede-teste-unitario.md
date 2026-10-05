---
type: concept
title: "Acoplamento que Impede o Teste Unitário"
aliases: ["3 tipos de acoplamento", "acoplamento mata teste unitário"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [testes, teste-unitario, acoplamento, testabilidade]
skill: tech-mentor-testing
status: draft
---

# Acoplamento que Impede o Teste Unitário

Sintoma: o teste unitário de um método **tenta executar coisas que não são o assunto do teste** (banco, rede, configuração) e quebra. Causa: o método depende de implementações concretas que o teste não consegue trocar. Segundo [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]] há **três fontes comuns**, todas fáceis de achar no código:

| Tipo | Como identificar | Por que quebra o teste | Cura |
|---|---|---|---|
| `new` de classe de infraestrutura | procurar `new` | instancia a classe real (ex.: repositório MongoDB sem collection/connection string) | interface + [[wiki/concepts/dependency-injection]]; ver [[wiki/concepts/acoplamento-desejavel-vs-indesejavel]] |
| Herança de classe base com tecnologia | `: BaseService` que chama `HttpClient`/banco | método herdado não é substituível nem mockável | composição: [[wiki/concepts/heranca-vs-composicao]] |
| Classe/método estático | `Helper.Metodo()` | chamada direta, sem ponto de troca | classe instanciável injetada: [[wiki/concepts/metodo-estatico-e-testabilidade]] |

Efeito comum: o teste viola a premissa de [[wiki/concepts/teste-unitario-sem-io]] e "funciona na minha máquina" mas falha no servidor de build ou na máquina do colega. Quanto mais acoplamento, mais dependências o teste precisa montar — daí "acoplamento mata teste unitário".

**Reflexo errado:** mockar o detalhe interno (ex.: `IMongoCollection`) — o teste não depende dele; o correto é injetar a abstração que o método realmente usa (o repositório).

**Ciclo virtuoso/vicioso:** sem teste, o dev acumula acoplamento; com teste, o acoplamento é forçado a cair ([[wiki/concepts/testes-como-aprendizado]]). O primeiro passo é **identificar**, antes de corrigir. O autor cita um quarto tipo, *acoplamento por processo*, que não explica.

Relaciona-se a [[wiki/concepts/acoplamento]] (taxonomia geral), [[wiki/concepts/hard-to-test-code]] (Highly Coupled Code no catálogo xUnitPatterns) e [[wiki/concepts/test-doubles]].

## Key sources

- [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]]
