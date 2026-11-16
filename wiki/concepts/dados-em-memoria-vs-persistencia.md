---
type: concept
title: "Dados em memória x persistência"
aliases: ["estado em memória", "persistir dados", "persistência", "dados somem ao reiniciar", "in-memory state", "stateless"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 2
tags: [backend, persistencia, memoria, banco-de-dados, stateless, twelve-factor, nodejs]
skill: tech-mentor-backend
status: stub
---

# Dados em memória x persistência

Uma variável do programa (um array, um objeto) vive na RAM do processo. Quando o processo termina, por reinício, queda, deploy ou nova versão, tudo o que estava lá some. Persistir é gravar fora do processo, em algo que sobrevive a ele: um banco de dados, um arquivo, um serviço de armazenamento.

Guardar em memória tem um segundo problema: com mais de uma instância do servidor (escala horizontal), cada uma tem a sua cópia, e os usuários veem dados diferentes conforme a instância que os atende.

`[skill: tech-mentor-backend]` O fator 6 do Twelve-Factor App (*Processes*) diz que o app é *stateless*: o estado fica em um serviço de apoio (banco, Redis) e "qualquer instância pode morrer". Ver também [[wiki/concepts/sistema-de-arquivos-efemero]]: gravar em arquivo local também não persiste em plataformas com disco efêmero.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], os professores do Proffy ficam num `const profs = [...]` no `server.js`, e o cadastro entra com `profs.push(data)`. Depois de salvar o arquivo, o nodemon reinicia o servidor e o professor recém-cadastrado some: "toda vez que eu altero esse arquivo de server.js, a nossa aplicação é simplesmente resetada [...] eu perco todos os dados da memória". A saída que [[wiki/entities/mayk-brito|Mayk]] anuncia para o dia 5 é "guardar no banco de dados", porque "o banco de dados guarda isso em um HD". Ele compara com o computador que desliga antes de você salvar o arquivo.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o array do dia 4 dá lugar ao arquivo `database.sqlite`: os professores sobrevivem ao restart do nodemon. O arquivo fica dentro do projeto, o que funciona num servidor com disco persistente, mas não em plataformas de [[wiki/concepts/sistema-de-arquivos-efemero|disco efêmero]].

## Key sources

- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: cadastro em array some a cada restart do nodemon
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: o array vira SQLite
