# Os 3 Estágios de Maturidade Para Testar Código

Transcrição de vídeo em português, reescrita como Markdown estruturado por seções. Sem necessidade de tradução (fonte já em português).

## Introdução

Existe uma única coisa no fluxo de trabalho do autor que repetidamente se prova ser o que mais traz velocidade na hora de programar, mais segurança na hora de modificar código (por mais grosseira que seja a modificação), e um valor intrínseco muito maior em comparação com quem não faz isso. É, para o autor, a única forma que ele consegue programar hoje, e o que faz ele "domar" qualquer projeto sério. Ele não consegue mais voltar a programar como antes — dá ansiedade só de pensar em como era programar no passado, e em como ainda existem pessoas nesse estágio.

Para situar todo mundo, o autor descreve os três estágios de maturidade que ele pessoalmente passou na área de programação:

1. **Iniciante** — não sabia para onde correr.
2. **Intermediário** — achava que estava mandando bem, mas não estava.
3. **Experiente** — a forma mais madura de se programar algo sério.

## Estágio 1 — Iniciante (Filipe Deschamps, 2014, ~8 anos atrás)

Programando sistemas web em Angular (ou qualquer outra biblioteca/framework), toda vez que precisava testar alguma funcionalidade, o autor usava a própria interface do sistema para repetir sempre a mesma ação manualmente e observar o resultado.

Fluxo de trabalho:
- Tentava uma coisa; se não se comportava como esperado, investigava.
- Mudava algo no back-end, voltava para o front-end, repetia a exata mesma ação.
- Se o resultado mudasse (mesmo que não funcionasse ainda), ficava feliz — sinal de progresso.
- De tentativa em tentativa, revisava mentalmente todo o fluxo do código, anotava com logs, e navegava constantemente entre front-end e back-end até chegar ao resultado esperado.

**O problema, invisível na hora:** cada avanço era, na verdade, avanço para um problema pior. A cada passo dado na evolução do sistema, menos mobilidade ele tinha dentro do código — o sistema parecia ficar exponencialmente mais difícil de mexer. Mudar algo de um lado quebrava algo do outro lado. O ciclo constante de ida e volta entre front-end e back-end tomava muito tempo e confundia a cabeça. Muitas vezes ele queria fazer alterações isoladas no back-end, sem nenhuma relação com o front-end, mas precisava usar o front-end mesmo assim — porque essa era a única forma de "cutucar" e rodar o código.

## Estágio 2 — Intermediário (Pagar.me — "achava que estava mandando bem, mas não estava")

O tempo passou e o autor foi contratado para trabalhar no Pagar.me, um dos maiores meios de pagamento do Brasil. Aí ele "ficou exibido" e virou um intermediário que achava que estava mandando bem, mas não estava.

### Dogfooding como cultura

O Pagar.me era muito forte em **dogfooding** ("dog food"/"dog furin"): usar as próprias soluções no dia a dia. A mesma API fornecida para os clientes construírem suas próprias soluções era a mesma API que o Pagar.me usava internamente para construir, por exemplo, a própria dashboard oferecida aos clientes.

Ou seja: não importa se existe uma interface — o mais importante é disponibilizar uma API (no caso do Pagar.me, uma API REST). Isso força a pensar de forma completamente separada entre front-end e back-end, ou melhor: entre **cliente e servidor**, onde o servidor não conhece o cliente.

Isso é ótimo porque, para um mesmo servidor, é possível criar e conectar inúmeros clientes — uma interface web (a dashboard), um aplicativo mobile, ou soluções populares como o **Postman**.

### Postman como cliente HTTP especializado

O Postman é só mais um cliente HTTP, como qualquer outro citado — um "terminal" de frente para o usuário que sabe se comunicar com um back-end, só que especializado nisso. Com ele:

- Não era mais preciso clicar numa "página web maluca" para rodar coisas no back-end — dava para fazer tudo direto pela interface do Postman.
- Todos os endpoints da API ficavam organizados e pré-configurados.
- Era possível injetar variáveis em qualquer lugar (ex.: host da API, chaves secretas), e os valores mudavam automaticamente conforme o ambiente selecionado.
- Ficava muito mais fácil "cutucar" diretamente o back-end, ver o que acontecia e o que voltava.

Soluções equivalentes ficaram populares nos anos seguintes, incluindo as embutidas no próprio VS Code, como o Thunder Client — virtualmente a mesma coisa que o Postman.

### O problema recorrente: escala

Todas essas soluções (Postman, Thunder Client, etc.) têm um grande problema em comum, que é o motivo de existir um terceiro estágio. É extremamente recorrente que, ao adicionar funcionalidades a um sistema, uma funcionalidade comece a afetar outra. Isso é gerenciável (e os bugs são previsíveis) num sistema pequeno com duas funcionalidades. Mas nada é óbvio quando o sistema tem, digamos, 200 funcionalidades e um número imenso de combinações possíveis de propriedades e parâmetros.

