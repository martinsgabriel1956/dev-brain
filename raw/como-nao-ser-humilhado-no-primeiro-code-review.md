# Como Não Ser Humilhado no Primeiro Code Review

> Resumo/adaptação de vídeo sobre a dinâmica de code review para programadores juniores entrando no mercado de trabalho.

---

## Introdução

Programadores que entram no mercado costumam se surpreender com a quantidade de comentários e correções que recebem no primeiro code review. O choque é real: sai da faculdade/curso animado, sobe o primeiro código e recebe de volta uma revisão cheia de apontamentos.

Na maioria dos casos isso **não é sobre a pessoa ser ruim** — é sobre desconhecer o padrão de código, o framework e as convenções específicas daquela empresa. Quem revisa raramente tem intenção de humilhar; o problema costuma ser falta de tempo e de tato na hora de comentar (agenda cheia, pressão de entrega), não maldade.

O medo típico do júnior: perder a vaga, não passar no período de experiência, achar que cada entrega ruim é definitiva. Isso gera ansiedade, síndrome do impostor e retração — o júnior passa a evitar pedir ajuda por medo de expor desconhecimento, o que piora o ciclo.

---

## Passo 1 — Verificar a Regra de Negócio Antes de Tudo

Antes de se preocupar com estilo, formatação ou "código bonito", confirme que a implementação **cobre de fato** a regra de negócio descrita na tarefa. Um código limpo que não resolve o problema pedido pelo PO não serve. Prioridade:

1. A funcionalidade faz o que foi pedido?
2. Só depois disso: legibilidade, padronização, formatação.

---

## Passo 2 — Passar o Código por uma Revisão Automatizada Antes do PR

Antes de abrir o pull request, vale revisar o próprio código com apoio de uma IA (ou de um colega mais experiente), pedindo explicitamente para explicar **o que** mudaria e **por quê**, e para adequar o código ao stack/framework usado na empresa.

O ponto central: não se trata de aceitar sugestões sem entender — o objetivo é aprender o padrão para não depender da ferramenta indefinidamente. Depender cegamente da IA sem entender o motivo das mudanças cobra o preço depois (ex: num teste técnico sem acesso à ferramenta).

---

## Passo 3 — Testar em Ambiente Externo, Não Só na Máquina Local

Testar só localmente é enganoso: o ambiente de desenvolvimento pode ter variáveis, chaves de API ou configurações que não existem localmente. Sequência recomendada:

1. Ambiente de desenvolvimento/homologação (com QA, se a empresa tiver).
2. Só depois considerar o código pronto para revisão.

Nunca testar diretamente em produção — é o ambiente do cliente final.

---

## Passo 4 — Não Levar Comentários de Code Review para o Lado Pessoal

Antes de abrir o PR, alinhar com o PO se não há outra prioridade na fila. Depois de aberto, se vierem comentários ou reprovação:

- A crítica é ao **código**, não à pessoa.
- Vale manter um registro dos apontamentos recorrentes para não repetir os mesmos erros nos próximos PRs.
- Evitar reagir defensivamente ("não faz sentido") — presumir que quem revisou tinha um motivo, ouvir primeiro, questionar depois.
- Nos primeiros meses, é mais estratégico focar em entregar bem a própria tarefa do que insistir em mudanças fora do escopo pedido: se a iniciativa der errado, a responsabilidade recai sobre quem a propôs.

---

## Passo 5 — Testar em Produção Após o Deploy

Depois que o código sobe para produção, validar manualmente que a funcionalidade funciona para o cliente final (diferentes dispositivos/telas, se aplicável), antes de marcar a tarefa como concluída. Reportar proativamente um bug encontrado nessa checagem é visto como sinal de comprometimento, não como falha.

---

## Síntese

Checklist resumido:

1. Bate com a regra de negócio da tarefa?
2. Foi revisado/refinado antes do PR?
3. Foi testado em ambiente externo (dev/homologação)?
4. Comentários do review foram tratados sem tomar como crítica pessoal, com anotação dos pontos recorrentes?
5. Foi validado em produção após o deploy?

Seguir esses passos reduz drasticamente a fricção do code review e acelera a curva de aprendizado do padrão da empresa.
