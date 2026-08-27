---
type: concept
title: "Ciclo de Mercado Tech"
aliases: ["ciclo de abundância e depressão", "lei da oferta e procura em tech", "ciclo de contratação tech"]
date_created: 2026-07-03
date_updated: 2026-08-27
source_count: 11
tags: [carreira, mercado-de-trabalho, oferta-e-procura, ciclo-economico]
skill: tech-mentor-leadership
status: draft
---

## Definição

O mercado de trabalho em programação segue a lei de oferta e procura em ciclos alternados de **abundância** (alta demanda, contratação fácil, salários subindo) e **depressão** (demanda cai, oferta de profissionais supera vagas, seletividade aumenta). Nenhum ciclo de abundância dura para sempre.

## O Mecanismo

Quando a demanda por desenvolvedores excede a oferta, o mercado fica "aquecido": empresas contratam com critérios mais frouxos, salários sobem, e cursos rápidos (semanas a poucos meses) parecem suficientes para conseguir emprego. Esse próprio aquecimento, porém, atrai um volume enorme de gente nova para a profissão via cursos de formação rápida — o que aumenta a oferta de profissionais mais rápido do que a demanda cresce, empurrando o mercado de volta para um ciclo de depressão.

## Exemplo Histórico — Ondas de Tecnologia

[[wiki/entities/fabio-akita]] ilustra o ciclo com a evolução das linguagens mais demandadas por década:

| Época | Linguagens/tecnologias mais quentes |
|---|---|
| Anos 90 | Visual Basic, Delphi, Java |
| Virada do século | PHP, ASP, Flash |
| ~10 anos depois | Objective-C, Ruby, JavaScript |
| 2020s | Python, Go, Rust (segundo o autor) |

Quem ficou preso à ferramenta de uma onda perdeu, sequencialmente, as ondas seguintes: a primeira onda da web, a onda das redes sociais, a onda mobile, a onda dos e-commerces. Ver [[apego-a-ferramentas]] para o mecanismo psicológico por trás disso.

[[wiki/entities/lucas-badico]] reforça a onda 2020s do Go com um contra-exemplo de "onda que não emplacou": Ruby on Rails teve forte influência histórica no ecossistema mas nunca gerou volume relevante de vagas no Brasil além de algumas consultorias — ao contrário do Go, hoje consolidado em Mercado Livre, Mercado Pago e Stone. A diferença, segundo o autor, é que Go foi desenhado como linguagem *cloud native* (ver [[wiki/concepts/go-fundamentos]]), o que amplia sua adoção além de qualquer moda passageira.

Dados de pesquisa salarial dão números concretos a essa consolidação: em 2024, [[wiki/sources/golang-mercado-salarios-pesquisa-2024]] mostra Go pagando acima de Java em todos os níveis (maior gap no Sênior: ~R$ 6.000/mês), com o mercado de Go descrito como "mais seleto" — 75% dos devs Go atuam em backend puro, contra 59% em Java. É um exemplo concreto do efeito oferta/demanda: onda ainda não saturada de profissionais paga prêmio sobre onda mais madura e com mais gente disponível.

## O que Não Muda entre Ciclos

O autor argumenta que tentar prever qual será a próxima linguagem/framework "quente" é perda de tempo — o que não perde valor entre ciclos é [[raciocinio-matematico-aplicado|raciocínio fundamental]] (matemática, lógica, capacidade de aprender rápido), porque essas habilidades transferem entre qualquer ferramenta específica.

## Implicação Prática

Em ciclo de depressão, a prioridade das empresas deixa de ser "produzir funcionalidade nova rápido" e passa a ser **otimizar e extrair mais valor do que já existe** — o que favorece quem sabe raciocinar sobre trade-offs, não só seguir padrões prontos. Mercados em depressão filtram naturalmente quem tem [[fundacao-tecnica|fundação técnica]] real de quem só teve sorte de entrar durante a abundância.

## Cada onda como curva de adoção

Cada onda de tecnologia listada acima é, individualmente, uma [[wiki/concepts/curva-de-adocao-tecnologica|curva de adoção em S]]: começa devagar, cresce exponencialmente, desacelera. O próprio autor descreve ter apostado cedo em Ruby on Rails (2005), na fase inicial daquela curva — ilustrando a estratégia de [[wiki/concepts/antifragilidade|apostar em várias tecnologias ao longo de ~10 anos]] em vez de tentar prever com certeza qual onda vai vencer.

## Ciclo de Depressão Setorial: Frontend Pós-IA

