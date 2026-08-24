# Deployment Pipeline

> Tradução de "Deployment Pipeline", de Martin Fowler, publicado em 30 de maio de 2013 no bliki.
> Fonte original: https://martinfowler.com/bliki/DeploymentPipeline.html

---

Um dos desafios de um ambiente automatizado de build e teste é que você quer que seu build seja rápido, para conseguir feedback rápido, mas testes abrangentes levam muito tempo para rodar.

Um deployment pipeline é uma forma de lidar com isso quebrando seu build em estágios. Cada estágio fornece confiança crescente, geralmente ao custo de tempo extra.

Estágios iniciais conseguem encontrar a maioria dos problemas, gerando feedback mais rápido, enquanto estágios posteriores fazem uma investigação mais lenta e minuciosa.

Deployment pipelines são uma parte central da Continuous Delivery.

Normalmente, o primeiro estágio de um deployment pipeline faz a compilação e disponibiliza binários para os estágios seguintes.

Estágios posteriores podem incluir verificações manuais, como quaisquer testes que não possam ser automatizados.

Estágios podem ser automáticos, ou exigir autorização humana para prosseguir; podem ser paralelizados em várias máquinas para acelerar o build.

Fazer o deploy em produção costuma ser o estágio final de um pipeline.

De forma mais ampla, o trabalho do deployment pipeline é detectar qualquer mudança que vá gerar problemas em produção.

Isso pode incluir problemas de performance, segurança ou usabilidade.

Um deployment pipeline deveria viabilizar colaboração entre os vários grupos envolvidos na entrega do software e dar a todos visibilidade sobre o fluxo de mudanças no sistema, junto com uma trilha de auditoria completa.

Uma boa forma de introduzir continuous delivery é modelar seu processo de entrega atual como um deployment pipeline, e então examiná-lo em busca de gargalos, oportunidades de automação e pontos de colaboração.

**Leitura complementar:** para mais informações, ver o capítulo 5 do livro *Continuous Delivery*, disponível para download gratuito.

**Tags:** continuous delivery, build scripting
