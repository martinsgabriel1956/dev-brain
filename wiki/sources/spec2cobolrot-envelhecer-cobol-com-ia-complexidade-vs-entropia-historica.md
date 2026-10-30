---
type: source
title: "Spec2COBOLRot: Envelhecer COBOL com IA e a Diferença entre Complexidade Estrutural e Entropia Histórica"
aliases: ["spec2cobolrot", "envelhecer cobol com ia", "complexidade estrutural vs entropia histórica", "corpus sintético de cobol legado"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/spec2cobolrot-envelhecer-cobol-com-ia-complexidade-vs-entropia-historica.md
source_url: ""
author: "não identificado (canal sobre mainframe/COBOL; o nome não aparece na transcrição)"
date_published: ""
date_ingested: 2026-10-30
source_count: 0
tags: [cobol, mainframe, modernizacao, legado, entropia-de-software, agentes-ia, benchmark, pesquisa, tech-mentor-backend, tech-mentor-ai]
skill: tech-mentor-backend
status: stable
---

# Spec2COBOLRot: Envelhecer COBOL com IA e a Diferença entre Complexidade Estrutural e Entropia Histórica

## TL;DR

Vídeo comentando o paper **Spec2COBOLRot** ([[wiki/entities/spec2cobolrot]]), apresentado no workshop AISM 2026 (ASE 2026, Munique, 12/out). O problema: quem pesquisa ferramentas de [[wiki/concepts/modernizacao-de-mainframe|modernização de COBOL]] não tem acesso a sistemas legados reais (são de bancos, seguradoras, governo), e os sistemas de teste escritos "ontem" são limpos demais.

A proposta: um agente gera COBOL a partir de especificações, o programa é validado no GnuCOBOL e um segundo agente o **envelhece**, injetando um catálogo de 26 características de código legado até as métricas estruturais baterem com uma amostra de programas reais. → [[wiki/concepts/corpus-sintetico-de-codigo-legado]]

Funciona para métricas (até ~25 mil linhas), mas os próprios autores admitem que o resultado não parece uma história plausível de manutenção. O autor do vídeo tira daí a lição central: **complexidade estrutural ≠ entropia histórica**. Código feio é fácil de fabricar; o legado real é o acúmulo de décadas de regras de negócio (acordo sindical, lei, decisão judicial, nova patrocinadora, imposto) implementadas por equipes e empresas diferentes, cada uma "localmente justificável". → [[wiki/concepts/entropia-historica-vs-complexidade-estrutural]]

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Sistemas legados grandes raramente ficam disponíveis para pesquisa; corpora de teste ficam "didáticos" | Afirmação do autor; o abstract do paper diz o mesmo (corpora representativos raramente disponíveis) | Alta |
| Três pesquisadores; apresentação em outubro, em Munique, num workshop de IA e modernização | `[external]` Espinasse, Khelladi, Acher (Inria/DiverSe, CNRS/IRISA, INSA Rennes); AISM '26, co-located com ASE 2026, Munique, 12–16/out/2026; arXiv 2609.26835 | Alta |
| Pipeline: especificação → agente gerador → teste no GnuCOBOL → agente de envelhecimento | `[external]` Paper: três especificações (bancário, folha, seguros) validadas por especialista; ambos os agentes usam GPT-5.4; Fase 1 recompila/executa até 5×, Fase 2 injeta padrões até 5× | Alta. O vídeo descreve o retorno da fase 1 como uma equipe refazendo a especificação; no paper é um loop automático de compilação/execução |
| Catálogo de 26 características em três grupos (padrões da linguagem, vícios, características da linguagem) | `[external]` 26 *assets*: 8 *idioms*, 15 *smells*, 3 *mismatches*, extraídos de programas reais da Sopra Steria | Alta |
| Exemplos: laço por fim de arquivo, busca em tabela indexada, registros rejeitados (idioms); GO TO, working-storage inchada, I/O misturado com regra (smells); REDEFINES, decimal compactado (mismatches) | Tabela 4 do paper, repetida no vídeo | Alta |
| Nem toda característica é defeito: algumas são da plataforma (arquivo sequencial, batch) | Observação do autor, coerente com a separação idiom/smell do paper | Alta |
| Métricas comparadas: complexidade ciclomática, "palavras definidas pelo usuário", parágrafos, GO TO | `[external]` Paper usa SLOC, NPAR (parágrafos), DIVR (razão Data/Procedure), CC, APL (tamanho médio de parágrafo), NGO (GO TO), VUR (uso de variáveis) e DPR (parágrafos mortos). "Palavras definidas pelo usuário" não aparece com esse nome — provavelmente VUR | Média |
| Amostra real de referência | `[external]` 14 programas COBOL batch de folha de pagamento de um parceiro industrial (Sopra Steria); 360 a 28.387 SLOC | Alta (o vídeo não detalha) |
| Programas gerados de até 25 mil linhas, testados e semelhantes a legado real | `[external]` Nível L4 = 20–25 mil SLOC; todos os programas L3/L4 compilaram | Alta para tamanho e compilação; "semelhantes a legado real" é parcial — ver abaixo |
| Os autores reconhecem que o código envelhecido ainda está distante de legado real | `[external]` Abstract: mirar métricas estruturais independentemente da lógica de negócio arrisca produzir complexidade que não reflete uma história de manutenção plausível. Revisão de especialistas (20–30 anos de experiência): "promissor, mas ainda sintético demais" | Alta |
| Complexidade estrutural e entropia histórica são coisas diferentes | Tese do autor, apoiada pela limitação do paper | Alta como conceito → [[wiki/concepts/entropia-historica-vs-complexidade-estrutural]] |
| A entropia nasce do acúmulo de soluções localmente justificáveis nunca reorganizadas como um todo | Tese do autor, com exemplos (regra nova sem desligar a antiga, variável nova por medo, `if` hardcoded de madrugada) | Alta; converge com [[wiki/concepts/entropia-de-software]] |
| Não é exclusividade do COBOL; no COBOL só fica mais visível por causa da idade (30–50 anos) | Afirmação do autor | Alta |
| Os fontes gerados estão públicos no GitHub | `[external]` github.com/jbespi/spec2cobolrot-samples (pacote de replicação) | Alta |
| Muitos projetos descobrem tarde demais que modernizar não é só traduzir a linguagem | Afirmação do autor | Média-alta; converge com [[wiki/concepts/descoberta-de-regras-de-negocio-legado]] |

## O que o paper diz e o vídeo não

`[external]` Leitura do PDF (arXiv 2609.26835):

- **Comportamento nem sempre preservado.** No nível L1, só 5 de 9 execuções mantiveram as saídas idênticas antes e depois do envelhecimento; o agente tinha liberdade demais. Os autores sugerem verificar a cada iteração.
- **Em escala, o LLM "trapaceia" no tamanho.** Para bater a meta de linhas, ele duplica parágrafos muito parecidos em vez de criar construções legadas diversas. As métricas fecham, o realismo cai — exatamente a tese do vídeo, agora medida.
- **O que faltou segundo os especialistas:** ausência de `COPY` (ubíquo no legado real), `IF` sempre fechado com `END-IF` em vez do ponto final, `STRING ... DELIMITED BY SIZE` em excesso, e REDEFINES quase nunca introduzido. O vídeo cita REDEFINES como uma das características reproduzidas; no paper ele aparece no catálogo, mas o agente raramente conseguiu aplicá-lo.
- **Trabalho futuro:** gerar programas legados simulando uma história de desenvolvimento, não só injetando padrões — a resposta direta à limitação.

## Entities

[[wiki/entities/spec2cobolrot]] · [[wiki/entities/github]]

## Concepts

[[wiki/concepts/entropia-historica-vs-complexidade-estrutural]] · [[wiki/concepts/corpus-sintetico-de-codigo-legado]] · [[wiki/concepts/entropia-de-software]] · [[wiki/concepts/cobol]] · [[wiki/concepts/mainframe]] · [[wiki/concepts/modernizacao-de-mainframe]] · [[wiki/concepts/codigo-legado-ia]] · [[wiki/concepts/complexidade-ciclomatica]] · [[wiki/concepts/code-smells]] · [[wiki/concepts/conhecimento-perdido-em-legado]] · [[wiki/concepts/descoberta-de-regras-de-negocio-legado]] · [[wiki/concepts/refactor-vs-rewrite-matrix]]

## Conexão com outras fontes

Complementa o caso do DMV da Califórnia ([[wiki/sources/dmv-california-ia-descoberta-regras-negocio-mainframe-cobol]]): lá, o valor estava em recuperar regras de negócio antes de traduzir; aqui, a pesquisa mostra que nem um benchmark consegue simular essas regras só com métricas. Também conversa com [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] (as quatro forças da degradação), que descreve as mesmas causas — perda de contexto entre equipes, hotfix sob pressão — que o vídeo usa para explicar a entropia histórica.

[skill: tech-mentor-backend] A skill trata degradação como *architectural smells* e *technical debt quadrant* (`architecture-evolutionary.md`), mas não tem referência específica para modernização de legado ou corpora sintéticos; a calibração aqui ficou nas definições de *smell* e débito.

## Open Questions

- **Quem é o autor?** Canal de mainframe/COBOL, não identificado. Pode ser o mesmo de [[wiki/sources/mainframe-as-a-service-casas-bahia-sulamerica-kyndryl]] ("semana que vem a gente continua esse papo"), não confirmado.
- **"Do Nat"** (trecho literal da legenda) pode ser Natural (linguagem da Software AG no mainframe) — não confirmado.
- **Como medir entropia histórica?** O paper e o vídeo dizem o que ela não é (métrica estrutural). Candidatos [inferência]: número de regras de negócio por programa, código condicional por data/categoria, variáveis com o mesmo papel, regras antigas ainda ativas.
- **Os samples servem como benchmark?** Os autores dizem que sim para estrutura e não para comportamento; quem usar para testar ferramenta de tradução precisa dos dados de teste junto.

## Raw Quotes

> "[...] fazer um programa complicado e confuso não é exatamente a mesma coisa que você construir um programa legado."

> "A entropia nasce do acúmulo de soluções localmente justificáveis, mas que nunca são reorganizadas como um todo."

> "[...] complexidade estrutural de um programa e entropia histórica são coisas diferentes."

> "[...] para modernizar, não bastava só traduzir a linguagem."
