---
type: source
title: "Os 3 Estágios de Maturidade Para Testar Código"
aliases: ["3 estágios de maturidade programador", "postman vs jest watch mode", "de iniciante a testes automatizados"]
date_created: 2026-07-22
date_updated: 2026-07-22
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/os-3-estagios-de-maturidade-para-testar-codigo.md
source_url: ""
author: "Filipe Deschamps"
date_published: ""
date_ingested: 2026-07-22
source_count: 0
tags: [testes, tdd, jest, watch-mode, postman, api-first, dogfooding, pagar-me, carreira, maturidade-tecnica]
skill: tech-mentor-testing
status: stable
---

# Os 3 Estágios de Maturidade Para Testar Código

## TL;DR

Autoria inferida por evidência interna forte (ver seção "Autoria" abaixo): o autor narra os três estágios de maturidade pessoal que viveu para validar e depurar código — (1) iniciante, clicando manualmente na própria interface web para repetir ações e observar resultado; (2) intermediário, no Pagar.me, usando um cliente HTTP dedicado (Postman) contra uma API pensada API-first/dogfooding; (3) experiente, usando testes automatizados em **modo watch** (Jest), onde expectativas viram especificação executável e pegam regressões futuras automaticamente. Demonstração prática ao vivo: uma rota de migrations do TabNews vulnerável (retorna `200` para usuário anônimo) é primeiro capturada por um teste que espera `403`, depois corrigida com um middleware de autorização, e finalmente usada para provar que uma regressão futura (permissão liberada por engano no Model do usuário) é pega instantaneamente pelo mesmo teste, sem qualquer verificação manual.

## Autoria

Não há confirmação explícita no áudio, mas a evidência interna é muito forte: a transcrição cita "Felipinho de Champs de 2014", a experiência no Pagar.me (um dos maiores meios de pagamento do Brasil), e o exemplo prático usa o TabNews (projeto do próprio Filipe Deschamps) como codebase de demonstração. Essas três pistas coincidem exatamente com o perfil já registrado em [[wiki/entities/filipe-deschamps]] e [[wiki/entities/pagar-me]] a partir de [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]]. Atribuição tratada como confiança alta, não como certeza absoluta.

## Key Claims

- **Estágio 1 (iniciante, 2014, Angular/web)**: validar funcionalidade clicando manualmente na própria interface, alterando código e repetindo a mesma ação até obter o resultado esperado. Sensação de avanço, mas cada avanço reduzia a mobilidade dentro do código — o sistema ficava exponencialmente mais difícil de mexer, e mudanças isoladas no back-end exigiam passar pelo front-end mesmo sem relação nenhuma com ele. → [[wiki/concepts/tres-estagios-maturidade-testes]]
- **Estágio 2 (intermediário, Pagar.me)**: cultura de dogfooding — a mesma API que os clientes usavam para construir suas soluções era a que o próprio Pagar.me usava para construir seus produtos internos (ex.: a dashboard). Isso força pensar em termos de cliente/servidor desacoplados, onde o servidor não conhece o cliente — permitindo múltiplos clientes (web, mobile, Postman) contra o mesmo back-end. → [[wiki/concepts/tres-estagios-maturidade-testes]]
- **Postman como cliente HTTP especializado**, não fundamentalmente diferente de qualquer outro cliente (dashboard, app mobile) — organiza endpoints, permite variáveis de ambiente (host, chaves secretas) trocadas automaticamente por contexto. Mas testar manualmente cada endpoint e cada combinação de parâmetros não escala à medida que o sistema cresce (ex.: ~200 funcionalidades).
- **Estágio 3 (experiente)**: testes automatizados em **modo watch** (Jest) fecham o loop de feedback — qualquer alteração salva reroda o teste automaticamente. O mesmo cliente HTTP (`fetch`) usado no Postman é usado dentro do teste; a diferença é que o resultado da requisição vira uma **expectativa executável** (`expect(response.status)...`). → [[wiki/concepts/setup-live-reload-debug-testes]]
- **Expectativa correta expõe bug real, não o contrário**: ao esperar `403` (proibido) para uma rota sensível de migrations acessada por usuário anônimo, o teste quebra porque o código retorna `200` — a expectativa estava certa, o código é que estava exposto. Corrigido com um middleware de autorização que checa uma *feature*/credencial antes do handler.
- **Teste automatizado como rede de segurança contra regressão futura, não apenas validação do momento**: meses depois, uma alteração completamente não relacionada (adicionar por engano uma permissão de leitura de migrations no Model do usuário) faz o mesmo teste antigo voltar a falhar — pegando a regressão sem qualquer ação manual de verificação. → [[wiki/concepts/tdd]]
- **A progressão dos três estágios preserva a mesma relação cliente-servidor** — GUI manual, Postman e teste automatizado com `fetch` são, no fundo, três clientes HTTP diferentes contra o mesmo servidor; a mudança real está em quem/o quê dispara a chamada e se o resultado vira uma especificação permanente ou uma verificação descartável.

## Entities

[[wiki/entities/filipe-deschamps]] · [[wiki/entities/pagar-me]]

## Concepts

[[wiki/concepts/tres-estagios-maturidade-testes]] · [[wiki/concepts/setup-live-reload-debug-testes]] · [[wiki/concepts/tdd]] · [[wiki/concepts/piramide-de-testes]]

## Open Questions

- Grafia real do nome do autor do curso recomendado ("Fábio Vedovelle", transcrito foneticamente) não confirmada — se uma fonte futura citar esse nome corretamente, corrigir aqui e considerar criar entidade própria.
- Não há dado quantitativo sobre o tempo economizado entre os estágios — é relato de experiência pessoal, tratado como opinião de mercado experiente, não como estudo controlado.

## Raw Quotes

> "Cada passo que eu dava na evolução do sistema, cada vez menos mobilidade eu tinha dentro do código."

> "A expectativa tá certa, a request deveria ser negada para um usuário anônimo. Quem tá errado é o código."

*(Transcrição completa em `raw/os-3-estagios-de-maturidade-para-testar-codigo.md`.)*
