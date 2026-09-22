---
type: source
title: "Filosofia do Design de Software — bate-papo Eduardo Matos, Otávio Santana e Maurício Linhares"
aliases: ["podcast filosofia do design", "otavio santana mauricio linhares philosophy of software design"]
date_created: 2026-09-08
date_updated: 2026-09-08
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares.md
source_url: ""
author: "Eduardo Matos (host), Otávio Santana e Maurício Linhares (convidados)"
date_published: ""
date_ingested: 2026-09-08
source_count: 0
tags: [ousterhout, complexidade, design, tdd, ddd, api-design, comentarios, tech-debt, java, craftsmanship]
skill: tech-mentor-backend
status: stable
---

# Filosofia do Design de Software — bate-papo entre Eduardo Matos, Otávio Santana e Maurício Linhares

## TL;DR

Podcast em português onde Eduardo Matos entrevista [[wiki/entities/otavio-santana]] e [[wiki/entities/mauricio-linhares]] sobre *A Philosophy of Software Design*, de [[wiki/entities/john-ousterhout]]. É uma fonte de **discussão de segunda mão sobre o mesmo livro** já ingerido diretamente em [[wiki/sources/filosofia-do-design-de-software-livro-completo]] e [[wiki/sources/filosofia-do-design-de-software-introducao]] — não repete o conteúdo do livro, mas adiciona: (1) o vocabulário do Cap. 2 do livro (change amplification, cognitive load burden, unknown unknowns) que as duas ingestões anteriores ainda não cobriam explicitamente; (2) relatos de experiência profissional real dos dois convidados aplicando (ou discordando de) os conceitos do livro; (3) um debate direto sobre TDD que cita DHH ("TDD is dead") e distingue explicitamente arquitetura de design de código; (4) exemplos adicionais de má/boa API além dos já ingeridos (Java I/O, PHP `file_get_contents`, cliente HTTP do Go, chamadas de sistema do Unix).

## Key Claims

**Claim:** Os primeiros sinais de complexidade crescente em um sistema são (a) *change amplification* — uma mudança que parecia localizada numa classe explode em alterações de dependências desconhecidas — e (b), pelo caminho inverso, falta de documentação/onboarding lento como sintoma de que o conhecimento do sistema está mal encapsulado ou mal registrado.
**Evidence:** Maurício Linhares descreve change amplification como o sinal mais visível ao entrar numa base de código nova; Otávio Santana complementa com o tempo de onboarding e o meme "a documentação sou eu" como sintoma do problema inverso (conhecimento não espalhado/documentado).
**Confidence:** alta — mapeia diretamente para os três sintomas de complexidade do Cap. 2 do livro (change amplification, cognitive load, unknown unknowns), que nenhuma das duas fontes anteriores do livro no wiki havia nomeado explicitamente até agora.

**Claim:** Não é possível decidir de antemão, no início de um projeto, o grau ideal de modularidade — a estrutura correta emerge conforme o software evolui e o domínio é compreendido; tentar "acertar" a modularidade logo no início tende a errar para um lado ou para o outro.
**Evidence:** Otávio relata só perceber se uma classe estava assumindo responsabilidade demais (e precisava ser quebrada) *depois* de ver o software evoluir. Maurício generaliza: só ao migrar um monolito existente para microsserviços já se enxergam os bounded contexts reais; começando do zero, é normal "quebrar a cara" na primeira tentativa.
**Confidence:** média — opinião qualitativa de experiência pessoal, sem estudo citado, mas convergente com o enquadramento de "design contínuo, nunca uma fase única" do capítulo introdutório do livro (já ingerido).

**Claim:** Programação tática vs. estratégica (termos do livro, Cap. 3) é reformulada pelos convidados como um hábito concreto de time: ao aceitar uma solução tática sob pressão, criar imediatamente um card/ticket linkado no código explicando por que a solução foi feita daquele jeito e o que precisa ser revisto no futuro — em vez de deixar a dívida implícita.
**Evidence:** Maurício descreve esse hábito como sua prática pessoal para equilibrar entrega com qualidade; Otávio conecta ao conceito do livro de "tactical tornado" — o programador que entrega rápido mas deixa rastro de código intocável atrás de si — e relata um caso real de dois anos de bugs recorrentes após a saída de um dev que trabalhava isolado, sem documentar nada.
**Confidence:** alta quanto à prática relatada (relato de primeira mão de ambos); a ligação com "tactical tornado" é interpretação dos convidados, não citação literal do livro.

