# Vertical Slice — Organizando o código por funcionalidade, não por camada (Bernardo Lobato)

> **Origem:** transcrição de vídeo em português (YouTube) de Bernardo Lobato sobre o padrão Vertical Slice, colada pelo usuário em 2026-10-01. Já estava em português (sem tradução). Texto limpo, pontuado e dividido em seções; o conteúdo foi preservado. Foram omitidos apenas os pedidos de like/inscrição/compartilhamento, a chamada para comentários e um ruído de legenda no fim (caracteres tailandeses).
>
> **Correções de reconhecimento de fala (por contexto):** "architecture syncle" → *Architecture Sinkhole*; "vertical sliss" / "slides" / "slando" → *slice* / *slices* / "chamando"; "fites" → *features*; "repositores" → *repositories*; "tech" (fim do vídeo) → provavelmente "tech lead"; "fatias horizontais" / "camadas verticais" mantidos como ditos (o autor inverte a nomenclatura usual: ver nota abaixo); "ela" em "camada específica" → "aquela". **Nota:** o autor diz que, em camadas, "separamos em camadas verticais" e no Vertical Slice em "fatias horizontais"; a terminologia corrente é o oposto (camadas = cortes horizontais, slices = cortes verticais). Preservado como dito.

## Abertura

Você já sentiu que, para fazer uma mudança mínima no código, precisava mexer em uma infinidade de arquivos, em um monte de pastas que você nem sabe direito para que servem? Já viu que o projeto tem muitas camadas inúteis e que o request só passa de camada em camada, sem lógica acoplada àquela camada específica? O vídeo apresenta um padrão que pode mudar a forma de organizar o código: o **Vertical Slice**, para quem busca mais clareza, foco e isolamento de funcionalidades.

Olá, devs, eu sou Bernardo Lobato. O padrão propõe uma organização um pouco diferente da que estamos acostumados.

## Ponto de partida: o padrão em camadas

O ponto de partida é um projeto organizado no padrão em camadas tradicional (há um vídeo detalhado do canal sobre ele). Resumidamente, nesse modelo os módulos são separados por **camadas de responsabilidades técnicas** — controllers, services, repositories, acesso a dados e o que mais for preciso. Isso força a navegar por múltiplos arquivos ou pastas para entender ou alterar uma única funcionalidade, o que, como visto no vídeo sobre o padrão em camadas, constitui o antipadrão chamado **Architecture Sinkhole**: um request vai passando de camada em camada dentro da aplicação, sem necessariamente haver lógica acoplada a ela, simplesmente porque é preciso seguir o padrão e manter as camadas fechadas.

## A ideia do Vertical Slice

No Vertical Slice, em vez de separar a aplicação em camadas, separamos em **fatias**, e cada fatia representa uma **funcionalidade** do sistema, configurável da maneira mais adequada ao projeto. A separação é **por intenção, por funcionalidade**.

Exemplo com duas funcionalidades atreladas ao mesmo conjunto de classes e entidades: a **autenticação** de um usuário e a **gestão do perfil** desse usuário. Cada uma é uma slice, e cada uma trabalha com as classes e entidades necessárias para funcionar por completo e isoladamente.

Uma slice representa uma funcionalidade completa do sistema e tudo o que está atrelado a ela: controller, validação, domínio, regras de negócio, acesso a dados e o que mais for preciso. A distinção importante frente a outros padrões: o foco é a **separação por negócio e não por tecnologia**. Isso muda como criamos e configuramos o projeto, os diretórios e a organização do código, e traz mudanças de paradigma em relação ao que se aprende desde o início da jornada como desenvolvedor.

## O domínio centralizado e seus efeitos colaterais

Um exemplo importante: a camada de domínio. Desde o paradigma orientado a objetos temos como padrão um **modelo de domínio centralizado**: uma camada de domínio que funciona para a aplicação inteira, de modo que diversos casos de uso aproveitam a mesma classe.

*Disclaimer do autor:* o exemplo é uma simplificação grosseira de modelos do mundo real, para facilitar a didática; não levar ao pé da letra.

Imagine que a classe `Usuário` é a mesma usada para autenticar e para alterar o perfil. Ela deve comportar propriedades e métodos das duas funcionalidades: `username` e `password`, mas também nome, endereço, redes sociais etc., e toda a lógica da gestão de perfil. Agora imagine uma alteração na gestão de perfil — um campo novo, um e-mail secundário, mais de um telefone. Ao fazê-la, corre-se o risco de causar **efeito colateral no módulo de autenticação**, porque ambos compartilham a mesma estrutura de usuário: há **autoacoplamento** entre os dois módulos.

Agora some outras funcionalidades — gestão de pessoas físicas, de seguidores, de produtos, de entregas — cada uma com um usuário associado (quem criou, quem alterou por último, quem está atrelado). O domínio de usuário passa a lidar com todas essas funcionalidades e **infla**. Cada alteração em qualquer módulo pode ter efeito colateral em outros sem relação com o que está sendo alterado. Isso impacta como as alterações são implementadas e exige boa cobertura de testes automatizados para garantir que mudar o módulo A não quebre B, C, D ou E.

