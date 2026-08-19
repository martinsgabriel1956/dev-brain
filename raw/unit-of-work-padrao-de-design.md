# Unit of Work — Padrão de Design

Transcrição de vídeo (autor identificado no próprio texto por menção a "arjancodes.com" e ao "meu workshop gratuito de diagnóstico de código" — canal técnico de Python). Colada pelo usuário no chat, em português (pt-BR), sem necessidade de tradução. Organizada em seções abaixo; conteúdo integral preservado.

## Abertura

Hoje, vou abordar o padrão de design da unidade de trabalho. É útil aprender sobre esse padrão, especialmente se você interage regularmente com o banco de dados. A essência do que a unidade de trabalho faz é reunir todas as transações e executá-las todas de uma vez. Por que nós precisamos disso? Você pode se perguntar. Vou falar sobre isso neste vídeo. E não só isso, você também aprenderá que esse padrão é útil em alguns outros cenários.

Se estiver revisando o código de outra pessoa, você pode impressioná-la mencionando que ela deve usar o padrão de unidade de trabalho. E para outras dicas sobre como encontrar problemas em seu código com mais facilidade, confira meu workshop gratuito de diagnóstico de código no link abaixo. Também está na descrição deste vídeo.

## O que é e por que precisamos

O padrão de design da unidade de trabalho é semelhante ao padrão de comando. Mas o principal é que serve como uma espécie de ponto de coleta para múltiplas operações e depois aplica todas essas operações de uma só vez.

E, em particular, em bancos de dados, isso é muito útil porque você pode criar uma série de alterações que deseja aplicar ao banco de dados e, em seguida, confirmar todas as alterações de uma só vez. Isso economiza tráfego de rede. Mas também significa que, se um desses comandos falhar, você poderá implementar um mecanismo de reversão. E especialmente em áreas muito sensíveis como finanças ou outras coisas onde você quer ter muito cuidado com o que acontece com os dados, onde há muitas conexões entre diferentes tipos de dados, então é útil que você possa fazer esse tipo de mecanismo de reversão.

## Exemplo básico (sem dependências externas)

Primeiro mostrarei um exemplo bem básico que não possui nenhuma dependência externa, apenas para explicar como o padrão realmente funciona. Mas então passarei para um exemplo da vida real usando um banco de dados.

Aqui tenho um exemplo simples que define uma classe de usuário. Mas pode ser qualquer tipo de dado com o qual você queira trabalhar. E há outra classe chamada unidade de trabalho que encapsula o padrão de unidade de trabalho. E esta classe unidade de trabalho contém uma espécie de histórico das operações que foram realizadas. Portanto, quaisquer novos usuários que foram adicionados, quaisquer usuários que foram atualizados (usuários "sujos"), ou quaisquer usuários que foram removidos.

E então temos alguns métodos para adicionar esse tipo de operações. Então, queremos poder registrar um novo usuário. Podemos cadastrar um usuário sujo (usuário que precisa ser atualizado). E também podemos cadastrar usuários que precisam ser removidos.

E então temos um método `commit` que realiza a tarefa real de realizar o trabalho. Portanto, ele insere novos usuários, atualiza usuários sujos e exclui todos os usuários que precisam ser removidos. E atualmente isso não faz nada, porque não há conexão com o banco de dados. Este é apenas um exemplo simples. Mas aqui você pode basicamente realizar as operações reais. E como realmente confirmar as alterações é um método separado, você pode estender esse método e também adicionar um mecanismo de reversão. Por exemplo, se este método gerar algum tipo de exceção, você poderá desfazer as operações de inserção que fez aqui, basicamente reverter as alterações feitas.

E aqui tenho a função principal onde simplesmente tenho algum código de teste. Então eu crio essa unidade de trabalho, crio um novo usuário, atualizo outro usuário, removo outro usuário e então estou confirmando essas alterações. Então, quando eu executo isso, é isso que obtemos, certo? Essas operações são executadas todas de uma vez quando eu chamo o método `commit`.

## Unit of Work vs. Repository

A propósito, outro tipo de padrão que você verá usado em conjunto com o padrão de unidade de trabalho é o padrão de repositório. Portanto, a unidade de trabalho realmente se concentra nas operações. O padrão de repositório se concentra em fornecer uma camada de abstração no topo do banco de dados. Assim você pode interagir com o banco de dados sem conhecer todos os detalhes de implementação.

