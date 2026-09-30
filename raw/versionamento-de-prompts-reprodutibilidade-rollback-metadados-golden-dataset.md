# Versionamento de prompts: reprodutibilidade, metadados, versionamento semântico e rollback instantâneo

> **Origem:** transcrição de vídeo em português (brasileiro), colada pelo usuário em 2026-09-30. Autor não identificado; o falante conta que estuda e constrói agentes de IA há cerca de dois meses e mantém um projeto de assistente financeiro (repositório chamado "prompt manager", link prometido na descrição do vídeo, não incluído na transcrição). Canal e data de publicação desconhecidos.
>
> **Tratamento:** o texto original é uma transcrição automática corrida, sem pontuação. Aqui foi limpo e dividido em seções, sem alterar o conteúdo. Já estava em português; não houve tradução.
>
> **Termos corrompidos pela transcrição, corrigidos por contexto:**
> - "a gente" (no sentido de "construir um agente") → agente; "os agentes" idem
> - "prompt"/"promete"/"promptos"/"pronts" → prompt(s)
> - "suit de testes" → suíte de testes
> - "Tropic" → Anthropic; "Open Ai"/"Open Ei" → OpenAI; "Open Houter" → OpenRouter (o autor diz que usa o ID do modelo do OpenRouter)
> - "KitHub"/"gitub" → GitHub
> - "LLN" → LLM
> - "Jason" → JSON; "metadata.jonjason do Jason" → `metadata.json`
> - "personamento" (no fecho do vídeo) → provavelmente "versionamento"
> - "add expensive add expenses" → provavelmente `add_expense` / "adicionar despesa" (nome de um dos três prompts do projeto financeiro); **inferência**
> - "financial agent agent prompts" → caminho de diretório do projeto (provavelmente algo como `financial_agent/agent/prompts`); **incerto**
> - "quem desenvolveu prompt também é uma variável" → "quem desenvolveu o prompt também é uma variável"
> - "Felipe" (no meio da explicação de reprodutibilidade) → vocativo dirigido a um espectador, não conteúdo
> - "workflow que eu apresentei há pouco tempo" → referência a outro vídeo do autor, não identificado
> - "Golden Test" e "golden dataset" são usados quase como sinônimos pelo autor; ver seção de testes

---

## Abertura: o erro que motivou o vídeo

Nos últimos dois meses o autor estudou e construiu bastante com inteligência artificial e se deparou com um erro recorrente, sobre o qual quer saber se os espectadores também passam. O erro: ao construir um agente, ele pegava o prompt, testava, e quando via algum problema colava o prompt num **bloco de notas**, pedia para melhorá-lo, colava a nova versão no agente e rodava de novo. O resultado é que o prompt copiado para o bloco de notas ficava esquecido. Se algum dia ele voltava a olhar, a versão em geral "já não tinha importância" e era descartada, ou melhor, ele **achava** que não tinha importância **porque não lembrava mais por que aquela mudança foi necessária**.

A solução que adotou: **versionar prompts**. Com isso ganhou "controle absurdo" do que fez, do porquê fez e com quais outras variáveis o prompt funciona, e uma "rastreabilidade gigantesca" de todas as modificações do agente.

## Tratar prompt com o mesmo respeito que o código

O título do vídeo pede para tratar os prompts **com o mesmo respeito e cuidado que se tratam os códigos**, porque o prompt é "o coração central de toda a arquitetura e estrutura do agente". Exemplo do autor: se rodamos uma suíte de testes com o prompt "Você é um assistente gentil", o resultado será de um jeito; se acrescentamos uma única palavra ("Você é um assistente **muito** gentil"), a resposta já será diferente. Se uma palavra altera a resposta, é preciso muito cuidado com o prompt. Foi esse o problema que levou o autor a buscar soluções.

## Objetivo: reprodutibilidade

O objetivo do versionamento é a **reprodutibilidade**: conseguir "voltar no tempo" e reproduzir exatamente o mesmo comportamento que o LLM teve. Exemplo:

- Existe a **versão inicial** do prompt, com suas instruções, a **temperatura** configurada e o **modelo** (ex.: OpenAI ou Anthropic). Quem desenvolveu o prompt também é uma variável.
- Ao longo do projeto, decide-se mudar para uma **versão 2.0**; as variáveis também mudam (outro modelo, outra temperatura etc.).
- Reprodutibilidade é ter a capacidade de **voltar exatamente à versão 1** e fazer o LLM cumprir aquela mesma execução. (O autor justifica: porque não estaremos monitorando, a cada momento, o que mudou.)

## Versionar prompt não é versionar string

A frase central: **versionar o prompt não significa versionar a string**. Não é só guardar o system prompt grande, cheio de instruções, guardrails, tom e formato de saída. É versionar **o ecossistema completo** do prompt: as variáveis e os **metadados**. Exemplos de metadados que o autor lista:

- quem fez o prompt (autor);
- a temperatura;
- o modelo e o provedor;
- a data de criação;
- o **porquê** da mudança, registrado a cada nova versão.

## Os pilares do versionamento

1. **Rastreamento de metadados**: o item acima; permite saber o que mudou, quando, por quem e por quê.
2. **Versionamento semântico**: controlar se a mudança é significativa. Uma alteração **major** modifica quase toda a estrutura do prompt; uma alteração **minor** é uma pequena alteração cujo comportamento do agente provavelmente continua o mesmo ("muda uma coisa ou outra"); há ainda a correção simples (na interface do autor, "major, minor ou apenas uma correção simples").
3. **Saber qual versão está ativa**: parece óbvio, mas é importante porque cada agente terá "não sei quantas" versões de prompt; é preciso que a versão ativa esteja sempre especificada.
4. **Rollback instantâneo**: com **um único clique** na interface gráfica (mostrada depois) é possível ativar uma versão ou marcá-la como depreciada. Exemplo do autor: a 2.0 está em produção e "não deu certo", mas a 1.2.1 funcionava, então volta-se a ela automaticamente. Casa com a reprodutibilidade.

## Versionar não melhora as respostas

Ressalva explícita do autor: **versionar não significa que as respostas vão melhorar.** O versionamento dá controle sobre o prompt e suas versões; a **qualidade** depende totalmente das instruções, da forma como são estruturadas e, também, das **tools**, entre outras coisas.

## Como testar se um prompt está bom

Formas de testar: **testes unitários**, **testes de integração** e **golden test**. O autor promete outro vídeo sobre **testes de regressão de prompt**: fazer o teste a partir de uma base de dados chamada **golden dataset**, que contém as **respostas esperadas** do LLM. Com ele é possível comparar, por exemplo, a **versão 1** de um prompt com a **versão 1.2** do mesmo prompt, usando as mesmas respostas esperadas, e ver se a mudança foi melhor ou pior para os dados do projeto.

## Demonstração prática: interface web

A aplicação roda localmente. A interface web tem, **à esquerda, a criação de novos prompts** e, **à direita, o gerenciamento**. A explicação usa o primeiro prompt do projeto (chamado, na transcrição, "add expense(s)", ver nota acima).

**Gerenciamento (lado direito):**

- mostra qual é a **versão ativa**;
- para ativar qualquer outra versão, agora obsoleta, basta apertar um botão;
- clicando em uma versão, aparecem as variáveis dela. No exemplo: uma versão usa o **modelo Gemini com temperatura zero**, foi criada em **21/08**; a **versão 2.0**, por exemplo, usava um modelo da OpenAI;
- há data, modelo, temperatura, o **system prompt** de cada versão e os **comentários** dizendo o que mudou. Como só o autor mexe no projeto, o nome dele aparece em todas as versões.

**Criação (lado esquerdo):**

- campo para o system prompt;
- escolha do **modelo**, com alguns **presets** já configurados (alterável no código); o autor usa o **OpenRouter**, então basta pegar o ID do modelo lá;
- nome de quem cria/altera o prompt;
- **temperatura**;
- escolha do tipo de versão semântica (**major, minor ou correção simples**);
- **esforço de raciocínio** (effort), "caso o modelo permita", pois nem todos os modelos têm essa possibilidade.

## Demonstração prática: código

- Um arquivo **`metadata.json`** é "o comandante": guarda **a versão ativa de cada prompt**. Os três prompts da interface aparecem ali, cada um com sua versão ativa.
- Na pasta de prompts há os três prompts; **cada versão é um arquivo JSON** com todas as informações (nome, versão, conteúdo, temperatura etc.). Exemplo citado: a versão 3.0.
- O projeto é um **assistente financeiro**; o repositório se chama **prompt manager** (o link seria colocado na descrição do vídeo, junto com um workflow apresentado antes). É o "prompt manager" que "comanda tudo".
- Uma **variável no `.env`** define o **diretório** onde os prompts são salvos (o autor definiu um caminho dentro do agente financeiro); o gerenciador entende o diretório e começa a salvar os prompts ali.
- Como camada opcional ("não é uma regra obrigatória, mas é muito interessante"), há um **prompt loader** e um **agent builder**. Ambos olham diretamente para o `metadata.json`, leem a **versão ativa** e carregam o prompt ativo naquele momento. Não importa se uma versão foi depreciada; o loader sempre consulta o metadata, "com um certo controle de tempo e atualização, para não ter o risco de pegar o dado desatualizado" (ou seja, algum tipo de cache/refresh com intervalo controlado).
- O loader carrega **não só o system prompt**, mas também **o modelo, a temperatura e tudo mais**, e com isso o **agente é criado**. Essa é a união entre criação do agente e controle do prompt.

## Fecho

O autor espera que os espectadores adotem esse método ou criem outro, pede dúvidas nos comentários, curtida e inscrição no canal.
