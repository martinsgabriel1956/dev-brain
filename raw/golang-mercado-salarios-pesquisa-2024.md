# Golang: Mercado, Salários e Pesquisa Código Fonte TV (2024)

> Transcrição de vídeo do canal Código Fonte TV. Limpa de repetições e disfluências de fala, organizada em seções. Idioma original: português (sem necessidade de tradução).

## Abertura e contexto

O canal já produz vídeos há quase 9 anos e reconhece que Go (Golang) é uma tecnologia que recebeu pouca atenção ao longo do tempo. Em 2019 o canal publicou um episódio do "Dicionário do Programador" sobre Go, questionando se ela seria "a linguagem do futuro". Cinco anos depois (2024), o vídeo revisita o tema para mostrar como Go evoluiu tecnicamente e, principalmente, em adoção de mercado — cobrindo salários com dados atualizados da pesquisa própria do canal (pesquisa.codefonte.com.br) e da pesquisa oficial do time do Go no Google, o "Go Developer Survey".

Muita gente que usa Go migrou de outras stacks (ex.: Java) e percebeu que é possível resolver os mesmos problemas de forma mais simples — especialmente em concorrência, onde Go se destaca claramente de outras stacks.

## O que é Go

Linguagem procedural, estaticamente tipada, com sintaxe próxima de C. Criada em 2007 pelo Google, open source desde 2009. Tornou-se tendência entre devs e projetos que exigem eficiência e desempenho. O grande destaque de uso está em desenvolvimento nativo em nuvem, especialmente em arquitetura de microsserviços, por causa de:

- Capacidade de concorrência
- Processos leves (goroutines)
- Garbage collector eficiente

O uso de Go também vem crescendo em Inteligência Artificial e IoT.

## Pesquisa salarial Código Fonte — Go vs. Java

A pesquisa do canal (pesquisa.codefonte.com.br) permite filtrar por linguagem principal declarada pelo respondente. A comparação abaixo usa Java como baseline por ser a linguagem com maior volume de respostas com quem também atua em Go.

**Java — mais de 2.000 respondentes, média salarial por nível:**
- Estágio: R$ 1.800
- Júnior: R$ 4.200
- Pleno: R$ 7.900
- Sênior: R$ 14.300

**Go — média salarial por nível:**
- Estágio: menor que Java
- Júnior: R$ 5.500
- Pleno: R$ 10.700
- Sênior: R$ 20.565
- Outros (especialista / Tech Lead / Principal): R$ 22.000

Diferença mais marcante no nível Sênior: quase R$ 6.000 a mais em Go sobre Java. Interpretação do canal: o mercado de Go é mais seleto e paga melhor.

**Área de atuação:**
- Go: 75% backend
- Java: 59% backend, 33% fullstack (reflexo do maior ecossistema de frameworks fullstack em Java)

**CLT vs. PJ (Go):**
- CLT: média de R$ 12.000
- PJ: média de R$ 21.000 (transcrição original citou "211.000", tratado como erro de transcrição/fala; valor mantido como possível erro — ver Open Questions na fonte)

**Por estado (Go, ordenado por volume de respostas):**
- São Paulo: R$ 15.800 (maior volume de respostas)
- Santa Catarina: R$ 15.000 (37 participantes)
- Minas Gerais: R$ 14.000
- Seguem Rio de Janeiro e Paraná

**Atuação remota para empresas no exterior (morando no Brasil):**
- Go: ~27,7% atuam em projetos no exterior
- Java: ~12%

Interpretação do canal: existe demanda internacional maior por Go, e por ser uma linguagem de nicho relativo, paga melhor (oferta e demanda).

## Go Developer Survey (Google) — satisfação e uso

Pesquisa oficial do time do Go, feita duas vezes por ano.

**Satisfação geral:**
- Go Developer Survey: 93% dos entrevistados "um pouco" ou "muito" satisfeitos com Go no último ano
- Pesquisa Código Fonte (filtro Go): 97% satisfeitos com a stack atual; satisfação com a renda soma mais de 75% entre "satisfeito" e "muito satisfeito"

**Provedor de nuvem utilizado:**
- AWS: 52%
- Data centers internos (próprios): 42%
- GCP e Azure na sequência

