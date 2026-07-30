---
type: concept
title: "Over-Engineering"
aliases: ["overengineering", "verde neném", "engenharia excessiva", "gold plating"]
date_created: 2026-06-09
date_updated: 2026-07-30
source_count: 9
tags: [design, qualidade, anti-pattern, aprendizado, design-patterns, dora, under-engineering]
skill: tech-mentor-leadership
status: stable
---

## Definição

Aplicar soluções mais complexas do que o problema exige — frequentemente por falta de entendimento do domínio, por querer usar um conceito recém-aprendido, ou por antecipar requisitos que nunca chegarão.

No contexto de aprendizado, a forma mais comum é o **"verde neném"**: alguém que acabou de aprender design patterns tenta aplicar todos eles em tudo, tornando o código mais difícil, não melhor.

---

## O maior problema da indústria não é over-engineering — é under-engineering

Antes de tratar dos cuidados contra over-engineering, vale registrar a proporção: segundo observação de David Farley e consenso informal coletado entre desenvolvedores, o problema mais comum na indústria de software é o oposto — falta de engenharia, não excesso. Over-engineering é real e merece atenção, mas não é a causa mais frequente de sistemas ruins. Ver [[wiki/sources/como-evitar-over-engineering-david-farley]].

Essa mesma tese aparece de forma independente em [[wiki/sources/underengineering-overengineering-mario-souto]] (Mário Souto), que descreve a versão detalhada do problema oposto em [[wiki/concepts/under-engineering]] — com sintomas concretos (acoplamento, hardcode, ausência de CI) e antídotos práticos que não exigem nenhuma técnica de over-engineering para serem resolvidos.

## Por Que Acontece

### Em iniciantes
- Querer aplicar tudo que aprendeu de uma vez
- Ainda não ter julgamento para saber quando um pattern cabe
- Confundir complexidade com qualidade

### Em devs experientes

**Perfeccionismo por falta de objetivo ou conhecimento** — construir uma "torre de marfim" sem fim, geralmente por não ter claro qual valor de negócio está sendo entregue, ou por aplicar princípios (Clean Code, Clean Architecture) sem entender por que — o "gamer" que tem noções vagas dos princípios e se perde no processo em vez de entregar.

**Falta de confiança — resolver requisitos não-funcionais antes de qualquer valor** — antecipar escala, performance e resiliência antes de ter algo rodando: já entrar com Kubernetes, microsserviços e arquitetura "à prova de tudo" de cara. O antídoto documentado por David Farley é o [[walking-skeleton]]: implementar uma fatia mínima da arquitetura fim-a-fim, colocar em produção cedo, isolar as peças provisórias atrás de abstrações trocáveis, e só otimizar quando a necessidade for comprovada (caso do LMAX).

- Antecipar requisitos hipotéticos ("vamos precisar disso no futuro")
- Otimizar prematuramente para flexibilidade que nunca será necessária

---

## Velocidade e qualidade não competem (refutação do "triângulo de ferro")

O "triângulo de ferro" — a ideia de que entre rápido, barato e bom você só pode escolher dois — é tratado como mito para software. Dados do [[dora-metrics|DORA]] (publicados em *Accelerate*) mostram que equipes que entregam mais rápido, em incrementos pequenos e frequentes, também entregam com **mais** qualidade, não menos. Isso reformula o motivo de se evitar over-engineering: não é só "para entregar mais rápido", é porque a mesma disciplina que evita over-engineering (fatias pequenas, feedback cedo, abstrações só quando necessárias) é a que a pesquisa DORA associa a menor change failure rate e menor MTTR.

Medo de quebrar em produção tende a gerar o efeito oposto ao pretendido: portões de deploy excessivos (muitas aprovações, PRs grandes por serem "a única chance" de revisão) atrasam o feedback e, paradoxalmente, aumentam o risco por deploy em vez de reduzi-lo.

---

## Sintomas

- Abstração onde não há variação real
- Padrões GoF aplicados a problemas simples
- Interfaces com uma única implementação criadas "por precaução"
- Hierarquias de herança profundas para algo que poderia ser um enum
- Mais infraestrutura do que lógica de negócio

---

## Causa Raiz no Aprendizado

Over-engineering em quem está aprendendo é quase sempre sintoma de **pular etapas na progressão**. Quem aprende design patterns sem antes dominar [[modelagem-orientada-a-objetos]] não tem julgamento para saber quando um pattern resolve um problema real — então aplica em tudo.

A progressão que evita isso:
1. Dominar [[logica-de-programacao]] e algoritmos
2. Dominar [[modelagem-orientada-a-objetos]]
3. Só então estudar [[design-patterns]] e arquitetura

---

## Como Escape Malsucedido da Paralisia por Análise

