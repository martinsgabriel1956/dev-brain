# Harness Engineering — Dicionário do Programador

> Transcrição de vídeo (série "Dicionário do Programador", canal não identificado na transcrição), colada pelo usuário e limpa. Já estava em português; sem tradução.
> Correções de ASR: "Harners/Har" → *harness*; "Michael Hashimoto" → **Mitchell Hashimoto** (criador do Terraform); "Birgita Bockler" → **Birgitta Böckeler** (Thoughtworks); "Vivec Trivedy da Langcha" → **Vivek Trivedy** (LangChain); "agents.m"/"agents MD" → `AGENTS.md`; "cloud MD"/"Cloud Code" → `CLAUDE.md`/Claude Code; "readmeli" → README; "BESH" → Bash; "NCPs" → MCPs; "Codex curso RLIT" → Codex, Cursor, Replit; "Deepsic" → DeepSeek; "half loops" → provavelmente *Ralph loops* (incerto).
> Omitidos: publicidade de conta internacional (Higlobe) e encerramento com pedido de comentários e indicação do vídeo sobre MCP.

## Definição

**Harness engineering** é tudo que compõe um agente de IA, exceto o modelo de linguagem. O LLM fornece a capacidade de raciocínio e geração de texto; o harness fornece o **ambiente, as ferramentas, os limites, o contexto e os mecanismos de execução**. O modelo contém a inteligência; o harness a torna útil.

Um modelo puro e bruto não é um agente. Ele se torna um quando o harness fornece **controle, injeção de contexto, consistência, ação, observação e verificação**.

## Origem do termo

O termo ganhou força depois que **Mitchell Hashimoto** (criador do Terraform), **Birgitta Böckeler** (Thoughtworks) e **Vivek Trivedy** (LangChain) sintetizaram e formalizaram a prática.

**Princípio de Hashimoto:** toda vez que um agente de IA comete um erro no seu projeto, não corrija apenas o prompt "no braço". Gaste tempo planejando uma **trava determinística** no harness para que o agente seja incapaz de cometer aquele erro novamente.

## Dois propósitos do harness

1. Aumentar a probabilidade de o agente **acertar na primeira tentativa**.
2. Fornecer um **ciclo de feedback** que corrige o maior número possível de problemas.

## Guias e sensores (Böckeler)

Böckeler dividiu os controles do harness em duas categorias funcionais:

- **Guias (feed-forward):** atuam no modelo *antes* de qualquer ação, injetando instruções e regras arquiteturais no prompt do sistema.
- **Sensores (feedback):** entram em ação *depois* que o agente gera código ou altera o ambiente; observam o resultado, executam validações técnicas e acionam hooks de correção quando encontram um problema.

### Exemplos de guias

- **`AGENTS.md`**: guia de navegação e instruções para agentes de IA — uma espécie de "README para agentes". Traz orientações diretas sobre arquitetura do sistema, convenções de código, comandos de build e teste e regras invioláveis do repositório. É comum ter um `AGENTS.md` principal na raiz com as regras globais e, como boa prática, `AGENTS.md` adicionais em subpastas ou módulos específicos, com contexto relevante àquela parte da aplicação.
- **`CLAUDE.md`**: específico do Claude Code; muitas vezes importa o `AGENTS.md` e só acrescenta o que é específico da ferramenta.
- **Skills**: instruções especializadas que o agente carrega quando precisa de determinado tipo de tarefa. Em vez de colocar todas as instruções no contexto desde o início, o agente tem uma "biblioteca de habilidades". Exemplo: uma skill que valida segurança, performance e padrões de arquitetura de **migrações de banco de dados** antes de executá-las — identifica automaticamente alterações destrutivas ou que travem tabelas (locks, exclusão de colunas), executa um script de validação de sintaxe e gera um relatório aprovando ou bloqueando a alteração.

### Exemplos de sensores

- Testes automatizados.
- Linters.
- Type checkers (inconsistências de tipos).
- Testes de integração (a aplicação funciona como esperado?).
- Logs, incluindo análise dos erros produzidos.
- Métricas e observabilidade (comportamento, performance ou falha da aplicação).

## De-para de Trivedy (LangChain): o que o harness adiciona ao modelo

| Comportamento desejado | O que o harness adiciona |
|---|---|
| Trabalhar com dados reais de forma persistente | File system + Git |
| Escrever e executar código | Bash + ambiente de execução de código |
| Execução segura e ferramentas padrão | Ambiente em sandbox + tooling |
| Lembrar e acessar novos conhecimentos | Arquivos de memória + pesquisa na web + MCPs |
| Manter desempenho em contextos longos | Compactação + tool-offloading + skills |
| Concluir trabalhos de longo prazo | (Ralph?) loops + planejamento + verificação |

O autor ressalva que a lista não se limita a isso.

## Três camadas de um agente de código

1. **Núcleo:** o modelo de linguagem.
2. **Harness da ferramenta:** infraestrutura base do agente — system prompt, execução de comandos de terminal, orquestração, gerenciamento de contexto. Vem embutido no produto; o desenvolvedor tem pouco controle.
3. **User harness:** o conjunto de feed-forward e feedback configurado pelos desenvolvedores para o seu sistema específico.

Qualquer ferramenta de codificação com IA (Claude Code, Codex, Cursor, Replit, Lovable) já tem o seu próprio harness.

### DeepSeek Harness

Segundo o autor, a DeepSeek lançou recentemente o **DeepSeek Harness**, ferramenta **open source** voltada ao agent harness. Diferencial: arquitetura **"Everything is a plugin"** — modelos, ferramentas, skills, sessões, sandbox, armazenamento e até a interface podem ser trocados ou combinados; conceito mais flexível que Claude Code ou Codex. Na gravação, o projeto ainda estava em *developer preview*.

## Por que importa

A diferença na resposta de um LLM está **mais ligada ao harness do que ao modelo em si**: dependendo do que se usa junto com o modelo, o agente será mais assertivo e útil.

## Exemplo fora de software: crédito financeiro

Agentes autônomos analisam extratos, histórico de consumo e scores para aprovar financiamento e limite de crédito. O harness impõe **limites rígidos de risco**: travar aprovações automáticas acima de determinado valor, exigir **explicação auditável** para cada recusa e validar a conformidade do algoritmo com as regras do Banco Central.

## Fechamento

Antes conversávamos com o modelo só por prompt; para desenvolvimento de software isso já não faz sentido. Por isso surgiram termos como harness engineering — e já se explora **meta harness, loop engineering, graph engineering** etc. Muitas vezes o dev já usa essas práticas no dia a dia; só estão nomeando. O desenvolvimento com IA evolui em ritmo frenético e muitas técnicas vão surgir e morrer nos próximos meses e anos.
