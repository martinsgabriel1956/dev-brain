# Subagentes: Quando Vale a Pena Usar — Um Case Real de Custo x Velocidade

> Transcrição de vídeo (autor não identificado por nome completo/canal na fala). O vídeo é descrito como uma aula da comunidade do autor ("minha comunidade"), com referência direta à skill **"TLC Spec Driven"** — mesma skill documentada em [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] — o que aponta fortemente para o mesmo autor/canal daquela fonte (indício, não confirmação, de autoria ligada à Tech Leads Club). Erros de reconhecimento de fala (ASR) corrigidos por contexto técnico ao transformar em Markdown — ver observações ao final.

Subagentes são extremamente importantes para desenvolver software com IA, mas podem ser muito caros e muito lentos. Este vídeo mostra um case real de avaliação de quando usar subagentes e como equilibrar custo e velocidade — a jornada de como o autor otimizou a skill **TLC Spec Driven** para ficar mais efetiva e mais barata. O objetivo é uma fórmula prática, baseada num benchmark que pode ser rodado repetidamente, para decidir quando delegar para um subagente vale a pena, quando se paga, e quando isso deixa a implementação mais lenta em vez de mais rápida.

## O Ponto de Partida: Janela de Contexto

Antes de comparar cenários, a pergunta é sobre janela de contexto: imagine 10% ocupados, depois 45% no meio da tarefa — sem usar subagentes — e no final da tarefa a janela chegou a 74%. Isso foi o que aconteceu na implementação de teste do autor.

## O Experimento

Para testar isso, o autor fez várias implementações da mesma tarefa: integração com Stripe (usada como benchmark de referência), organizada em uma spec do TLC Spec Driven com 17 tasks agrupadas num único épico grande.

### Cenário 1 — Sem Subagentes (Baseline)

Todas as 17 tasks executadas na mesma janela de contexto, sem nenhum subagente.

- **Tempo:** em torno de 15-19 minutos (o autor cita os dois números em momentos diferentes do vídeo; ver nota de transcrição ao final).
- **Janela de contexto final:** 74% (num modelo com janela de 200.000 tokens) — isso é o *one-shot*, sem contar nenhuma correção depois.
- **Tokens consumidos:** ~9 milhões.
- **Nota de qualidade:** ~0,93.

Com a janela já em 74% no one-shot, qualquer correção subsequente provavelmente levaria a janela a 100% — ou seja, dava para fazer, mas ficou extremamente apertado: pouco espaço para corrigir sem começar a degradar qualidade (por ficar reenviando e recebendo de volta uma janela quase cheia) e sem começar a pagar mais por isso.

### Cenário 2 — Um Subagente por Task (Granularidade Máxima)

Cada uma das 17 tasks do spec disparou seu próprio subagente.

- **Tempo:** 43 minutos.
- **Tokens consumidos:** 25 milhões — **150% a mais de tokens** que o baseline sem subagentes.
- **Nota de qualidade:** caiu para 0,81.

**Por que a qualidade cai e o custo sobe:** cada subagente inicia sem contexto nenhum — ele recebe o que precisa fazer e recarrega os arquivos necessários do zero, mesmo que o agente principal já tivesse esse contexto carregado. Com 17 tasks, isso significa recarregar contexto 17 vezes. Além do custo de tokens, o contexto fica tão fragmentado entre tasks pequenas que o subagente perde a noção do todo, e a qualidade da implementação cai.

### Cenário 3 — Agrupamento por Fases (Implementação Atual da TLC Spec Driven)

Na versão atual da skill, as tasks do spec são agrupadas em **fases**: conjuntos coesos de tasks que podem ser feitas juntas. Isso serve a dois propósitos — saber quais fases podem ser paralelizadas, e agrupar trabalho relacionado num mesmo subagente em vez de espalhar por muitos subagentes pequenos.

- **Janela de contexto do agente principal:** caiu para 32% (contra 74% do baseline sem subagentes) — sobra espaço para trabalhar depois, inclusive para correções.
- **Tempo:** 35 minutos (contra 43 minutos do Cenário 2).
- **Tokens consumidos:** 15 milhões — 50% a mais que o baseline sem subagentes (9 milhões), mas bem menos que o Cenário 2 granular (25 milhões).
- **Nota de qualidade:** 0,90 — já próxima da nota do baseline com um único agente.

