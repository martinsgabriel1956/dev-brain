# Secrets Vazadas no GitHub — Por Que Acontece e Os Limites da Busca (versão conceitual)

> Transcrição de vídeo em português (criador de conteúdo de segurança; canal e autor não identificados) sobre vazamento de secrets em repositórios do GitHub. Texto limpo, estruturado e **expurgado**: o vídeo original demonstra, na prática, acesso não autorizado a bancos de dados de terceiros e sobrescrita de credencial de admin em um sistema real — esses trechos foram **removidos deliberadamente** e não constam aqui. Mantido apenas o conteúdo conceitual (o que é uma secret, por que vaza, limites técnicos da busca do GitHub, categorias de ferramentas de scanning). Já estava em português — sem tradução.
>
> **Correções de transcrição aplicadas pelo contexto:** "debs" → devs; "ponto env" → `.env`; "Dantropic" → Anthropic; "a Kia" → `AKIA` (prefixo de access key da AWS); "SK Live" → `sk_live` (Stripe); "Truffle hog" → TruffleHog; "gatory"/"gatos de pagamento" → gateways de pagamento.
>
> **Trechos incertos:** a identificação do autor e do canal; números citados (quantidade de secrets encontradas) são afirmação do autor, não verificados, e **omitidos aqui** por estarem ligados à demonstração removida. O nome da ferramenta citada pelo autor como base do seu script também foi omitido, já que seu uso no vídeo é para varredura/exploração em massa sem autorização.

## O que é uma secret

Quando um sistema precisa mandar e-mail, cobrar Pix ou chamar uma IA, ele conversa com outro sistema e, para provar que é ele, usa uma chave — a secret. Não existe "login": **a secret é o próprio acesso**. Quando a secret é colocada no meio do código-fonte, qualquer pessoa com acesso ao código passa a ter acesso à secret. Por isso a prática comum é isolar as chaves num arquivo separado (`.env`) e configurar o projeto para ignorar esse arquivo ao subir para o controle de versão, de modo que ele fique só na máquina local.

## Por que o `.env` vaza mesmo assim

Muita gente esquece de configurar o `.gitignore` corretamente e acaba subindo o `.env` inteiro para um repositório público — ou, em outros casos, a secret é deixada *hardcoded* direto no código-fonte, sem nem passar por um `.env`. Um repositório público pode ter milhares de arquivos e milhões de linhas, o que tornaria inviável procurar uma chave "na mão" — daí o interesse (ofensivo e defensivo) em ferramentas automatizadas de busca.

## Formato reconhecível das chaves

Vários provedores geram chaves em formato específico e identificável por prefixo: Anthropic começa com `sk-`, AWS com `AKIA`, Stripe com `sk_live` (produção) ou `sk_test` (teste), e até URLs de conexão a banco de dados seguem um formato padronizado (ex.: `mongodb://usuario:senha@host`). Nem toda chave tem essa característica — vários sistemas usam tokens genéricos, sequências aleatórias de letras e números sem prefixo — mas as chaves dos grandes provedores costumam ser reconhecíveis de cara, o que as torna buscáveis por *regex* (padrão de texto).

## Limites técnicos da busca de código do GitHub

A API de busca de código do GitHub (`search code`) tem uma característica pouco conhecida: ela não lê o estado atual de todos os repositórios do mundo a cada consulta — ela consulta um **índice**, e esse índice **não é instantâneo**. Quando um repositório é criado ou recebe um commit, leva tempo até ser indexado; como milhões de repositórios são criados todos os dias, o indexador prioriza o quê indexar, e projetos pequenos de um único autor tendem a ficar para trás na fila. Além disso, a busca:

- devolve **no máximo 1000 resultados por consulta**, mesmo que existam dezenas de milhares de repositórios compatíveis com os termos buscados;
- ordena os resultados por **relevância**, não por data — não há como pedir "o que foi commitado mais recentemente";
- considera apenas o **branch padrão** do repositório, e só arquivos **abaixo de um limite de tamanho**.

Essas limitações explicam por que uma busca ingênua por prefixo de chave (ex.: `sk_live`) tende a devolver repositórios antigos e já bem indexados, e não o que acabou de ser publicado — que é justamente onde uma secret recém-vazada tem mais chance de ainda estar ativa.

## Por que histórico de commits importa (e scanning de git history)

Uma secret pode estar em qualquer lugar: num `.env` atual, *hardcoded* no meio do código, ou num **commit antigo** que o autor do repositório achou que tinha removido. Apagar um arquivo num commit novo **não remove o conteúdo do histórico do git** — ele continua acessível em algum commit anterior para quem tiver acesso ao repositório, mesmo que a situação atual pareça limpa. Isso é o motivo pelo qual ferramentas de *secret scanning* sérias (ex.: TruffleHog, Gitleaks) não olham só o estado atual dos arquivos: elas varrem **todo o histórico de commits** do projeto, desde o início.

## Categorias de secrets mais visadas

Chaves de serviços de IA (ex.: provedores de LLM) e credenciais de **gateways de pagamento** estão entre as mais procuradas por quem faz esse tipo de varredura — justamente por terem valor de revenda ou uso indevido imediato (consumo de créditos de API, movimentação financeira). Termos de busca associados a integração de pagamento (ex.: variáveis relacionadas a Pix, *postback URL*) são usados como indicador indireto de que um repositório trabalha com sistemas financeiros reais, mesmo sem buscar a chave diretamente.

## A lição central

A regra prática que decorre disso tudo (já coberta na wiki em [[wiki/concepts/secrets-management]]) é que uma secret **commitada deve ser considerada comprometida no instante em que o commit é público**, independentemente de o autor perceber o vazamento rapidamente ou não — bots de varredura automatizada, tanto defensivos (secret scanning corporativo) quanto ofensivos, monitoram continuamente novos commits em busca exatamente desse tipo de padrão.
