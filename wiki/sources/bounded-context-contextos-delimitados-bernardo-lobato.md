---
type: source
title: "Bounded Context (Contextos Delimitados) — Dominando DDD #4 (Bernardo Lobato)"
aliases: ["dominando ddd 4", "bounded context bernardo lobato", "contextos delimitados bernardo lobato"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 0
tags: [ddd, bounded-context, ubiquitous-language, subdominio, context-map, anti-corruption-layer, modularizacao, acoplamento, coesao]
skill: tech-mentor-backend
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/bounded-context-contextos-delimitados-bernardo-lobato.md"
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: "2026-09-30"
---

## TL;DR

Quarto vídeo da série "Dominando DDD" de [[wiki/entities/bernardo-lobato]] (vídeos 1–3 sobre DDD, domínio/subdomínio e [[wiki/concepts/ubiquitous-language|linguagem ubíqua]] não estão na wiki). Define **[[wiki/concepts/bounded-context]]** como limite **linguístico e semântico** do *domínio da solução*: até onde um termo tem um significado consistente. O exemplo central (adaptado de [[wiki/entities/martin-fowler]]) mostra "Produto" em Vendas (preço, palavras-chave, estoque…) vs. Suporte (só ID, nome, descrição curta) e defende **duas classes distintas para o mesmo conceito**, mesmo que mapeiem a mesma tabela do banco — menos [[wiki/concepts/acoplamento]] entre times/módulos, mais [[wiki/concepts/coesao]] interna. Desfaz duas confusões comuns: bounded context **≠** [[wiki/concepts/subdominio]] (divisão do negócio; um subdomínio pode ter 1+ contextos) e **≠** linguagem ubíqua (o contexto define *onde* a linguagem vale; analogia país/dialeto). Sinal prático para achar contextos: discussão de significado de um termo entre times. Cita, sem detalhar (próximo vídeo), as estratégias de integração [[wiki/concepts/shared-kernel]], [[wiki/concepts/customer-supplier]], [[wiki/concepts/conformist]] e [[wiki/concepts/anti-corruption-layer]] (ACL, típica na modernização de legado) — o conjunto que forma o [[wiki/concepts/context-map]].

---

## Reivindicações Principais

**Claim:** Um bounded context é um limite linguístico e semântico: determina até onde um termo/conceito pode ser usado de forma consistente; fora dele o mesmo termo pode ter significado diferente ou complementar.
**Evidência:** Definição do autor, ilustrada com "pedido" (intenção de compra em Vendas vs. ordem de entrega em Logística) e "produto" (Vendas vs. Suporte).
**Confiança:** Alta — coincide com [[wiki/sources/ddd-strategic]] (mesmo exemplo de termo com significados distintos por contexto) e com a definição já consolidada em [[wiki/concepts/bounded-context]].

**Claim:** O mesmo conceito de negócio deve ser modelado por classes/entidades separadas em cada contexto, com apenas os atributos relevantes a ele (Produto "completo" em Vendas; Produto enxuto com ID/nome/descrição em Suporte); reusar a entidade completa acopla o contexto de suporte a funcionalidades que não lhe dizem respeito.
**Evidência:** Raciocínio do autor sobre o exemplo; sem código, sem caso real medido.
**Confiança:** Média-alta — alinhado ao princípio DDD de "um modelo por contexto" ([external] Eric Evans, *Domain-Driven Design*, 2003; não consultado nesta sessão). O trade-off (duplicação de conceito e necessidade de sincronizar/traduzir entre contextos) não é discutido no vídeo, só adiado para o vídeo seguinte.

**Claim:** Classes separadas não exigem tabelas separadas: várias classes podem ser mapeadas para a mesma tabela, cada uma com os campos que lhe interessam.
**Evidência:** "Disclaimer" do autor, sem exemplo de ORM.
**Confiança:** Média — tecnicamente plausível (mapeamento parcial de colunas é comum em ORMs), não demonstrado. Nota de inferência: compartilhar tabela entre contextos mantém acoplamento no nível de dados, o que contrasta com [[wiki/concepts/database-per-service]] em microsserviços (o vídeo não aborda).

**Claim:** Bounded context ≠ subdomínio. Subdomínio é divisão do negócio (domínio do problema); bounded context é limite técnico/linguístico (domínio da solução); um subdomínio pode ter um ou mais bounded contexts.
**Evidência:** Definição do autor.
**Confiança:** Alta — distinção problema/solução é a leitura padrão do DDD estratégico; ver [[wiki/concepts/subdominio]]. Observação: o próprio autor, no exemplo, chama Vendas e Suporte ao mesmo tempo de "contextos" e de "subdomínios", o que ilustra por que a confusão é comum.

**Claim:** Bounded context ≠ linguagem ubíqua: a linguagem ubíqua é o vocabulário compartilhado; o contexto delimita onde esse vocabulário vale. Analogia: contexto = país, linguagem ubíqua = dialeto.
**Evidência:** Explicação conceitual do autor.
**Confiança:** Alta — consistente com [[wiki/concepts/ubiquitous-language]] e [[wiki/concepts/ddd]].

**Claim:** Conflito de vocabulário — discussão sobre o significado de um termo entre times (inclusive entre especialistas de domínio) durante refinamento/discovery — é um forte sinal de contextos diferentes ou sobrepostos.
**Evidência:** Heurística prática do autor, sem caso documentado.
**Confiança:** Média — heurística razoável e prática; complementar ao Event Storming já citado em [[wiki/sources/ddd-strategic]]; não validada empiricamente.

**Claim:** Bounded contexts reduzem ambiguidade, facilitam modularização (base para arquiteturas distribuídas/microsserviços), melhoram comunicação entre times e reduzem acoplamento entre contextos.
**Evidência:** Lista de benefícios do autor; microsserviços apenas antecipados ("guarda bem esse conceito").
**Confiança:** Média-alta — bate com [[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]] (mesmo autor: serviços "fortemente inspirados" em bounded context) e [[wiki/sources/microsservicos-monolito-first-renato-augusto]] (bounded context como módulo do [[wiki/concepts/monolito-modular]]). Afinidade com [[wiki/sources/conways-law]] (autonomia de times espelhando fronteiras do sistema), embora o vídeo não cite Conway.

**Claim:** Padrões de integração entre contextos: Shared Kernel (compartilhamento controlado de modelos), Customer/Supplier (dependência hierárquica), Conformist (um contexto se adapta ao outro) e ACL (camada de tradução, muito usada na modernização de legado).
**Evidência:** Apenas enumeração de 1 linha cada; detalhamento prometido para o próximo vídeo.
**Confiança:** Média — definições resumidas e corretas em linhas gerais; a caracterização de ACL como "mais abrangente" que os demais é opinião do autor (na literatura é apenas mais um padrão do Context Map [external]). Profundidade vem de [[wiki/concepts/anti-corruption-layer]] e da skill [skill: tech-mentor-backend, `references/architecture/ddd-advanced.md`].

---

## Entidades e Conceitos Tocados

- [[wiki/entities/bernardo-lobato]] — autor (série "Dominando DDD")
- [[wiki/entities/martin-fowler]] — imagem de Vendas/Suporte citada como retirada do site dele (não verificado qual artigo: provável *BoundedContext*, bliki — [external] não consultado)
- [[wiki/concepts/bounded-context]] — conceito central
- [[wiki/concepts/ddd]] — abordagem geral; este vídeo = terceiro pilar
- [[wiki/concepts/ubiquitous-language]] — novo (stub)
- [[wiki/concepts/subdominio]] — novo (stub)
- [[wiki/concepts/context-map]] — novo (stub)
- [[wiki/concepts/shared-kernel]], [[wiki/concepts/customer-supplier]], [[wiki/concepts/conformist]] — novos (stubs)
- [[wiki/concepts/anti-corruption-layer]] — ACL, citado como ponte para modernização de legado
- [[wiki/concepts/acoplamento]], [[wiki/concepts/coesao]] — justificativa do isolamento de modelos
- [[wiki/concepts/microsservicos]], [[wiki/concepts/monolito-modular]] — destino natural dos contextos
- [[wiki/concepts/strangler-fig-pattern]] — modernização de legado (contexto de uso do ACL)

## Perguntas em Aberto

- Como sincronizar/traduzir os dois "Produto" (Vendas ↔ Suporte) sem reintroduzir acoplamento? (vídeo 5 da série, não ingerido)
- Quando um subdomínio deve ter mais de um bounded context? O vídeo afirma "dependendo da complexidade", sem critério.
- Compartilhar a mesma tabela entre contextos preserva a autonomia pretendida? Ver tensão com [[wiki/concepts/database-per-service]].
- Vídeos 1–3 da série (DDD, domínio/subdomínio, linguagem ubíqua) e o vídeo 5 (comunicação entre contextos) ainda não estão na wiki.

## Citações Brutas

> "Um bounded context é um limite linguístico e semântico dentro de um sistema."

> "Um subdomínio é uma divisão do negócio [...] já o bounded context é um limite técnico e linguístico do domínio da solução."

> "Você pode pensar num contexto delimitado como se fosse um país e a linguagem ubíqua como se fosse o dialeto conversado dentro desse país."

> "Quando um termo passa a ter uma certa discussão de significados entre times diferentes [...] é um grande sinal de que eles pertencem ou podem pertencer a contextos diferentes."