**Por que menos subagentes deixa a janela do principal mais leve:** cada subagente, ao terminar, devolve um output para o agente principal. Quanto mais subagentes, mais outputs se acumulam na janela do agente principal, poluindo-a — mesmo que cada subagente individualmente processe pouco. Menos subagentes (mas cada um cobrindo mais trabalho coeso) significa menos outputs somados de volta ao principal.

### Cenário 4 — O Sweet Spot: 3 Subagentes

Buscando o ponto de equilíbrio onde tempo e custo não aumentam muito mas ainda há ganho de paralelismo, o autor chegou a **três subagentes** para esse contexto — agrupando, por exemplo, tasks T1 a T6 em três grupos (dois grupos de tasks relacionadas por subagente).

- **Tempo:** 18 minutos (praticamente igual ao baseline sem subagentes, citado como ~19 minutos neste ponto do vídeo).
- **Tokens consumidos:** 10 milhões (praticamente igual aos ~9 milhões do baseline).
- **Nota de qualidade:** 0,95 — comparável (estatisticamente equivalente, segundo o autor) aos 0,93 do baseline.
- **Janela de contexto final do agente principal:** 26%.

Ou seja: no sweet spot de três subagentes, tempo, custo e qualidade ficam basicamente equivalentes a rodar tudo num único agente — mas com a vantagem de terminar com a janela de contexto do agente principal quase vazia (26%), em vez de quase cheia (74%).

## Por Que Isso Pode Ficar Mais Barato que Não Usar Subagente Nenhum

A comparação acima foi feita com um one-shot (17 tasks). Mas o ganho do agrupamento em subagentes aparece com mais força à medida que a tarefa cresce:

- No cenário sem subagentes (Cenário 1) e no cenário mais granular (Cenário 2), terminar o one-shot já deixa pouca margem de janela de contexto para correções — qualquer ajuste depois começa a degradar qualidade e a custar mais caro.
- No sweet spot (Cenário 4), a janela termina em 26%, sobrando muito espaço: dá para abrir outros subagentes para explorar, criar novas tasks na spec e corrigir sem esbarrar no teto da janela.
- Esse mesmo agrupamento escalaria bem para specs muito maiores (o autor cita hipoteticamente mais de 100 tasks): a partir de um certo tamanho de tarefa, o cenário sem subagentes começa a inflar demais a janela e o custo, enquanto o cenário agrupado em poucos subagentes coesos continua com folga.

## Aplicando Fora da TLC Spec Driven

Para quem não usa a TLC Spec Driven: olhar como o próprio framework de spec-driven usado faz a granularidade das tasks (a TLC Spec Driven usa tasks atômicas e granulares), comparar com o agrupamento por fases descrito aqui, e pedir ao agente para agrupar de forma similar — sem garantia de que o resultado numérico será idêntico ao benchmark deste vídeo, mas seguindo a mesma lógica.

Resumo da curva observada no benchmark:

| Cenário | Tempo | Tokens | Nota |
|---|---|---|---|
| Sem subagentes | ~15-19 min | ~9M | 0,93 |
| 1 subagente por task (17) | 43 min | 25M | 0,81 |
| Agrupado por fases | 35 min | 15M | 0,90 |
| 3 subagentes (sweet spot) | 18 min | 10M | 0,95 |

## O Que Diz a Indústria

O autor pesquisou se esses resultados batiam com pesquisas recentes do setor — e descreve a indústria como dividida entre duas posições, ambas compatíveis com o que o benchmark encontrou:

- **Anthropic:** pesquisa longa indicando que multi-agente aumenta o custo, mas em 90% dos casos a resposta final foi melhor — a lógica sendo que, à medida que um agente único roda por muito tempo, a qualidade começa a degradar. O autor nota que, no caso da pesquisa da Anthropic, o custo chegou a ser **15 vezes maior** com subagentes (razão não detalhada na fonte) — número que ele não conseguiu explicar totalmente, mas especula que, se as tasks tivessem sido agrupadas de forma menos granular (como no Cenário 3/4 deste benchmark), o custo provavelmente equilibraria com o de um agente único e passaria a haver ganho real.
- **Cognition** (empresa por trás do Devin, que adquiriu o Windsurf): posição de que subagentes são perigosos e atrapalham o contexto — cada ação de um agente carrega uma decisão que fica registrada na janela; quando o trabalho passa para um subagente novo, esse subagente não tem acesso a essas decisões anteriores. O autor conecta isso diretamente ao Cenário 2 deste benchmark (granularidade excessiva fragmenta o contexto e derruba a qualidade), e argumenta que é por isso que trabalhar a partir de uma spec compartilhada (em vez de deixar o agente principal fragmentar contexto livremente ao delegar) importa: o subagente, ao carregar a spec, já recebe o contexto necessário para fazer seu trabalho sem depender de decisões implícitas do agente pai.

