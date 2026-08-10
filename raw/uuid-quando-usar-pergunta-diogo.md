# UUID: qual o melhor caminho? (pergunta do Diogo)

Transcrição de áudio (fala espontânea). Limpo de repetições e cacoetes de fala, mantendo o conteúdo técnico e a estrutura do raciocínio do apresentador. Sem tradução — conteúdo original em português.

## Contexto

O Diogo mandou uma pergunta ao apresentador: ele está trabalhando em um sistema e pensando em usar UUID (Universally Unique Identifier) como identificador único. Ele nota que vê muita gente falando sobre o custo do UUID e pergunta qual é o melhor caminho, a melhor abordagem em relação ao uso de UUID.

## O que é UUID/GUID

Existem dois termos que representam a mesma ideia: **UUID** (Universally Unique Identifier) e **GUID** (Globally Unique Identifier). Na versão atual mais usada — a v4, a mais randômica — o identificador tem 128 bits de tamanho. Cada caractere é representado em hexadecimal, não apenas numérico. O UUID tem uma versão embutida e contém várias informações importantes na sua estrutura.

A ideia central: ao invés de usar chaves primárias/estrangeiras sequenciais (sequências numéricas incrementais — registro 1, registro 2, registro 3...), você gera um identificador randômico que segue um padrão definido (a versão do UUID), e passa a usar isso como chave ao invés de sequências.

## Vantagem 1 — Merge de bases de dados (sharding / múltiplas origens)

Se você tem sharding de dados — ou seja, separa trechos da sua base em pedaços, seja por cliente, seja por região — eventualmente você vai precisar fazer o merge desses dados.

Isso já aconteceu com o apresentador: teve que integrar bases de clientes diferentes para consolidar em um único banco. Com chaves sequenciais, você invariavelmente tem conflito — o banco 1 tem um registro com ID 1, o banco 2 também tem um registro com ID 1, e quando você junta as bases, há colisão de chaves. Nessa situação você acaba tendo que reescrever chaves — o apresentador relata ter passado "boas semanas" reescrevendo chaves para permitir a junção desses dados depois de já ter esse problema em produção.

Nesse sentido, o UUID é muito válido: o risco de colisão é extremamente baixo (por ser randômico e ocupar um espaço grande — 128 bits), a ponto de ser considerado praticamente impossível de colidir mesmo gerando bilhões de UUIDs por dia. Isso é um dos pontos positivos: unicidade, e você evita ter que reescrever chaves depois.

## Vantagem 2 — Proteção contra enumeração de recursos (dificultar IDOR)

Ponto mais controverso, mas o apresentador defende: em APIs REST, ao navegar, você expõe números sequenciais na URL — por exemplo `/organizacoes/1/usuarios/2`. Isso dá brecha para ataques de enumeração: um usuário autenticado varia o ID na URL e eventualmente pode acessar dados de outro cliente, ou de outro usuário no mesmo sistema (multi-tenant, base compartilhada entre clientes nas mesmas tabelas/documentos).

Um UUID como identificador dificulta esse tipo de ataque — não é sinônimo de segurança, mas funciona como uma proteção extra. Isso não substitui um filtro de segurança adequado, que precisa analisar toda requisição e validar se os parâmetros realmente estão dentro dos critérios de autorização definidos para aquele usuário.

**Exemplo de furo comum:** rotas costumam ser bem protegidas, mas o *dado* nem sempre é. Exemplo ilustrativo: uma rota de comentário em vídeo, tipo `/channels/{id}/videos/{id}/comment`, faz um POST identificando o usuário que criou o comentário. O mesmo padrão se aplica a qualquer entidade que tenha chaves estrangeiras para outras entidades — como saber se o sistema realmente valida se cada uma dessas chaves está dentro das regras de autorização definidas? Diferentes tipos de brecha podem ser exploradas exatamente nesse ponto — não coragem, mas falta de validação de cada referência entre entidades.

**Caso de uso interessante:** usar UUID como "senha" implícita de um recurso. Exemplos: comprovante de compra de passagem aérea ou ingresso de show feito sem autenticação — o link com o UUID protege o recurso porque o identificador é suficientemente randômico e difícil de adivinhar, sem exigir login/senha. Ressalva: quanto maior o volume de dados (bilhões de registros), maior o risco teórico de alguém acertar um desses números — por isso isso não é sinônimo de segurança, é apenas uma estratégia possível.

## Desvantagens

1. **Espaço.** Enquanto uma chave inteira (int) ocupa 4 ou 8 bytes, um UUID ocupa no mínimo 16 bytes. Isso pode representar 2, 3, 4 vezes mais espaço necessário para armazenar um volume grande de dados, e impacta índices e comparações (mais caras do que comparar números menores).

2. **Comparação manual chata.** UUID em hexadecimal não é fácil de digitar/comparar de cabeça — diferente de um ID sequencial pequeno onde dá para "olhar e saber" (10582, 13582...). Com 128 bits, praticamente só dá para copiar e colar (Ctrl+C/Ctrl+V).

3. **Performance.** Consequência direta do tamanho: índices maiores, comparações mais caras.

O custo de cada uma dessas desvantagens precisa ser bem pesado e analisado — não é uma decisão automática.

## Caminho intermediário (o que o apresentador usa)

Duas abordagens que o apresentador já usou:

- **UUID em tudo.** Já usou em sistemas inteiramente modelados com UUID e funciona bem — dá uma sensação de solidez na navegação/modelagem do banco.
- **Híbrido (abordagem "neutra").** Usa sequência numérica (int) internamente — em todas as joins, todas as queries internas — para ganhar agilidade tanto no código quanto no processamento do banco. Em cima disso, nas tabelas que fazem sentido (tabelas expostas em rotas, nem toda tabela precisa) cria um hash/UUID adicional, com o tipo de dado que fizer sentido, e usa esse identificador de forma pública — seja para proteger, seja para desencorajar ataques de numeração.

Reforço: isso não substitui um bom sistema de autorização de usuário, que precisa mapear com cuidado quem pode acessar o quê. É chato de modelar, mas necessário — o UUID é um complemento, principalmente contra furos que acabam passando despercebidos.

## Onde UUID é mais comum

Pergunta de um espectador (Marco Vinícius): UUID é mais comum em algum tipo específico de banco de dados?

Resposta: bancos NoSQL — orientados a documentos, ou bancos de grafos — costumam não ter o conceito de "tabela" nem de ciclo/sequence do jeito que bancos relacionais têm. Como os documentos não têm esquema fixo, esses bancos tendem a usar funções que geram IDs dinamicamente, e por isso é comum ver estratégias de geração de UUID sendo usadas nesse contexto, principalmente em bancos orientados a documentos.
