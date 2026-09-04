---
type: concept
title: "MVP (Minimum Viable Product)"
aliases: ["mvp", "produto mínimo viável", "minimum viable product"]
date_created: 2026-04-29
date_updated: 2026-09-04
source_count: 9
tags: [projetos, produtividade, entrega, planejamento, carreira, startup]
skill: tech-mentor-leadership
status: stable
---

# MVP (Minimum Viable Product)

O menor conjunto de funcionalidades que (1) resolve o problema central e (2) pode ser entregue a um usuário real para validar a hipótese. Não é um produto incompleto — é um produto completo com escopo mínimo.

## O Que "Mínimo" Significa na Prática

**Mínimo não é:**
- Lista de features cortada aleatoriamente
- Produto bugado "pra sair logo"
- Protótipo não funcional

**Mínimo é:**
- Uma coisa que o usuário consegue usar do início ao fim
- Sem features que não provam a hipótese central
- Qualidade suficiente para não gerar atrito na validação

## Por Que Devs Falham no MVP

1. **[[concepts/scope-creep]]**: adicionam features antes de ter usuários
2. **[[concepts/perfeccionismo-em-devs]]**: ficam polindo o que já funciona
3. **[[concepts/planning-fallacy]]**: subestimam o tempo de cada "pequena adição"
4. **Automação prematura**: no framework [[concepts/lean-startup]], o erro simétrico é automatizar processos (pagamento, entrega) antes de validar que alguém quer o produto — um MVP de assinatura pode rodar inteiramente com Pix manual e mensagem de WhatsApp

## Regra Prática

> "Bom o suficiente para shippar > perfeito mas eternamente em dev."

Se o MVP não gera vergonha, está grande demais.

## MVP como Unidade do Ciclo Lean Startup

No [[concepts/lean-startup]], o MVP não é o produto final reduzido — é o artefato construído em cada volta do ciclo [[concepts/build-measure-learn]], com escopo de **uma única funcionalidade** por iteração, para gerar aprendizado real com o menor investimento possível.

## Estrutura Inicial a Serviço do MVP

O [[wiki/concepts/checklist-primeiro-dia-projeto]] propõe documentar a estrutura inicial do projeto num `.md` **antes** de codar, pensando explicitamente no MVP — evita tanto a gambiarra sem plano quanto o over-engineering para um produto que ainda não existe.
## MVP e Vibe Coding

MVPs e protótipos são o contexto onde [[wiki/concepts/vibe-coding]] entrega valor real: validar uma hipótese de negócio rapidamente, sem o custo de implementação manual completa. O risco não é usar vibe coding para validar — é confundir o MVP validado com um sistema pronto para produção sem revisão arquitetural, de segurança e de contexto de negócio. Ver [[wiki/sources/vibe-coding-limites-maturidade-profissional]].

## Caso real: infraestrutura mínima como teste do MVP

Em [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]], o autor leva a lógica do MVP até a infraestrutura: hospeda o Find My SaaS numa única VPS de 1 vCPU/4GB, monolito sem [[wiki/concepts/over-engineering|Kubernetes ou microsserviços]], de propósito, para descobrir se o MVP "aguenta porrada" (230 mil+ requisições em 15 dias, incluindo ataques). A escolha reforça que "mínimo" no MVP não se limita a features — também se aplica ao dimensionamento de infraestrutura, evitando gastar tempo/dinheiro em capacidade que ainda não tem uso comprovado.

## MVP e a Compressão do Tempo de Construção com IA

Em [[wiki/sources/pare-de-ter-ideias-icp-lean-canvas-obsoleto-ia]], o autor argumenta que o gargalo histórico do MVP — o tempo de programar — deixou de ser o fator limitante. Em 2012, um MVP decente levava meses (recrutar sócio técnico, desenhar arquitetura, testar). Em 2026, com IA, o mesmo MVP leva dias, deslocando o gargalo real para a validação: medir a interação de usuários reais em vez de gastar tempo em planejamento pré-código (ver [[wiki/concepts/lean-canvas]]). Cita dois estudos como evidência: um estudo controlado do GitHub em 2022, no qual 55% dos devs que usaram IA entregaram a solução mais rápido que o grupo de controle sem IA; e um estudo da Y Combinator mostrando que startups de batches recentes entregam 5x mais rápido que batches anteriores, com a maioria do código gerado por IA.