## Modelo Mental Para Decidir Quando Usar Subagentes

1. **Busca/varredura em codebase, pesquisa (fase de Research do padrão Research → Plan → Implement):** sempre vale usar subagente. O agente principal passa um prompt dizendo o que quer de volta; o subagente varre o codebase, agrupa e retorna só o necessário — preserva a janela do principal e não a polui.
2. **Tarefas longas, com várias tasks (o caso central deste benchmark):** se a tarefa for rodar por muito tempo (o autor cita a referência de "mais de meia hora"), provavelmente vai encher a janela do agente principal — sem contar correções depois. A partir daí, começa a valer a pena separar em subagentes. **Mas não separar de forma muito granular** — granularidade excessiva aumenta tempo e custo (Cenário 2) em vez de reduzir.
3. **Tarefas pequenas e fortemente acopladas (ex.: uma refatoração pontual):** não há problema em manter na mesma janela — mas vale monitorar o quanto isso está enchendo a janela, para não cair num loop de passar muitos tokens para frente e para trás e começar a pagar mais por isso.
4. **O trabalho pode ser paralelizado?** Se sim, subagentes ajudam a ganhar velocidade — mas de novo, avaliando o tamanho do trabalho, o quanto está agrupado, e se realmente compensa dividir ou não.

## Fechamento

O autor menciona que a TLC Spec Driven será atualizada para refletir esses achados (agrupamento por fases em vez de por task individual), mas que já é possível pedir esse comportamento na versão atual da skill, dizendo explicitamente na hora de implementar que se quer usar, por exemplo, três fases por subagente — o agente faz um agrupamento equivalente ao demonstrado no vídeo.

---

## Notas de Transcrição

Transcrição original obtida via reconhecimento automático de fala (ASR), com erros corrigidos por contexto técnico ao formatar em Markdown. Pontos de atenção:

- **"Sablementar" / "saber a gente" / "Sub a gente"** → corrigidos para **subagente(s)**, erro recorrente de ASR ao longo de todo o áudio (o reconhecimento frequentemente separa "sub-agente" em fragmentos foneticamente parecidos com outras palavras).
- **"TLC Speck Driven" / "Telec Pack Driven" / "Telec Spec Driven"** → normalizado para **TLC Spec Driven**, mesma skill referenciada em [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]].
- **"pur tesk"** (nome de uma run/ferramenta mostrada na tela, não identificada com clareza no áudio) → mantido como transcrito foneticamente; não foi possível confirmar o nome exato da ferramenta/interface mostrada (possivelmente um nome próprio de produto ou de run específica, não decifrável apenas pelo áudio).
- **Inconsistência numérica no próprio vídeo:** o autor cita o tempo do baseline sem subagentes como "15 minutos" no início e como "19 minutos" mais adiante, ao comparar com o Cenário 4. Ambos os números foram preservados nesta transcrição, sem tentar resolver a divergência — possivelmente o autor está se referindo a execuções ligeiramente diferentes do mesmo baseline, ou a um lapso de fala.
- **"Antropic"** → corrigido para **Anthropic**.
- **"Winds surf"** → corrigido para **Windsurf** (produto adquirido pela Cognition, mencionado no vídeo).
- Marcadores de fala coloquiais comuns em português brasileiro ("né", "tá vendo", "gente" em excesso, repetições) foram reduzidos na reescrita para melhorar a legibilidade, sem alterar o conteúdo técnico.
- Autoria não confirmada por nome completo nesta transcrição — inferida por contexto (menção direta à skill "TLC Spec Driven", ao termo "nossa comunidade") como possivelmente ligada ao mesmo autor/canal de [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]], mas isso **não está confirmado**.
