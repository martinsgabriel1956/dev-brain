---
type: concept
title: "Estimativas de Software"
aliases: ["software estimation", "por que subestimamos tarefas", "estimativa de tarefas"]
date_created: 2026-07-29
date_updated: 2026-08-18
source_count: 3
tags: [carreira, gestao-de-projetos, planejamento, produtividade]
skill: tech-mentor-leadership
status: draft
---

# Estimativas de Software

## TL;DR

Segundo [[wiki/sources/14-habitos-desenvolvedores-altamente-produtivos]] (Hábito 11, "Não subestime"), desenvolvedores subestimam tarefas cronicamente por cinco razões comportamentais recorrentes — não por falta de técnica. A fonte cita o livro *Software Estimation: Demystifying the Black Art* de Steve McConnell como referência técnica para mitigar o problema, mas reconhece: estimativa 100% precisa é impossível, o objetivo realista é se aproximar cada vez mais dela.

## As cinco razões para subestimar (segundo a fonte)

1. **Queremos impressionar os outros** — estimar baixo para parecer mais rápido/competente do que estimar de forma realista.
2. **Esquecemos que não é só código** — a estimativa mental vai direto para "tempo de codar", ignorando compilação, testes, documentação, reuniões, resolução de conflitos, revisão de comentários.
3. **Não nos concentramos em uma coisa só** — trabalhar em múltiplos projetos simultâneos gera custo cognitivo real de reorientação de contexto a cada troca.
4. **Acreditamos que todos são iguais** — tratar estimativa como tempo médio de equipe, ignorando que é uma medida estritamente individual (o tempo que a pessoa X leva não é o tempo que a pessoa Y leva para a mesma tarefa).
5. **Não conseguimos lidar com a pressão** — pressão vinda de cliente/gerente/CTO é repassada para baixo, e é difícil comunicar que "não vai ser tão rápido assim" sob essa pressão.

## Recomendações práticas (McConnell, citado pela fonte)

- Dividir tarefas grandes em unidades de no máximo 2 dias de esforço — melhora precisão.
- Estimar em três cenários: pior caso, caso mais provável, melhor caso.
- Ao usar linguagem/ferramenta nova (vs. familiar), adicionar 20–40% de esforço extra.
- Documentar e comunicar as suposições por trás da estimativa, não só o número final.
- Para projetos pequenos, estimativa "de baixo para cima" (feita por quem vai executar o trabalho) tende a ser mais precisa que estimativa "de cima para baixo".
- Tratar a conversa de estimativa como resolução conjunta de problema com os stakeholders, não como negociação adversarial — "você e as partes interessadas estão do mesmo lado da mesa".

## Nota sobre feedback loop

A fonte destaca um ponto frequentemente ignorado: sem medir o tempo real gasto e comparar com a estimativa original, não existe *feedback loop* — e sem feedback loop, a habilidade de estimar não melhora com a experiência, só a ilusão de que melhora.

## Por Que a Estimativa Original Nunca é Formalmente Invalidada

