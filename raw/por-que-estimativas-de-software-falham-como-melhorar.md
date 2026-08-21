# Por Que Estimativas de Software Sempre Dão Errado (e Como Melhorar a Precisão)

> Transcrição de vídeo (autor não identificado — canal cita patrocínio da Abacus/Abacus.AI, pt-BR). Original em ASR bruto, sem pontuação nem parágrafos; limpa, pontuada e organizada em seções abaixo. Sem necessidade de tradução (já em pt-BR). O bloco publicitário do patrocinador foi condensado numa nota curta, sem valor técnico para a wiki.

## Abertura

Estimativas nunca funcionam em software. Depois de uns 10 anos lidando com estimativas que não funcionavam, o autor diz ter uma noção do que está acontecendo. Proposta do vídeo: entender por que as estimativas estão sempre erradas, por que às vezes não faz sentido fazer estimativas, e nos momentos em que faz sentido, como melhorar a precisão delas.

> **Nota (patrocínio, sem relevância técnica):** o vídeo inclui um bloco publicitário da Abacus (Abacus.AI) — chat multi-modelo, geração de imagem/código/PowerPoint, Deep Research, Deep Agent e IDE própria por assinatura mensal. Omitido do restante da transcrição por ser conteúdo comercial, não técnico.

## Parte 1 — Por Que a Estimativa Está Sempre Errada

Na maioria das empresas que fazem estimativas, o grau de precisão é baixo — e se a empresa não mede esse erro, é quase certo que a precisão real seja baixíssima. Isso não é necessariamente culpa da empresa: é que o modelo mental usado para estimar não é fazível.

### O modelo mental que não funciona

O modelo padrão é: você tem a ideia de uma feature → faz **uma única estimativa** → desenvolve a feature esperando que ela saia dentro de uma margem pequena (ex.: uma semana para mais ou para menos). A chance de isso dar certo é muito baixa, porque existe uma série de fatores que invalidam esse modelo.

Durante o desenvolvimento é comum perceber que os requisitos não estavam bem explicados, que não era bem aquilo que era esperado, ou que a gestão mudou de ideia — ou seja, no momento da estimativa a informação disponível era incompleta. Conforme mais informação chega, a estimativa original deixa de fazer sentido. Mas as empresas raramente invalidam a estimativa quando isso acontece — em vez disso, tentam forçar os fatores de produção para que a estimativa original ainda seja alcançada, mesmo sem a informação completa que ela exigiria.

### Fator 1 — Requisitos incompletos ou ambíguos

A compreensão que o stakeholder tinha ao pedir algo e a compreensão que a equipe técnica tinha ao estimar são frequentemente coisas diferentes — às vezes o cliente queria outra coisa, independente de o requisito mudar depois no meio do desenvolvimento. Ao perceber que um requisito é incompleto, ambíguo, ou que mudou, a estimativa é invalidada — mas raramente é essa invalidação que acontece na prática.

### Fator 2 — Incerteza tecnológica

Experiência comum: achar que algo é simples e, ao tentar implementar, descobrir que a tecnologia escolhida não dá suporte àquilo que se queria fazer (a lib, a ORM, o framework). Se os pontos possíveis de incerteza não são explorados antes de estimar, quando eles surgirem à tona vão alterar a viabilidade da estimativa já feita.

### Fator 3 — Pressão organizacional

Vendas, marketing e o CEO pressionam por uma estimativa menor do que a real. Exemplo: o líder da equipe acha que uma tarefa vai demorar um mês, mas o CEO pressiona por duas semanas — mesmo o líder achando quase impossível cumprir esse prazo. Em organizações disfuncionais, é mais fácil ceder à pressão, depois jogar a culpa em algo aleatório no meio do caminho (ex.: "deu problema na configuração da AWS") e esticar o prazo — superfaturando-o depois. Isso acontece em empresas reais.

### Fator 4 — Viés humano (planejar para o cenário ideal)

Bem documentado em estudos: as pessoas planejam para as coisas darem certo, esquecendo de deixar margem para imprevistos e para custos ocultos como troca de contexto.

**Exemplo real do autor** — estimar uma feature simples (usuário clica um botão, envia um formulário para um endpoint):

```
Estimativa inicial ingênua:                    2h
+ revisão de PR (15 min "puro")                2h15
+ custo de troca de contexto do revisor
  (quem revisa também perde produtividade)      ~2h30 (30 min reais)
+ correção de algo pego na revisão              ~3h30 (+1h)
+ escrever e rodar testes, garantir build verde ~4h (se der tudo certo)
+ margem para imprevistos aleatórios
  (~1h de imprevisto a cada 5 tarefas de 4h)     5h
+ pausas humanas (café, banheiro, lanche)        6h
```