[[wiki/sources/7-habitos-programador-altamente-eficaz]] amarra o over-engineering a um estágio específico de progressão de carreira, complementando a "causa raiz no aprendizado" já registrada acima: o pleno, ao ganhar uma altura de abstração maior, passa a enxergar mais variáveis do problema e tenta controlar todas — cai em [[wiki/concepts/paralisia-por-analise]]. Quem consegue sair da paralisia sem resolver a causa (julgamento de escopo ainda imaturo) tende a cair "na margem" do over-engineering: em vez de travar, produz uma solução desnecessariamente complexa só para ter "feito alguma coisa". A fonte nomeia o sênior como quem escapa dos dois extremos, produzindo um plano técnico *suficiente* — nem a paralisia do pleno, nem o excesso do over-engineering.

## "Escalável Para Quê?" — Complexidade Confundida com Maturidade

[[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] traz um caso de over-engineering em nível arquitetural que não é sobre um pattern isolado, mas sobre a escolha do desenho inteiro: diante de 4 sistemas de fornecedores heterogêneos, a solução "vendida" (unificar tudo via [[wiki/concepts/microfrontends-parciais|microfrontends parciais]] com container/shell e comunicação por eventos) resolve fragmentação de experiência — um problema que ninguém tinha reportado — em vez da causa raiz real (falta de visibilidade de status/atraso entre fornecedores), que uma solução muito mais enxuta (dashboard read-only + [[wiki/concepts/bff-pattern|BFF]] agregador) resolveria em uma fração do tempo. A fonte generaliza isso como pergunta de reflexão: "escalável" é relativo — escalável para produto, para usuário ou para times? — e a arquitetura deveria ser julgada por resolver o problema na causa raiz com o menor atrito, não por parecer madura ou "à prova de futuro". Ver [[wiki/concepts/causa-raiz]] e [[wiki/concepts/senior-vs-staff-visao-arquitetural]].

## Relação com Otimização Prematura

[[otimizacao-prematura]] é o análogo de over-engineering no nível de performance: aplicar esforço excessivo onde não há necessidade comprovada. Ambos são sintomas de afoiteza.

---

## Conexões

- [[otimizacao-prematura]] — análogo em performance
- [[anti-pattern]] — over-engineering é um anti-pattern clássico
- [[design-patterns]] — fonte mais comum de over-engineering em quem está aprendendo
- [[modelagem-orientada-a-objetos]] — o pré-requisito que, quando pulado, leva ao verde neném
- [[fundacao-tecnica]] — base necessária para o julgamento de quando não sobre-engenheirar
- [[walking-skeleton]] — técnica concreta para evitar over-engineering por falta de confiança
- [[dora-metrics]] — evidência empírica de que a disciplina que evita over-engineering também melhora velocidade de entrega
- [[kiss]] — princípio irmão, mesma disciplina de suprimir complexidade desnecessária
- [[wiki/concepts/under-engineering]] — extremo oposto; ambos derivados do mesmo card de sintomas em [[wiki/sources/underengineering-overengineering-mario-souto]]
- [[wiki/concepts/paralisia-por-analise]] — over-engineering como escape malsucedido da paralisia por análise, na leitura de estágios júnior/pleno/sênior

---

## Key Sources

- [[wiki/sources/aprender-antes-de-aplicar-fundamentos-e-otimizacao-prematura]]
- [[wiki/sources/como-evitar-over-engineering-david-farley]]
- [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] — KISS e YAGNI apresentados como os dois princípios que atacam diretamente o dilema velocidade vs. qualidade, o mesmo dilema que over-engineering resolve mal
- [[wiki/sources/underengineering-overengineering-mario-souto]] — segunda fonte, independente de David Farley, chegando à mesma conclusão de que under-engineering é o problema mais comum; origem da página [[wiki/concepts/under-engineering]]
- [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] — descreve o "efeito manada" histórico de microsserviços (startups adotando o estilo desde o início sem necessidade real, só para parecer em dia com o mercado) como caso concreto de over-engineering em nível arquitetural, hoje corrigido por decisões mais "com pé no chão"
- [[wiki/sources/verdades-duras-programador-20-anos-pedro-nauck]] — terceira fonte independente reforçando a refutação do "triângulo de ferro": entregar algo funcional e imperfeito vale mais que algo inacabado e "perfeito", e overthinking sobre escalabilidade sem usuários é citado como erro pessoal do próprio autor mesmo após 20+ anos de carreira
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — dois exemplos concretos no mesmo material: (1) Kafka citado como possível over-engineering para um sistema de reserva de hotel, usado mesmo assim como exercício didático com ressalva explícita; (2) o próprio autor admite ter incluído um "simulador de caos" no MVP de um produto novo antes de validar a funcionalidade central (o simulador), classificando isso como erro de escopo em retrospecto
- [[wiki/sources/7-habitos-programador-altamente-eficaz]] — amarra over-engineering a um estágio de carreira (pleno escapando da paralisia por análise sem julgamento maduro de escopo), complementar à causa raiz de aprendizado já registrada
- [[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] — estudo de caso de over-engineering arquitetural completo (microfrontends parciais para unificar 4 sistemas de fornecedores) resolvendo o sintoma errado, contrastado com a solução enxuta (dashboard read-only + BFF) que resolve a causa raiz