[[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] complementa o "porquê comportamental" acima com um mecanismo organizacional: o modelo padrão de estimar (uma ideia → uma estimativa única → executar esperando bater um prazo apertado) está condenado porque requisitos incompletos/ambíguos, mudança de requisito, incerteza tecnológica e pressão de vendas/CEO tipicamente só se revelam *depois* de a estimativa já ter sido dada. O problema não é que a estimativa erra — é que, quando o erro se revela, a organização raramente invalida a estimativa original; em vez disso, força os fatores de produção (hora extra, corte de escopo silencioso, atalhos) para tentar cumpri-la mesmo sem a informação que ela exigiria.

## Custo Oculto: Quanto uma Tarefa "de 2h" Vira 6h

Exemplo numérico da mesma fonte, ilustrando como o "trabalho invisível" citado acima se acumula: uma feature trivial (clicar um botão, submeter um formulário a um endpoint) estimada ingenuamente em 2h chega a 6h somando revisão de PR (+15min), troca de contexto do revisor (+15min reais de produtividade perdida), correção do que foi apontado na revisão (+1h), escrever e rodar testes garantindo build verde (+30min), margem para imprevisto aleatório (~1h a cada 5 tarefas de 4h) e pausas humanas — sem que nada excepcionalmente ruim tenha acontecido no processo.

## Redução de Incerteza Como Pré-Requisito (Não Só Multiplicador de Fator)

A mesma fonte argumenta que não basta multiplicar a estimativa instintiva por um fator de correção quando a tarefa envolve algo nunca feito antes — não é possível estimar, nem dar prazo, para algo cuja viabilidade técnica ainda não foi confirmada. Ver [[wiki/concepts/reducao-de-incerteza-antes-de-estimar]] para o método completo: testar as presunções mais desconhecidas primeiro (via [[wiki/concepts/prova-de-conceito|PoC]]), só então desenhar o sistema, só então quebrar em tarefas pequenas ([[wiki/concepts/divisao-de-tarefas-em-partes-menores]]) e estimar cada uma.

## Range em Vez de Número Único

Uma estimativa de "um mês" isolada não comunica margem de erro nenhuma. O formato recomendado por [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] é um range com média e margem — ex.: "1 a 2 meses, média de 1 mês e meio, ±33%" — que (1) dá margem de segurança, (2) impede a área comercial de vender um prazo que não vai ser cumprido, e (3) força o planejamento pela parte maior do range, não pela otimista. É funcionalmente equivalente à técnica de estimativa em três pontos (otimista/provável/pessimista, fórmula PERT) documentada em `references/engineering-management.md` do skill `tech-mentor-leadership`, embora a fonte não a nomeie explicitamente.

## Calibrando a Direção do Erro

Complementando a nota de feedback loop acima: medir o erro não basta — é preciso identificar a **direção** dele. Se as estimativas do time erram consistentemente para baixo, o ajuste é estimar para cima; se erram consistentemente para cima, estimar para baixo; se o erro é **disperso** (sem padrão, ora muito abaixo, ora muito acima), o problema não é calibração de viés — é falta de redução de incerteza antes de bater o martelo na estimativa (ver seção acima).

## Relação com outros conceitos

- [[wiki/sources/story-points-po-forcando-30-40-pontos-por-sprint]] — story points/T-shirt sizing/poker planning são citados na fonte atual como técnicas alternativas de estimativa, sem escolha de uma única "correta"; a outra fonte aprofunda por que forçar meta numérica de story points corrompe a métrica (Lei de Goodhart).
- [[wiki/concepts/tech-debt-como-ferramenta]] — subestimar cronicamente é um dos gatilhos comuns de dívida técnica não deliberada (pressão de prazo forçando atalhos).
- [[wiki/concepts/reducao-de-incerteza-antes-de-estimar]] — método passo a passo para tornar uma estimativa possível quando a tarefa envolve algo desconhecido, em vez de só aplicar um fator de correção sobre a estimativa instintiva.
- [[wiki/concepts/planning-fallacy]] — mesmo viés comportamental de fundo (planejar para o cenário ideal), com framing mais amplo sobre por que devs são vulneráveis a ele.
- [[wiki/concepts/story-points]] — a fonte atual questiona a equivalência implícita entre story points e horas dentro de uma sprint, sem contradizer a definição formal de "complexidade relativa" já registrada naquela página.

## Key Sources

- [[wiki/sources/14-habitos-desenvolvedores-altamente-produtivos]] — Hábito 11
- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — foco complementar: mensurar o *erro* da estimativa (gap planejado × entregue por sprint) importa mais do que acertar a estimativa; sem isso a empresa não sabe sua capacidade real
- [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] — mecanismo organizacional de por que a estimativa original nunca é invalidada, exemplo numérico de custo oculto (2h→6h), método de redução de incerteza, estimativa em range, e calibração da direção do erro
