---
title: "RFC 7636 — Proof Key for Code Exchange by OAuth Public Clients"
source_url: https://datatracker.ietf.org/doc/html/rfc7636
original_language: en
translated: true
authors: [N. Sakimura (Nomura Research Institute), J. Bradley (Ping Identity), N. Agarwal (Google)]
published: 2015-09
category: Standards Track
ietf_stream: IETF
issn: "2070-1721"
---

# RFC 7636 — Proof Key for Code Exchange by OAuth Public Clients

> Tradução técnica (PT-BR) do texto normativo original em inglês. Fonte: https://datatracker.ietf.org/doc/html/rfc7636 (texto oficial: https://www.rfc-editor.org/rfc/rfc7636.txt). Estrutura de seções preservada para fidelidade ao documento original.

**Internet Engineering Task Force (IETF)** — N. Sakimura, Ed. (Nomura Research Institute)
**Request for Comments:** 7636
**Categoria:** Standards Track — J. Bradley (Ping Identity)
**ISSN:** 2070-1721 — N. Agarwal (Google)
**Data:** setembro de 2015

## Resumo

Clientes públicos OAuth 2.0 que utilizam o Authorization Code Grant são suscetíveis ao ataque de interceptação de código de autorização (*authorization code interception attack*). Esta especificação descreve o ataque, bem como uma técnica para mitigar essa ameaça através do uso do **Proof Key for Code Exchange** (PKCE, pronunciado "pixy").

## Status deste memorando

Este é um documento do tipo Internet Standards Track. É produto do Internet Engineering Task Force (IETF), representa o consenso da comunidade IETF, recebeu revisão pública e foi aprovado para publicação pelo Internet Engineering Steering Group (IESG). Mais informações sobre Internet Standards estão disponíveis na Seção 2 da RFC 5741. Informações sobre o status atual deste documento, erratas e como enviar feedback podem ser obtidas em http://www.rfc-editor.org/info/rfc7636.

## Aviso de copyright

