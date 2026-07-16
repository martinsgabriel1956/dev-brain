# Custo Real da IA: Tokens, Produtividade e Demissões

> Transcrição de episódio do CDF Café discutindo se a promessa de que a IA generativa tornaria o desenvolvimento de software mais barato é realmente verdadeira, ou se produtividade e redução de custo são coisas diferentes que não caminham juntas.

---

## A promessa e a ilusão

Todo mundo comprou a mesma ideia: a de que a inteligência artificial vai tornar o desenvolvimento de software muito mais barato. Mas então por que as empresas estão gastando milhões com IA? E por que uma consultoria como a Gartner diz que, em pouco tempo, algumas empresas vão gastar mais com tokens do que com o salário médio de um desenvolvedor?

Talvez exista aí uma grande ilusão: a IA realmente aumenta a produtividade, mas a relação entre produtividade e redução de custos não é tão direta assim. A discussão vai muito além de devs, prompts, agentes e código — ela envolve dinheiro, poder e quem realmente está lucrando nessa história.

## A promessa não é falsa, mas o modelo de cobrança pesa

Segundo a pesquisa salarial de 2026 do canal, 98% (ou um pouco mais) dos devs brasileiros já dizem usar IA no dia a dia de trabalho. Isso ajuda mesmo, e ajuda as equipes a entregarem mais com menos esforço — a promessa de produtividade não é falsa.

O que não está se confirmando é a ideia de que, com o avanço dos modelos, a IA ficaria mais barata. Pelo contrário: o modelo de cobrança por token tem trazido contas cada vez maiores. Um exemplo citado foi o do presidente do Uber, que declarou que o gasto com IA já está ficando difícil de justificar — a empresa estourou em abril todo o orçamento que tinha reservado para inteligência artificial, aparentemente por não ter colocado limite no consumo de tokens (estratégia conhecida como **token maxing**, que já está ficando para trás).

Talvez seja aqui que mora a primeira ilusão da IA: produtividade e redução de custo não são necessariamente a mesma coisa — às vezes nem caminham juntas.

## Paralelo com outras revoluções da computação

Para entender esse fenômeno, vale comparar com outras revoluções da computação:

- **Nuvem**: muitas empresas economizaram comprando menos servidores, mas passaram a ter uma conta mensal enorme com serviços de nuvem.
- **Microsserviços**: facilitam escalar aplicações, mas aumentam bastante a complexidade operacional.
- **Contêineres**: simplificam o deploy, mas criaram novos desafios de observabilidade, segurança, orquestração e infraestrutura.

Toda evolução da engenharia resolve alguns problemas e cria outros — não haveria motivo para a IA ser diferente. Em poucos anos de IA em produção, já é possível ver esses problemas emergindo: alucinações, débito técnico, segurança e, claro, custo.

## A previsão da Gartner

A Gartner prevê que os custos de codificação com IA vão superar o salário médio de um desenvolvedor até **2028**. Isso explica por que já existem tantas iniciativas tentando trocar o paradigma de LLM, buscando os mesmos resultados por outro caminho — porque, do jeito que está, escalar IA tende a aumentar o custo continuamente.

Um analista da Gartner resumiu assim:

> "As organizações estão se movendo rapidamente da experimentação para implantação em escala de agentes de codificação de IA, mas muitos estão subestimando o impacto financeiro do aumento do consumo de tokens."

Isso não é surpresa para quem já paga por planos de Claude Code ou Codex e percebeu como o GitHub Copilot mudou o próprio sistema de cobrança: os modelos e os tokens que bastavam antes muitas vezes não são mais suficientes para obter o mesmo resultado, porque todo mundo busca resultados melhores.

Essas empresas de IA estão operando alavancadas — buscando lucro, mas ainda precisando derrubar custos, senão a operação fica inviável. Há quem já cogite que, se continuar operando do jeito que opera, a própria OpenAI pode não existir mais daqui a alguns anos.

O mesmo analista da Gartner ainda apontou que a disciplina de tokens não vai surgir por escolha do desenvolvedor, pois desenvolvedores tendem a otimizar velocidade e conveniência em vez de eficiência de custo. Ou seja: se a empresa não está medindo o custo, não vai ser o desenvolvedor que vai medir.

## Rodar modelos on-premise não resolve (ainda)

Muitas empresas e desenvolvedores estão investindo em rodar modelos localmente (on-premise) — comprando GPUs e computadores próprios. O problema é que, com tanto investimento em infraestrutura de IA para data centers, o custo de memória e GPUs está caríssimo, o que torna essa alternativa também cara. Isso provavelmente vai durar muitos anos, porque as empresas alavancadas estão praticamente suprindo o mercado inteiro de hardware.

A maioria das organizações ainda não tem maturidade nem estrutura para medir efetivamente custo versus impacto no negócio. Existem pesquisas sugerindo que as empresas não estão vendo, na ponta, toda a produtividade prometida — de novo, o caso do Uber: a sensação de produtividade existe, mas não necessariamente é possível justificá-la no papel. Algumas empresas conseguem provar o ganho, outras não, e ainda não existe uma forma padronizada de medir isso — o que abre espaço para dúvidas sobre se está sendo gerado valor real ou apenas uma dependência maior (tema já tratado em outro vídeo do canal sobre dívida cognitiva).

A Gartner reforça: sem visibilidade clara do uso de tokens em tarefas de desenvolvimento, as organizações arriscam estouros de orçamento e perdem a capacidade de rastrear resultados de custo versus valor.