**Satisfação por provedor:**
- AWS: 77%
- GCP: 77%
- Azure: 57% (37% neutro — nem satisfeito nem insatisfeito)

**Área mais importante ao desenvolver com Go (múltipla escolha):**
- Latência: 61%
- Uso total de memória
- Uso total de CPU
- Performance do garbage collector / alocação

Interpretação: como Go é muito usado em cloud, esses fatores (latência, memória, CPU) têm impacto direto em custo de infraestrutura.

**Experiência profissional dos respondentes:**
- Maior grupo: 16 ou mais anos de experiência em codificação
- Em seguida: 6 a 10 anos
- Depois: 3 a 5 anos

Interpretação: Go tende a ser adotado por desenvolvedores experientes, muitas vezes vindos de outras linguagens (ex.: Java) para casos de uso específicos (cloud, microsserviços) — não uma substituição total, mas um intercâmbio de linguagens conforme o tipo de serviço.

**Situação de emprego dos respondentes:**
- 81% empregados em tempo integral (full employed)
- 6% trabalham por conta própria
- 4% freelancer
- 4% estudante

**Para que serve Go (uso declarado, múltipla escolha):**
- APIs e serviços RPC: 74%
- Ferramentas CLI: 63%
- Frontend/sites (via frameworks Go): 45%

## Salário por tempo de experiência (Go Developer Survey)

- Maior concentração de respondentes: 2 a 4 anos de experiência, faixa salarial entre R$ 6.000–7.000 subindo até R$ 7.000–9.000
- Faixa de R$ 20.000–30.000: concentrada em profissionais com 10 a 15 anos de experiência em TI (não necessariamente todos em Go — geralmente seniors migrados de outra stack, que mantêm o nível sênior ao migrar para Go)

Interpretação: a curva de aprendizado para quem já é sênior em outra stack costuma ser mais suave em Go.

**Tempo até a primeira oportunidade em Go:**
- Menos de 1 ano: 63%
- Entre 1 e 2 anos: 27%

**Quantidade de processos seletivos até conseguir a vaga, por nível:**
- Sênior: mais de 8
- Estágio: mais de 8
- Júnior: entre 2 e 4 (maioria)

**Como conseguiu a oportunidade atual, por nível:**
- Estágio e Júnior: LinkedIn é o principal canal
- Pleno e Sênior: indicação pessoal fica em segundo lugar (mas ainda relevante), LinkedIn continua forte

## Verificação rápida no LinkedIn (busca ao vivo no vídeo)

Busca por "golang" no Brasil no LinkedIn: 1.203 resultados no momento da gravação, incluindo empresas grandes (Totvs, Sigma, Épico Systems) e vagas remotas para empresas internacionais (Coinbase, PagBank).

**Exemplo — Mercado Livre (vaga Sênior Software Engineer):**
Stack e práticas citadas na vaga: SOLID, AWS, GCP, Git Flow, Clean Architecture, Design Patterns, microsserviços.

**Exemplo — vaga remota (empresa sediada em Curitiba, vaga 100% remota):** evidencia oferta real de trabalho remoto para quem trabalha com Go.

**Exemplo — vaga remota (empresa "Dev"):** requisitos incluem microsserviços, cloud, SQL, e conhecimento amplo de SRE, DevOps e testes automatizados — reforçando que Go raramente é usado isolado, sempre dentro de um conjunto mais amplo de práticas de backend moderno.

## Conclusão do canal

Go é considerada pelo canal uma linguagem sólida para investir: ainda não é "hype" entre devs (comparado a linguagens mais faladas), mas já tem mercado consolidado e atrativo financeiramente, especialmente para quem migra de stacks mais maduras como Java ou C#.

## Menção comercial (Full Cycle)

O vídeo inclui uma menção patrocinada à Full Cycle e sua pós-graduação "Go Expert", estruturada em 6 pilares: fundamentos da linguagem, testes automatizados, desenvolvimento de APIs, performance e multithreading em Go, Clean Code, e internals do Go runtime. Citados como cases de clientes da Full Cycle: Mercado Livre, Itaú e Globo Play.
