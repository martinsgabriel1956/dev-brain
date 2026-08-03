# Escalabilidade Horizontal vs Vertical — Diferença e Custo

> Transcrição de aula curta (traduzida/formatada em Markdown, sem alterações de conteúdo).

Nessa aula vamos falar sobre a diferença entre escalabilidade horizontal e escalabilidade vertical.

## Escalabilidade Horizontal

Quando a gente fala de escalabilidade horizontal, estamos falando sobre a capacidade de aumentar o compute — número de CPUs, memória, rede — de forma horizontal.

Vamos supor que você tem três servidores: A, B e C. Eles têm a mesma quantidade de CPU e memória (2/8, 2/8, 2/8). Nesse exemplo, o que você faz é adicionar novos servidores. Você não tem nenhuma indisponibilidade nos servidores existentes — eles continuam operando. O que você faz é adicionar mais servidores, com o mesmo tamanho ou não (depende da estratégia).

Isso é escalabilidade horizontal. Ela tem um custo inferior ao da escalabilidade vertical (explicado adiante o porquê do custo).

**Analogia:** pensar no horizonte — além do horizonte, um monte de servidores "aparecendo no chão".

## Escalabilidade Vertical

Pensando verticalmente é como pegar uma imagem e aumentá-la verticalmente — ela cresce de todos os lados.

O vertical é adicionar mais compute a um único servidor: ele tinha 2 de CPU, você faz esse mesmo servidor ficar com 4 de CPU. Ele tinha 8 de memória, você faz ele ficar com 16 de memória.

Já existe há bastante tempo hypervisor que permite aumentar memória e CPU online. A redução é sempre mais arriscada — quase ninguém tem coragem de fazer, mas existe. É possível aumentar online, mas há sempre um risco associado — para online, garantias existem, mas não são absolutas.

Geralmente o que se observa é uma indisponibilidade: a aplicação precisa de um refresh, ou dependendo do que você usa, seria necessário um reboot no servidor, um stop/start — depende do hypervisor ou do cloud provider usado.

## Resumo da Diferença

Essa é a diferença entre horizontal e vertical. Hoje em dia se fala muito em ter uma arquitetura que escale horizontalmente. Porém, existem aplicações legadas que não comportam esse tipo de escalabilidade.

## Custo — Exemplo Gráfico

### Escala Horizontal

Em um gráfico de consumo de CPU ao longo do tempo (timeline), em um momento específico o consumo aumenta. A resposta é adicionar mais servidores — nesse exemplo, apenas um servidor a mais. Não foi necessário dobrar o tamanho de um servidor existente.

**Diferença:** com servidores pequenos, além de maior resiliência, há melhor tolerância a falha, porque há menos pontos únicos de falha (quanto mais servidores, mais o sistema tolera um deles falhar enquanto os outros continuam operando).

### Escala Vertical

Usando o mesmo tracejado de utilização do exemplo anterior: quando você vai para o vertical, dependendo de onde você está, não é possível simplesmente adicionar um número quebrado de CPU ou memória — em cloud providers, geralmente é o dobro do tamanho anterior.

Nesse exemplo, o resultado é ser obrigado a dobrar o tamanho do servidor. Isso acontece quando existe um monolito centralizado em um único servidor, não modularizado — você é obrigado a aumentá-lo inteiro.

**Desperdício:** a quantidade extra de memória/CPU obtida no dobro nem sempre é necessária, gerando uma porcentagem de uso baixa e gasto de dinheiro desnecessário — "queimando dinheiro" com capacidade ociosa.

## Conclusão

Quanto mais você consegue escalar horizontalmente, melhor. Porém, existem diversos pré-requisitos para uma arquitetura conseguir escalar horizontalmente.

