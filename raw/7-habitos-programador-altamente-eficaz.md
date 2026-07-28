# 7 Hábitos de um Programador Altamente Eficaz

> Transcrição de vídeo (PT-BR), reestruturada em markdown a partir de transcrição bruta sem pontuação/seções. Fonte e autor não identificados no material bruto — o autor referencia dois vídeos próprios ao final ("4 hábitos que tornam você um programador ineficiente" e um "checklist do programador... dez itens"), sugerindo o mesmo canal já ingerido em [[wiki/sources/4-habitos-programador-ineficiente]] / [[wiki/sources/habitos-ruins-de-programador]] e [[wiki/sources/desenvolvedor-acima-da-media-10-itens]].

## Introdução

Pelo menos um desses sete hábitos deve gerar um momento "eureka" que muda a forma como você evolui como programador — isso aconteceu com o próprio autor em alguns pontos ao estudar e escrever sobre o assunto.

## 1. Gostar de caçar informação do jeito certo

Diferença observada entre pessoas "ótimas" e pessoas medianas no mercado: diante de uma dúvida ou bloqueio, a pessoa ótima busca a solução por conta própria antes de perguntar para qualquer um. A pessoa mediana, tomada pela ansiedade, "desliga o cérebro" sem perceber e a única alternativa que sobra é pedir a resposta pronta para quem está do lado.

Perguntar para um amigo é de fato mais rápido do que pesquisar sozinho — mas é um trade-off, a natureza não dá nada de graça: você ganha velocidade e perde o processo de raciocínio. Nenhuma ideia nova passou pela sua cabeça; você virou apenas um "proxy super conectado".

Analogia da lâmpada: dentro dela existe um filamento (resistência) que, ao resistir à corrente elétrica, emite luz e calor. Para crescer de verdade nessa área — bom emprego, bom salário — o cérebro precisa funcionar como uma lâmpada: em vez de corrente elétrica, é *informação* passando pela resistência do cérebro, até o ponto de gerar luz — os momentos de eureka.

## 2. Não morrer da paralisia do planejamento

Três estágios (categorização didática, não uma verdade absoluta):

- **Júnior**: não planeja nada — ataca o problema diretamente já pensando em quais funções/código conhece para produzir uma solução.
- **Pleno**: planeja demais. Numa altura de abstração maior, a pessoa enxerga mais coisas e tenta também dominar e controlar tudo isso. É nessa fase que surge a **analysis paralysis** (paralisia por excesso de análise/planejamento). Quem escapa dela cai facilmente na margem do **over-engineering** — a maioria do que essa pessoa constrói acaba desnecessariamente complexo ou ineficiente.
- **Sênior**: cria um plano técnico *suficiente* para resolver o problema de hoje, considerando também o suficiente para a evolução do projeto ao longo do tempo.

Pergunta-chave que um programador altamente eficaz sempre faz diante de um projeto ou problema: **isso [do jeito que está sendo pedido] precisa mesmo ser resolvido assim?** Essa pergunta economiza muito tempo e retrabalho, especialmente quando surge uma demanda urgente do nada. Não é feita por preguiça ou birra com o gestor — o objetivo é afastar a análise dos interesses pessoais de programador e gestor, para enxergar o legado tecnológico e o interesse real por trás do pedido, e então enxergar **alternativas**.

Um gestor mais próximo do cliente às vezes chega com a solução já pronta junto da demanda urgente — mas nem sempre sabe explorar a alavancagem da tecnologia. Júnior tende a ficar acuado e aceitar; pleno/sênior deveriam empurrar de volta uma ideia melhor.

**Caso pessoal do autor:** situação complexa com clientes, fluxo proposto pelo autor era linear e simples (início → sucesso → fim). O chefe insistia em um fluxo alternativo, muito mais complexo, cheio de exceções para cobrir todos os casos possíveis. O autor não conseguiu fazer o chefe visualizar a simplicidade do fluxo original — foi implementado o fluxo complexo do chefe. Ambas as abordagens resolviam o mesmo problema, mas a "inflamação técnica" (dívida técnica) causada pelo fluxo complexo no sistema foi deprimente.

## 3. Saber ler e entender código de outras pessoas

Ler código alheio costuma provocar a reação "que diabos é isso, para onde essa ponte leva, arquivo mal projetado, ineficiente" — mas é uma habilidade importante: ela ensina quais coisas dificultam a leitura de um código, para que você mesmo escreva código mais rápido de se ler. Além disso, ler código bom é fonte de aprendizado direto.

