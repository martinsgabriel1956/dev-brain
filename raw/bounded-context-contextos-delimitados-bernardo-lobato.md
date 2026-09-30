# Bounded Context (Contextos Delimitados) — Dominando DDD #4 (Bernardo Lobato)

Fonte: transcrição de vídeo do YouTube, canal de Bernardo Lobato, quarto vídeo da série "Dominando DDD". Já em português — sem necessidade de tradução. Transcrição automática colada pelo usuário; apenas pontuação, parágrafos e títulos de seção foram adicionados, e o texto foi limpo de erros de reconhecimento de fala.

Termos corrigidos por contexto (transcrição automática): "Domen and Driven Design" → Domain-Driven Design; "DVD" → DDD; "bound context / bonded context / Bald / Balding / Bnet contest" → bounded context; "linguagem umbíqua / bíqua" → linguagem ubíqua; "Martin Faller" → Martin Fowler; "inxuta" → enxuta; "Web" final ("เฮ") → ruído de áudio descartado; "éí de nome" → "ID e nome".

---

## Abertura

Você já participou de um projeto em que as palavras "pedido", "usuário" ou "produto" pareciam ter significados diferentes dependendo de quem falava? Já entrou em uma reunião falando um determinado termo e todo mundo começou a te olhar estranho, como se aquele termo não fizesse nenhum sentido naquele contexto?

Olá, devs, eu sou Bernardo Lobato e esse é o quarto vídeo da série **Dominando DDD**. Nos três primeiros vídeos fundamentamos o que era DDD e as motivações que nos levam a usar essa abordagem de desenvolvimento. Falamos também de domínios e subdomínios e detalhamos a linguagem ubíqua — dois dos pilares do DDD. Se você perdeu algum vídeo da série, o link está no card; recomendo assistir antes deste.

## Recapitulação

Resumidamente, o Domain-Driven Design (DDD) é uma abordagem para o desenvolvimento de software que foca em modelar o sistema com base no seu domínio, ou seja, na lógica central do negócio.

- **Domínio**: o conjunto central das regras que o sistema pretende implementar.
- **Subdomínios**: subconjuntos dessas regras — divisões naturais do domínio, cada um com suas próprias regras, responsabilidades e complexidades.
- **Linguagem ubíqua**: vocabulário comum e consistente, criado em colaboração entre o time técnico e os especialistas de domínio, usado ao longo do projeto inteiro, entre outros motivos para diminuir as ambiguidades que surgem naturalmente no desenvolvimento.

A partir desses conceitos, hoje definimos um terceiro pilar do DDD: os **bounded contexts**, ou, em bom português, **contextos delimitados**.

## O que é um Bounded Context

Um bounded context é um **limite linguístico e semântico** dentro de um sistema. É um conceito tão importante no DDD quanto a separação de responsabilidades em domínios e subdomínios. Assim como a linguagem ubíqua, os contextos delimitados são simples de entender, porém difíceis de implementar na prática.

A prática do uso de bounded context facilita o entendimento e a desambiguação de um conceito ou termo dentro do contexto maior, exercitando e explicitando de maneira clara **até onde aquele termo pode ser usado sem ambiguidades**. Na prática, ele determina limites claros de onde um determinado termo ou conceito pode ser utilizado de forma consistente dentro do sistema.

Dentro de um mesmo bounded context, um termo tem um significado que os especialistas de domínio dominam e, por consequência, os especialistas de tecnologia também. Fora desse contexto, em outros contextos do mesmo sistema e do mesmo domínio, esse mesmo termo pode ter um significado completamente diferente ou um significado complementar ao original. Por isso é essencial mapear e modelar bem esses contextos, para:

1. Evitar a ambiguidade dentro do sistema;
2. Garantir boa autonomia dos times de desenvolvimento;
3. Manter a clareza do código e do sistema como um todo.

## Exemplo: Produto em Vendas vs. Suporte

O exemplo usa uma imagem do site de Martin Fowler com dois contextos bem diferentes — **Vendas** e **Suporte** — cada um com seus próprios módulos, mas com algumas entidades presentes em ambos. Como implementar essas entidades? Deve-se usar a mesma classe nos dois contextos?

**Produto no contexto de Vendas** precisa de atributos como preço, nome, descrição, palavras-chave, quantidade em estoque etc. — tudo o que é necessário para efetuar a venda.

**Produto no contexto de Suporte**: digamos que abro um ticket pedindo ajuda referente a algum aspecto de um produto comprado. Preciso saber o preço? As palavras-chave cadastradas? As categorias? A quantidade em estoque? Provavelmente não. Faz mais sentido uma representação mais enxuta da entidade, somente com **ID, nome e uma pequena descrição** — só o que é preciso para atrelar um produto a um ticket de suporte.

