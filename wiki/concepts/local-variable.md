---
type: concept
title: "Local Variable"
aliases: ["variável local"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 1
tags: [oo, testes, xunit, terminologia]
skill: tech-mentor-testing
status: stub
---

# Local Variable

Uma variável associada a um **bloco de código**, e não a um objeto ou classe: só acessível de dentro do bloco onde foi declarada, e sai de escopo quando esse bloco retorna para quem o chamou ([[wiki/sources/local-variable-xunitpatterns]]).

## Contraste com instance variable

É o único mecanismo de shadow citado em [[wiki/concepts/instance-variable]]: dentro de um método, uma local variable com o mesmo nome sobrepõe (faz shadow de) uma instance variable do objeto. O par de contraste é direto — instance variable tem escopo de objeto, local variable tem escopo de bloco de código — mas o terceiro termo do trio, **class variable** (escopo de classe), ainda não tem fonte primária isolada na wiki.

## Status: stub

Criado a partir de [[wiki/sources/local-variable-xunitpatterns]], verbete de glossário curto (uma frase, sem exemplo de código). Candidato a expansão futura se surgir fonte que amarre o termo diretamente a algum padrão de xUnit (por exemplo, variáveis locais dentro de um Test Method).

## Key Sources

- [[wiki/sources/local-variable-xunitpatterns]] — fonte primária isolada: definição genérica de escopo por bloco de código, contraste com instance variable