**Exemplo pessoal:** o autor se inspirou na biblioteca `clipboard.js` para construir a primeira versão de uma extensão para Chrome.

> "Um projeto funcionando é muitas vezes melhor do que qualquer documentação."

## 4. Saber documentar de forma inteligente

O autor já documentou, no passado, todas as linhas de um projeto — análise linha a linha do que o código de baixo fazia. Foi ótimo para o próprio aprendizado, porque só se consegue explicar algo (mesmo que para si mesmo, via comentário) quando de fato se entendeu o assunto.

Exercício mais avançado: escrever código já legível por si só, documentando apenas o **porquê** de uma decisão, qual regra de negócio precisa ser atendida, ou qual caso exige atenção além do normal.

Onde documentar isso de forma "extremamente inteligente": em **testes automatizados**. Escrever testes pode ser chato, mas encará-los como documentação viva do comportamento esperado do código — com a garantia extra de não haver regressão — é valioso. Para quem está aprendendo um sistema novo, os testes automatizados costumam ser a documentação mais correta disponível; o autor relata ter aprendido o comportamento de funções dentro de sistemas complexos só observando o que os testes cobriam e como.

## 5. Conseguir desacoplar e abstrair com maestria

Um programador altamente eficiente não pensa mais só em código — pensa primeiro nas abstrações, no limite de cada abstração, e na interface que cada uma vai expor. Os detalhes de implementação viram preocupação para depois, "detalhe de interior".

No início da carreira isso é muito difícil; com o tempo, certos padrões e limites começam a aparecer — principalmente quando um componente fere o limite do outro.

**Analogia médica:** um cardiologista entende a fundo os limites do coração, um dentista os limites do dente, porque o corpo humano não é uma "ameba" — é separado em órgãos, cada um com seu limite e responsabilidade. Da mesma forma que problemas graves surgem quando o limite de um órgão começa a furar o limite de outro, um software sofre os mesmos sintomas quando abstrações e responsabilidades são mal feitas e tudo fica acoplado e misturado.

## 6. Gostar de futucar código (sem medo)

A maioria das pessoas tem medo de código — parece que ele está "julgando" a cada tecla pressionada, como se fosse um ser vivo observando. Essa sensação, segundo o autor, está inteiramente na cabeça de quem programa.

Reformulação proposta: é o código quem precisa de você, não o contrário. O código está ali, "machucado, quebrado, triste", e você é o especialista capaz de salvá-lo (pelo menos do ponto de vista dele). Em vez de ter medo do código, é o código quem deveria agradecer pela sua existência.

Esse hábito se conecta com escrever código de propósito, "na moral" — a forma mais rápida de fazer dúvidas e lacunas de conhecimento se manifestarem.

## 7. Conseguir "entortar" o tempo

**Caso pessoal do autor:** período difícil liderando um setor com mais de 100 pessoas, com controle total perdido sobre a própria agenda. Reuniões passaram a invadir até o horário de almoço — qualquer espaço vago na agenda era ocupado por outra pessoa. O autor percebeu que estava 100% reativo a tudo que acontecia na empresa.

**Estratégia que funcionou:** importar de volta o próprio tempo, começando por **reservar a própria agenda** — mesmo que pareça "ridículo" bloquear os próprios horários. Funcionou bem o suficiente para inverter a lógica e passar a bloquear tempo para o que mais importava, principalmente saúde (academia) e estudo (aulas de inglês).

Alerta geral: independente da ferramenta usada, nunca acreditar que você já está no máximo de aproveitamento do seu tempo, principalmente se não há nenhuma ação consciente a respeito. Sem essa ação, a única coisa que resta é reagir às urgências do próprio contexto. Quem estiver infeliz com a rotina deveria aprender a importar o tempo na medida do possível, reservando horas para estudo, saúde, ou o que ajudar a sair de um ciclo vicioso.

## Referências a outros vídeos do canal (fechamento)

- "4 hábitos que tornam você um programador ineficiente" — cf. [[wiki/sources/4-habitos-programador-ineficiente]] / [[wiki/sources/habitos-ruins-de-programador]].
- "Checklist do programador... dez itens para ser um programador muito acima da média" — cf. [[wiki/sources/desenvolvedor-acima-da-media-10-itens]].
