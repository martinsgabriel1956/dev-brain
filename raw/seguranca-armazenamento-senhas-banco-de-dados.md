# Segurança e Armazenamento de Senhas no Banco de Dados

> **Fonte:** Transcrição de vídeo — Canal Renato Augusto  
> **Autor:** Renato Augusto  
> **Domínio:** Segurança, Criptografia, Backend

---

## Introdução

Se o banco de dados da sua aplicação vazasse hoje e um hacker conseguisse acesso aos dados, quanto tempo levaria para ele decifrar a maior parte das senhas dos seus usuários? Minutos? Horas? Dias? Semanas? Ou seria impossível porque você usa algoritmos de hash?

Este material cobre tudo que um programador precisa saber sobre segurança e armazenamento de senhas, incluindo técnicas avançadas — desde a década de 90 até os algoritmos modernos.

---

## 1. A Era do Plaintext (Década de 90)

### Como funcionava

Quando um usuário se cadastrava, o servidor pegava a senha e armazenava **literalmente como o usuário digitou** — texto puro, sem nenhuma proteção.

### O problema

A popularização dos ataques de **SQL Injection** na década de 90 permitia que hackers ganhassem acesso ao banco de dados. Com senhas em plaintext:

- A senha do usuário era exposta diretamente
- Como humanos reutilizam senhas em vários serviços, o hacker ganhava acesso não só à aplicação invadida, mas a e-mails, redes sociais, etc.

### Caso real: RockYou (2009)

Em 2009 — décadas após as primeiras recomendações de segurança — a empresa RockYou (ligada ao Facebook, criadora de widgets para MySpace) sofreu um ataque e **32 milhões de senhas foram vazadas em plaintext**.

Esse vazamento originou a famosa **wordlist RockYou**, que os próprios hackers foram atualizando ao longo dos anos:

- RockYou 2020, 2021, 2022, 2023, 2024, 2025, 2026...
- Hoje a lista tem **bilhões de senhas reais de usuários reais**
- Disponível em sites como [WikiLeaks / SecLists](https://github.com/danielmiessler/SecLists) — versão "All-In-One": 317 GB, ~29.6 bilhões de senhas

> **Atenção:** Até hoje existem empresas armazenando senhas em plaintext.

---

## 2. Algoritmos de Hash (MD5 e SHA-1)

### Como funcionava

O mercado adotou funções de hash como **MD5** e **SHA-1** como primeira solução. A senha era passada pela função e o hash resultante era armazenado no banco.

```
senha "123456" → MD5 → "e10adc3949ba59abbe56e057f20f883e"
```

### Propriedades das funções de hash

| Propriedade | Descrição |
|---|---|
| **Determinística** | Mesma entrada sempre produz mesma saída |
| **Efeito avalanche** | Pequena mudança na entrada muda completamente a saída |
| **Unidirecional** | Não é possível reverter — só vai "pra frente" |

> **Sobre sites de "MD5 Decrypt":** Eles **não** revertem o hash. Usam Rainbow Tables — listas pré-computadas de hash → senha. Não é descriptografia.

### Problemas do MD5/SHA para senhas

#### Problema 1: Velocidade extrema

MD5 e SHA geram **bilhões de hashes por segundo**. Isso permite que um atacante teste bilhões de combinações em pouquíssimo tempo.

#### Problema 2: Senhas iguais geram hashes iguais

Se Maria e Juliana usam a senha "123456", ambas terão o mesmo hash. Ao quebrar uma, o atacante ganha acesso a ambas automaticamente.

#### Problema 3: Ataques de pré-computação (Rainbow Tables)

O atacante pega a wordlist RockYou (bilhões de senhas), **gera o hash de cada uma** e armazena numa tabela. Quando o banco vaza, basta comparar os hashes do banco com a tabela pré-computada.

- Trabalho feito **uma vez**, reutilizado para **todos os vazamentos**
- Com a lista de 29.6 bilhões de senhas + MD5: a varredura leva frações de segundo

---

## 3. Salt — Mitigação Parcial

### O que é

Salt é uma **string aleatória** gerada no momento do cadastro do usuário. Ela é concatenada com a senha antes de gerar o hash.

```
senha "123456" + salt "dHuY7k3m" → hash("123456dHuY7k3m") → armazenado no banco
```

O salt é armazenado junto no banco (não precisa ser secreto).

### O que o salt resolve

- **Senhas iguais geram hashes diferentes** (por causa do efeito avalanche)
- **Invalida Rainbow Tables pré-computadas**: o atacante teria que recomputar a tabela inteira para cada salt diferente

### O que o salt NÃO resolve com MD5/SHA

MD5/SHA continuam sendo extremamente rápidos. Para cada linha do banco, o atacante precisa rodar a wordlist toda, mas como gera bilhões de hashes/segundo, ainda é viável.

> Salt é excelente — continuamos usando. O problema é o algoritmo subjacente (MD5/SHA), não o salt.

---

## 4. Algoritmos Especializados: BCrypt e PBKDF2

### A virada: CPU-Hard

O mercado adotou algoritmos especificamente projetados para ser **lentos por natureza** — o conceito de **CPU-Hard**.

Algoritmos: **BCrypt**, **PBKDF2** (ainda usado em sistemas legados).

### Como o BCrypt funciona

O hash gerado pelo BCrypt tem o formato:

```
$2a$12$[22 chars salt][31 chars hash]
```

| Parte | Descrição |
|---|---|
| `2a` | Versão do algoritmo |
| `12` | Fator de trabalho (cost factor) |
| Próximos 22 chars | Salt gerado aleatoriamente pelo próprio algoritmo |
| Últimos 31 chars | Hash resultante |

### Fator de trabalho (Work Factor)

O BCrypt usa uma **escala logarítmica**: `2^N` iterações.

- Fator 12 → `2^12 = 4096` iterações internas
- Fator 13 → `2^13 = 8192` iterações → **dobra o tempo**
- A cada incremento de 1, o tempo dobra

**Exemplo prático:** Com fator 12, gerar um único hash leva ~323ms → apenas ~3 hashes/segundo.

### Comparação: MD5/SHA vs BCrypt

| Algoritmo | Velocidade | Hashes/segundo |
|---|---|---|
| MD5/SHA | Extremamente rápido | ~bilhões/segundo |
| BCrypt (fator 12) | Lento por design | ~3/segundo |

**Cálculo do custo para o atacante com BCrypt (fator 12, CPU single-core):**

```
3 hashes/s × 60s × 60min × 24h = ~259.200 tentativas/dia
Em 1 ano: ~94 milhões de tentativas
```

Para uma wordlist de 29 bilhões → levaria mais de **300 anos** só para a primeira linha do banco.

### O problema do BCrypt: Paralelismo com GPU

**Processadores modernos** (ex: Ryzen 9 — 16 núcleos):

```
3 hashes/s × 16 núcleos = 48 hashes/s
Em 1 dia: ~4.147.200 tentativas
Em 1 ano: ~1,5 bilhão de tentativas
```

**GPUs modernas** (ex: RTX 5090 — 21.760 núcleos CUDA):

```
3 hashes/s × 21.760 núcleos = ~65.280 hashes/s
Em 1 dia: ~5 bilhões de tentativas
Em 1 ano: ~2 trilhões de tentativas
```

O BCrypt ocupa apenas **4 KB de memória RAM** por instância → cabe milhares de instâncias paralelas em qualquer GPU.

**Conclusão:** Com uma rig de múltiplas GPUs (similar a mineração de Bitcoin), um atacante varre um banco de dados em **dias**. O BCrypt, sozinho, **não é mais considerado seguro**.

---

## 5. Argon2 — Estado da Arte

### Por que Argon2?

A fraqueza da GPU é a **memória RAM** (uma RTX 5090 topo de linha tem apenas 32 GB). O mercado precisava de um algoritmo que travasse justamente aí.

O **Argon2** foi o vencedor do [Password Hashing Competition (2015)](https://password-hashing.net/) e até hoje é o algoritmo mais seguro para armazenamento de senhas.

### Conceito: Memory-Hard

Além de CPU-Hard, o Argon2 é **Memory-Hard**: para gerar cada hash, ele ocupa uma quantidade configurável de memória RAM.

### Variantes do Argon2

| Variante | Uso recomendado |
|---|---|
| Argon2i | Resistente a side-channel attacks |
| Argon2d | Máxima resistência a GPU |
| **Argon2id** | **Híbrido — recomendado para senhas** |

### Estrutura do hash Argon2

```
$argon2id$v=19$m=65536,t=3,p=4$[salt]$[hash]
```

| Parte | Descrição |
|---|---|
| `argon2id` | Variante do algoritmo |
| `v=19` | Versão |
| `m=65536` | Custo de memória em KB (= 64 MB) |
| `t=3` | Número de iterações (time cost) |
| `p=4` | Paralelismo (threads) |
| Salt | Gerado automaticamente |
| Hash | Resultado final |

### Configuração em código (PHP)

```php
$password = $_POST['password']; // senha do usuário

$options = [
    'memory_cost' => 65536,  // 64 MB em KB
    'time_cost'   => 3,       // 3 iterações
    'threads'     => 4,       // 4 threads
];

$hash = password_hash($password, PASSWORD_ARGON2ID, $options);
```

### Por que Memory-Hard derrota GPUs

- Cada instância do Argon2 com `m=65536` ocupa **64 MB de RAM**
- Paralelizar 10 instâncias → 640 MB
- Paralelizar 100 instâncias → 6.4 GB
- Com `m=1048576` (1 GB) → paralelizar 32 instâncias já esgota 32 GB de VRAM da RTX 5090

O atacante pode ter **milhões de núcleos CUDA**, mas não tem RAM suficiente para paralelizar de forma eficaz.

> Configurar `memory_cost` para 64 MB ou mais é ser "generoso" — valores de 256 MB ou 1 GB são válidos dependendo da capacidade do servidor.

---

## 6. Pepper — Camada Extra de Segurança

### O que é

Pepper é um **valor secreto único**, armazenado na variável de ambiente (`ENV`) do servidor — **nunca no banco de dados**.

Ao contrário do salt (que é único por usuário e fica no banco), o pepper é:
- O mesmo para todos os usuários
- Armazenado fora do banco (no servidor)

### Como aplicar

```
hash_input = senha_do_usuario + PEPPER_VALUE
hash_final = argon2id(hash_input)
```

Exemplo:
- Senha do usuário: `123456`
- Pepper (no ENV): `f3A7cB9xQ2`
- Valor hasheado: `123456f3A7cB9xQ2`

### Por que funciona

Se o banco de dados vazar:
- O atacante tem o hash, o salt e os parâmetros do Argon2
- Mas **não sabe que existe um pepper** concatenado à senha
- Mesmo que tente bruteforce, nunca chegará à senha correta porque está tentando reverter `hash(senha + pepper)` sem saber o pepper

Só é comprometido se o atacante **também** ganhar acesso ao servidor (ao arquivo `.env`). Nesse cenário, a empresa já tem problemas maiores de segurança.

### Implementação

```
# .env
PASSWORD_PEPPER=f3A7cB9xQ2mN5pL8vR1sY4
```

```php
$pepper = $_ENV['PASSWORD_PEPPER'];
$hash = password_hash($password . $pepper, PASSWORD_ARGON2ID, $options);
```

---

## 7. Arquitetura Final Recomendada

```
[Usuário cadastra] 
    → senha enviada via HTTPS
    → servidor concatena: senha + PEPPER (do ENV)
    → Argon2id gera hash (m=64MB+, t=3+, p=4+)
    → armazenado no banco: apenas o hash completo (com salt embutido)

[Usuário faz login]
    → servidor busca hash no banco
    → concatena: senha_digitada + PEPPER
    → Argon2id verifica se hash bate
    → autenticação aprovada ou negada
```

### Nível de segurança resultante

| Técnica | Proteção |
|---|---|
| Plaintext | Nenhuma |
| MD5/SHA sem salt | Fraca — Rainbow Tables |
| MD5/SHA com salt | Fraca — velocidade do algoritmo |
| BCrypt/PBKDF2 | Moderada — vulnerável a rigs de GPU |
| **Argon2id** | **Alta — Memory-Hard derrota paralelismo de GPU** |
| **Argon2id + Pepper** | **Muito alta (~99.9%) — requer acesso ao banco E ao servidor** |

---

## 8. Conceitos Fundamentais Relacionados

Para entender e aplicar essas técnicas corretamente, são necessários conhecimentos de:

- **Paralelismo e threads** — como explorar múltiplos núcleos de CPU/GPU
- **Arquitetura de hardware** — diferença entre CPU e GPU, núcleos, memória
- **Funcionamento interno de algoritmos de hash**
- **Ataques de pré-computação / Rainbow Tables**
- **SQL Injection** — vetor original que tornou o plaintext perigoso
- **Gerenciamento de secrets** — uso correto de variáveis de ambiente

---

## Linha do Tempo Resumida

| Período | Prática | Status |
|---|---|---|
| ~1990s | Plaintext | Obsoleto e inseguro |
| ~1990s–2000s | MD5/SHA sem salt | Inseguro |
| ~2000s | MD5/SHA + salt | Insuficiente |
| ~2000s–2010s | BCrypt / PBKDF2 | Legado — aceitável com fator alto |
| 2015–hoje | **Argon2id** | **Recomendado** |
| 2015–hoje | **Argon2id + Pepper** | **Melhor prática atual** |