[[wiki/sources/impacto-ia-mercado-frontend]] documenta uma versão setorial (não de linguagem/framework, mas de nicho de atuação) do mesmo mecanismo: a IA comoditizou o escopo de CRUD simples que sustentava agências, freelancers de landing page e consultorias pequenas/médias — encolhendo a demanda nesses nichos e comprimindo salário de sênior remoto (14–18k pandemia → 11–14k pós-IA, majoritariamente híbrido). Times com arquitetura de plataforma madura (microfrontends, design system, observabilidade, governança) ficaram relativamente blindados, porque nunca competiram nesse escopo simples em primeiro lugar — reforçando que fundação técnica/arquitetural, e não o nicho onde se está, é o que atravessa o ciclo de depressão.

## Conexões

- [[apego-a-ferramentas]] — por que ficar preso a uma ferramenta específica amplia o dano de cada virada de ciclo
- [[raciocinio-matematico-aplicado]] — a habilidade que não perde valor entre ciclos
- [[fundacao-tecnica]] — o que sobrevive quando o mercado esfria e filtra profissionais
- [[autodidata]] — quem aprendeu a aprender sozinho consegue "nadar" tanto em ciclos de abundância quanto de depressão
- [[wiki/concepts/curva-de-adocao-tecnologica]] — o padrão em S por trás de cada onda individual
- [[wiki/concepts/antifragilidade]] — a estratégia de aposta que lida com a incerteza sobre qual onda vai vencer

## O Mecanismo Financeiro por Trás do Ciclo de Depressão Atual

[[wiki/sources/crise-vagas-tech-juros-altos-nao-e-so-culpa-da-ia]] preenche uma lacuna que as fontes anteriores desta página deixavam em aberto: **por que** o mercado entra em depressão além de "oferta de profissionais cresceu rápido demais". A resposta proposta é a taxa básica de juros (Selic, no Brasil, em ~14,25%–15% desde meados de 2024): crescimento de empresa costuma depender de capital captado, não só do caixa disponível, e a esse nível de juros a maioria das empresas não gera EBITDA suficiente para justificar o empréstimo — tornando "não contratar" o cálculo financeiro racional, não uma decisão sobre qualidade de profissionais disponíveis. Ver detalhamento completo em [[wiki/concepts/custo-de-capital-e-contratacao-tech]].

Essa lente é complementar, não concorrente, ao mecanismo de oferta/procura de profissionais já documentado acima — os dois operam em paralelo: o lado da demanda (quantas vagas as empresas conseguem financiar) é regido pelo custo de capital, enquanto o lado da oferta (quantos profissionais competem por essa vaga) é regido pelo ciclo de atração/formação descrito na seção "O Mecanismo". A fonte também conecta com [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]] (pesquisa em que 59% dos gestores admitem usar IA como justificativa para corte de vagas, mas só 9% relatam substituição real) para argumentar que boa parte da "culpa da IA" no ciclo de depressão atual é, na prática, bode expiatório para um aperto financeiro estrutural.

## Possível Manifestação em Nível de Categoria de Vaga

[[wiki/sources/marco-bruno-3-dicas-vaga-junior]] relata um padrão específico no mercado brasileiro — vagas rotuladas como "júnior" passando a exigir nível pleno na prática — sem identificar a causa. Ver [[wiki/concepts/vaga-junior-vira-pleno]] para o detalhe; a conexão com o ciclo de abundância/depressão descrito aqui é inferência, não fato verificado nas duas pontas, já que nenhuma das fontes cruza dados diretamente.

## Defasagem EUA → Brasil como Preditor de Onda

[[wiki/sources/o-que-sobrou-pro-dev-junior-eric-wendel]] adiciona uma heurística de defasagem geográfica ao mecanismo do ciclo: mudanças de mercado tech "geralmente acontecem fora, principalmente nos Estados Unidos, e pouco tempo depois se aplicam ao Brasil". O autor usa isso para prever que a exigência americana atual — vagas júnior já esperando fluência com ferramentas de IA como parte do perfil — deve chegar ao mercado brasileiro em breve, ainda que no momento do vídeo as vagas brasileiras de nível júnior continuassem cobrando fundamentos clássicos sem essa exigência. É observação qualitativa do autor (quem trabalha remotamente para empresas americanas), não dado de pesquisa comparativa formal.

## Concentração de Cargos: Front-end Absorvido pelo Full-Stack