Um bom exemplo de biblioteca que combina o padrão de repositório com unidade de trabalho é SQLAlchemy. Já uso esse pacote há algum tempo. Funciona muito bem e também está em muitos dos exemplos dos meus vídeos do YouTube. E normalmente, unidade de trabalho ou repositório não é algo que você vai implementar do zero, mas é bom saber que existe e como funciona.

## Exemplo real com SQLAlchemy

Aqui tenho um exemplo um pouco mais completo que usa SQLAlchemy. E neste exemplo, ele usa apenas um banco de dados na memória porque não preciso de um banco de dados real neste exemplo de código. Eu faço coisas padrão como criar uma sessão e criar uma base declarativa, que posso usar como base para o ORM.

Então eu tenho algumas classes. Tenho uma classe de usuário que possui um ID, que é a chave primária, o usuário tem um nome e também há alguns relacionamentos. Assim, os usuários têm detalhes e também algumas preferências. A estrutura exata de como isso é configurado realmente não importa. É mais sobre como usar o SQLAlchemy e o padrão de unidade de trabalho integrado a ele.

Portanto, também tenho outras tabelas: um detalhe do usuário e a preferência do usuário, que contém algumas preferências do usuário. E então eu tenho funções para criar um usuário, para atualizar o usuário, excluir o usuário, e obter um usuário ou obter todos os usuários. E então, na minha função principal, chamo essas funções para trabalhar com os dados reais do banco de dados.

A parte ORM disso — a definição dessas classes — fornece uma espécie de implementação de padrão de repositório. É uma abstração no topo do banco de dados. Não interagimos diretamente com o banco de dados. Interagimos com esses objetos e isso resulta em alterações no banco de dados.

A forma como isso funciona no SQLAlchemy é que, para cada uma dessas funções que fazem alguma interação com o banco de dados, eu passo o objeto de sessão como argumento. E então eu uso isso para especificar quais operações precisam ser executadas. Neste caso, criei um usuário, adicionei alguns detalhes e preferências e depois chamo `add` no objeto de sessão. E o mesmo para, por exemplo, excluir um usuário. Então estou interagindo com o objeto `session` para realizar essas operações. E a sessão tem um método `commit` que realmente faz o trabalho real. Antes de fazer isso, nada mudou no banco de dados. E é exatamente isso que a unidade de trabalho faz.

## Gerenciador de contexto: commit e rollback

Aqui você vê um exemplo de como você pode usar isso. Crie uma sessão, que eu "rendo" (yield). Estou usando um gerenciador de contexto aqui. E depois de concluir o trabalho com a sessão, eu confirmo as alterações. Mas se houver algum tipo de exceção acontecendo aqui, então estou chamando `session.rollback` para desfazer as alterações feitas até agora na sessão. E finalmente, vou encerrar a sessão.

E como o usamos? Bem, temos um gerenciador de contexto. Então estou criando a sessão aqui. Então eu crio o usuário, atualizo o usuário e então posso realizar as operações, como criar um usuário. Enquanto você trabalha com a sessão, nada muda no banco de dados. Mas se você precisar fazer uma alteração no banco de dados — por exemplo, aqui estou atualizando o usuário, mas só posso atualizar o usuário se ele estiver realmente sendo armazenado no banco de dados — então você pode chamar `session.flush` no meio.

Quando executo esse código, ele faz todo esse trabalho. Primeiro eu crio o usuário. Inicialmente ele tem um ID `None` porque ainda não está sendo confirmado no banco de dados, mas então eu faço `session.flush`, que na verdade o armazena no banco de dados. Nesse ponto, quando imprimo o usuário novamente, ele agora tem um ID atribuído a ele. Então posso atualizar o usuário. E mesmo que ainda não tenha sido confirmado no banco de dados localmente, o usuário já está atualizado — quando eu pegar o usuário mais tarde e imprimi-lo, ele já me mostrará o usuário atualizado.

E finalmente, o que faço é simplesmente excluir o usuário. Depois de todo esse trabalho, eu crio uma nova sessão, pego todos os usuários e imprimo — o que, claro, depois disso fica uma lista vazia porque apaguei o único usuário que criei. Em termos de fluxo: depois de tudo isso ter sido feito, a instrução `with` é finalizada, então a sessão é confirmada, e então ela cria uma nova sessão para realmente imprimir os usuários.

