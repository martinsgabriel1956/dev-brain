# Mitos e Fable 5: os modelos de IA bloqueados pelo governo dos EUA por poder de cybersegurança

Transcrição de vídeo (Código Fonte TV), em português, sem necessidade de tradução.

---

E eu quero compartilhar uma dica que pode facilitar a vida de quem desenvolve software, porque em algum momento, em algum projeto, você vai precisar integrar pagamentos, e esse momento é mais crítico do que parece, porque a escolha de infraestrutura de pagamento é uma decisão de arquitetura e não só operacional — um negócio vive com ela por anos. Por isso segura aí essa nossa dica: a Appmax foi construída unindo tecnologia e performance em pagamentos, sendo ideal para quem integra via API recebendo pagamentos. Com Appmax o negócio tem acesso a antifraude com machine learning, recorrência nativa, split de pagamentos, recuperação de carrinho com AI e documentação completa que facilita todo esse processo, além de suporte técnico especializado. E para quem vem do Código Fonte TV tem condição especial: Pix com taxa zero integrando pela API. O link para falar com o time da Appmax está aqui na descrição.

Opa, mas calma aí: dia 1º de julho, enquanto a gente editava o vídeo, o governo dos Estados Unidos liberou finalmente o Fable 5, e depois de três semanas, agora tudo isso com um novo conjunto de classificadores para atingir e bloquear mais tarefas relacionadas à cybersegurança. De qualquer forma as informações continuam pertinentes, então segue o vídeo.

Aí agora já chegou num ponto que tá acendendo alertas para várias empresas e até países. Não é à toa que modelos como Mitos 5, Fable 5 e GPT 5.6 estão bloqueados para acesso ao público. A NSA já admitiu que vários sistemas importantes foram quebrados em questão de horas. Mas a verdade é que modelos com esse poder já não são exclusividade de empresas americanas. Então nós vamos entender o que essa nova classe de modelos tem de diferente, como eles vêm sendo tratados e utilizados, e o que nós podemos esperar para um futuro — mas um futuro bem próximo.

## Linha do tempo do Mitos

O Mitos foi anunciado em abril de 2026. Ele foi o primeiro modelo dessa classe de super poderosos no quesito de cybersegurança, tanto para explorar o lado bom quanto o lado ruim.

O preview card do Mitos, disponibilizado pela Anthropic, cita o Mitos como um modelo de IA extremamente avançado, com grande potencial em segurança e programação, e que levanta preocupações suficientes para não ser lançado ao público em geral.

O card descreve o treinamento do Mitos em três etapas:
1. Pré-treinamento em larga escala, com grandes volumes de dados textuais, para desenvolver capacidades gerais de linguagem, raciocínio e programação.
2. Fine-tuning com feedback humano, para melhorar a utilidade das respostas e a aderência às instruções.
3. Técnicas de alinhamento de segurança, inspiradas na abordagem da Anthropic, que guiam o comportamento do modelo com regras explícitas de segurança e redução de respostas perigosas.

Nada muito inovador nesse processo em si. Mas o card também traz uma avaliação descrita como mais rigorosa que as versões anteriores, incluindo:
- Red teaming, onde especialistas tentam induzir comportamentos inseguros ou explorar falhas do modelo.
- Avaliação de segurança e utilidade, medindo o equilíbrio entre responder bem às tarefas e evitar respostas arriscadas ou indevidas.
- Testes específicos de capacidades de cybersegurança.
- Comparações com versões anteriores para medir ganhos de capacidade e mudanças no comportamento de segurança.

Esse processo não difere muito do que outras empresas fazem — a OpenAI, por exemplo, também testa tentativas de jailbreak, prompts maliciosos e exploratórios, além de usar especialistas externos em segurança. É difícil comparar a profundidade real desses testes entre empresas com as informações públicas disponíveis.

## Projeto Glasswing

Pensando que um dos seus projetos já seria capaz de transformar profundamente a cybersegurança (pro bem ou pro mal), a Anthropic criou o projeto Glasswing: um consórcio de empresas e pessoas selecionadas para poder utilizar o Mitos.

Empresas listadas no consórcio inicial: Amazon Web Services, Apple, Broadcom, Cisco, CrowdStrike, Google, JP Morgan, Linux Foundation, Microsoft, Nvidia, entre outras.

A Mozilla, que não estava selecionada oficialmente, também usou o Mitos para corrigir vários bugs no Firefox, identificando vários problemas de segurança em número recorde.

Resumo do que o Mitos já fez até agora:
- Sozinho, encontrou uma vulnerabilidade de 27 anos no OpenBSD que permitia travar o sistema remotamente com apenas uma conexão.
- Encontrou uma falha de 16 anos no FFmpeg, biblioteca extremamente utilizada.
- Cruzou diversas brechas no próprio núcleo do Linux.