Uma tarefa que "em teoria" leva 2 horas pode realisticamente demorar 6 horas sem que nada de excepcionalmente ruim aconteça — isso é comum, não exceção.

### O problema dos Story Points e a equivalência oculta a horas

Muitas empresas evitam estimar em horas e usam **story points** em escala Fibonacci (1, 2, 3, 5, 8, 13, 21…) — pontos altos demais (ex.: 21) indicam que a tarefa deveria ser quebrada em tarefas menores. Story points, em tese, não representam tempo — representam quantos pontos cabem numa sprint de duas semanas. Se uma sprint de duas semanas (80h de trabalho, considerando 40h/semana) comporta 80 pontos, existe uma **equivalência implícita não declarada de 1 ponto = 1 hora**, mesmo que "pontos não sejam para valer horas".

Na prática, é bem possível que duas tarefas de 1 ponto cada consumam um dia inteiro inteiro (idas e vindas de revisão, bikeshedding, tempo de build, tempo de teste) — ou seja, 2 pontos (que "equivaleriam" a 2 horas pela conta implícita) tomam um dia inteiro. Ninguém costuma admitir essa discrepância abertamente porque contraria a lógica declarada do sistema de pontos.

## Como Corrigir Cada Fator

- **Viés humano** → mensurar o erro das estimativas passadas. O viés tende a ser consistente (subestimar de forma recorrente), então medir esse erro permite ajustar estimativas futuras.
- **Requisitos incompletos/ambíguos e incerteza tecnológica** → reduzir a incerteza *antes* de estimar (ver Parte 2).
- **Pressão organizacional** → é, em essência, um problema de empresa mal ajustada / adultos não agindo como adultos — fora do escopo de uma técnica individual de estimativa.

### O problema de medir (ou não medir) a estimativa

Se uma equipe promete entregar 40 story points toda semana e entrega consistentemente 30, a estimativa é **precisa** (consistente) mas **mal calibrada** — na prática ela consegue prever com precisão que vai entregar 10 pontos a menos do que promete. A correção óbvia (prometer 30 da próxima vez) só é possível se a empresa **medir** se as estimativas passadas bateram com a realidade. A maioria das empresas não faz essa mensuração — o que anula o propósito de estimar.

## Parte 2 — Como Estimar Algo Que Nunca Foi Feito

### O cenário hipotético

Um banco de dados com 1 milhão de clientes; a feature pedida é gerar PDFs baseados nos dados de cada cliente. Como estimar isso?

**Pergunta 1:** É possível estimar algo que a gente nunca fez, sem saber como vai ser feito? Resposta: não, é impossível.

**Pergunta 2:** É possível dar um prazo para algo que é virtualmente impossível de ser feito (porque ainda não se sabe se é possível)? Também não.

Para que a estimativa tenha qualquer grau de precisão, é preciso primeiro ter confiança de que (1) sabemos o que vamos fazer, (2) sabemos que o que pretendemos fazer é possível, e (3) sabemos que a estimativa não vai ser perfeita — o objetivo é reduzir o erro, não eliminá-lo.

### Range é aceitável, "meio ano de erro" não é

Estimar "vai demorar entre um mês e um ano" não tem valor algum. Uma estimativa com range de aproximadamente ±33% (ex.: 1 mês e meio de média, podendo ser 1 mês na melhor hipótese ou 2 meses na pior) já é considerada uma estimativa bem precisa — e a maioria das empresas estima pior do que essa margem.

### Passo 1 — Reduzir incerteza / testar presunções

Partes do sistema que já se sabe como fazer (ex.: um endpoint, um lugar para armazenar o PDF gerado) não geram incerteza relevante — já foram feitas antes. O trabalho de redução de incerteza deve focar nas partes desconhecidas. No exemplo do PDF, as presunções a testar seriam algo como:

- Temos acesso a esses dados? O backend aguenta gerar esses PDFs na escala de 1 milhão de clientes? Se não aguentar, quanto custaria (tempo e dinheiro) redimensionar o backend?
- Existe uma maneira realista de gerar esse PDF especificamente? Qual lib, qual função, de qual biblioteca?

