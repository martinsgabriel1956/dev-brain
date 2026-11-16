---
type: concept
title: "Regra de negócio"
aliases: ["regras de negócio", "business rule", "business logic", "lógica de negócio"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 3
tags: [backend, dominio, regra-de-negocio, seguranca, validacao]
skill: tech-mentor-backend
status: stub
---

# Regra de negócio

As decisões que o sistema toma por causa do negócio, não da tecnologia: quanto custa, quem pode comprar, quando há desconto, o que acontece ao cancelar. Ela muda quando o negócio muda e precisa valer igual para todos os clientes (web, app, API). Por isso fica no back-end, ou no domínio, longe da tela. Ver [[wiki/concepts/configuracao-vs-regra-de-negocio]] para separar regra de parâmetro, e [[wiki/concepts/descoberta-de-regras-de-negocio-legado]] para quando ela está escondida no código.

O que o front-end faz com a regra é ajudar a experiência, como mostrar o preço ou avisar um campo vazio. Ele nunca é a fonte da verdade: tudo o que roda no navegador pode ser lido e alterado por quem usa. Ver [[wiki/concepts/confiar-no-frontend]].

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], [[wiki/entities/mayk-brito|Mayk]] define a preparação dos pedidos no back-end como "regra de negócio": "todo negócio tem regras". Os exemplos são desconto no sapato no Natal e presente para quem está a 10 km. "Dá para fazer no front-end? Até que dá", mas quem "entende um pouquinho mais de programação" muda o preço no navegador; por isso o back-end "vai verificar se realmente o preço daquele sapato é aquele mesmo". "O cliente não pode meter o pé na porta do cozinheiro lá." Na mesma aula, o cadastro de professor entra na lista sem nenhuma verificação no servidor: a regra é anunciada, mas não aplicada ao Proffy.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], "é muito mais responsabilidade da aplicação fazer a regra de negócio, como eu falei ontem", e o banco guarda os dados. O cadastro continua sem validação nenhuma no servidor, e a regra de horário (`time_from <= x < time_to`) é a única regra da aula escrita em código.

## No JStack, aula 06

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]], a regra sai do `index.js` para o [[wiki/concepts/controller]], definido como "o responsável por armazenar toda a regra de negócio". O exemplo ("verificar se o email [...] já não está inserido no banco") é regra de negócio de fato, mas o lugar dela numa arquitetura em camadas é um service/use case, não o controller HTTP.

## Key sources

- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: regra de negócio no back-end (o preço do sapato) e o cadastro sem validação
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: aplicação regra, banco guarda
- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: regra movida para o controller (lugar discutível)
