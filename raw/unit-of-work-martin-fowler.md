# Unit of Work

Fonte: https://martinfowler.com/eaaCatalog/unitOfWork.html
Autor: Martin Fowler
Data de publicação: 05 de março de 2003
Tradução: PT-BR (conteúdo original em inglês, traduzido integralmente)

## Definição

"Mantém uma lista de objetos afetados por uma transação de negócio e coordena a escrita das alterações e a resolução de problemas de concorrência."

## Corpo do texto

Quando você está trazendo dados para dentro e para fora de um banco de dados, é importante manter o controle do que você alterou; caso contrário, esses dados não serão gravados de volta no banco de dados.

Da mesma forma, você precisa inserir novos objetos que criar e remover quaisquer objetos que excluir.

Uma Unit of Work (Unidade de Trabalho) mantém o controle de tudo o que você faz durante uma transação de negócio que pode afetar o banco de dados.

Quando você termina, ela calcula tudo o que precisa ser feito para alterar o banco de dados como resultado do seu trabalho.

## Referência

Para mais detalhes, veja o Capítulo 11 do ebook online em oreilly.com.

Este padrão faz parte de *Patterns of Enterprise Application Architecture*.

## Atribuição

Martin Fowler, 05 de março de 2003.

© Martin Fowler
