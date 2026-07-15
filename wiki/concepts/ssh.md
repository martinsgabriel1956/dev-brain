---
type: concept
title: "SSH e Chaves SSH"
aliases: ["ssh", "secure shell", "chave ssh", "ssh-keygen", "authorized_keys", "openssh"]
date_created: 2026-07-10
date_updated: 2026-07-15
source_count: 2
tags: [ssh, openssh, ed25519, autenticacao, criptografia-assimetrica, iam, hardening, bastion]
skill: tech-mentor-security
status: stable
---

## Definição

SSH (Secure Shell) é um protocolo cliente-servidor para acesso remoto autenticado e criptografado. A autenticação por chave usa um par assimétrico: **chave privada** (fica só na máquina de origem, nunca é compartilhada) e **chave pública** correspondente (distribuída e registrada no destino). Pode-se pensar na chave privada como a chave física e no host de destino como a fechadura — quando as duas "batem", a sessão é liberada sem senha.

Ver [[wiki/concepts/criptografia]] e [[wiki/concepts/encryption]] para o fundamento matemático (chave pública cifra/verifica, chave privada decifra/assina) que a autenticação por chave SSH reaproveita.

## Como a autenticação por chave funciona

1. O cliente gera um par de chaves com `ssh-keygen -t ed25519 -f ~/.ssh/id_<nome>`.
2. A chave pública (`id_<nome>.pub`) é copiada para o arquivo `authorized_keys` (por padrão em `~/.ssh/authorized_keys`) do usuário no host de destino.
3. Na conexão, o OpenSSH verifica se o cliente possui a chave privada correspondente a alguma entrada do `authorized_keys` — sem transmitir a chave privada em nenhum momento.

**Direção é unidirecional por par de chaves.** Se a chave privada está só na máquina A e a pública correspondente só foi copiada para B, A consegue acessar B, mas B não consegue acessar A de volta. Para acesso bidirecional é preciso um segundo par de chaves, com privada em B e pública em A — os dois pares coexistem de forma independente.

### Permissões de arquivo

- Diretório `~/.ssh`: `700` (só o dono acessa).
- Chave privada: leitura/escrita restrita ao dono — nunca legível por grupo ou outros.
- `authorized_keys` (chave(s) pública(s) autorizadas): `644` — leitura para grupo/outros é aceitável, é a parte pública.
- Comando `install` cria diretório/arquivo + permissão + dono numa única chamada, preferível a `mkdir`+`chmod`+`chown` separados.

### Passphrase

`ssh-keygen` oferece proteger a chave privada com uma passphrase adicional — boa prática, mas exige digitá-la a cada carregamento da chave no agente SSH. Trade-off comum: usar uma chave dedicada por serviço em vez de passphrase, trocando um pouco de segurança por menos fricção.

## Configuração do servidor (sshd)

Arquivo principal: `/etc/ssh/sshd_config`, que geralmente inclui (`Include`) tudo em `sshd_config.d/*.conf`. Regras são lidas de cima para baixo — a primeira que casa prevalece. Boa prática: colocar overrides num arquivo próprio dentro de `sshd_config.d/`, prefixado com número baixo (ex.: `00-*.conf`) para ser lido primeiro, em vez de editar o arquivo principal.

Diretivas centrais para autenticação só-por-chave:

```
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
PermitRootLogin no
```

`PubkeyAuthentication yes` é considerado padrão de indústria — desativar autenticação por senha elimina o vetor de brute force por completo, já que não existe fallback de senha.

Ver [[wiki/concepts/hardening-de-servidor]] para o espectro de presets (paranoico/equilibrado/básico) e outras diretivas como `AllowTcpForwarding`.

## Configuração do cliente (~/.ssh/config)

Cria aliases para evitar repetir usuário, IP, porta e chave a cada conexão:

```
Host two
    HostName 10.0.0.3
    User otavio
    Port 22
    IdentityFile ~/.ssh/id_two
    IdentitiesOnly yes
```

`IdentitiesOnly yes` restringe o SSH a tentar apenas a identidade especificada — sem essa diretiva, com muitas chaves cadastradas, o SSH tenta cada uma em ordem e pode esgotar as tentativas do servidor antes de alcançar a chave correta.

## Relação com outros conceitos

- [[wiki/concepts/criptografia]] / [[wiki/concepts/encryption]] — Ed25519 é o mesmo tipo de criptografia assimétrica usada em TLS e assinaturas digitais.
- [[wiki/concepts/principio-do-menor-privilegio]] — SSH é o canal citado para acesso a bastion hosts em arquiteturas de VPC fechada.
- [[wiki/concepts/hardening-de-servidor]] — chave SSH é a base sobre a qual o hardening de acesso remoto é construído.
- [[wiki/concepts/porta-de-rede]] — SSH é uma das quatro well-known ports citadas como exemplo canônico (porta 22), ao lado de HTTP/80, HTTPS/443 e SMTP/25; a diretiva `Port` no `~/.ssh/config` e no `sshd_config` é justamente onde essa porta pode ser trocada do padrão.

## Key Sources

- [[wiki/sources/ssh-chaves-como-funcionam]]
- [[wiki/sources/portas-de-rede-como-funcionam]] — porta 22 como well-known port do SSH
