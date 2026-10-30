---
title: "Como a Anthropic faz code review com agentes — as sete camadas (e o que dá para copiar)"
source_type: transcrição de vídeo (PT-BR, legenda automática)
author: "não identificado (canal brasileiro de engenharia de software com IA; vende treinamento próprio e lê papers)"
date_ingested: 2026-10-26
---

# Como a Anthropic faz code review com agentes — as sete camadas

> Transcrição limpa (pontuação, parágrafos e termos corrigidos). Já em português; sem tradução. Correções de ASR: "Tropic" → Anthropic; "Cloud"/"Cloud Code"/"Cloudinho" → Claude/Claude Code; "Cloud MD" → CLAUDE.md; "review MD"/"Reval" → REVIEW.md; "B request"/"PR"/"pers"/"PS" → PR (pull request); "niripque"/"nirpque"/"nitpak" → nitpick; "Fature Flag" → feature flag; "LMA Jud" → LLM-as-a-judge; "EE ETH" → ETH Zurique; "hacker rank" → HackerRank; "Lightoft/Bights Off" → lights-off (fábrica de software "no escuro"); "queijo suíço" = modelo do queijo suíço. Trechos ilegíveis/ambíguos mantidos entre colchetes: "Manulou esse código" lido como "Alguém leu esse código?"; "gerou briga na boletec" lido como "bolha tech"; "SCV MD" (arquivo não identificado, provavelmente outro arquivo de instruções além do CLAUDE.md); "200.500 por dia" em maio (provável "200 a 500"); "o PR que precisa de cinco rodadas ou mais [caiu] para 1,5" (valor inicial e unidade perdidos); "Shura Software Factory" (nome do paper ilegível). O link do post original da Anthropic e dos três papers está na descrição do vídeo e **não** foi fornecido. Nome do apresentador não identificado.

## Abertura: o volume

Este é o tanto de mudança de código que entra por dia na Anthropic: em maio eram cerca de 200–500 por dia [ASR: "200.500"]; em setembro, mais de **30.000 mudanças de código por dia**. **90% desse código é escrito pelo Claude, e quem revisa também é o próprio Claude.** Todo PR passa por uma revisão de agente antes de qualquer pessoa olhar — e há um tipo de mudança que **nunca** passa por pessoa nenhuma.

O que o apresentador traz é um post que a Anthropic publicou "essa semana" sobre como tudo isso funciona por dentro: **sete camadas**. Há muita coisa que dá para copiar e coisa que é impossível para "meros mortais" — ele separa o que é aplicável do que é "sonho de consumo". Como vende treinamento, avisa que vai ser mais chato que o normal com o que tem prova e o que não tem, e que lê os papers para o espectador não precisar; há fontes de estudos para ver se vale seguir o que a Anthropic faz.

## A frase que gerou briga na bolha tech

> "Nobody on the team keeps a complete mental model of Claude Code in their head, and we don't think anyone needs to."

Ninguém no time tem um modelo mental completo do Claude Code na cabeça — e eles acham que não precisa. Muita gente da indústria lê isso e estranha. O que a Anthropic faz é mostrar **por quê** e quais são os processos.

**A mudança de pergunta.** A pergunta antiga era "alguém leu esse código?". A nova é: **"o que pode dar errado se esse commit for para produção, e qual é a checagem que pega isso melhor?"** — e a checagem pode ser automática, uma pesquisa ou manual. Junto vem uma condição: **menos revisão humana não pode significar mais coisas quebrando.** Eles medem quanto precisa ser desfeito (revert) e quantos problemas chegam à produção; se qualquer um dos dois sobe, a economia é falsa — o trabalho humano só mudou de lugar, de revisar para consertar em produção, "com todo o impacto negativo que isso tem".

## As sete camadas (queijo suíço)

Eles descrevem como o modelo do queijo suíço (cada camada tem furos; juntas, cobrem).