Outro ponto que o autor viu acontecer várias vezes: **mais de uma equipe** trabalhando no mesmo projeto, em funcionalidades diferentes, acaba alterando os mesmos arquivos, serviços e classes de domínio ao mesmo tempo — conflitos, retrabalho e quebra de funcionalidades que funcionavam.

## Abrindo a mente: não precisamos de um único `Usuário`

> "Não precisamos de um único domínio representando a classe de usuário no nosso sistema."

Com cada slice representando uma funcionalidade, cada uma pode ter **a sua própria representação** do objeto de usuário, conforme os campos que aquela feature manipula durante a execução. Assim usa-se a estrutura de usuário sem causar efeito colateral negativo nas outras funcionalidades.

Consequência: **cada vertical slice pode seguir o seu próprio padrão de arquitetura**, o que melhor atender ao escopo ou à eficácia daquela funcionalidade.

No exemplo: a slice de autenticação/autorização trata só `username`, senha e dados que ajudem a autenticar (código temporário, token enviado por e-mail). A slice de gestão de perfis atualiza nome, documento, endereços, redes sociais. Nela há outra classe que também representa os dados de usuário, diferente da usada no login. Outros módulos que referenciam o usuário seguem a mesma fórmula, mantendo as classes desacopladas; qualquer alteração de gestão de perfil fica restrita à slice correspondente.

## Benefícios

- **Alta coesão:** todo o código e as classes de uma mesma funcionalidade ficam agrupados.
- **Baixo acoplamento entre slices:** cada slice isolada é mais fácil de manter, testar e entender.
- **Alinhamento com a jornada do usuário:** a jornada fica mais aderente ao código e mais fácil de manter atualizada.
- **Testes:** normalmente o mesmo desenvolvedor ou time cuida das mesmas funcionalidades ou das mais próximas, o que facilita testes automatizados e de integração, pois só terá aquela funcionalidade em mente.

## A pegadinha: acoplamento entre slices

Na teoria mantém-se baixo acoplamento, mas **é permitido** nesse estilo que slices chamem umas às outras, sem compartilhar código — uma slice chamando a outra **como se fosse um cliente**, como um request. Sem cuidado, o código pode ter **autoacoplamento entre slices** sem que se perceba; é preciso estar sempre de olho nessas integrações.

## Quando aplicar

- Projetos em que as features **crescem de forma orgânica** ou com muitas alterações do negócio, e se quer manter as features desacopladas.
- Projetos com **funcionalidade delicada** que exige cuidado e tratamento diferenciado — por exemplo, um módulo de cálculo complexo ou que usa algoritmo proprietário, ou que receba muitos ajustes; vale isolar.
- Quando é preciso **extrair uma funcionalidade para um serviço separado**. Exemplo: isolar toda a autenticação/autorização para adotar um serviço externo de autenticação. Cria-se a slice dentro do projeto, isola-se o comportamento; depois de comprovar o isolamento completo por uso e testes automatizados, recria-se como serviço externo isolado.

## Passo a passo para aplicar em projeto existente

Primeiro, criar uma **pasta específica por funcionalidade**. Dentro dela, tudo que for necessário para a execução completa: o handler ou controller da ação, a validação de entrada, a lógica de negócio, o acesso a dados, o consumo de mensageria etc. Cuidado para não criar dependências em partes que já estão bem organizadas.

## Limites e cuidados

- **Não é bala de prata.** Um dos grandes desafios é lidar com o acoplamento entre slices: apesar de isoladas e independentes, é preciso cuidado na forma como se implementa a interação entre elas, para não criar acoplamento excessivo.
- **Exige disciplina** para manter as slices isoladas, principalmente quando há domínios que representam a mesma entidade espalhados por funcionalidades diferentes. O autor já presenciou mais de uma vez um desenvolvedor novo, que não conhecia o padrão, tentar **unificar todos esses modelos numa classe centralizada**, como já tinha feito em outros projetos. Por isso é essencial acompanhamento rigoroso de cada nova implementação.
- **Nem todo projeto precisa seguir esse modelo**, e mesmo os que seguem não precisam aplicá-lo em todas as funcionalidades: é possível **mesclar** esse e outros estilos arquiteturais no mesmo projeto. É preciso discernimento para identificar a necessidade e aplicar conforme o caso.

## Fechamento

Vertical Slice é um estilo arquitetural que favorece a **organização por funcionalidade e não por tecnologia**, para times e projetos que queiram escalar com clareza e independência. Para quem está migrando para uma arquitetura distribuída como microsserviços, pode ser um **excelente caminho intermediário**. O autor pergunta nos comentários se o público já conhecia o padrão, se já o aplicou na prática ou se procurava algo parecido para começar a extrair uma funcionalidade.