Diante disso, a Anthropic decidiu não disponibilizar o modelo ao público geral. No lugar, ampliou o projeto Glasswing: no início de junho, o consórcio (antes com 50 parceiros iniciais) passou a ter cerca de 150 organizações distribuídas em 15 países.

Com esses parceiros, o Mitos preview já encontrou mais de 10.000 falhas de segurança de gravidade alta ou crítica.

Curiosamente, o Mitos ficou extremamente famoso mesmo sem nunca ter sido liberado ao público geral — todo mundo conhece o nome e o que ele faz, mas a maioria nunca teve acesso. Há também relatos de pessoas que conseguiram acesso indevido a credenciais vazadas relacionadas ao acesso ao Mitos (ainda na época do Mitos preview).

## Fable 5, Mitos 5 e o bloqueio do governo americano

Depois, a Anthropic decidiu quebrar essa linha em outros modelos: lançamento do Fable 5 e do Mitos 5. O governo americano rapidamente reagiu, decidindo bloquear o acesso ao Fable 5 e ao Mitos 5:
- Mitos 5: bloqueado totalmente.
- Fable 5: bloqueado para não-americanos e empresas não-americanas, incluindo funcionários da própria Anthropic que não são americanos.

O Fable 5 é da mesma classe do Mitos, lançado em 5 de junho. Tem salvaguardas maiores, principalmente para exploração de vulnerabilidades, biologia, química e técnicas de destilação (métodos usados para treinar um modelo menor a reproduzir o comportamento e conhecimento de um modelo maior).

Mesmo assim, logo depois do lançamento surgiram vários alertas de jailbreak bem-sucedido — pessoas conseguindo bypassar restrições e fazer perguntas que o modelo teoricamente não deveria responder, incluindo sobre coisas proibidas. Um estudo de um laboratório de IA da Itália realizou 7.828 tentativas de jailbreak no Fable 5 e no Opus (modelo anterior da Anthropic); no Fable 5 especificamente, conseguiram ultrapassar as salvaguardas em 702 vezes — evidência de que, mesmo com todas as proteções, ainda é possível quebrar os guardrails do modelo.

A NSA encontrou vulnerabilidades em sistemas confidenciais dos EUA, o que motivou o bloqueio governamental. Isso não afeta só a Anthropic: qualquer empresa que lance modelos equivalentes dentro dos Estados Unidos deve sofrer bloqueio semelhante — é o caso do GPT 5.6, lançado há poucos dias pela OpenAI, que também não terá acesso liberado ao público.

O assunto foi discutido no Senado americano. O senador Mark Warner declarou que a ferramenta "invadiu quase todos os nossos sistemas classificados, não em semanas, mas em horas" — por isso a preocupação em não liberar o acesso para pessoas que não sejam americanas.

Em 26 de junho, o GPT 5.6 saiu em preview e também já foi bloqueado, sem acesso ao público por enquanto.

## Outros países entrando na corrida

Outras empresas e países já afirmam ter chegado a um nível equivalente ao do Mitos e do Fable 5:

- **Japão — Sakana AI**: lançou o Fugo, que funciona como um pool de outros modelos (não é necessariamente um modelo próprio), combinando modelos abertos (open source) e fechados. Em testes realizados pela própria Sakana AI e por um laboratório parceiro, o Fugo passou em vários benchmarks acima do Fable 5 e de alguns benchmarks do Mitos preview.

- **China — 360**: empresa gigante de segurança cibernética sediada em Pequim, revelou dois novos sistemas de segurança de IA, incluindo o **Tulong Fang**, modelo de IA projetado para enfrentar o Mitos da Anthropic, digitalizando e descobrindo automaticamente vulnerabilidades de software ocultas.

- **China — Zhipu AI**: lançou o GLM 5.2, também com o mesmo propósito de competir de frente com o Mitos.

A expectativa é que essa corrida gire uma "roda" em todos os países para desenvolver modelos próprios de cybersegurança — hoje, por exemplo, o Brasil não tem acesso a algo equivalente ao Mitos 5 para proteger sistemas ou criar soluções de cybersegurança, enquanto outros países já estão se armando (tanto para proteção quanto potencialmente como arma de ataque).

## Reflexão final

Tudo isso aconteceu num intervalo de menos de 3 meses. Há muita coisa ainda por vir até o fim de 2026 em termos de segurança da informação e desses modelos de IA. A preocupação que a computação quântica trazia para segurança chegou antes, via inteligência artificial — trazendo preocupação tanto para empresas quanto para governos. É uma corrida em andamento, e os governos ainda estão descobrindo como se proteger, tudo acontecendo muito rápido.

(Encerramento com novo chamado para o patrocinador Appmax sobre integração de pagamentos.)