## De capital humano para capital computacional

Conclusão possível: o custo da indústria de software era capital humano; agora, uma parte crescente desse custo está migrando para capital computacional. Isso conecta com um comentário do Satya Nadella, da Microsoft, sobre o que ele chamou de **"capital de tokens"** — um paralelo com o capital humano que gera conhecimento, mas agora com o capital de tokens cumprindo papel semelhante.

## Demissões: IA como bode expiatório?

Ligado a esse assunto está a redução de times. Casos como o da Ford (que teria voltado a contratar centenas de engenheiros após demitir) e o de Mark Zuckerberg mostram um padrão: o CEO da Meta admitiu que a tecnologia de agentes de IA não está progredindo como ele esperava — mesmo citando o Cloud Code como referência. A meta esperava colher frutos mais rápido com a implantação de agentes e viu que isso não aconteceu, o que fez o ajuste de funcionários parecer antecipado demais.

Zuckerberg reconheceu que a Meta cometeu erros na reestruturação de equipes por IA (o caso do assistente de recuperação de senha no Instagram que "recitava" senhas de usuários foi citado como exemplo). Em memorando interno, ele escreveu algo como:

> "Dada a complexidade dessas mudanças, cometemos erros e quase certamente cometeremos mais", reforçando o foco em dar "o máximo de estabilidade possível" nas mudanças organizacionais daqui para frente, e completando: "não quero prometer demais, porque o mundo está mudando de maneiras que estão fora do nosso controle."

Ele reitera que a Meta não espera mais demissões em massa em toda a empresa neste ano — diferente da Microsoft, que fez sua primeira grande onda de demissões há poucos dias.

### A pesquisa da Resume Templates

Um levantamento da Resume Templates com mais de 1.000 gestores de contratação mostrou números reveladores:

- **59%** das empresas admitem destacar a inteligência artificial ao justificar demissões ou congelamento de vagas — porque essa explicação é melhor recebida do que admitir dificuldades financeiras.
- **9%** dos gestores afirmam que determinadas funções foram completamente substituídas por IA.
- **45%** relatam que a IA reduziu parcialmente a necessidade de novas contratações.
- **45%** dizem que a IA teve pouco ou nenhum efeito sobre o tamanho das equipes.
- **17%** afirmam que suas empresas usam diretamente a IA como justificativa para congelar vagas ou promover demissões; outros **42%** dizem fazer isso parcialmente.

Ou seja: boa parte das empresas está usando a IA como bode expiatório — fica mais bonito dizer que se está trazendo inovação do que admitir dificuldade financeira ou reestruturação. Não dá para atribuir tudo à IA, mas também não dá para descartar o efeito real da automação, especialmente em grandes empresas com milhões de processos. Ao mesmo tempo, há um terceiro motivo possível: usar a IA como justificativa para baratear a folha de pagamento (recursos humanos costumam ser o maior custo dessas empresas).

## Palantir: quem controla essa nova economia de IA?

Uma entrevista do CEO da Palantir Technologies (empresa com contratos de longa data com o governo dos EUA, fornecendo softwares de análise de dados para agências de defesa, inteligência e segurança pública) levantou duras críticas ao modelo de cobrança por tokens:

> "À medida que os custos aumentam e novos modelos se mostram mais caros que interações anteriores, as empresas estão mudando de uma mentalidade de token maxing em prol de retorno sobre investimento."

O ponto central: o problema agora é o *timing* — quanto tempo as empresas vão continuar investindo do jeito que estão investindo, e quanto tempo vai levar para os hyperscalers reduzirem os custos. Se esse timing não bater, as empresas vão começar a abandonar os investimentos maciços em IA.

O CEO também enfatizou, com bastante ênfase na entrevista, o risco de as empresas passarem seus dados para esses modelos de IA — já que os dados são o ativo mais valioso de uma empresa, o "ouro" que sustenta seus produtos e serviços.

## Contratação de juniors: sinal contraditório

Algumas semanas atrás, veio a notícia de que o CEO da AWS estaria contratando 11 mil estagiários e funcionários juniores, muitos na área de desenvolvimento. Isso pode ser demanda reprimida, resultado de demissões anteriores, ou o reconhecimento de que, sem juniors trabalhando hoje, faltarão profissionais seniores capazes de resolver problemas no futuro. O mercado, nesse momento, parece meio distópico e nebuloso — mas também cheio de oportunidades que só vão ficar claras com o tempo.

---

## Resumo dos números citados

| Métrica | Valor |
|---|---|
| Devs brasileiros que usam IA no dia a dia (pesquisa salarial 2026) | 98%+ |
| Profissionais em modelo PJ (pesquisa salarial 2026) | 27% |
| Previsão Gartner: custo de codificação com IA supera salário médio de dev | até 2028 |
| Empresas que admitem usar IA como justificativa para demissões/congelamento (parcial ou total) | 59% |
| Funções completamente substituídas por IA (segundo gestores) | 9% |
| Empresas onde IA reduziu parcialmente novas contratações | 45% |
| Empresas onde IA teve pouco/nenhum efeito no tamanho das equipes | 45% |
| Empresas que usam IA diretamente como justificativa para congelar vagas/demitir | 17% |
| Empresas que usam isso parcialmente como justificativa | 42% |
| Estagiários/juniores contratados pela AWS (notícia citada) | 11.000 |
