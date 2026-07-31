> Artigo original em inglês, traduzido/adaptado para português a partir do conteúdo extraído da página. Não é uma tradução literal palavra-por-palavra, e sim uma reconstrução fiel do conteúdo e da estrutura do artigo original, preservando números, nomes de ferramentas e a sequência de argumentação.

# Release Rápido em Escala Massiva (Facebook Engineering, 2017)

- **Fonte original:** https://engineering.fb.com/2017/08/31/web/rapid-release-at-massive-scale/
- **Publicado em:** 31 de agosto de 2017
- **Autor:** Chuck Rossi
- **Categorias:** DevInfra, Web

## Resumo

O artigo descreve como o Facebook evoluiu seu processo de deploy do frontend web, saindo de um modelo de três pushes diários baseados em branch de release/master com cherry-picks manuais, para um sistema quase-contínuo de "push a partir da master", permitindo iteração rápida sem sacrificar qualidade, mesmo em escala massiva de engenharia.

## Evolução da estratégia de release (Web)

Historicamente, o Facebook usava um modelo de branch master + branch de release, com engenheiros solicitando "cherry-picks" — mudanças de código que já haviam passado por uma bateria de testes automatizados — para serem puxadas para os pushes diários. Esse processo chegava a lidar com **500 a 700 cherry-picks por dia**.

Por volta de 2016, o volume de mudanças tornou esse modelo insustentável: a master passou a receber **mais de 1.000 diffs por dia**, e os pushes semanais chegavam a acumular até **10.000 diffs**. Diante disso, o Facebook migrou gradualmente, a partir de abril de 2016, para um sistema quase-contínuo de "push direto da master". Ao longo de aproximadamente um ano — expandindo primeiro para funcionários internos e depois para porcentagens crescentes de tráfego de produção — o sistema atingiu **100% dos servidores web de produção rodando código direto da master em abril de 2017**.

## Como funciona o processo de deploy

No novo modelo, o sistema publica **dezenas a centenas de diffs a cada poucas horas**. O rollout acontece em estágios:

1. Primeiro para os próprios funcionários (dogfooding interno);
2. Depois para uma fatia pequena de produção (cerca de **2%** do tráfego);
3. Só então para **100%** dos servidores.

Esse escalonamento permite monitorar o impacto de cada mudança e interromper o rollout rapidamente caso surjam problemas, sem precisar reverter uma versão inteira.

Outro elemento chave é o sistema **Gatekeeper**, que desacopla o release do código da ativação da funcionalidade: features podem ser habilitadas/desabilitadas via toggle, em vez de exigir reverter ou re-deployar uma versão.

## Vantagens do deploy contínuo

- **Elimina hotfixes de emergência** — como commits vão para produção quase imediatamente, não é mais necessário fazer pushes fora de banda para corrigir problemas urgentes.
- **Suporta um time de engenharia global** — remove a dependência de janelas de push amarradas a fusos horários específicos.
- **Força melhorias de infraestrutura** — testes automatizados, tooling e automação precisam evoluir para sustentar o ritmo do deploy contínuo.
- **Acelera o ciclo de feedback** — engenheiros aprendem mais rápido sobre o efeito real de suas mudanças em produção.

## Desafios no mobile

Diferente da web, o mobile não permite deploy verdadeiramente contínuo por causa das restrições das lojas de aplicativos (App Store/Play Store) e do tempo de propagação de atualizações para os usuários. Ainda assim, o Facebook aplicou os princípios de entrega contínua ao processo mobile, evoluindo de **ciclos de release de quatro semanas para ciclos de uma semana**.

Para isso, a empresa desenvolveu e adotou ferramentas internas como **Nuclide**, **Buck**, **Phabricator**, **React Native** e **Infer**, que aceleram testes e iteração no desenvolvimento mobile.

Mesmo com os times de Android e iOS crescendo **15 vezes** em tamanho, a produtividade por engenheiro se manteve constante, e o número de problemas críticos originados por releases mobile permaneceu praticamente estável — indicando que o aumento da frequência de deploys não comprometeu a qualidade.
