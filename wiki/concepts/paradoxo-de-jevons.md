---
type: concept
title: "Paradoxo de Jevons"
aliases: ["jevons paradox", "efeito rebote", "rebound effect", "paradoxo jevons ia"]
date_created: 2026-05-31
date_updated: 2026-09-14
source_count: 4
tags: [paradoxo-de-jevons, token-economics, era-agentica, custo-ia, economia]
skill: tech-mentor-ai
status: stable
---

# Paradoxo de Jevons

## TL;DR

Quando uma tecnologia fica mais eficiente (mais barata por unidade), o consumo total *aumenta* em vez de cair — porque o menor custo expande o número de casos de uso e usuários. Aplicado à IA: o preço do token despenca, mas a conta das empresas sobe porque o consumo cresce muito mais rápido que o preço cai.

## Origem

Formulado pelo economista William Stanley Jevons em 1865 ao observar que motores a vapor mais eficientes não reduziram o consumo de carvão na Inglaterra — aumentaram, porque tornaram o carvão acessível a mais indústrias.

## Aplicação à Era da IA

| Variável | Direção |
|----------|---------|
| Preço de inferência (custo/token) | ↓ Caindo — Gartner projeta 90% menos até 2030 |
| Consumo de tokens (por dev, por empresa) | ↑ Subindo — Goldman Sachs estima 24x até 2030 |
| Conta total das empresas | ↑ **Subindo** — o paradoxo |

**O mecanismo:**
1. Token mais barato → mais casos de uso viáveis
2. Agentes fazem tarefas inteiras (não só autocomplete) → muito mais tokens por tarefa
3. Mais agentes rodando em paralelo → multiplicação do consumo
4. Power users passam de **$2.000/mês** em tokens

> *"Token mais barato, conta maior."* — o paradoxo central da era agêntica.

## Por que Importa para Planejamento

Empresas que planejam orçamento de IA baseado em "o token vai ficar mais barato" estão usando a lógica errada. O custo total é função de `preço × volume`, e o volume cresce exponencialmente com a [[era-agentica]].

Uber queimou o orçamento de IA de 2026 em 4 meses. Microsoft cancelou licenças internas do Claude Code por uso excessivo. O GitHub congelou novas assinaturas do Copilot porque o modelo de uso ilimitado não fechava com o custo de agente.

## Paradoxo de Jevons vs. Escalabilidade

É tentador pensar que o problema é temporário — "quando o token ficar barato o suficiente, a conta vai cair". O Paradoxo de Jevons mostra que essa conta nunca cai: ela se expande para novos usos que antes eram inviáveis.

## Relação com [[token-anxiety]]

O Paradoxo de Jevons opera no nível organizacional (conta total). [[token-anxiety]] opera no nível individual (ansiedade de desperdiçar tokens disponíveis). São faces do mesmo fenômeno de escassez percebida em um contexto de abundância crescente.

## Segundo Caso Documentado: Uber

O caso Uber (orçamento de IA de 2026 estourado em 4 meses) já estava registrado aqui de fonte anterior; uma segunda fonte ([[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]]) confirma o mesmo episódio com o detalhe de que o estouro veio especificamente de token maxing sem limite de consumo — ver [[wiki/concepts/token-maxing]]. A mesma fonte traz a formulação do CEO da [[wiki/entities/palantir-technologies]] sobre o "timing" entre token maxing e ROI: o paradoxo só se resolve se a queda de custo de inferência dos hyperscalers acompanhar a velocidade com que o consumo cresce — e, pela lógica de Jevons, ela estruturalmente não acompanha.

## Aplicação a Emprego (Não Só a Custo de Token)

[[wiki/sources/oracle-demite-milhares-anatomia-agente-dba-autonomo]] aplica a mesma estrutura de raciocínio a um domínio diferente do custo de inferência: capacidade de trabalho, não tokens. O argumento — automação não implica demissão automaticamente, desde que o tempo liberado seja canalizado para gerar mais valor — é a versão "efeito rebote" aplicada a headcount: uma empresa que mantém 3 programadores agora produzindo 3x cada (9x de output total) supera uma concorrente que demite 2 para "ficar só com quem produz por 3". É uma tese normativa do autor, não um resultado observado, mas estruturalmente é o mesmo mecanismo de Jevons — eficiência maior expande o total consumido/produzido, em vez de reduzir proporcionalmente o insumo (tokens no caso original, headcount aqui).

## Três Casos Históricos de Automação Que Aumentaram (Não Reduziram) Emprego

[[wiki/sources/ia-paradoxo-de-jevons-camada-de-abstracao-futuro-do-programador]] contribui evidência histórica adicional para a aplicação do paradoxo a emprego (não só a custo de token), além do caso único da Oracle já registrado acima:

- **Radiologia:** [[wiki/entities/geoffrey-hinton]] previu em 2016 que a IA acabaria com a profissão de radiologista. O número de radiologistas cresceu, porque a automação parcial baratear o diagnóstico por imagem expandiu a demanda total (hospitais que antes não ofereciam esse serviço passaram a oferecer).
- **Caixas eletrônicos (ATM):** ao baratear a operação de uma agência bancária, o ATM permitiu abrir mais agências — o que aumentou, em vez de reduzir, o número total de caixas humanos (tellers) necessários. [[wiki/entities/james-bessen]] formaliza esse padrão: "a automação não elimina a profissão, ela muda a economia da atividade."
- **Contraexemplo explícito — mecanização agrícola:** a própria fonte reconhece que esse padrão **não é universal** — a mecanização do campo durante a Revolução Industrial de fato reduziu a demanda por trabalhadores rurais e causou grande impacto negativo. Isso evita tratar "Jevons sempre se aplica a emprego" como lei geral: o padrão depende de quanto o barateamento expande o *total* de demanda pela atividade versus apenas substitui o insumo humano por máquina sem gerar novos casos de uso.

A conclusão da fonte é que o caso da profissão de dev de software se parece mais com radiologia/ATM (mais software barato → mais software construído → mais gente para mantê-lo) do que com mecanização agrícola — mas isso é apresentado como expectativa/previsão do autor, não como resultado observado no mercado de trabalho de dev.

## Key Sources

- [[wiki/sources/ia-custo-roi-bolha-ou-realidade]]
- [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]] — segunda confirmação do caso Uber, com crítica do CEO da Palantir ao timing token maxing vs. ROI
- [[wiki/sources/oracle-demite-milhares-anatomia-agente-dba-autonomo]] — aplicação do mesmo mecanismo a headcount/emprego em vez de custo de token
- [[wiki/sources/ia-paradoxo-de-jevons-camada-de-abstracao-futuro-do-programador]] — três casos históricos adicionais (radiologia/Hinton, ATM/Bessen, mecanização agrícola como contraexemplo) aplicando o paradoxo a emprego, não a custo de inferência