[[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]] observa uma manifestação adicional do ciclo de depressão setorial já documentado em "Frontend Pós-IA": contratações segregadas de front-end, back-end e DevOps estão dando lugar a cargos mesclados de full-stack (focado em back-end, focado em front-end, ou puro), com contratação de front-end especificamente reduzida. Ops e segurança parecem ter se mantido do mesmo tamanho relativo (segurança talvez até crescido). A causa apontada é a mesma comoditização do CRUD simples via IA já documentada na fonte de impacto no mercado de frontend — aqui vista pela ótica de reorganização de cargo, não de nicho de negócio (agência/freelancer vs. plataforma madura).

## Paralelo com a Bolha da Internet (2000-2001) e Contratação Como Métrica de Vaidade

[[wiki/sources/organizando-equipes-de-tecnologia-fabio-akita]] estende a tese de ciclos com um paralelo histórico direto: no fim dos anos 90 até 2001, programadores (nem todos excepcionais) ganhavam salários "astronômicos", disputados por empresas recebendo investimento sem correlação clara com valor gerado — até o mercado financeiro questionar esse valor e o dinheiro secar, forçando terceirização em massa para a Índia por eficiência de custo. A fonte generaliza o mecanismo: em ciclos de dinheiro fácil, empresas sem lucro/receita como métrica de sucesso usam **contratação (headcount) e número de usuários como métricas substitutas de crescimento** para investidores — o que leva a contratar gente para produzir pouco, só para inflar a operação. Ver [[wiki/concepts/overhead-de-coordenacao-tamanho-de-equipe]] para o mecanismo de por que isso reduz eficiência real, e [[wiki/concepts/body-shop-terceirizacao]] para a manifestação do lado da oferta de mão de obra terceirizada nesse mesmo ciclo aquecido.

A mesma fonte cita, como contraponto histórico, o Google (nascido de restrição de recursos — PageRank + máquinas baratas) versus o Cadê/kd.com.br (diretório manual, dependente de centenas de pessoas cadastrando páginas, inviável sem dinheiro sobrando) — tratado como `[external, não verificado nesta fonte]`, mas coerente com a tese central de que fundação construída sob restrição sobrevive melhor à virada do ciclo do que operação inflada por capital abundante.

## Salários Altos e Estresse Já Existiam Antes do ZIRP e Antes da IA

[[wiki/sources/code-was-never-the-hard-part-reacao-lucas-montana]] usa um contra-argumento de mercado contra a tese de que "programar sempre foi fácil": se fosse, não explicaria por que devs eram tão requisitados e exigiam salários altos por anos mesmo antes do [[wiki/concepts/ciclo-de-mercado-tech|ciclo de ZIRP]], nem por que havia tanto estresse e esgotamento antes da IA passar a gerar PRs de milhares de linhas — empresas já buscavam "programadores 10x mais rápidos" e submetiam candidatos a entrevistas de LeetCode em múltiplas etapas, um padrão de seletividade que não combina com "trabalho fácil".

## Key Sources

- [[wiki/sources/code-was-never-the-hard-part-reacao-lucas-montana]] — salários altos e estresse pré-ZIRP/pré-IA como evidência contra "programar sempre foi fácil"
- [[wiki/sources/akita-oferta-procura-matematica-carreira]]
- [[wiki/sources/organizando-equipes-de-tecnologia-fabio-akita]] — paralelo com a bolha de 2000-2001, contratação como métrica de vaidade para investidor, contraste Google vs. Cadê
- [[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]] — concentração de cargos: front-end segregado sendo absorvido por full-stack, mesma causa (CRUD comoditizado) já vista em "Frontend Pós-IA"
- [[wiki/sources/o-que-sobrou-pro-dev-junior-eric-wendel]] — heurística de defasagem EUA → Brasil; vagas júnior americanas já exigindo fluência com IA, vagas brasileiras ainda não
- [[wiki/sources/golang-mercado-trabalho-frontend-para-backend]]
- [[wiki/sources/pare-de-terceirizar-suas-decisoes]]
- [[wiki/sources/golang-mercado-salarios-pesquisa-2024]]
- [[wiki/sources/impacto-ia-mercado-frontend]]
- [[wiki/sources/marco-bruno-3-dicas-vaga-junior]] — possível manifestação em nível de categoria de vaga (júnior exigindo pleno), causa não identificada
- [[wiki/sources/crise-vagas-tech-juros-altos-nao-e-so-culpa-da-ia]] — mecanismo financeiro (custo de capital/Selic) por trás do ciclo de depressão atual