## MVP de Aprendizado Pessoal (Sem Mercado, Sem Usuário Real)

[[wiki/sources/escopo-de-projetos-processo-nao-resultado-lorehub]] aplica o conceito de MVP fora do contexto de startup/mercado: um app de clima cuja v1 inteira é "(1) buscar dados de uma API, (2) mostrar os dados" já conta como MVP completo se cobre exatamente a lacuna de aprendizado que o autor queria preencher (consumir API, renderizar dados). O critério de "mínimo" aqui não é "resolve o problema central de um usuário real" (definição de mercado usada no restante desta página), mas "cobre o objetivo de aprendizado que motivou o projeto" — ver [[wiki/concepts/necessidade-como-gatilho-de-aprendizado]] para o mecanismo por trás dessa variante.

## MVP Como Ferramenta de Descoberta de Escopo com Cliente Externo

[[wiki/sources/3-fatores-nao-tecnicos-para-entregar-projetos-de-ia-em-empresas]] descreve uma terceira variante de MVP, além das já cobertas nesta página (validação de mercado, aprendizado pessoal): o MVP **integrado** entregue o quanto antes a um cliente pagante externo em um projeto de consultoria/implementação de IA, especificamente para expor divergências de escopo que só se revelam quando o cliente vê e testa o produto funcionando. Diferente do MVP de startup (validar hipótese de mercado), aqui o objetivo é gerenciar expectativa e prevenir o padrão "cliente empolgado no início, insatisfeito no fim" — ver [[wiki/concepts/gerenciamento-de-expectativa-em-servicos-de-ia]].

## Ver Também

- [[concepts/scope-creep]] — inimigo principal do MVP
- [[concepts/dopamina-e-projetos]] — entrega do MVP gera dopamina real, não apenas antecipada
- [[concepts/lean-startup]] — metodologia onde o MVP é a unidade tática de validação
- [[concepts/build-measure-learn]] — ciclo iterativo que consome e refina o MVP
- [[wiki/concepts/checklist-primeiro-dia-projeto]] — sequência tática do dia 1 a serviço do MVP
- [[wiki/concepts/vibe-coding]] — ferramenta natural para construir MVPs rápido

## Key Sources

- [[sources/por-que-devs-nao-terminam-projetos]]
- [[sources/lean-startup-para-devs-mano-deivin]]
- [[wiki/sources/5-ou-6-dicas-para-projetos-novos]]
- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — MVP como um dos contextos onde vibe coding brilha
- [[wiki/sources/system-design-simulador-hotel-booking-replit]] — reforça a tese de lançar com monetização desde o dia um e escopo mínimo sendo exatamente a única funcionalidade pela qual alguém pagaria (o simulador em si, não uma tela de diagramação gratuita); o próprio autor admite em retrospecto ter violado essa regra ao incluir um "simulador de caos" no MVP inicial
- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — MVP mínimo estendido à infraestrutura (VPS 1 vCPU/4GB), testado sob carga real e ataque
- [[wiki/sources/vibe-coding-jogos-um-prompt-vs-varios-estagios-produto]] — MVP jogável (jogo de golfe na Unreal) construído por vibe coding em 3 prompts; [[wiki/concepts/estagios-de-maturidade-de-produto|estágio 1]] é "um estranho consegue usar"
- [[wiki/sources/escopo-de-projetos-processo-nao-resultado-lorehub]] — variante de MVP de aprendizado pessoal, sem mercado nem usuário real: "mínimo" medido pela lacuna de conhecimento preenchida, não por validação de hipótese de negócio
- [[wiki/sources/pare-de-ter-ideias-icp-lean-canvas-obsoleto-ia]] — gargalo do MVP mudou de "programar" para "validar" com IA; estudos GitHub (2022) e Y Combinator sobre ganho de velocidade
- [[wiki/sources/3-fatores-nao-tecnicos-para-entregar-projetos-de-ia-em-empresas]] — MVP integrado como ferramenta de descoberta de escopo em serviços de IA para cliente externo