Pergunta natural: no contexto de vendas já existe um produto completo; por que não aproveitar essa entidade e usar só os dados que interessam no suporte? Porque assim acoplamos ao contexto de suporte funcionalidades que não lhe dizem respeito. O ideal é ter **outra entidade** que represente o produto somente com os campos de interesse do suporte.

Isso significa ter **duas classes "Produto"** no sistema? Sim — para esse exemplo, o ideal é ter duas classes/entidades separadas tratando do mesmo conceito em contextos diferentes. Isso mantém a clareza e a coesão dos módulos. Em sistemas complexos, com muitos módulos e muitos times trabalhando ao mesmo tempo, isso **diminui o acoplamento entre times e módulos e aumenta a coesão dentro de cada módulo**, mantendo sua responsabilidade apenas no que interessa. O módulo de suporte não precisa se preocupar com detalhes de produto, pois é um subdomínio completamente diferente do de vendas.

**Disclaimer importante:** criar classes separadas representando o mesmo conceito **não implica necessariamente ter tabelas separadas no banco de dados**. É possível mapear classes diferentes para a mesma tabela, mapeando apenas os campos específicos que cada uma precisa manipular.

## Bounded Context ≠ Subdomínio

Dúvida honesta e comum: "então bounded context é a mesma coisa que subdomínio?" Não.

- **Subdomínio**: divisão do **negócio**, parte do **domínio do problema**.
- **Bounded context**: limite **técnico e linguístico** do **domínio da solução**.

Um bounded context não corresponde necessariamente a um subdomínio. Um subdomínio pode ter **um ou mais bounded contexts** atrelados a ele, dependendo da sua complexidade.

## Bounded Context ≠ Linguagem Ubíqua

Para quem viu o vídeo anterior e ainda tem o conceito fresco, a diferença pode ter ficado nebulosa:

- **Linguagem ubíqua**: vocabulário comum e compartilhado que a equipe adota para se comunicar com clareza sobre o domínio do problema e da solução. Nasce da colaboração constante entre especialistas de tecnologia e de domínio e é usada em reuniões, documentação, código-fonte etc.
- **Bounded context**: define **até onde** essa linguagem ubíqua é utilizada — até onde o significado de uma palavra vale e deixa de valer.

Exemplo: mesmo com linguagem ubíqua bem definida e domínios bem mapeados, o termo **"pedido"** pode ter significados diferentes. No contexto de **vendas**, pode significar uma **intenção de compra**; no contexto de **logística**, pode significar **ordem de entrega**. É preciso definir os contextos para limitar exatamente até onde aquela linguagem ubíqua funciona.

**Analogia:** um bounded context é como um **país**, e a linguagem ubíqua é o **dialeto** falado nesse país. Os países vizinhos podem ter a mesma língua ou dialetos diferentes.

## Por que são importantes (a ponto de serem um pilar do DDD)

- Reduzem a ambiguidade da documentação e do código;
- Facilitam muito a modularização da aplicação — será muito útil quando falarmos de arquiteturas distribuídas e até de microsserviços ("guarda bem esse conceito");
- Melhoram a comunicação entre equipes de desenvolvimento e especialistas de domínio;
- Tornam o sistema mais sustentável e evolutivo;
- Reduzem o acoplamento entre contextos diferentes e aumentam a coesão dentro de cada módulo/subdomínio correspondente.

## Como identificar contextos no processo de desenvolvimento

Nas entrevistas de refinamento e nas sessões de *discovery* podemos observar comportamentos como **conflitos de vocabulário** — termos que parecem não estar bem definidos entre todos os especialistas de domínio.

**Dica valiosa:** quando um termo passa a ter **discussão de significados entre times diferentes** — mesmo entre times de especialistas de domínio — é um grande sinal de que eles pertencem ou podem pertencer a **contextos diferentes** (e contextos sobrepostos).

## Prévia: comunicação entre contextos (próximo vídeo)

No próximo vídeo da série o autor detalhará como um contexto conversa com outro, já que múltiplas entidades podem ser implementadas de maneiras diferentes em cada contexto. Neste vídeo, apenas cita estratégias:

- **Shared Kernel**: compartilhamento controlado de modelos;
- **Customer/Supplier**: tipo de dependência hierárquica;
- **Conformist**: um contexto se adapta ao outro;
- **ACL (Anti-Corruption Layer)**: uma espécie de camada de tradução entre contextos — mais abrangente, bastante utilizada na modernização de sistemas legados.

## Encerramento

Pergunta ao público: já conhecia esse tipo de distinção de contextos limitados? Já fez essa divisão no seu projeto sem saber que era DDD, ou mesmo sabendo? Já teve mais de uma classe no sistema representando a mesma entidade? Comente. Pedido de like, inscrição e compartilhamento com o time — cada interação ajuda o YouTube a espalhar o vídeo ("a gente está bastante no começo aqui").
