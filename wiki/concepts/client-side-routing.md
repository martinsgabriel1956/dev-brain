---
type: concept
title: "Client-Side Routing (Roteamento no Cliente)"
aliases: ["roteamento no cliente", "SPA routing", "History API", "pushState", "popstate"]
date_created: 2026-08-03
date_updated: 2026-11-16
source_count: 3
tags: [frontend, spa, routing, history-api, browser]
skill: tech-mentor-frontend
status: stable
---

# Client-Side Routing

Mecanismo que permite a uma Single Page Application (SPA) trocar o que aparece na tela ao navegar entre "páginas", sem fazer uma nova requisição HTTP nem recarregar o documento.

## Site tradicional vs. SPA

- **Site tradicional**: clicar num link dispara requisição ao servidor → novo HTML → página renderiza do zero. A tela pisca, estado em memória se perde, leva pelo menos algumas centenas de ms.
- **SPA**: o JavaScript intercepta o clique, atualiza a URL e troca o conteúdo renderizado sem requisição de rede — praticamente instantâneo.

## O mecanismo: History API

- `history.pushState()` muda a URL exibida na barra do navegador sem disparar nenhuma requisição.
- O evento `popstate` dispara quando o usuário usa os botões voltar/avançar do navegador.

Todo router de framework (React Router, Vue Router, Angular Router) é construído sobre essa API nativa do navegador.

## Armadilha: acesso direto a rota profunda

Se o usuário digita `seusite.com/produtos` diretamente na barra do navegador (em vez de navegar via SPA), o servidor recebe essa requisição HTTP de verdade. Se o servidor não estiver configurado para devolver o `index.html` como fallback para qualquer rota desconhecida, ele retorna 404 antes mesmo do JavaScript ter chance de rodar. A correção é configurar um catch-all no servidor (ou CDN) que sirva `index.html` para toda rota não estática, deixando o roteador client-side assumir a partir daí.

## Ver também

- [[wiki/concepts/hydration]] — outro mecanismo de troca de conteúdo sem reload completo, mas no contexto SSR

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], o React Router v5 (`BrowserRouter`, `Route exact`, `Link`, `useHistory`) faz o roteamento no cliente do Ecoleta. O `exact` existe porque o v5 casava por prefixo.

## Na NLW #2, dia 1 (Diego Fernandes)

React Router v5 com `BrowserRouter`, `Route exact` e `Link to`. Sem `exact`, a landing aparece em `/study`; Diego chama de "verificação de conteúdo", mas o v5 testa prefixo por segmento. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]].

## Key Sources

- [[wiki/sources/10-conceitos-internos-frameworks-frontend]]
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: React Router v5 no Ecoleta
- [[wiki/sources/nlw-2-diego-fernandes-dia-1-react-typescript-mobile-first-proffy]]: NLW #2, Diego, dia 1: Route exact e Link no Proffy
