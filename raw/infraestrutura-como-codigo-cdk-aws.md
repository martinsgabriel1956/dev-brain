# Infrastructure as Code — Por Que Parar de Clicar no Console da AWS (com Demo em AWS CDK)

## Bloco patrocinado (AmaX)

Escolher infraestrutura de pagamentos para o seu projeto é crucial — você vai viver com ela por anos. A AmaX foi construída priorizando performance e tecnologia de pagamentos, ideal para quem integra via API. Eles têm antifraude, recorrência nativa, split de pagamentos, recuperação de carrinho com IA e documentação completa. Link com taxa zero no Pix integrando via API na descrição do vídeo original.

## O problema: configurar infraestrutura manualmente pelo console

Isso aqui é o console da AWS — e geralmente, se você seguir algum tutorial, ele vai te mostrar como abrir o console da AWS, abrir o Lambda, clicar em "create function", criar e subir suas funções e projetos por ali.

Isso tem um problema grande: quando a gente entra no console da AWS e manipula tudo manualmente, está fazendo algo que talvez não seja facilmente reproduzível e, com certeza, não vai estar bem documentado.

## O que é Infrastructure as Code (IaC)

O vídeo de hoje é uma aula sobre IaC — Infrastructure as Code. IaC é tratar infraestrutura da mesma maneira que a gente trata código: como um cidadão de mesma categoria, com controle de versionamento, documentação clara e de maneira reproduzível e revisável.

A primeira forma com que as pessoas geralmente configuram sua infraestrutura é manualmente, e isso está certo para aprender a lidar com qualquer provedor — seja AWS, Google Cloud ou Azure. Recomendo inclusive começar manualmente: seguir alguma documentação, algum curso, algum tutorial (a própria AWS tem documentações e tutoriais extensivos), subir um S3 manualmente, subir um Lambda manualmente — só tomando cuidado para não gastar dinheiro à toa.

Mas vai chegar um ponto em que empresas maduras — e toda empresa madura deveria ter isso — vão querer infraestrutura como código (ou algo similar) pelos benefícios que ela dá: versionamento, revisão, auditabilidade, replicabilidade e automação. Se a infraestrutura é sempre gerada manualmente clicando no console, a gente não tem nenhum desses benefícios, e está fazendo as coisas de uma maneira que eu julgo não profissional. Para uma startup nova, às vezes não tem problema; mas para um projeto verdadeiramente robusto, a gente quer caminhar para IaC.

## Por que IaC existe — o problema da configuração invisível

Imagina que você tem toda a sua infraestrutura criada clicando nos botões do console da AWS, e do nada você decide alterar alguma configuração do seu banco de dados — vai lá no Aurora/RDS e altera manualmente. Isso não fica claro para ninguém, não fica bem documentado, não fica visível. Pode ser que você faça essa alteração em staging e esqueça de fazer em produção, ou faça em dev e esqueça de fazer em produção.

Resumindo: IaC é pegar toda a configuração possível de uma infraestrutura e transformar isso em código. Esse código pode se dar de diversas maneiras — muitas dessas configurações estão em YAML, ou em TypeScript, ou em diversas outras linguagens.

## Ferramentas de IaC

Existem diversas ferramentas:

- **AWS CDK** — o autor usa com TypeScript. Você escreve código em TypeScript e ele gera CloudFormation.
- **Terraform** — provavelmente a ferramenta mais popular. Por um tempo (ou por muito tempo) era open source; depois a HashiCorp fechou a licença e mais cara, e surgiu o **OpenTofu** como fork gratuito do Terraform.
- **AWS CloudFormation** — a forma nativa da AWS de gerar uma configuração de cloud e ter isso em um arquivo. No próprio dashboard da AWS existe uma seção CloudFormation onde você cria uma "stack" (conjunto de serviços da AWS).
- Outras citadas: **Pulumi**, **Ansible**, **Bicep** (Azure), e — de certa forma — **Kubernetes** também pode ser considerado IaC.

## Exemplo de arquitetura descrita como stack

Imagine uma stack (usando a terminologia da AWS) composta de:

- Um **API Gateway**, que conecta a diferentes **Lambdas** (λ1, λ2) baseado em rotas — por exemplo, `/user` e `/products` direcionam para Lambdas diferentes.
- Cada Lambda roda TypeScript.
- Ambos os Lambdas se conectam a um banco de dados **Postgres**.