Numa abordagem manual via Postman, para ter o máximo de certeza de que nada quebrou após uma alteração, seria preciso testar manualmente cada endpoint e cada combinação de parâmetro, verificando se algo retorna resultado inesperado. Isso **não escala**.

O próprio Postman, ao longo do seu desenvolvimento, incorporou uma feature para escrever testes automatizados por dentro dele — útil inclusive para monitoramento. Mas a forma que hoje mais dá performance e segurança ao autor é usar testes automatizados com a "cereja do bolo": o **modo watch**.

## Estágio 3 — Experiente: Testes Automatizados em Modo Watch

Demonstração prática, feita dentro do VS Code com a tela dividida: à esquerda, o código de teste automatizado; à direita, o Jest rodando em **modo watch** para aquele arquivo. Qualquer alteração salva no arquivo de teste (até mesmo um `console.log`) é percebida automaticamente pelo Jest, que roda o teste de novo sozinho.

O exemplo usado é a rota de migrations do banco de dados de um projeto (TabNews), que retorna as migrations ainda não rodadas. Essa é uma rota extremamente sensível, e não deveria estar acessível para qualquer pessoa.

### Passo a passo do fluxo de trabalho

1. **A relação cliente/servidor se mantém.** O teste usa um cliente chamado `fetch`, que aceita uma URL — igual ao Postman — e por padrão faz um `GET`, retornando um objeto de resposta com tudo o que aconteceu na requisição.
2. O resultado é salvo numa constante; como o objeto tem muita informação, extrai-se só o `response.body` em formato JSON.
3. Ao dar um `console.log` nesse valor, aparece exatamente o mesmo resultado que vinha do Postman: um `array` com as migrations ainda não rodadas.
4. **Primeira virada de chave**: como agora o resultado está dentro de código, é possível criar **expectativas** sobre esse resultado. Ex.: esperar que `response.status` seja igual a um valor específico. Ao salvar, o Jest roda os testes automaticamente e confirma que passaram.
5. Só que esse endpoint é sensível e **não deveria** retornar `200` para usuários anônimos — deveria retornar `403`, informando que o usuário não tem permissão. Ao mudar a expectativa para `403`, o teste **quebra**: era esperado `403`, mas veio `200`.

A expectativa está certa — o acesso deveria ser negado para um usuário anônimo. Quem está errado é o código, que está retornando `200` e mandando os dados para qualquer um.

### Corrigindo o problema no mesmo fluxo

- No Controller responsável, o handler do `GET` está "completamente pelado" — não passa por nenhum fluxo de autorização.
- Correção: importar uma abstração do projeto que controla autorizações e injetar um middleware antes do handler do `GET`. Esse middleware aguarda uma *feature* (uma credencial) que o usuário precisa ter; se a checagem falhar, a requisição é automaticamente rejeitada com `403`.
- Ao salvar, o teste passa: o endpoint agora retorna `403` para a requisição anônima.
- As expectativas podem ir além: um `console.log` no `body` da resposta mostra um objeto com o erro. Nova expectativa é adicionada — a propriedade `name` deve vir exatamente com o valor `"ForbiddenError"`. Ambas as expectativas continuam sendo atendidas.

Rapidamente, e de graça, o fluxo produziu um **teste automatizado** que garante que esse comportamento se mantenha daqui para frente.

### Segunda virada de chave: teste automatizado como rede de segurança contra regressão

Se, meses depois, alguém — atendendo a algum outro requisito mal pensado, em outro canto totalmente diferente do código — libera essa rota para qualquer pessoa, o teste vai apontar que algo está errado.

Demonstração: abrindo o Model do usuário, que define o que um usuário anônimo pode fazer, o autor adiciona **por engano** uma permissão de leitura nas migrations. Ao salvar esse código — sem mexer em nenhum outro lugar — o teste de antes reclama: esperava `403` (acesso proibido), mas agora está vindo `200`. Isso está errado, e o teste automatizado pegou a regressão instantaneamente, sem qualquer ação manual de verificação.

## Recomendação de curso

Para quem quiser se tornar profissional no assunto de testes, o curso mais completo que o autor encontrou até agora é o do **Fábio Vedovelle** (nome citado foneticamente na transcrição original, grafia não confirmada) — cobre desde o básico até testar e garantir uma API como a demonstrada aqui, de forma mais completa, incluindo o front-end. Cupom de desconto mencionado na descrição do vídeo original (não reproduzido aqui).

## Fechamento

"Tá fechado, valeu."