**Camada 1 — antes do PR existir.** O Claude roda todos os testes, o build e o linter. Depois, **um segundo agente com contexto limpo revisa o diff.** O detalhe é o *contexto limpo*: o agente que escreveu o código carrega o raciocínio dele na memória e isso contamina a revisão. O apresentador subiu na semana anterior um paper sobre isso: quanto mais contexto, mais enviesado o raciocínio. Exemplo da vida real: se na semana passada você disse que estava com dor de cabeça e febre, e hoje diz que está com febre, o agente, com o contexto da semana passada, vai assumir/adivinhar que também é dor de cabeça — nem sempre a resposta correta. Então: contexto limpo, subagente, só o diff.

**Camada 2 — CI/CD de sempre.** Lint, tipos, testes, build. Vermelho trava o merge. "Não tem muito segredo."

**Camada 3 — o Claude Code Review em todo PR.** É onde "fica da hora". Roda automático, antes de qualquer pessoa olhar. Ele **não lê só o diff**: lê o diff **contra o repositório inteiro** e **contra a intenção declarada no PR**. As perguntas: isso resolve o problema que diz resolver? Encaixa no sistema? Quebra outra coisa?

Como roda (o apresentador gostou do post da Anthropic que saiu no HackerRank e diz que tenta algo parecido no trabalho): **vários agentes caçam bugs ao mesmo tempo**; um **grupo separado** volta com cada achado para verificar; **só vira comentário no PR se os agentes que saem em paralelo concordam que é um problema de verdade.** O que for só estilo, limpeza ou que não foi achado por todos é descartado antes de chegar a você — "um filtro social dos agentes". Eles testaram esses filtros com A/B nos próprios PRs antes de mantê-los. O que sobrevive vira comentário no PR, **ordenado por gravidade e etiquetado** (importante, nitpick, pré-existente).

**O arquivo REVIEW.md.** No meio disso há um arquivo que o apresentador quer começar a usar. Quem o escreve é o **dono do código**; serve para dizer ao revisor o que importa naquele repositório — se o time se importa com nome de variável, ou o agente está pegando algo que não deveria, isso vai ali: "minha colinha pro revisor". Exemplos da Anthropic:
- Em **documentação**, a falha é *mentir*: se a doc diz algo que não está no código — por exemplo, um README dizendo que uma configuração vem ligada por padrão quando não vem — é falha, e o revisor tem que pegar.
- Em **configuração**, a falha é *apontar para o lugar errado*: apontar para produção quando deveria apontar para staging/dev.
- Não é regra de código; é a descrição de qual é o *smell* (o indicador) para pesquisar na hora de revisar.
- Pede-se ao revisor que dê **o arquivo e a linha como prova**, e limita-se **quantos nitpicks** ele pode fazer por PR.

**O ciclo de retroalimentação.** Se os agentes apontam o mesmo erro em vários PRs, não se corrige PR por PR (senão o próximo PR repete). Pergunta-se: **é um erro de verdade?** Se for, vira **regra de lint, linha no CLAUDE.md ou skill** — procura-se a parte do harness que está faltando. Se for **falso positivo**, vira **uma linha no REVIEW.md** para o revisor parar de reclamar (ex.: reclamar de formatação num script em que a indentação não importa — adiciona-se "ignore esse tipo de formatação nesse tipo de arquivo"). Resultado: o CLAUDE.md e as skills ensinam a *escrever*; o REVIEW.md ensina a *revisar* — ambos "arquivos de memória/checkpoint" que melhoram no longo prazo.

**Camada 4 — segurança.** Tratada de passagem ("tranquila").

**Camada 5 — onde um humano entra.** Quantas pessoas revisam depende do nível:
- **Nenhuma**: documento de texto, feature interna, algo atrás de flag — baixo impacto.
- **Pelo menos uma**: mudanças normais de produto, feature nova, **áreas sensíveis** (cache, auto-updater, system prompt). Para a Anthropic, essa "uma pessoa" **pode ser o próprio autor** — quem pediu ao agente para fazer — não precisa ser um par.
- **Duas**: código mais crítico, "hot code" — caminhos importantes que trazem muito revenue.

