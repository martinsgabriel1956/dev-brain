---
type: source
title: "Princípios SOLID Ilustrados"
aliases: ["solid principles in pictures", "solid ilustrado", "robôs solid"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 1
tags: [solid, oop, architecture, design-patterns, dependency-inversion, interface-segregation]
skill: tech-mentor-backend
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/principios-solid-ilustrados.md"
source_url: ""
author: "desconhecido (vídeo YouTube, PT-BR) — baseado no artigo de [[wiki/entities/ugonna-thelma]]"
date_published: ""
date_ingested: "2026-08-06"
---

## TL;DR

Vídeo que percorre os cinco princípios SOLID usando as ilustrações de robôs do post "The SOLID Principles in Pictures", conectando cada uma a exemplos práticos (processador de pagamentos, ORM, extensões de navegador) e propondo um "efeito dominó" entre os princípios — aplicar Open/Closed de verdade já arrasta Liskov Substitution e Dependency Inversion junto.

---

## Reivindicações Principais

**Claim:** SRP não é sobre "fazer uma coisa só", é sobre isolar responsabilidades para permitir raciocinar sobre uma parte do sistema sem carregar o programa inteiro na cabeça.
**Evidência:** Analogia da máquina de lavar — uma meia vermelha (componente acoplado) mancha toda a carga; exemplo de cadastro/login acoplados numa entidade "usuário" onde mudar o cadastro quebra o login de quem já está cadastrado.
**Confiança:** Alta — consistente com a formulação de Uncle Bob ("uma razão para mudar") já presente em [[wiki/concepts/single-responsibility]].

**Claim:** Open/Closed na prática significa não abrir a classe base para adicionar `if`s a cada requisito novo, e sim receber objetos que se auto-validam e se auto-processam via interface comum.
**Evidência:** Exemplo do processador de pagamentos — adicionar boleto sem OCP exige abrir a classe base; com OCP, a classe base só pede para o objeto injetado se validar e se cobrar, sem conhecer os campos específicos de cada produto financeiro.
**Confiança:** Alta — mesmo padrão do exemplo do Strategy em [[wiki/concepts/open-closed-principle]].

**Claim:** Liskov Substitution serve para forçar a pensar no nível certo de abstração da hierarquia de herança, não como justificativa para substituir a classe pai pela subclasse.
**Evidência:** Exemplo clássico Ave → PicaPau (ok) → Pinguim (`voar()` lança exceção) — se toda subclasse nova exige "lutar" contra o que herdou, a abstração da base está errada.
**Confiança:** Média — é a interpretação pessoal do apresentador; ele mesmo reconhece divergência da leitura mais acadêmica do princípio.

**Claim:** Interface Segregation é SRP+OCP+LSP aplicados especificamente a interfaces — cliente não deve implementar métodos que não usa.
**Evidência:** Ilustração dos dois robôs de exercício, um sem antena forçado a implementar `mexerAntena()`; correção é segregar em interfaces menores (`Girável`, `RotacionávelDeBraços`, `ComAntena`).
**Confiança:** Alta — leitura padrão do ISP na literatura.

**Claim:** Dependency Inversion é o "soquete" que troca uma ferramenta fundida ao objeto por uma ferramenta injetada via interface — e Robert C. Martin (1996) generalizou o uso conjunto de OCP+LSP nesse princípio.
**Evidência:** Ilustração do robô com braço-faca-de-pizza fundido (errado) vs. braço com soquete que aceita qualquer ferramenta injetada (certo).
**Confiança:** Alta para a mecânica; a atribuição histórica exata ao paper de 1996 não foi verificada contra a fonte primária nesta ingestão — marcar como [external, não confirmado].

---

## Os 5 Princípios (resumo)

| Letra | Princípio | Regra em uma frase |
|---|---|---|
| S | [[wiki/concepts/single-responsibility-principle]] | Uma única razão para mudar |
| O | [[wiki/concepts/open-closed-principle]] | Aberto para extensão, fechado para modificação |
| L | [[wiki/concepts/liskov-substitution-principle]] | Subclasse substitui a base sem quebrar o esperado |
| I | [[wiki/concepts/interface-segregation-principle]] | Não force o cliente a depender do que não usa |
| D | [[wiki/concepts/dependency-inversion-principle]] | Dependa de abstração, não de implementação concreta |

## Conceitos

- [[wiki/concepts/single-responsibility-principle]] — analogia da máquina de lavar e dica de nomear a função com tudo que ela faz
- [[wiki/concepts/open-closed-principle]] — exemplo do processador de pagamentos e do ORM
- [[wiki/concepts/liskov-substitution-principle]] — exemplo Ave/PicaPau/Pinguim
- [[wiki/concepts/interface-segregation-principle]] — página nova criada nesta ingestão
- [[wiki/concepts/dependency-inversion-principle]] — página nova criada nesta ingestão
- [[wiki/concepts/strategy-pattern]] — mesma solução de fundo do exemplo de pagamentos

## Entidades

- [[wiki/entities/uncle-bob]] — criador dos princípios SOLID e autor da generalização de OCP+LSP em DIP (1996)
- [[wiki/entities/ugonna-thelma]] — autora das ilustrações originais de robôs usadas como fio condutor do vídeo; identidade confirmada via [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]]

## Conexões com Outras Sources

- [[wiki/sources/design-pattern-proxy]] — mesma tríade SRP/OCP/LSP aplicada a um padrão estrutural concreto
- [[wiki/sources/design-pattern-strategy]] — mesma resolução de OCP via Strategy usada no exemplo de pagamentos
- [[wiki/sources/design-pattern-facade-renato-augusto]] — mesma discussão sobre "razão única para mudar" vs. "fazer uma coisa só" em SRP
- [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]] — artigo original de onde vêm as ilustrações de robôs usadas neste vídeo; traz as definições formais em uma frase e o exemplo textual `Coffee`/`Cappuccino`/`Water` para LSP

## Nota sobre Skill Carregada

Skill carregada: `tech-mentor-backend`, lida de `/home/gabriel-martins/Documentos/skills/tech-mentor-backend/SKILL.md` e do arquivo de referência `references/architecture-evolutionary.md` (seção "SOLID na Prática para Arquitetos"). O `CLAUDE.md` do repositório aponta para `/home/nemomartins/Documentos/new/skills/`, caminho que não existe neste ambiente — mesma situação já registrada em ingestões anteriores; a skill real foi localizada em `/home/gabriel-martins/Documentos/skills/`.

## Perguntas Abertas

- A atribuição da generalização de OCP+LSP em Dependency Inversion ao documento de Robert C. Martin de 1996 não foi cross-checada com a fonte primária — vale verificar contra o artigo original "The Dependency Inversion Principle" (C++ Report, 1996) antes de tratar como fato consolidado.
- ~~O nome da autora do post original "The SOLID Principles in Pictures" ficou incompreensível na transcrição do áudio — não foi possível confirmar autoria/URL do artigo citado.~~ **Resolvido em 2026-08-06**: autora é [[wiki/entities/ugonna-thelma]] — artigo original ingerido em [[wiki/sources/solid-principles-in-pictures-ugonna-thelma]].
