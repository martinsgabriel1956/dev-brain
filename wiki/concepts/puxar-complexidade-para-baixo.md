---
type: concept
title: "Puxar a Complexidade para Baixo (Pull Complexity Downwards)"
aliases: ["pull complexity downwards", "puxe a complexidade para baixo", "empurrar complexidade para cima", "interface simples, implementação complexa"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 2
tags: [design, ousterhout, complexidade, interface, modulo-profundo]
skill: tech-mentor-backend
status: draft
---

# Puxar a Complexidade para Baixo

## TL;DR

Princípio do cap. 8 de *A Philosophy of Software Design* ([[wiki/entities/john-ousterhout]]): quando uma complexidade é inevitável e ligada à função do módulo, o módulo deve absorvê-la em vez de deixá-la para quem o usa. Um módulo tem mais usuários que desenvolvedores, então a complexidade empurrada para cima é paga muitas vezes; a absorvida, uma vez. "É mais importante para um módulo ter uma interface simples do que uma implementação simples." É mais um caminho para o [[wiki/concepts/modulo-profundo]]. Fonte: [[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]].

## Como a complexidade sobe

- **Exceção:** não se sabe tratar uma condição, então se lança e todo chamador trata. O cap. 10 desenvolve a alternativa ([[wiki/concepts/definir-erros-para-fora-da-existencia]]).
- **[[wiki/concepts/parametro-de-configuracao]]:** não se sabe que política escolher, então se exporta um valor e todo administrador de toda instalação aprende a ajustá-lo.
- **Interface do tamanho da implementação:** a classe de texto por linhas deixa a UI dividir e juntar linhas (8.1, o mesmo caso da 7.4 em [[wiki/concepts/camada-diferente-abstracao-diferente]]).

## Exemplos de puxar para baixo

- **Classe de texto por caracteres:** a UI insere e apaga intervalos arbitrários; a classe divide e junta linhas por dentro. A implementação fica mais complexa e o sistema, mais simples.
- **Intervalo de retentativa calculado:** o protocolo mede o tempo das respostas bem-sucedidas e usa um múltiplo disso, em vez de pedir o valor ao usuário. Ainda se ajusta quando as condições mudam. É o RTO do TCP [external: RFC 6298, https://www.rfc-editor.org/rfc/rfc6298]; ver [[wiki/concepts/retry-backoff]].

## O limite (8.3)

Levado ao extremo, tudo cabe numa classe só. Puxar para baixo vale quando:

1. a complexidade está intimamente ligada à função existente da classe;
2. isso simplifica outras partes da aplicação;
3. isso simplifica a interface da classe.

Contraexemplo: um método `backspace` na classe de texto. Não simplifica muito a UI e o conhecimento é da UI, não do texto. O resultado é só vazamento de informação ([[wiki/concepts/ocultamento-de-informacao]]).

## Relação com outros conceitos

- [[wiki/concepts/modulo-profundo]]: interface simples sobre implementação complexa é a definição de profundidade.
- [[wiki/concepts/modulo-de-proposito-geral]]: o cap. 6 manda a **especialização** subir para a UI; o cap. 8 manda a **complexidade da função** descer. O `backspace` é o contraexemplo dos dois, e os critérios da 8.3 fazem a ponte.
- [[wiki/concepts/sensible-defaults-paved-road]]: quando o parâmetro é inevitável, o padrão razoável é a forma mínima de puxar para baixo.
- [[wiki/concepts/carga-cognitiva]]: cada complexidade empurrada para cima é mais uma coisa que cada usuário tem de aprender.

## Key sources

- [[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]] — texto do cap. 8: regra, classe de texto, parâmetros de configuração, três critérios e `backspace`
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — resumo do cap. 8 com o exemplo do intervalo de retry