**Quem decide o nível é um agente classificador, e um segundo classificador confere o primeiro.** Frase do post: **"quem define o nível é a mudança, não o autor."** O classificador lê a mudança e escolhe o nível; o segundo pergunta se aquela mudança específica precisa mesmo do número de pessoas que o nível diz. "É o LLM-as-a-judge." Mudança de baixo risco não precisa de nenhuma pessoa.

**Camada 6 — a fila de merge.** As checagens rodam de novo, agora com a mudança aplicada em cima da main. "Um CI/CD de novo."

**Camada 7 — depois do merge.** Atrás de uma flag interna; release gradual; monitoram, e se não está tudo certo, consertam ou desfazem. Parecido com um canary release.

## Metade do segredo: reverter em minutos

Boa parte da confiança da Anthropic **não vem da revisão do PR em si, mas de saber que conseguem desfazer a mudança em minutos.** Mudança pequena, atrás de feature flag, com revert muito rápido — isso muda quanto risco se aguenta antes de ser problema.

O apresentador alinha isso ao que faz no trabalho: **desenvolvimento incremental com PRs pequenos (máximo de 300 linhas de mudança)**, para ter o mínimo testável e dar mais *ownership* a quem faz a mudança; estimulam os engenheiros a fazerem o release e o deploy eles mesmos; têm continuous integration/delivery (ninguém "pede para alguém fazer o deploy"); no merge é fácil voltar e saber se funciona; há feature flag por trás; se for crítico, a pessoa já pensa assim desde que começa a programar. Daí "a revisão meio que é um detalhe, e por isso você se dá o luxo de poder pular" — no pior caso o código é ruim e o rollback é rápido. Condições: **observabilidade** (saber a saúde do sistema) e **engenheiros com ownership** — não delegar a responsabilidade a quem revisa o PR, mas ter o autor responsável e autônomo.

## Como saber que o revisor é bom: incidentes viram evals

Tudo isso só vale se o agente revisor for bom. A resposta da Anthropic tem a ver com **post-mortem**: **todo incidente vira um caso de teste.** Pegam PRs antigos que causaram incidentes, junto com os consertos e reverts. **Um engenheiro que conhece aquele código confirma** se cada bug realmente foi causado ali (às vezes se reverte um PR e a causa era outra). Confirmado, o caso entra num conjunto de *evals*; o que o revisor deixou de pegar vira regra no CLAUDE.md, numa skill ou numa checagem nova. **Qualquer mudança no revisor — prompt novo, modelo novo, ferramenta nova — é rodada contra todos esses casos que falharam no passado**; se passa, ótimo; senão, tem que calibrar. É um **teste de regressão do revisor** — o apresentador diz que é a primeira vez que vê esse paradigma aplicado assim (para bugs de código já se cria um teste unitário/e2e).

## Barulho, nitpicks e o loop de 50 rodadas

Em observabilidade, quanto mais estrito, mais barulho: se todo erro gera alerta, você ignora o que de fato é incidente. A forma de medir se um comentário deve existir é **olhar o que a pessoa fez com ele**: consertou, disse que estava errado, disse que era intencional, ou disse que era nitpick e não se importava. Isso retroalimenta o revisor e ajuda a achar o ponto ótimo: pegar o máximo de erros com o mínimo de falso positivo.

**Por que barulho custa mais caro quando o autor é um agente.** Uma pessoa ignora um nitpick em 2 segundos ou corrige. O agente corrige → vira commit novo → nova rodada de revisão → novo nitpick → novo conserto → … "nunca acaba". Houve **um PR com mais de 50 rodadas de revisão numa noite só**, rodando e gastando token até alguém acordar e ver (token eles nem se importam, mas era um loop eterno em que autor e revisor faziam "o que tinham que fazer").

**A correção:** depois de **três rodadas**, o agente revisor **para de pedir conserto e manda o autor repensar a abordagem**; as revisões seguintes **olham só o que mudou**; e quando acham um bug, apontam a **classe inteira do bug** para consertar em todo lugar de uma vez. **Resultado na Anthropic:** PRs que passam em **uma rodada** foram de **65% para 78%**; PRs que precisam de **cinco rodadas ou mais** caíram [para 1,5 — unidade/valor inicial ilegíveis].