Testar essas presunções pode revelar dois mundos radicalmente diferentes: ou a lib padrão da linguagem já resolve exatamente o problema (questão de um dia), ou nunca ninguém gerou um PDF daquele jeito específico em lugar nenhum, e seria preciso construir um gerador do zero (questão de meses). Sem testar a presunção, não há como saber em qual desses dois mundos o time está — e a estimativa não tem nenhum valor real.

Nem toda presunção precisa ser validada construindo o artefato real: às vezes basta ler relatos de quem já resolveu um problema parecido — isso não dá certeza absoluta, mas pode dar algo como 95% de confiança de que a abordagem é viável.

**Tarefas concretas de redução de incerteza no exemplo do PDF:**
- Proof of concept de utilização dos dados (o banco de dados aguenta a carga, ou está subdimensionado?)
- Proof of concept de geração do PDF em si (a lib escolhida resolve realmente o que é preciso?)

### Passo 2 — Desenho do sistema

Só depois de reduzida a incerteza (A, B e C confirmados como possíveis) faz sentido desenhar o sistema. Features simples não precisam disso; features complexas se beneficiam de um desenho — pode ser em qualquer ferramenta (Excalidraw, papel, Figma) ou até um documento em texto. No exemplo: endpoint recebe o pedido → gera evento numa fila → worker consome o evento, pega os dados, gera o PDF, sobe o PDF no S3, envia e-mail via SES ao cliente → cliente baixa o PDF. Cada uma dessas partes, isoladamente, já é um problema resolvido/conhecido pela equipe.

### Passo 3 — Quebrar em tarefas e estimar

Só a partir daqui, com o sistema desenhado e a incerteza reduzida, a estimativa começa a fazer sentido. A estimativa total é o agregado das estimativas individuais de cada tarefa quebrada do desenho. Boas práticas para reduzir o erro nessa quebra:

- **Tarefas pequenas e bem definidas** — melhoram a precisão e dão mais visibilidade do que vai acontecer.
- **Participação da equipe (especialmente quem tem a expertise específica)** — quanto mais pessoas envolvidas, maior a chance de alguém já ter enfrentado um obstáculo específico de alguma das tarefas antes. Quem vai efetivamente executar uma tarefa deveria participar da estimativa dela.
- **Priorizar o menos conhecido primeiro** — nas etapas de redução de incerteza, não dá para testar tudo; vale mais testar antes as partes mais desconhecidas / com maior chance de dar errado. Isso pode poupar trabalho (o time desiste da tarefa) ou ajustar a estimativa cedo, antes de comprometer um prazo.

### Estimativas não são cravadas em pedra — refinamento contínuo

A estimativa precisa ser iterativa, ajustada conforme mais informação é obtida durante a execução — não fixada no momento inicial. No time do autor, há uma revisão semanal rápida (não consome muito tempo) das estimativas feitas, comparando com a informação obtida até o momento: mantém se ainda fizer sentido, ajusta se não fizer. Em sistemas complexos, as tarefas normalmente não chegam refinadas no detalhe mínimo desde o início — a execução de algumas tarefas esclarece o funcionamento do sistema, o que permite refinar (e reestimar) as tarefas seguintes numa nova iteração.

### Range, de novo

Uma estimativa de "um mês" isolada não comunica nada. O formato recomendado é um range com uma média e margem — por exemplo, "1 a 2 meses, média de 1 mês e meio, ±meio mês". O range:
1. Dá uma margem de segurança.
2. Impede que a área comercial venda algo que não vai estar pronto no prazo mínimo.
3. Ajuda a empresa a se planejar para a parte maior do range, não para o cenário mais otimista.

### Mensurar é o passo mais importante

Uma empresa que dá valor a estimativas precisa **medir** o quanto as estimativas estão erradas, e em que direção:
- Se o erro é **consistentemente para baixo** (estimativas menores que a realidade) → a empresa precisa aprender a estimar para cima.
- Se o erro é **consistentemente para cima** (estimativas maiores que a realidade) → precisa estimar para baixo.
- Se o erro é **disperso** (às vezes muito para baixo, às vezes muito para cima, sem padrão) → o problema não é calibração de viés, é falta de clareza antes de bater o martelo na estimativa — reduzir a variabilidade exige mais redução de incerteza, não um ajuste de fator fixo.

## Fechamento

Se vale a pena fazer estimativas em software não é uma pergunta respondida definitivamente no vídeo — mas algum grau de estimativa provavelmente vale a pena, não necessariamente no menor nível de detalhe possível. O fato é que estimativas continuam sendo feitas na indústria; a proposta é ao menos fazê-las bem.