Toda a parte de trás (Lambdas + banco) não tem acesso à internet — o usuário só acessa o API Gateway.

Tudo isso pode ser transformado numa especificação formal (um arquivo de CloudFormation, por exemplo), commitado no GitHub, disponível para todo mundo olhar, revisar e sugerir modificações. Se depois for necessário que um dos Lambdas passe a bater numa API externa (logo, precise de acesso à internet — via algo como um Internet/NAT Gateway), essa alteração é feita no código, revisada e versionada como qualquer outra mudança.

## Demo prática: um bucket S3 e um Lambda com AWS CDK

Para rodar isso é preciso configurar a CLI da AWS — gerando credenciais de API em "Security Credentials" no canto superior direito do console.

O projeto de demonstração é puro TypeScript. No `package.json` importa-se o pacote do CDK, e a partir daí se usa CDK dentro do código TypeScript.

No CDK, cria-se um `app` (aplicativo vazio). Esse app tem um projeto com um nome determinado, e um `environment` que pode ser alterado dinamicamente (dev ou prod) baseado em variáveis de ambiente — o mesmo código funciona para dev e para prod, com lógica condicional (`if (environment === 'dev') {...} else {...}`) dentro do próprio TypeScript. Exemplo real citado: numa empresa em que o autor trabalhou, o banco de produção tinha backups muito mais resilientes que o banco de dev (que praticamente não tinha backup) — e essa diferença era configurada dinamicamente via código.

Dentro da stack:

- **`Bucket`** — cria um bucket S3. Como é TypeScript puro, o nome do bucket (ou qualquer outra configuração) pode ser gerado dinamicamente por qualquer regra arbitrária — inclusive bater numa API externa antes de decidir. O autor recomenda não abusar disso e manter as coisas o mais reproduzível possível, mesmo sendo tecnicamente possível.
- **`HelloFunction`** — instancia um Lambda. Esse Lambda executa o código de `index.handler`, apontando para um arquivo `index.js` local que exporta um handler (JavaScript puro, retornando um status code simples). Toda vez que esse código é alterado e o CDK roda de novo, o código do Lambda na AWS é atualizado.
- **Permissões**: o bucket recebe uma regra de permissão de escrita concedida à `HelloFunction`, permitindo que o Lambda escreva no bucket via uma linha de código.
- Há também trechos que geram **outputs** (como prints do que foi criado).

### Deploy

Comando: `npx cdk deploy`. O CDK sintetiza a stack, lista todas as mudanças que vão acontecer (relacionadas ao bucket e ao Lambda) para aprovação antes de aplicar, e então efetivamente cria os recursos na conta AWS configurada.

Internamente, o CDK pega todo o TypeScript escrito, interpreta e usa isso para gerar um arquivo de CloudFormation (descrito como "tenebroso" de se ler diretamente) — é esse CloudFormation gerado que é de fato aplicado na AWS.

### Destroy

Comando: `npx cdk destroy` — destrói tudo o que foi criado pela stack.

### Verificação no console

Depois do deploy, é possível abrir o Lambda no console da AWS e ver o código exato que foi deployado (idêntico ao `index.js` local), rodar um teste pela própria interface e ver o output. O bucket S3 criado também aparece na lista de buckets da conta.

Nota da gravação: o autor notou que o recurso foi deployado na região errada (esperava US East 1 / N. Virginia, mas foi parar na Irlanda/EU) — um lembrete de como é fácil errar a configuração de região padrão, e de que isso já aconteceu "muitas vezes" com ele antes.

## Por que isso é reprodutível

Sempre que `npx cdk deploy` roda, ele deploya exatamente a mesma stack, com exatamente o mesmo código. Esse código é commitado no GitHub e, na prática, rodado através de uma pipeline (não do PC pessoal do desenvolvedor, embora seja tecnicamente possível fazer isso, como na demo). A partir daí, qualquer pessoa do time consegue revisar a infraestrutura, debugar, criar pull request, testar localmente, baixar o código, rodar localmente e olhar o CloudFormation gerado.

## Fechamento

O autor menciona ter um curso de system design, onde ensina esses conceitos (API Gateway, Lambda, network, banco de dados etc.) — descrito como o curso mais extenso já produzido pelo autor, com reembolso integral e sem questionamento dentro do primeiro mês para quem comprar e não gostar. Encerra com a frase: "Infrastructure as Code não é o futuro, é o presente — e se sua empresa não faz isso, ela está presa no passado."