## Voltando à realidade: funciona na nossa empresa?

1. **Quantos desses PRs são problema ou revert?** Um paper que o apresentador já comentou diz que ~40% dos PRs de agente viram trabalho depois ou são revertidos. A Anthropic diz que a **proporção** de reverts **caiu mais de 40% de junho a setembro**, enquanto os PRs mergeados **mais que dobraram** no mesmo período. Conta dele: melhorou muito **por PR**, mas em números absolutos pode haver mais PRs revertidos — "ainda assim mais coisa quebra por dia do que antes".
2. **Custo.** São vários agentes em paralelo, grupo de verificação, classificadores, conjunto de avaliação rodando todo dia. É caro — e eles rodam o produto deles com tokens deles: "em teoria têm token infinito; a gente não".
3. **O código revisado é o do Claude Code**, público e provavelmente o código que o modelo mais conhece do mundo.

**Paper 1 — Benchmarking code review agents on bug detection** (do mês; **Microsoft**; ele ressalta que é contra o interesse de quem paga a conta da ferramenta, logo mais crível). Montaram **1.000 tarefas de revisão com bugs reais**: uma parte de **98 repositórios abertos** e outra de **repositórios fechados de uma empresa grande** (cerca de 800 tarefas, segundo a fala). Nos **abertos**, o revisor achou o bug **nos primeiros cinco comentários em 71%** das vezes; nos **fechados** o desempenho **despencou**. Conclusão do apresentador: a Anthropic está no **melhor caso possível** para um revisor de IA.

**Paper 2 — ETH Zurique.** Pediram a um agente que escrevesse a suíte de testes a partir da especificação: **até 88% dos testes que ele escreveu passam** na suíte válida (verde, bonita), mas essa suíte **pega menos de 60% dos erros plantados de propósito**. Frase do paper: **"o agente constrói software que ele não consegue verificar."**

**Paper 3.** Acompanharam **67.774 PRs de agentes já mergeados** contra **5.000 PRs humanos** nos mesmos repositórios: o PR de agente precisa de **fix posterior ~1,5× mais vezes**, e quando precisa, **quem conserta é o próprio agente em quase 70% das vezes**. Duas metades: a boa — os agentes dão conta de terminar o próprio serviço; a outra — mesmo assim precisam de fix várias vezes mais que um humano.

## O que levar (cinco coisas que não custam dinheiro)

1. **Revisão com contexto limpo:** para revisar o que você fez, use um subagente novo que recebe só o diff — não o agente que criou.
2. **REVIEW.md:** como é a cara da falha *naquele* pedaço de código.
3. **Erro que se repete vira regra** (lint, CLAUDE.md, skill), não só comentário no PR — exercite o músculo de ter um `.md` onde documentar isso para o agente ser cada vez mais autônomo.
4. **Teto de rodadas:** depois de três ou quatro, peça a um humano para verificar (se for fazer lights-off).
5. **Aprovação de bot nunca conta como aprovação de pessoa.**

## O que sobra para os humanos na Anthropic

Decidir **se vale a pena construir**; **revisar o que é perigoso**; **revisar a arquitetura que vai virar padrão** e será copiada; **ler evidência — a saída do teste, não o resumo do agente**; e **ser dono do resultado**: "você mergeou, você é o dono; quebrou, você conserta". O apresentador ressalta que **não é blame** (não é achar o culpado): é porque **quem fez tem mais contexto e conserta mais rápido**. Ele já fala de *ownership* em outro vídeo do canal.

## Fecho

O post da Anthropic e os três papers estão na descrição do vídeo (possível vídeo só sobre eles); code review é "o gargalo da indústria". Ele menciona seu treinamento de engenharia de software com IA, pede inscrição/membership e pergunta nos comentários quem já faz PR automatizado 100%.