**Claim:** TDD como ferramenta de design de código funciona bem para os dois convidados no nível de método/classe (usar a facilidade de testar como sinal de bom design), mas nenhum dos dois concorda que teste unitário consiga guiar decisões de *arquitetura* — a arquitetura é uma camada acima do que um teste unitário enxerga.
**Evidence:** Maurício usa o teste como "primeiro usuário" do código, mas ressalva que isso funciona melhor para backend/testes unitários que para interfaces. Otávio usa linguagem ubíqua + teste para checar alinhamento com o negócio, mas hoje não pratica TDD estrito — escreve o teste, geralmente corrige um bug reproduzindo-o em teste primeiro, e usa testes majoritariamente como ferramenta de regressão. Ambos comentam a citação de DHH ("the units of development should be abstractions, not features... don't create the abstraction in pieces over time; design it all at once") e concordam parcialmente, mas insistem que ele mistura design de código (nível de método/classe, onde teste unitário atua) com arquitetura (estrutura da aplicação, fora do alcance do teste unitário).
**Confidence:** média-alta — opinião pessoal madura de dois praticantes experientes, não um estudo; converge com o Cap. 19 do livro já ingerido ("TDD é tática, não estratégica"), mas os convidados chegam à mesma desconfiança por caminho argumentativo diferente (separação design-de-código vs. arquitetura, não a crítica de Ousterhout sobre "criar abstração aos pedaços").

**Claim:** A API de I/O do Java (`java.io`) é citada como o exemplo mais didático de módulo raso: exige compor manualmente uma cadeia de decorators (`FileInputStream` → `BufferedInputStream` → `ObjectInputStream`) porque foi desenhada para maximizar opções de otimização em vez de oferecer um caminho simples para o caso comum; só ganhou um método de leitura de arquivo inteiro em bytes no Java 9, depois de duas décadas.
**Evidence:** Maurício detalha o motivo estrutural (ausência de retorno múltiplo na linguagem, forçando constantes especiais para sinalizar fim de arquivo; herança de conceitos do C); Otávio reforça que é o exemplo canônico usado até hoje pelo comitê executivo do Java como erro reconhecido de design, e nota que é ao mesmo tempo o exemplo didático mais citado do padrão Decorator (bom exemplo de padrão, péssimo exemplo de API).
**Confidence:** alta quanto ao relato histórico (Java 9/NIO2 introduziu `Files.readAllBytes`); é opinião técnica compartilhada por ambos, não citação direta do livro (o livro também usa Java I/O como exemplo — ver [[wiki/concepts/modulo-profundo]] — mas por outro ângulo, focado em classitis).

**Claim:** O antídoto ao design ruim de API não é eliminar opções avançadas, mas oferecer as duas camadas: uma interface simples e de alto nível para o caso comum (o "caminho feliz"), e acesso de baixo nível disponível para quem precisa de controle fino — sem forçar todo usuário a conhecer a camada de baixo nível. Exemplos: chamadas de sistema Unix (`open`/`read`/`write`/`lseek`/`close`) escondendo formato de sistema de arquivos e tipo de mídia; o cliente HTTP padrão do Go escondendo negociação de versão de protocolo e handshake TLS; e a função `file_get_contents` do PHP aceitando tanto caminho local quanto URL.
**Evidence:** Maurício detalha o exemplo do cliente HTTP do Go (implementa três versões do protocolo por baixo, mas expõe uma interface simples de request/response) e do PHP; Otávio complementa com a analogia do micro-ondas (usuário não precisa entender micro-ondas eletromagnéticas) e cita o "paradoxo da escolha" (atribuído a um colaborador do Spring) — excesso de opções pode atrapalhar mais que ajudar, mesmo quando cada opção é boa isoladamente.
**Confidence:** alta — mesma mecânica de "camadas" (layering) do Cap. 6 do livro, já documentada em [[wiki/concepts/modulo-profundo]] via o exemplo Unix I/O; os exemplos do Go e do PHP são complementares, não estavam na fonte já ingerida.

**Claim:** O padrão Repository (DDD) é frequentemente aplicado de forma equivocada quando os nomes dos métodos permanecem genéricos de CRUD ("inserir", "deletar", "atualizar") em vez de usar vocabulário do domínio — o objetivo do padrão é abstrair a implementação usando linguagem próxima do negócio (exemplo: um repositório de carros de uma locadora deveria se chamar "garagem", com métodos como "registrar" ou "estacionar" em vez de "inserir").
**Evidence:** Otávio cita esse erro como um dos mais recorrentes que observa em código real usando DDD.
**Confidence:** média — opinião de um praticante experiente, exemplo didático próprio, não citado de fonte primária de DDD.

**Claim:** Eliminar a possibilidade de um erro acontecer (redesenhar a semântica da operação) é preferível a lançar exceções na cara do usuário da API sempre que a entrada não bate exatamente com o esperado — uma API também é uma interface de usuário, e deveria ser tratada com o mesmo cuidado de usabilidade que uma UI.
**Evidence:** Otávio escolhe esse como o trecho mais importante do livro para todo engenheiro conhecer (equivalente ao Cap. 10, "Define Errors Out of Existence", já ingerido em [[wiki/sources/filosofia-do-design-de-software-livro-completo]]), contrastando a experiência de usar Ruby (a API tenta inferir a intenção do usuário) com APIs que lançam exceção sem necessidade; usa o exemplo de pedir um substring além do tamanho de uma string — o ideal seria retornar o que existe (como Python faz em list slices), não lançar `IndexOutOfBoundsException` (como o Java faz).
**Confidence:** alta — exemplo idêntico ao já citado na ingestão completa do livro (substring do Java vs. list slices do Python), reforçando que é um ponto central do Cap. 10, não uma leitura isolada dos convidados.

