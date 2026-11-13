---
type: source
title: "Como inspecionar problemas de performance em Node.js com CPU profiling e módulos nativos"
aliases: ["cpu profiling node erick wendel", "node inspector autocannon lodash", "clonedeep 2000 para 11000 requisições"]
date_created: 2026-11-11
date_updated: 2026-11-11
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/cpu-profiling-nodejs-inspector-autocannon-erick-wendel.md"
source_url: ""
author: "Erick Wendel"
date_published:
date_ingested: 2026-11-11
tags: [nodejs, javascript, performance, cpu-profiling, node-inspector, v8, teste-de-carga, autocannon, lodash, garbage-collector, consultoria]
skill: lang-dynamic
status: draft
---

# Como inspecionar problemas de performance em Node.js com CPU profiling e módulos nativos

**Formato:** transcrição de vídeo do YouTube (legenda automática, PT-BR), limpa sem alteração de conteúdo. Boa parte do vídeo é codificação ao vivo, então a transcrição descreve o código sem mostrá-lo.

## TL;DR

[[wiki/entities/erick-wendel]] mostra como achou o gargalo de um cliente sem APM nem [[wiki/concepts/opentelemetry]]: gravou um [[wiki/concepts/cpu-profiling|CPU profile]] com o módulo nativo `node:inspector/promises` enquanto um [[wiki/concepts/teste-de-carga]] com autocannon batia na rota lenta. O arquivo `.cpuprofile`, aberto no VS Code ou num visualizador web, pôs funções do [[wiki/entities/lodash]] no topo, e o `cloneDeep` sozinho respondia por pouco mais de 10% do tempo gravado. Tirar a cópia profunda levou a rota de 2000 para 11.000 requisições no teste padrão de 10 s. Trocar o `filter` do Lodash pelo nativo subiu para 13.000; a troca do `map` ficou inconclusiva. A lição do autor: pacotes são úteis, mas conhecer a linguagem permite cortá-los no caminho quente.

## Key Claims

