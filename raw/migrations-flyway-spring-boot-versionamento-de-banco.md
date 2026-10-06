# Migrations com Flyway e Spring Boot: versionamento do banco de dados

> Transcrição de vídeo colada pelo usuário e limpa. Já estava em português (sem tradução). Corrigidos erros de reconhecimento de fala: "Toncat" → Tomcat; "Spring Webr" → Spring Web; "post grec / Postgris / post grassell" → PostgreSQL / Postgres; "IntelJ" → IntelliJ; "PG de Min" → pgAdmin; "Springniter" → Spring Initializr; "Spring Boot 411" → Spring Boot 4.1.1 (leitura provável); "DB.migrations" → `db/migration` (pasta padrão do Flyway; ver nota); "flyway esquema histórico/story" → `flyway_schema_history`; "checks / checksan / checks s" → checksum; "outer table" → `ALTER TABLE`; "Ibernate" → Hibernate; "aplicativo no teu ORM" → no teu pgAdmin (leitura provável); "PSQL / pon SQL" → `.sql`; "big serial primary keyrula" → `BIGSERIAL PRIMARY KEY`. Autor/canal não identificado. O autor menciona que o código do projeto foi montado só para o vídeo.

---

## Abertura (o problema)

Imagine que você criou uma coluna nova no seu banco local e funcionou perfeitamente. Você subiu a aplicação para produção e ela quebrou. Por quê? Porque ninguém criou a coluna no banco de produção. O tema do vídeo é **migrations**: o que são, e o que aparece em entrevista técnica.

## O que são migrations

Migrations são **versões do banco de dados em forma de scripts** (SQL, ou ferramentas) que criam tabelas e colunas, alteram a estrutura e **mantêm um histórico do que foi aplicado**.

## Projeto de demonstração

Gerado no Spring Initializr:

- Java 21, Maven, Spring Boot 4.1.1, artefato `migrations`.
- Dependências: **Spring Data JPA** (persistência), **Spring Web** (Spring MVC), **Flyway Migration** (o pacote central do vídeo) e **PostgreSQL Driver**.

No IntelliJ, o primeiro passo é configurar o `application.properties` para conectar no PostgreSQL. O autor criou um banco chamado `migrations` (pelo pgAdmin) para os testes. Configurações citadas:

- `spring.jpa.hibernate.ddl-auto=validate` (o Hibernate só valida o schema, não o cria);
- `spring.jpa.show-sql=true`;
- `spring.flyway.enabled=true`.

Pré-requisito: o **banco** (database) precisa existir. O Flyway cria tabelas, não o banco em si.

## Como o Flyway entra

Só de adicionar o Flyway como dependência no `pom.xml`, o Spring Boot passa a procurar scripts na pasta `db/migration`, dentro de `resources`. É ali que se colocam os scripts de controle e gerenciamento do banco.

### Primeira migration: criar a tabela `cliente`

O arquivo segue o padrão do Flyway: `V` maiúsculo + número da versão + **dois underscores** + descrição livre + `.sql`. Exemplo: `V1__create_cliente.sql`. O prefixo `V<n>__` é **obrigatório** para o Flyway reconhecer o arquivo como script de migração; o resto do nome pode ser qualquer coisa.

Conteúdo:

```sql
CREATE TABLE cliente (
  id    BIGSERIAL PRIMARY KEY,
  nome  VARCHAR(250) NOT NULL,
  email VARCHAR(150) NOT NULL
);
```

Ao subir o servidor (Tomcat embutido), a aplicação sobe ("Started MigrationsApplication") e a tabela `cliente` aparece no banco (refresh no pgAdmin, em schemas → tables).

### A tabela de histórico

Junto com `cliente`, aparece a tabela **`flyway_schema_history`**, onde o Flyway controla o que já foi executado na inicialização. Ao reiniciar o servidor, **nada acontece**: o Flyway consulta a tabela, vê que a V1 já foi executada e não reaplica. Um `SELECT * FROM flyway_schema_history` mostra a versão 1, tipo SQL, descrição ("create cliente"), o **checksum**, quem instalou (o usuário `postgres`) e data/hora da instalação.

### Segunda migration: adicionar CPF

O cliente pede um CPF na tabela. Ponto central: **não se cria a coluna direto no banco** (por exemplo, pelo pgAdmin). O colega de time não teria a coluna e não vai criá-la manualmente. A mudança vira um novo script, `V2__cpf_cliente.sql`:

```sql
ALTER TABLE cliente ADD COLUMN cpf VARCHAR(11);
```

Ao reiniciar, o Flyway roda só a V2. Em `flyway_schema_history` aparece a versão 2 (script do CPF); a tabela `cliente` agora tem a coluna `cpf` (nome e e-mail vieram da V1).

Efeito prático: o mesmo conjunto de scripts roda em teste; quando a aplicação sobe para produção, o banco de lá também se constrói pelos mesmos scripts. Cada pessoa do time faz o mesmo, criando scripts de controle para o banco.

## Não se altera uma migration já aplicada

Se alguém do time **alterar um script já executado**, a aplicação não sobe: o Flyway dá o **erro de checksum**. Uma migração aplicada **virou parte do histórico do banco**; não é um arquivo para ficar editando. Para mudar algo, crie um **script novo**. Exemplo: para criar mais dois scripts (um índice na tabela `cliente` e uma coluna de data de nascimento), criam-se mais dois arquivos de migração (V3, V4), em vez de editar os anteriores.

Na tabela de controle, cada script tem seu checksum, e é isso que faz o Flyway saber que não precisa executar de novo.

## O que o Flyway garante (fechamento)

1. **Todo mundo do time tem o mesmo banco.**
2. **Ambientes** (dev, homologação, produção) **evoluem do mesmo jeito.**
3. **Alterações rastreáveis e, às vezes, reversíveis** ("reversíveis às vezes", nas palavras do autor).

Há várias ferramentas para isso; o autor prefere o Flyway e o usa no dia a dia. A ideia final: **tirar do Hibernate a responsabilidade de criar e manipular as estruturas** a partir das entidades e passar a ter **controle de versão também para o banco de dados**.

## Encerramento

Pedido para curtir, comentar e ativar notificações; cumprimento a um espectador recorrente. (Não é conteúdo técnico.)