## Demonstração de rollback

Vamos ver o que acontece se quebrarmos isso. Digamos que colocamos um erro de valor (`ValueError`). O que vai acontecer é que essas coisas — as atualizações e as criações — serão revertidas. Então criou o usuário, mas estamos revertendo. No final, o que vamos imprimir ainda é uma lista vazia porque a criação do usuário foi revertida, já que esta unidade específica em que estávamos trabalhando aqui gerou um erro.

Isso acontece quando eu levanto explicitamente um erro assim, mas também posso, por exemplo, errar aqui no ID (não há usuário com ID três). Se eu executar, obteremos a mesma coisa: há um erro, usuário três não encontrado, e ainda está revertendo — obtemos a lista vazia novamente no final.

O que também podemos fazer é pegar essa parte e transformá-la em uma sessão separada. Agora estou simplesmente criando um usuário. O que vai acontecer agora é que isso criará o usuário, que será confirmado no banco de dados. Em seguida, atualizará o usuário, recuperá-lo e excluí-lo em uma sessão separada. E então simplesmente listará os usuários no banco de dados. Aqui estou excluindo um usuário que não existe — isso significa que essas coisas serão revertidas, mas esta é uma sessão separada, então o usuário ainda será criado. Quando executo isso, o usuário não é encontrado, então vai reverter — realizou a atualização aqui, mas foi exatamente isso que foi revertido. No final, quando eu imprimir a lista de usuários, vou pegar o usuário com ID 1, e o nome é o nome original que foi definido nesta unidade de trabalho específica (não o nome atualizado, porque essa atualização foi revertida numa unidade de trabalho separada que falhou).

## Conclusão sobre banco de dados

A unidade de trabalho pode ser útil principalmente em operações de banco de dados, onde precisamos garantir que o banco de dados permaneça consistente. Também pode ajudar a esclarecer seu código, pois permite agrupar operações e ver o que cada uma das transações inclui, e isso pode ser útil na depuração, por exemplo.

Se você gosta desse tipo de discussão, você também pode querer se inscrever no boletim informativo gratuito do autor, em arjancodes.com, para receber notícias sobre Python e a indústria de software em geral.

## Outros domínios onde Unit of Work é útil (além de banco de dados)

Você pode pensar: ok, ótima unidade de trabalho que é útil para bancos de dados, mas, na verdade, é um padrão que você também verá em outras áreas, não apenas em bancos de dados. Em particular, em áreas onde precisamos gerir algum tipo de coisa complexa e queremos ter certeza de que ela permanece consistente.

1. **Utilitário de sincronização de arquivos (ex: Dropbox).** Se você sincronizar um arquivo grande e a conexão de rede falhar, você deseja reverter o upload para que o armazenamento em nuvem não contenha algum tipo de arquivo corrompido.

2. **Jogos.** Se precisar salvar um estado de jogo complexo com todos os tipos de configurações e coisas, e se houver um problema ao salvar aspectos específicos do jogo, você pode reverter e desfazer tudo o que já salvou.

3. **Infraestrutura como código, para provisionar recursos de nuvem.** Se você quiser lançar algum tipo de serviço que consiste em um banco de dados, vários servidores, armazenamento etc., e no meio do provisionamento de todos os recursos houver algum tipo de erro, você deseja reverter e desfazer a criação de todos os outros recursos da nuvem para não pagar por coisas que não está usando. Portanto, confirmar e reverter unidades de trabalho também é muito comum em infraestrutura como código.

## Encerramento

Espero que este vídeo tenha ajudado você a entender o que realmente são unidades de trabalho. Você provavelmente não precisa implementar isso sozinho, mas é bom saber que ele existe e que, se estiver usando SQLAlchemy, você pode usar `commit` e `rollback` para garantir que seus dados permaneçam consistentes.

Pergunta para os comentários: você já usou o padrão de unidade de trabalho ao interagir com seu banco de dados? Você está contando com a capacidade de confirmar e reverter as alterações em algumas das coisas que você faz? Ou você tem ideia de outras áreas ou domínios onde o padrão de unidade de trabalho pode ser útil além dos já mencionados?

(Nota: SQLAlchemy é citado como tendo muitos recursos, com indicação de vídeo seguinte sobre o tema — sem relevância técnica adicional para esta transcrição.)