1. **A maior parte dos problemas de performance dos clientes do autor não é difícil de resolver; o difícil é ter visibilidade.** Os casos típicos se resolvem atualizando ou removendo um pacote, evitando iterações em listas grandes em memória ou corrigindo vazamento de memória. Evidência: relato de consultoria, sem números. Confiança: média. Ver [[wiki/concepts/observabilidade]].
2. **Sem APM instalado, o `node:inspector` basta para gravar um CPU profile.** Node.js roda sobre V8 e expõe o mesmo protocolo do Chrome DevTools. O fluxo é `new Session()`, `session.connect()`, `Profiler.enable`, `Profiler.start` e, no fim, `Profiler.stop`, que devolve o profile. Evidência: demonstração ao vivo, que bate com a documentação do módulo, onde `Profiler.stop` devolve `{ profile }` e o exemplo grava `JSON.stringify(profile)` num `.cpuprofile` ([external](https://nodejs.org/api/inspector.html)). Confiança: alta. Ver [[wiki/concepts/cpu-profiling]].
3. **O autor afirma ter contribuído com o `node:inspector/promises`.** Confiança: baixa, não conferido. A busca não achou o PR. A API existe na documentação oficial.
4. **O mesmo profile abre no VS Code, num visualizador web e na aba Performance do Chrome.** O site usado não é nomeado. Pela menção a "Discover" e à separação entre módulo e pacote, pode ser o CPUpro, feito sobre Discovery.js, mas isso é inferência. Confiança: alta para VS Code e DevTools, baixa para a identidade do site.
5. **Ler o profile: recortar só a janela do teste de carga e começar pelo topo.** O trecho ocioso (idle) fica fora da análise. As funções do topo costumam ser as mais caras, e o visualizador mostra também quando o [[wiki/concepts/gerenciamento-de-memoria|garbage collector]] rodou. Seguindo a árvore a partir da rota, o autor chegou ao `cloneDeep`: 7 s, um pouco mais de 10% do tempo gravado. Confiança: alta para o método. Ver [[wiki/concepts/flame-graph]].
6. **Uma linha levou a rota de 2000 para 11.000 requisições.** A linha removida era o `cloneDeep(data)`, e o código passou a usar `data` direto. Evidência: autocannon com o padrão de 10 conexões por 10 s ([external](https://github.com/mcollina/autocannon)). Confiança: alta para a medição local. Há uma ressalva de correção que o vídeo não faz: tirar a cópia só é seguro se nada adiante mutar `data`. Se a cópia for necessária, `structuredClone` é a opção nativa, e não é garantido que seja mais rápido ([external](https://measurethat.net/Benchmarks/Show/29642/0/lodash-clonedeep-vs-structuredclone-vs-jsonstringify)). Ver [[wiki/concepts/imutabilidade]].
7. **`Array.prototype.filter` nativo no lugar do `_.filter` subiu de 11.000 para 13.000.** Confiança: média. Foi uma rodada só, e o próprio autor mostra logo depois uma variação de 10.000 a 11.000 entre execuções iguais.
8. **Trocar o `map` do Lodash pelo nativo não mostrou ganho.** O resultado caiu para 10.000 e voltou para 11.000 na segunda rodada. O autor atribui a variação ao aquecimento da aplicação. Confiança: alta para a conclusão de que um único teste não basta. O aquecimento combina com a compilação JIT do V8 `[skill: lang-dynamic]`.
9. **Com o `cloneDeep` de volta, a rota volta a 2000 requisições, e o Lodash volta ao topo do profile.** É a prova reversa da causa. Confiança: alta.
10. **"Duplicar a capacidade de resposta."** O ganho medido foi bem maior, de 2000 para 11.000, cerca de 5,5 vezes, num caso montado para o vídeo. Confiança: baixa como promessa geral.
11. **Gravar o profile ao encerrar o processo.** O autor registra `process.on` para SIGTERM e SIGQUIT, chama o `stop` e sai com código 0. Confiança: média. O Ctrl+C manda SIGINT, segundo a documentação de sinais do Node.js ([external](https://nodejs.org/api/process.html#signal-events)), e o SIGINT não está na lista que ele fala. Se o profile foi gerado no Ctrl+C, o código na tela provavelmente tinha outro sinal. Ver [[wiki/concepts/graceful-shutdown]].

> "Os pacotes são legais, mas é importante a gente conhecer JavaScript a fundo." (Erick Wendel)

## Entidades

- [[wiki/entities/erick-wendel]]: autor, que se apresenta como consultor de performance em JavaScript.
- [[wiki/entities/lodash]]: biblioteca da rota lenta. Página criada neste ingest.
- [[wiki/entities/opentelemetry]]: recomendado como primeira opção de visibilidade; ausente no cliente.
- Sem página própria: autocannon, V8, Chrome DevTools, VS Code, CPUpro (inferido), Higlobe (patrocínio), treinamento JavaScript Expert.

## Conceitos

- [[wiki/concepts/cpu-profiling]]: página criada neste ingest.
- [[wiki/concepts/teste-de-carga]]: página criada neste ingest.
- [[wiki/concepts/flame-graph]]
- [[wiki/concepts/event-loop-performance-js]]: CPU gasto no caminho da requisição segura todas as outras.
- [[wiki/concepts/observabilidade]], [[wiki/concepts/opentelemetry]]
- [[wiki/concepts/gerenciamento-de-memoria]]: o GC aparece no profile.
- [[wiki/concepts/standard-library-e-ecossistema]]: nativo no lugar de dependência no caminho quente.
- [[wiki/concepts/decisao-tecnica-embasada-em-metricas]]: cada mudança é medida antes e depois.
- [[wiki/concepts/graceful-shutdown]]: gravar o profile ao receber sinal.
- [[wiki/concepts/imutabilidade]]: por que alguém escreve `cloneDeep` em primeiro lugar.

## Relação com fontes anteriores

- [[wiki/sources/5-dicas-performance-javascript]], do mesmo autor, recomenda OpenTelemetry e teste de carga com Artillery. Esta fonte é o plano B quando não há instrumentação, e troca o Artillery pelo autocannon.
- [[wiki/sources/performance-methods]] cita flame graph para CPU profiling e p95/p99 como métrica certa. O vídeo só olha o total de requisições; latência e percentis não aparecem.

## Open Questions

- A rota `no-issue`, já otimizada, aparece com "mais de 8.000", menos que os 11.000 da rota `issue` com uma linha a menos. Pode ser outra métrica, outra rodada ou outro tamanho de lista. O vídeo não explica.
- Qual é o custo do profiler ligado durante o teste de carga? Todas as rodadas tinham o profiler ativo, então a comparação entre elas vale, mas os números absolutos não.
- O repositório do exemplo não tem URL na transcrição, então o código não foi conferido.
- Trechos ambíguos da transcrição estão no log e não mudam os claims técnicos.