Copyright (c) 2015 IETF Trust e as pessoas identificadas como autores do documento. Todos os direitos reservados. Este documento está sujeito ao BCP 78 e às Provisões Legais do IETF Trust relacionadas a documentos IETF (http://trustee.ietf.org/license-info), em vigor na data de publicação deste documento. Componentes de código extraídos deste documento devem incluir o texto da Licença BSD Simplificada, conforme descrito na Seção 4.e das Provisões Legais do Trust, e são fornecidos sem garantia, conforme descrito na Licença BSD Simplificada.

## Índice

1. Introdução
   1.1. Fluxo do Protocolo
2. Convenções Notacionais
3. Terminologia
   3.1. Abreviações
4. Protocolo
   4.1. Cliente cria um Code Verifier
   4.2. Cliente cria o Code Challenge
   4.3. Cliente envia o Code Challenge com a Authorization Request
   4.4. Servidor retorna o código
      4.4.1. Resposta de erro
   4.5. Cliente envia o Authorization Code e o Code Verifier ao Token Endpoint
   4.6. Servidor verifica o code_verifier antes de retornar os tokens
5. Compatibilidade
6. Considerações de IANA
   6.1. Registro de Parâmetros OAuth
   6.2. Registro de Métodos de Code Challenge do PKCE
      6.2.1. Template de Registro
      6.2.2. Conteúdo Inicial do Registro
7. Considerações de Segurança
   7.1. Entropia do code_verifier
   7.2. Proteção contra escutas (eavesdroppers)
   7.3. Salting do code_challenge
   7.4. Considerações de Segurança do OAuth
   7.5. Considerações de Segurança do TLS
8. Referências
   8.1. Referências Normativas
   8.2. Referências Informativas
Apêndice A. Notas sobre implementação de Base64url Encoding sem padding
Apêndice B. Exemplo para o método code_challenge S256
Agradecimentos
Endereços dos Autores

## 1. Introdução

Clientes públicos OAuth 2.0 [RFC6749] são suscetíveis ao ataque de interceptação de código de autorização.

Nesse ataque, o atacante intercepta o código de autorização retornado pelo authorization endpoint em um caminho de comunicação não protegido por TLS (Transport Layer Security), como a comunicação entre aplicações dentro do sistema operacional do cliente.

Uma vez que o atacante obtém acesso ao código de autorização, ele pode usá-lo para obter o access token.

A Figura 1 mostra o ataque graficamente. No passo (1), a aplicação nativa rodando no dispositivo final (por exemplo, um smartphone) emite uma OAuth 2.0 Authorization Request via browser/sistema operacional. A Redirection Endpoint URI, nesse caso, tipicamente usa um custom URI scheme. O passo (1) ocorre por uma API segura que não pode ser interceptada, embora possa potencialmente ser observada em cenários de ataque mais avançados. A requisição é então encaminhada ao authorization server OAuth 2.0 no passo (2). Como o OAuth exige o uso de TLS, essa comunicação é protegida por TLS e não pode ser interceptada. O authorization server retorna o código de autorização no passo (3). No passo (4), o Authorization Code é devolvido ao solicitante via a Redirection Endpoint URI fornecida no passo (1).

Note que é possível que um app malicioso se registre como handler do mesmo custom scheme usado pelo app OAuth 2.0 legítimo. Uma vez feito isso, o app malicioso passa a conseguir interceptar o código de autorização no passo (4). Isso permite ao atacante solicitar e obter um access token nos passos (5) e (6), respectivamente.

```
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    | End Device (e.g., Smartphone)  |
    |                                |
    | +-------------+   +----------+ | (6) Access Token  +----------+
    | |Legitimate   |   | Malicious|<--------------------|          |
    | |OAuth 2.0 App|   | App      |-------------------->|          |
    | +-------------+   +----------+ | (5) Authorization |          |
    |        |    ^          ^       |        Grant      |          |
    |        |     \         |       |                   |          |
    |        |      \   (4)  |       |                   |          |
    |    (1) |       \  Authz|       |                   |          |
    |   Authz|        \ Code |       |                   |  Authz   |
    | Request|         \     |       |                   |  Server  |
    |        |          \    |       |                   |          |
    |        |           \   |       |                   |          |
    |        v            \  |       |                   |          |
    | +----------------------------+ |                   |          |
    | |                            | | (3) Authz Code    |          |
    | |     Operating System/      |<--------------------|          |
    | |         Browser            |-------------------->|          |
    | |                            | | (2) Authz Request |          |
    | +----------------------------+ |                   +----------+
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+

           Figura 1: Ataque de Interceptação de Código de Autorização
```

Diversas pré-condições precisam se sustentar para que esse ataque funcione:

1. O atacante consegue registrar uma aplicação maliciosa no dispositivo do cliente e registra um custom URI scheme que também é usado por outra aplicação. O sistema operacional precisa permitir que um custom URI scheme seja registrado por múltiplas aplicações.

2. O OAuth 2.0 authorization code grant é usado.

3. O atacante tem acesso ao `client_id` e ao `client_secret` (se provisionado) do OAuth 2.0 [RFC6749]. Todas as instâncias de app nativo OAuth 2.0 usam o mesmo `client_id`. Secrets provisionados em aplicações binárias de cliente não podem ser considerados confidenciais.

4. Uma das seguintes condições é atendida:

   **4a.** O atacante (via a aplicação instalada) consegue observar apenas as respostas do authorization endpoint. Quando o valor de `code_challenge_method` é `plain`, apenas esse ataque é mitigado.

   **4b.** Um cenário de ataque mais sofisticado permite ao atacante observar requisições (além das respostas) ao authorization endpoint. O atacante, no entanto, não consegue atuar como man-in-the-middle. Isso foi causado por vazamento de informação de log HTTP no SO. Para mitigar esse caso, o valor de `code_challenge_method` deve ser definido como `S256` ou um valor definido por uma extensão de `code_challenge_method` criptograficamente segura.

Embora essa seja uma longa lista de pré-condições, o ataque descrito já foi observado em ambientes reais e precisa ser considerado em implantações OAuth 2.0. Embora o modelo de ameaças do OAuth 2.0 (Seção 4.4.1 da [RFC6819]) descreva técnicas de mitigação, elas infelizmente não são aplicáveis, pois dependem de um secret por instância de cliente ou de uma redirect URI por instância de cliente.

Para mitigar esse ataque, esta extensão utiliza uma chave criptograficamente aleatória, criada dinamicamente, chamada **code verifier**. Um code verifier único é criado para cada requisição de autorização, e seu valor transformado, chamado **code challenge**, é enviado ao authorization server para obter o código de autorização. O código de autorização obtido é então enviado ao token endpoint junto com o **code verifier**, e o servidor o compara com o código previamente recebido na requisição, de forma a realizar a prova de posse (*proof of possession*) do code verifier pelo cliente. Isso funciona como mitigação, pois o atacante não conheceria essa chave de uso único, já que ela é enviada via TLS e não pode ser interceptada.

### 1.1. Fluxo do Protocolo

```
                                                 +-------------------+
                                                 |   Authz Server    |
       +--------+                                | +---------------+ |
       |        |--(A)- Authorization Request ---->|               | |
       |        |       + t(code_verifier), t_m  | | Authorization | |
       |        |                                | |    Endpoint   | |
       |        |<-(B)---- Authorization Code -----|               | |
       |        |                                | +---------------+ |
       | Client |                                |                   |
       |        |                                | +---------------+ |
       |        |--(C)-- Access Token Request ---->|               | |
       |        |          + code_verifier       | |    Token      | |
       |        |                                | |   Endpoint    | |
       |        |<-(D)------ Access Token ---------|               | |
       +--------+                                | +---------------+ |
                                                 +-------------------+

                     Figura 2: Fluxo Abstrato do Protocolo
```

Esta especificação adiciona parâmetros extras às Authorization Requests e Access Token Requests do OAuth 2.0, mostrados de forma abstrata na Figura 2.

**A.** O cliente cria e registra um segredo chamado `code_verifier` e deriva uma versão transformada `t(code_verifier)` (referida como `code_challenge`), enviada na OAuth 2.0 Authorization Request junto com o método de transformação `t_m`.

**B.** O Authorization Endpoint responde normalmente, mas registra `t(code_verifier)` e o método de transformação.

**C.** O cliente então envia o código de autorização na Access Token Request como de costume, mas inclui o segredo `code_verifier` gerado em (A).

**D.** O authorization server transforma o `code_verifier` e o compara com `t(code_verifier)` de (B). O acesso é negado se não forem iguais.

Um atacante que intercepta o código de autorização em (B) não consegue trocá-lo por um access token, pois não está de posse do segredo `code_verifier`.

## 2. Convenções Notacionais

As palavras-chave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY" e "OPTIONAL" neste documento devem ser interpretadas conforme descrito em "Key words for use in RFCs to Indicate Requirement Levels" [RFC2119]. Quando usadas sem estar em maiúsculas, devem ser interpretadas com seu significado em linguagem natural.

Esta especificação usa a notação Augmented Backus-Naur Form (ABNF) da [RFC5234].

- `STRING` denota uma sequência de zero ou mais caracteres ASCII [RFC20].
- `OCTETS` denota uma sequência de zero ou mais octetos.
- `ASCII(STRING)` denota os octetos da representação ASCII [RFC20] de `STRING`.
- `BASE64URL-ENCODE(OCTETS)` denota a codificação base64url de `OCTETS`, conforme o Apêndice A, produzindo uma `STRING`.
- `BASE64URL-DECODE(STRING)` denota a decodificação base64url de `STRING`, conforme o Apêndice A, produzindo uma sequência de octetos.
- `SHA256(OCTETS)` denota um hash SHA2 de 256 bits [RFC6234] de `OCTETS`.

## 3. Terminologia

Além dos termos definidos no OAuth 2.0 [RFC6749], esta especificação define os seguintes termos:

**code verifier**
Uma string criptograficamente aleatória usada para correlacionar a authorization request com a token request.

**code challenge**
Um desafio derivado do code verifier, enviado na authorization request, para ser verificado posteriormente.

**code challenge method**
O método usado para derivar o code challenge.

**Base64url Encoding**
Codificação Base64 usando o conjunto de caracteres seguro para URL e nome de arquivo definido na Seção 5 da [RFC4648], com todos os caracteres `=` finais omitidos (conforme permitido pela Seção 3.2 da [RFC4648]) e sem a inclusão de quebras de linha, espaços em branco ou caracteres adicionais. (Veja o Apêndice A para notas sobre implementação de base64url encoding sem padding.)

### 3.1. Abreviações

| Sigla | Significado |
|---|---|
| ABNF | Augmented Backus-Naur Form |
| Authz | Authorization |
| PKCE | Proof Key for Code Exchange |
| MITM | Man-in-the-middle |
| MTI | Mandatory To Implement |

## 4. Protocolo

### 4.1. Cliente cria um Code Verifier

O cliente primeiro cria um code verifier, `code_verifier`, para cada OAuth 2.0 Authorization Request [RFC6749], da seguinte forma:

`code_verifier` = STRING aleatória de alta entropia criptográfica, usando os caracteres não-reservados `[A-Z] / [a-z] / [0-9] / "-" / "." / "_" / "~"` da Seção 2.3 da [RFC3986], com comprimento mínimo de 43 caracteres e máximo de 128 caracteres.

ABNF de `code_verifier`:

```
code-verifier = 43*128unreserved
unreserved = ALPHA / DIGIT / "-" / "." / "_" / "~"
ALPHA = %x41-5A / %x61-7A
DIGIT = %x30-39
```

**NOTA:** O code verifier DEVERIA (`SHOULD`) ter entropia suficiente para tornar impraticável adivinhar seu valor. É RECOMENDADO que a saída de um gerador de números aleatórios adequado seja usada para criar uma sequência de 32 octetos. Essa sequência é então codificada em base64url para produzir uma string URL-safe de 43 octetos, usada como code verifier.

### 4.2. Cliente cria o Code Challenge

O cliente então cria um code challenge derivado do code verifier, usando uma das seguintes transformações:

**plain**
```
code_challenge = code_verifier
```

**S256**
```
code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))
```

Se o cliente for capaz de usar `S256`, ele DEVE (`MUST`) usar `S256`, já que `S256` é de implementação obrigatória (Mandatory To Implement — MTI) no servidor. Clientes só têm permissão de usar `plain` se não puderem suportar `S256` por alguma razão técnica e souberem, via configuração fora de banda (out-of-band), que o servidor suporta `plain`.

A transformação `plain` existe para compatibilidade com implantações existentes e para ambientes restritos que não conseguem usar a transformação S256.

ABNF de `code_challenge`:

```
code-challenge = 43*128unreserved
unreserved = ALPHA / DIGIT / "-" / "." / "_" / "~"
ALPHA = %x41-5A / %x61-7A
DIGIT = %x30-39
```

### 4.3. Cliente envia o Code Challenge com a Authorization Request

O cliente envia o code challenge como parte da OAuth 2.0 Authorization Request (Seção 4.1.1 da [RFC6749]), usando os seguintes parâmetros adicionais:

**code_challenge**
REQUIRED (obrigatório). Code challenge.

**code_challenge_method**
OPTIONAL (opcional), padrão `plain` se ausente na requisição. Método de transformação do code verifier: `S256` ou `plain`.

### 4.4. Servidor retorna o código

Quando o servidor emite o código de autorização na resposta de autorização, ele DEVE (`MUST`) associar os valores de `code_challenge` e `code_challenge_method` ao código de autorização, para que possam ser verificados posteriormente.

Tipicamente, os valores de `code_challenge` e `code_challenge_method` são armazenados de forma criptografada dentro do próprio `code`, mas alternativamente podem ser armazenados no servidor, associados ao código. O servidor NÃO DEVE (`MUST NOT`) incluir o valor de `code_challenge` nas requisições do cliente de uma forma que outras entidades possam extraí-lo.

O método exato usado pelo servidor para associar o `code_challenge` ao `code` emitido está fora do escopo desta especificação.

#### 4.4.1. Resposta de erro

Se o servidor exigir Proof Key for Code Exchange (PKCE) de clientes públicos OAuth e o cliente não enviar o `code_challenge` na requisição, o authorization endpoint DEVE (`MUST`) retornar a resposta de erro de autorização com o valor `error` definido como `invalid_request`. O `error_description` ou a resposta de `error_uri` DEVERIA (`SHOULD`) explicar a natureza do erro (por exemplo, "code challenge required").

Se o servidor que suporta PKCE não suportar a transformação solicitada, o authorization endpoint DEVE (`MUST`) retornar a resposta de erro de autorização com `error` definido como `invalid_request`. O `error_description` ou a resposta de `error_uri` DEVERIA (`SHOULD`) explicar a natureza do erro (por exemplo, "transform algorithm not supported").

### 4.5. Cliente envia o Authorization Code e o Code Verifier ao Token Endpoint

Ao receber o Authorization Code, o cliente envia a Access Token Request ao token endpoint. Além dos parâmetros definidos na OAuth 2.0 Access Token Request (Seção 4.1.3 da [RFC6749]), ele envia o seguinte parâmetro:

**code_verifier**
REQUIRED (obrigatório). Code verifier.

O `code_challenge_method` fica vinculado ao Authorization Code no momento em que este é emitido. Esse é o método que o token endpoint DEVE (`MUST`) usar para verificar o `code_verifier`.

### 4.6. Servidor verifica o code_verifier antes de retornar os tokens

Ao receber a requisição no token endpoint, o servidor a verifica calculando o code challenge a partir do `code_verifier` recebido e comparando-o com o `code_challenge` previamente associado, após transformá-lo de acordo com o método `code_challenge_method` especificado pelo cliente.

Se o `code_challenge_method` da Seção 4.3 foi `S256`, o `code_verifier` recebido é hasheado com SHA-256, codificado em base64url, e então comparado ao `code_challenge`, ou seja:

```
BASE64URL-ENCODE(SHA256(ASCII(code_verifier))) == code_challenge
```

Se o `code_challenge_method` da Seção 4.3 foi `plain`, eles são comparados diretamente, ou seja:

```
code_verifier == code_challenge
```

Se os valores forem iguais, o token endpoint DEVE (`MUST`) continuar o processamento normalmente (conforme definido pelo OAuth 2.0 [RFC6749]). Se os valores não forem iguais, uma resposta de erro indicando `invalid_grant`, conforme descrito na Seção 5.2 da [RFC6749], DEVE (`MUST`) ser retornada.

## 5. Compatibilidade

Implementações de servidor desta especificação PODEM (`MAY`) aceitar clientes OAuth 2.0 que não implementam esta extensão. Se o `code_verifier` não for recebido do cliente na Authorization Request, servidores que suportam retrocompatibilidade revertem ao protocolo OAuth 2.0 [RFC6749] sem esta extensão.

Como as respostas do servidor OAuth 2.0 [RFC6749] permanecem inalteradas por esta especificação, implementações de cliente desta especificação não precisam saber se o servidor implementou esta especificação ou não, e DEVERIAM (`SHOULD`) enviar os parâmetros adicionais definidos na Seção 4 para todos os servidores.

## 6. Considerações de IANA

A IANA fez os seguintes registros conforme este documento.

### 6.1. Registro de Parâmetros OAuth

Esta especificação registra os seguintes parâmetros no registro IANA "OAuth Parameters" definido no OAuth 2.0 [RFC6749]:

- Nome do parâmetro: `code_verifier` — local de uso: token request — controlador de mudanças: IESG — documento: RFC 7636
- Nome do parâmetro: `code_challenge` — local de uso: authorization request — controlador de mudanças: IESG — documento: RFC 7636
- Nome do parâmetro: `code_challenge_method` — local de uso: authorization request — controlador de mudanças: IESG — documento: RFC 7636

### 6.2. Registro de Métodos de Code Challenge do PKCE

Esta especificação estabelece o registro "PKCE Code Challenge Methods", como um sub-registro do registro "OAuth Parameters".

Tipos adicionais de `code_challenge_method` para uso com o authorization endpoint são registrados usando a política "Specification Required" [RFC5226], que inclui revisão da solicitação por um ou mais Designated Experts (DEs). Os DEs garantem pelo menos duas semanas de revisão da solicitação na lista de discussão oauth-ext-review@ietf.org, e que qualquer discussão nessa lista convirja antes de responderem à solicitação. Para permitir a alocação de valores antes da publicação, os Designated Expert(s) podem aprovar o registro assim que estiverem satisfeitos de que uma especificação aceitável será publicada.

Solicitações de registro e discussões na lista oauth-ext-review@ietf.org devem usar um assunto apropriado, como "Request for PKCE code_challenge_method: example".

Os Designated Expert(s) devem considerar a discussão na lista, bem como as propriedades gerais de segurança do método de desafio ao avaliar solicitações de registro. Novos métodos não devem divulgar o valor do `code_verifier` na requisição ao Authorization endpoint. Recusas devem incluir uma explicação e, se aplicável, sugestões de como tornar a solicitação bem-sucedida.

#### 6.2.1. Template de Registro

**Code Challenge Method Parameter Name:** o nome solicitado (ex.: "example"). Como um objetivo central desta especificação é manter as representações compactas, é RECOMENDADO que o nome seja curto — não excedendo 8 caracteres sem uma razão convincente. Esse nome é case-sensitive. Nomes não podem coincidir com outros nomes já registrados de forma case-insensitive, a menos que o Designated Expert declare haver uma razão convincente para permitir uma exceção nesse caso específico.

**Change Controller:** para RFCs Standards Track, indicar "IESG". Para outros, informar o nome da parte responsável. Outros detalhes (endereço postal, e-mail, home page) também podem ser incluídos.

**Specification Document(s):** referência ao(s) documento(s) que especifica(m) o parâmetro, preferencialmente incluindo URI(s) para obter cópias do(s) documento(s). Uma indicação das seções relevantes também pode ser incluída, mas não é obrigatória.

#### 6.2.2. Conteúdo Inicial do Registro

Conforme este documento, a IANA registrou os Code Challenge Method Parameter Names definidos na Seção 4.2 neste registro:

- Code Challenge Method Parameter Name: `plain` — Change Controller: IESG — Specification Document(s): Seção 4.2 da RFC 7636
- Code Challenge Method Parameter Name: `S256` — Change Controller: IESG — Specification Document(s): Seção 4.2 da RFC 7636

## 7. Considerações de Segurança

### 7.1. Entropia do code_verifier

O modelo de segurança depende do fato de que o code verifier não é aprendido nem adivinhado pelo atacante. É vitalmente importante aderir a esse princípio. Assim, o code verifier precisa ser criado de forma criptograficamente aleatória e com alta entropia, de modo que não seja prático para o atacante adivinhá-lo.

O cliente DEVERIA (`SHOULD`) criar um `code_verifier` com no mínimo 256 bits de entropia. Isso pode ser feito usando um gerador de números aleatórios adequado para criar uma sequência de 32 octetos. Essa sequência de octetos pode então ser codificada em base64url para produzir uma string URL-safe de 43 octetos a ser usada como `code_challenge`, com a entropia necessária.

### 7.2. Proteção contra escutas (eavesdroppers)

Clientes NÃO DEVEM (`MUST NOT`) fazer downgrade para `plain` depois de tentar o método `S256`. Servidores que suportam PKCE são obrigados a suportar `S256`, e servidores que não suportam PKCE simplesmente ignoram o `code_verifier` desconhecido. Por causa disso, um erro quando `S256` é apresentado só pode significar que o servidor está com defeito ou que um atacante MITM está tentando um ataque de downgrade.

O método `S256` protege contra escutas que observam ou interceptam o `code_challenge`, pois o desafio não pode ser usado sem o verifier. Com o método `plain`, existe a chance de o `code_challenge` ser observado pelo atacante no dispositivo ou na requisição HTTP. Como o code challenge é igual ao code verifier nesse caso, o método `plain` não protege contra a escuta da requisição inicial.

O uso de `S256` protege contra a divulgação do valor de `code_verifier` a um atacante.

Por isso, `plain` NÃO DEVERIA (`SHOULD NOT`) ser usado, e existe apenas para compatibilidade com implementações já implantadas nas quais o caminho da requisição já está protegido. O método `plain` NÃO DEVERIA (`SHOULD NOT`) ser usado em novas implementações, a menos que não seja possível suportar `S256` por alguma razão técnica.

O método de code challenge `S256`, ou outra extensão de método criptograficamente segura, DEVERIA (`SHOULD`) ser usada. O método de code challenge `plain` depende do sistema operacional e da segurança de transporte para não divulgar a requisição a um atacante.

Se o método de code challenge for `plain` e o code challenge for retornado dentro do `code` de autorização para se obter um servidor stateless, ele DEVE (`MUST`) ser criptografado de forma que apenas o servidor consiga descriptografá-lo e extraí-lo.

### 7.3. Salting do code_challenge

Para reduzir a complexidade de implementação, não se usa salting na produção do code challenge, já que o code verifier contém entropia suficiente para prevenir ataques de força bruta. Concatenar um valor publicamente conhecido a um code verifier (contendo 256 bits de entropia) e então hasheá-lo com SHA256 para produzir um code challenge não aumentaria o número de tentativas necessárias para forçar um valor válido de code verifier.

Embora a transformação `S256` seja semelhante a hashear uma senha, há diferenças importantes. Senhas tendem a ser palavras de entropia relativamente baixa, que podem ser hasheadas offline e o hash procurado em um dicionário. Ao concatenar um valor único, ainda que público, a cada senha antes de hasheá-la, o espaço de busca do dicionário que o atacante precisa varrer é bastante ampliado.

Processadores gráficos modernos hoje permitem que atacantes calculem hashes em tempo real mais rápido do que conseguiriam consultá-los em disco. Isso elimina o valor do salt em aumentar a complexidade de um ataque de força bruta, mesmo para senhas de baixa entropia.

### 7.4. Considerações de Segurança do OAuth

Toda a análise de segurança do OAuth apresentada na [RFC6819] se aplica, então os leitores DEVERIAM (`SHOULD`) segui-la cuidadosamente.

### 7.5. Considerações de Segurança do TLS

Considerações de segurança atuais podem ser encontradas em "Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)" [BCP195]. Isso substitui as recomendações de versão do TLS presentes no OAuth 2.0 [RFC6749].

## 8. Referências

### 8.1. Referências Normativas

- [BCP195] Sheffer, Y., Holz, R., e P. Saint-Andre, "Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)", BCP 195, RFC 7525, maio de 2015.
- [RFC20] Cerf, V., "ASCII format for network interchange", STD 80, RFC 20, outubro de 1969.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, março de 1997.
- [RFC3986] Berners-Lee, T., Fielding, R., e L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, janeiro de 2005.
- [RFC4648] Josefsson, S., "The Base16, Base32, and Base64 Data Encodings", RFC 4648, outubro de 2006.
- [RFC5226] Narten, T. e H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 5226, maio de 2008.
- [RFC5234] Crocker, D., Ed. e P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, janeiro de 2008.
- [RFC6234] Eastlake 3rd, D. e T. Hansen, "US Secure Hash Algorithms (SHA and SHA-based HMAC and HKDF)", RFC 6234, maio de 2011.
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, outubro de 2012.

### 8.2. Referências Informativas

- [RFC6819] Lodderstedt, T., Ed., McGloin, M., e P. Hunt, "OAuth 2.0 Threat Model and Security Considerations", RFC 6819, janeiro de 2013.

## Apêndice A. Notas sobre implementação de Base64url Encoding sem padding

Este apêndice descreve como implementar uma função de codificação base64url sem padding, baseada na função padrão de codificação base64 que usa padding.

Para ilustrar, segue exemplo de código em C# implementando essa função. Código similar pode ser usado em outras linguagens.

```csharp
static string base64urlencode(byte [] arg)
{
  string s = Convert.ToBase64String(arg); // Codificador base64 regular
  s = s.Split('=')[0]; // Remove qualquer '=' final
  s = s.Replace('+', '-'); // 62º caractere da codificação
  s = s.Replace('/', '_'); // 63º caractere da codificação
  return s;
}
```

Exemplo de correspondência entre valores não codificados e codificados. A sequência de octetos abaixo se codifica na string abaixo, que, quando decodificada, reproduz a sequência de octetos.

```
3 236 255 224 193

A-z_4ME
```

## Apêndice B. Exemplo para o método code_challenge S256

O cliente usa a saída de um gerador de números aleatórios adequado para criar uma sequência de 32 octetos. Os octetos representando o valor neste exemplo (em notação de array JSON) são:

```
[116, 24, 223, 180, 151, 153, 224, 37, 79, 250, 96, 125, 216, 173,
187, 186, 22, 212, 37, 77, 105, 214, 191, 240, 91, 88, 5, 88, 83,
132, 141, 121]
```

Codificando essa sequência de octetos em base64url, obtém-se o valor do `code_verifier`:

```
dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

O `code_verifier` é então hasheado via a função SHA256, produzindo:

```
[19, 211, 30, 150, 26, 26, 216, 236, 47, 22, 177, 12, 76, 152, 46,
8, 118, 168, 120, 173, 109, 241, 68, 86, 110, 225, 137, 74, 203,
112, 249, 195]
```

Codificando essa sequência de octetos em base64url, obtém-se o valor do `code_challenge`:

```
E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM
```

A authorization request inclui:

```
code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM
&code_challenge_method=S256
```

O authorization server então registra o `code_challenge` e o `code_challenge_method` junto com o código concedido ao cliente.

Na requisição ao token_endpoint, o cliente inclui o código recebido na resposta de autorização, bem como o parâmetro adicional:

```
code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

O authorization server recupera as informações do code grant. Com base no `code_challenge_method` registrado sendo `S256`, ele então hasheia e codifica em base64url o valor de `code_verifier`:

```
BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))
```

O valor calculado é então comparado com o valor de `code_challenge`:

```
BASE64URL-ENCODE(SHA256(ASCII(code_verifier))) == code_challenge
```

Se os dois valores forem iguais, o authorization server pode fornecer os tokens, desde que não haja outros erros na requisição. Se os valores não forem iguais, a requisição deve ser rejeitada e um erro deve ser retornado.

## Agradecimentos

A versão inicial do rascunho desta especificação foi criada pelo OpenID AB/Connect Working Group da OpenID Foundation.

Esta especificação é fruto do trabalho do OAuth Working Group, que inclui dezenas de participantes ativos e dedicados. Em particular, os seguintes indivíduos contribuíram com ideias, feedback e redação que moldaram a especificação final: Anthony Nadalin (Microsoft), Axel Nenker (Deutsche Telekom), Breno de Medeiros (Google), Brian Campbell (Ping Identity), Chuck Mortimore (Salesforce), Dirk Balfanz (Google), Eduardo Gueiros (Jive Communications), Hannes Tschofenig (ARM), James Manger (Telstra), Justin Richer (MIT Kerberos), Josh Mandel (Boston Children's Hospital), Lewis Adam (Motorola Solutions), Madjid Nakhjiri (Samsung), Michael B. Jones (Microsoft), Paul Madsen (Ping Identity), Phil Hunt (Oracle), Prateek Mishra (Oracle), Ryo Ito (mixi), Scott Tomilson (Ping Identity), Sergey Beryozkin, Takamichi Saito, Torsten Lodderstedt (Deutsche Telekom), William Denniss (Google).

## Endereços dos Autores

**Nat Sakimura (editor)** — Nomura Research Institute, 1-6-5 Marunouchi, Marunouchi Kitaguchi Bldg., Chiyoda-ku, Tokyo 100-0005, Japão. Email: n-sakimura@nri.co.jp — URI: http://nat.sakimura.org/

**John Bradley** — Ping Identity, Casilla 177, Sucursal Talagante, Talagante, RM, Chile. Email: ve7jtb@ve7jtb.com — URI: http://www.thread-safe.com/

**Naveen Agarwal** — Google, 1600 Amphitheatre Parkway, Mountain View, CA 94043, Estados Unidos. Email: naa@google.com — URI: http://google.com/
