# CI, CD (Delivery) e CD (Deploy) — e a diferença entre Deploy e Release

Transcrição de aula/vídeo (idioma original: português). Nenhuma tradução necessária.

## Abertura: os "dois CDs"

Na aula de hoje eu quero te explicar a diferença entre CI, CD e CD — como assim, são dois CDs? Um é o CD (continuous delivery) e o outro é CD (continuous deployment). Vamos aprender hoje sobre:

- **Continuous Integration** — integração contínua
- **Continuous Delivery** — entrega contínua
- **Continuous Deploy** — deploy contínuo

Existe uma diferença aqui entre delivery e deploy que é tecnicamente diferente — diferente quase por tecnicalidade. Mas eu quero nessa aula também salientar a diferença entre **deploy e release**, é muito importante a gente entender isso.

Na aula de hoje eu vou também mostrar na prática, com um exemplozinho, um deploy para uma VPS, mostrando um pouco de código em que a gente vai estar aplicando aqui o continuous deploy.

Primeiro eu quero te falar que essas coisas não são regras escritas em pedra, não existe um manualzinho a ser seguido — são mais conceitos meio que abstratos, e cada empresa pode aplicar isso de uma maneira um pouco diferente de outra empresa.

## Continuous Integration (CI)

É a integração contínua de código para dentro da codebase. Isso se traduz, geralmente, em uma empresa provar que o código funciona sempre que ela faz merge. Criei uma feature nova, vou integrar minha feature nova ali na main — isso vai se dar de forma que essa feature nova vai passar por algum tipo de pipeline. Essa pipeline pode ter processos manuais ou não, e geralmente vai ter:

- **Build** — ver que o código builda corretamente, que ele compila corretamente.
- **Lint** — ver que ele segue as regras, os padrões de código definidos na ferramenta linter. Hoje em dia a maioria das pessoas está simplesmente utilizando um Prettier ou algo do tipo, e tá tudo bem; às vezes você tem um ESLint, ou um Ruff no Python.
- **Testes** — testes unitários, de integração, end-to-end, etc.

Geralmente as pessoas vão colocar isso para rodar numa pipeline no GitHub — um dos mais populares aqui é o **GitHub Actions**, que é o que eu vou usar hoje. Mas as pessoas também podem usar outras ferramentas: o Jenkins já foi muito popular, acredito que hoje o GitHub Actions é a mais popular de todas, mas o Jenkins é uma alternativa que existe também.

## Continuous Delivery vs. Continuous Deploy

**Continuous delivery** significa que o código vai estar pronto para ser lançado automaticamente quando eu fizer merge — para mim o código vai ficar pronto para ser lançado.

**Continuous deploy** — quando eu faço merge do meu código, significa que ele vai automaticamente ser deployado para minha cloud ou para meu servidor.

## Qual é a diferença técnica entre deploy e release?

Deploy e release não são a mesma coisa. Eu posso subir uma feature e ter o meu código pronto dentro do meu servidor sem lançar esse código. Eu posso, por exemplo:

- Subir uma feature atrás de uma **feature flag**; ou
- Subir, buildar e testar todo o código, sem que o público consiga utilizar isso, e lançar isso através de uma **release** em algum determinado período de tempo.

Existe um artigo muito famoso da Meta sobre "Rapid Release at Massive Scale", em que eles explicam como fazem (ou pelo menos faziam, em 2017) continuous delivery em escala gigantesca. Nesse artigo dá para ver, num gráfico, que o código vai indo continuamente para a main, mas cada release fica disponível primeiro para os funcionários, depois para 2% da produção, e depois para 100% da produção. O que a Meta faz aqui é desacoplar um deploy de uma release para todo mundo — eles fazem esse rollout mais gradativo.

Hoje em dia o padrão das empresas é fazer isso através de pipelines — você transforma tudo isso numa pipeline para rodar automaticamente. Isso é imprescindível para conseguir corrigir erros humanos: se você estiver fazendo a parte do deploy manualmente, está errado. Tudo que você consegue fazer através de um script manual, você consegue fazer através de um script codado dentro da codebase, sujeito aos mesmos padrões e reviews da codebase. Então é recomendado que você mova o máximo possível disso para dentro da codebase e trate isso como um cidadão de primeira classe.

Claro, também é possível testar essas coisas localmente, a nível de integração: antes de eu commitar um código, eu posso ter acesso a scripts no meu `package.json` — `npm run lint`, `npm run test`, `npm run build` — para ver se o teste, o lint e o build funcionam. Você provavelmente vai ter isso também na sua pipeline.

## Exemplo prático com GitHub Actions

Dentro do repositório, na pasta `.github/workflows`, ficam os workflows que rodam no GitHub Actions. Pode haver vários jobs diferentes:

1. **Job de CI** — roda `npm run test`, `npm run build` toda vez que o código é enviado para a main. É possível ver os detalhes de cada job rodado no próprio GitHub.
2. **Continuous delivery** — vai até o ponto em que se prova que a aplicação está pronta para ser entregue aos usuários. Isso varia muito de empresa para empresa; geralmente significa que a aplicação ou vai estar direto entregue aos usuários, ou vai ficar num estado em que dá para fazer um deploy/entrega através de um clique. Depois que esse "gate" passa, deixa de ser 100% contínuo quando há uma interação humana — fica um pouco mais travado.