**Claim:** Comentários não são sinal de descuido — projetos de referência amplamente reconhecidos (API pública do Google, kernel Linux, JVM, Spring) usam comentários extensivamente; a crença de que "código bem escrito não precisa de comentário" é uma utopia contrariada pela prática dos melhores projetos open source.
**Evidence:** Maurício escolhe o Cap. 15 do livro (equivalente ao que a wiki já documenta em [[wiki/concepts/comentarios-como-ferramenta-de-design]]) como o mais importante, citando esses projetos como contra-exemplo prático da "utopia do código autodocumentado".
**Confidence:** média — argumento por exemplos citados de memória (sem link/verificação nesta ingestão), mas consistente com a posição de Ousterhout já documentada.

## Entidades

- [[wiki/entities/john-ousterhout]] — autor do livro discutido; nenhuma citação nova além do que já está documentado.
- [[wiki/entities/otavio-santana]] — nova entidade, engenheiro de software convidado.
- [[wiki/entities/mauricio-linhares]] — nova entidade, engenheiro de software convidado.

## Conceitos tocados

- [[wiki/concepts/modulo-profundo]] — exemplo adicional do `java.io` como módulo raso, com detalhe de motivo estrutural (ausência de retorno múltiplo no Java).
- [[wiki/concepts/red-flags-de-design]] — reforço do red flag Shallow Module via novo exemplo.
- [[wiki/concepts/ocultamento-de-informacao]] — change amplification como sintoma-irmão de information leakage (mesmo capítulo 2 do livro).
- [[wiki/concepts/tech-debt-como-ferramenta]] — hábito prático de linkar ticket ao código tático no momento da entrega.
- [[wiki/concepts/comentarios-como-ferramenta-de-design]] — reforço do Cap. 15 com exemplos de projetos open source que comentam extensivamente.
- [[wiki/concepts/tdd]] — debate sobre TDD guiar design de código vs. arquitetura; citação de DHH.
- [[wiki/concepts/ddd]] — crítica ao uso raso do Repository (nomes CRUD genéricos em vez de vocabulário de domínio).
- [[wiki/concepts/repository-pattern]] — mesmo ponto, do lado do padrão em si.
- [[wiki/concepts/decorator-pattern]] — `java.io` como exemplo simultâneo de "bom padrão, péssima API".
- [[wiki/concepts/define-errors-out-of-existence]] — novo conceito, extraído do Cap. 10 do livro, agora com página própria.
- [[wiki/concepts/sintomas-de-complexidade-ousterhout]] — novo conceito, os três sintomas do Cap. 2 (change amplification, cognitive load burden, unknown unknowns).

## Open Questions

- A fonte não identifica o nome completo/sobrenome do colaborador do Spring citado por Otávio como origem do termo "paradoxo da escolha" aplicado a design de API ("Oliver [sobrenome não lembrado na fala]") — não verificável sem fonte adicional.
- Não há tradução publicada do livro para português confirmada nesta fonte nem nas anteriores; os três participantes reforçam isso no início da conversa.
- A fonte não detalha se os convidados usam alguma ferramenta ou processo formal (além do hábito pessoal de ticket linkado) para rastrear decisões de programação tática — fica registrado como prática individual, não de time/organização.

## Citações preservadas

> "Change amplification: você imaginar essa mudança é uma mudança que na sua cabeça ela é logicamente localizada em um pedaço do código, e quando você vai fazer essa mudança você descobre que agora, em vez de eu ter que mudar somente essa classe, eu tenho que mudar essas outras 10 classes que eu não sabia que estavam relacionadas." — Maurício Linhares

> "Entrega [...] mas eu boto o cardzinho lá no Jira dizendo: 'isso aqui a gente precisa rever porque isso aqui vai virar um problema no futuro'." — Maurício Linhares

> "O grande problema da API do Java é que, em vez de construir uma API fácil das pessoas usarem, eles pensaram: vamos construir uma API fácil das pessoas otimizarem." — Maurício Linhares

> "A resposta padrão de DDD é uma das coisas que eu mais vejo como nós erramos miseravelmente: a galera coloca 'inserir', 'deletar', 'atualizar' [...] o conceito é justamente o contrário — é abstrair implementação. [...] o meu repositório de carro deveria ser uma garagem, e ao invés de 'inserir' seria 'registrar' ou 'estacionar'." — Otávio Santana

> "Se a string só tem 10 caracteres e o cara pediu do 5 ao 11, o que é que você faz? Você traz do 5 ao 10. Não precisa lançar um erro na cara da pessoa por causa disso." — Otávio Santana

## Key Sources

Nenhuma — esta é a fonte primária desta ingestão.