Na prática, a maioria das empresas — com exceção talvez de empresas gigantescas como a Meta — não faz distinção entre delivery e deploy. Para a maioria das empresas médias, isso acaba sendo a mesma coisa.

## Continuous deploy na prática: branches

O deploy contínuo se dá, geralmente, a partir do momento em que o código é mergeado para a `main` (ou para alguma branch equivalente — antigamente essa branch se chamava `master`, ainda dá para ver code bases antigas com esse nome).

Fluxo típico com feature branches:

```
feature/* → dev (ou staging) → main
```

Você seta uma pipeline para que, toda vez que fizer merge de uma branch para a main, aconteça automaticamente um deploy e um delivery — o código vai para produção e fica disponível para o cliente.

Isso pode não dar tempo para testar — por isso a maioria das empresas faz a feature ir primeiro para outra branch (`dev` ou `staging`, às vezes as duas) antes de ir para a main. Uma feature começa na branch de feature, depois vai para dev/staging, depois vai para main. Enquanto está em dev/staging, rodam os QAs para testar, e o próprio desenvolvedor consegue testar a feature ali.

Muitas empresas também clonam o banco de dados de produção para dev/staging, anonimizando o que precisa ser anonimizado — não se clona senhas de usuários, nome de pessoa, compras ou pagamentos feitos, por exemplo; isso vem tudo randomizado. Mas se clona a estrutura do banco de dados e, mais ou menos, a estrutura e dispersão dos dados, permitindo testar num ambiente muito parecido com produção.

### Onde entra o deploy

O deploy pode estar no mesmo workflow do CI/delivery ou em um arquivo diferente — tanto faz. A parte de deploy varia muito de acordo com a infraestrutura usada: a Vercel tem uma maneira própria de fazer, a AWS tem infinitas maneiras. Para este exemplo de demo, o método usado é simplesmente: SSH para a VPS, instalar o que é necessário dentro da VPS, e colocar para rodar.

### Sobre a VPS usada na demo (bloco patrocinado)

A VPS utilizada é da patrocinadora do canal e do vídeo, a HostGator. Eles têm tudo que é preciso para criar e hospedar um site — inclusive servidores de N8N fáceis de hospedar, para trabalhar com fluxos de agentes de IA, e uma solução com Claude Code pré-instalado, mais fácil e versátil do que rodar localmente (não precisa manter o computador sempre ligado; dá para mandar mensagem do celular de qualquer lugar). Recomenda-se essa solução para quem quiser usar Claude Code numa VPS dedicada em vez do próprio PC.

Foi contratado o plano mais barato da HostGator, a partir de R$ 21,70/mês (com oferta especial via link de descrição do canal). Existem diversos tipos de VPS: com Ubuntu, com Alma Linux, com Rocky Linux, ou com painéis pré-instalados (cPanel), ou ainda voltadas para rodar N8N, Node, WordPress ou Docker — com possibilidade de trocar o sistema operacional depois, reiniciando a VPS. A VPS está localizada em São Paulo, com boa latência para clientes/usuários no Brasil, boa velocidade de conexão e poder de processamento.

### Credenciais e secrets

A parte de continuous delivery/deploy necessariamente envolve lidar com credenciais — não dá para fazer deploy numa cloud sem as credenciais dessa cloud. É muito importante que essas credenciais não estejam no código: nem localmente commitadas (se commitar, dá trabalho para limpar completamente do histórico do Git — não basta deletar o arquivo, já que dá para ver o histórico).

No GitHub Actions, o caminho é: **Settings → Secrets and variables → Actions**. Ali é possível adicionar um secret (por exemplo, a senha da VPS). Uma vez salvo, mesmo o dono do repositório não consegue mais ler o valor armazenado — só é possível atualizá-lo, nunca visualizá-lo. Isso demonstra o nível de seriedade com que esse tipo de credencial precisa ser tratado.

Recomendação: se estiver usando GitHub Actions, usar os Secrets nativos do GitHub Actions. A AWS tem soluções próprias de gerenciamento de segredos; existem outras soluções no mercado também. Dentro do workflow, o valor é acessado via `secrets.VPS_PASSWORD` (ou o nome equivalente para outra credencial, como AWS).

A partir daí, a etapa de deploy propriamente dita depende de como a aplicação roda — Next.js (`next start`), algum comando `npm`, `ruby`, etc. — sempre um script que sobe a aplicação no servidor.

Essa etapa é vista como uma das partes mais "chatas" de configurar bem — e por isso mesmo, uma das mais importantes de revisar com cuidado, já que um erro aqui é especialmente custoso.

## Demonstração ao vivo

Demonstração: alteração de cores no CSS do site, commit (`git commit -m .`) e push para a main. Ao atualizar a página do GitHub, aparecem os dois jobs rodando: primeiro o job de teste e build (CI), depois o job de deploy para a VPS. Após a finalização de ambos os jobs, o site em produção reflete as novas cores — confirmando que o continuous deployment funcionou de ponta a ponta, do commit até produção, sem intervenção manual.

Observação à parte: durante a gravação, o GitHub Actions apresentou instabilidade e atrasos, atribuídos de forma humorística à aquisição do GitHub pela Microsoft.

## Fechamento

Se a distinção entre CI, CD (delivery) e CD (deploy) — e a diferença entre deploy e release — não tiver ficado 100% clara, isso é esperado: são conceitos abstratos, sem "manual único", que cada empresa aplica à sua maneira.
