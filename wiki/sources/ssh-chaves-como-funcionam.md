---
type: source
title: "Chaves SSH — Como Funcionam, Servidor, Cliente e Configuração"
aliases: ["ssh keys", "chave ssh", "ssh-keygen", "authorized_keys"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/ssh-chaves-como-funcionam.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-10
source_count: 0
tags: [ssh, chave-ssh, ed25519, openssh, autenticacao, hardening, criptografia-assimetrica, iam, bastion]
skill: tech-mentor-security
status: stable
---

## TL;DR

Chave SSH funciona pelo par assimétrico chave privada (fica só na máquina de origem, nunca sai) / chave pública (copiada para o `authorized_keys` do destino). O servidor (`sshd`, configurado em `/etc/ssh/sshd_config` ou em `sshd_config.d/*.conf`, lido de cima para baixo) deve ter `PubkeyAuthentication yes` e desativar senha, senha vazia e login de root — sem isso a autenticação por chave não é forçada de verdade. `ssh-keygen -t ed25519 -f ~/.ssh/id_x` gera o par; a chave privada exige permissão restrita ao dono, a `authorized_keys` pode ter leitura para grupo/outros. `~/.ssh/config` cria aliases (`Host`, `HostName`, `User`, `IdentityFile`, `IdentitiesOnly yes`) evitando repetir usuário/IP/porta/chave a cada conexão.

## Key Claims

**Claim:** A autenticação por chave SSH é assimétrica — a chave privada nunca sai da máquina de origem, apenas a chave pública é distribuída.
**Evidence:** O vídeo demonstra o par gerado por `ssh-keygen`: o arquivo sem `.pub` fica com permissão restrita ao dono (nunca compartilhado); o arquivo `.pub` é copiado manualmente para o `authorized_keys` do host de destino. Sem a chave privada correspondente, a chave pública sozinha não permite acesso.
**Confidence:** alta

**Claim:** A direção do acesso SSH é unidirecional por padrão — só existe hierarquia bidirecional se dois pares de chaves distintos forem configurados, um em cada sentido.
**Evidence:** No exemplo com dois hosts Docker, gerar e distribuir apenas um par (privada em "one", pública em "two") permite "one" acessar "two", mas não o inverso — foi necessário gerar um segundo par (privada em "two", pública em "one") para a via inversa funcionar.
**Confidence:** alta

**Claim:** Desativar autenticação por senha no servidor SSH é padrão de indústria quando chave pública está disponível, especificamente para eliminar o vetor de brute force.
**Evidence:** Configuração do `sshd_config.d` usada no vídeo: `PubkeyAuthentication yes` combinado com desativação explícita de senha, senha vazia e login de root. O autor afirma que nunca desativaria `PubkeyAuthentication` a menos que exista sistema comprovadamente melhor.
**Confidence:** alta

**Claim:** As configurações do `sshd` são aplicadas na ordem em que aparecem — a primeira regra que casar prevalece — o que justifica colocar overrides customizados em arquivos numerados dentro de `sshd_config.d/`.
**Evidence:** O vídeo demonstra um arquivo `sshd_config.d/00-...` (prefixo numérico baixo para ser lido primeiro) contendo as diretivas customizadas, em vez de editar `sshd_config` diretamente.
**Confidence:** média (comportamento de `Include` e ordem de leitura é citado como fato mas não demonstrado com um exemplo de conflito real entre duas regras)

**Claim:** O comando `install` é preferível a `mkdir` + `chmod` + `chown` separados para criar a estrutura `~/.ssh` porque aplica diretório/permissão/dono numa única chamada idempotente.
**Evidence:** Demonstração de `install -d ~/.ssh -m 700 -o usuario -g grupo` para o diretório e `install -m 644 ... /dev/null ~/.ssh/authorized_keys` para o arquivo vazio.
**Confidence:** alta

**Claim:** Passphrase na chave privada é boa prática de segurança, mas tem custo de fricção (precisa ser digitada a cada carregamento no agente SSH) — o autor admite não usá-la na prática, preferindo uma chave dedicada por serviço.
**Evidence:** Declaração direta do autor ao gerar a chave com `ssh-keygen`, reconhecendo a tensão entre segurança adicional e conveniência.
**Confidence:** alta (é opinião declarada do autor, não uma alegação técnica objetiva)

**Claim:** `IdentitiesOnly yes` no `~/.ssh/config` evita falha de autenticação por esgotamento de tentativas quando há múltiplas chaves cadastradas.
**Evidence:** Explicação de que o SSH, sem essa diretiva, tenta cada identidade disponível em ordem e pode esgotar o número de tentativas do servidor antes de alcançar a chave correta para aquele host.
**Confidence:** alta

## Entities & Concepts Touched

- [[wiki/concepts/ssh]]
- [[wiki/concepts/criptografia]]
- [[wiki/concepts/encryption]]
- [[wiki/concepts/principio-do-menor-privilegio]]
- [[wiki/concepts/hardening-de-servidor]]

## Open Questions

- O vídeo promete um próximo vídeo sobre SSH Tunnels reaproveitando `AllowTcpForwarding yes` — ainda não ingerido na wiki; quando existir, deve linkar de volta para [[wiki/concepts/ssh]].
- A alegação de ordem de leitura de `sshd_config.d/*.conf` (primeira regra que casa prevalece) não foi verificada contra a documentação oficial do OpenSSH nesta ingestão — marcado como confiança média.

## Raw Quotes

> "A chave SSH, você pode imaginar ela como se fosse uma chave e uma fechadura. Eu tenho a chave, que seria a minha chave privada, e o servidor tem a fechadura."

> "Você pode imaginar isso aqui como uma senha para você usar a chave [...] mas na prática, eu mesmo, fazendo mea culpa aqui, eu mesmo não coloco senha nisso aqui, eu prefiro gerar uma chave para cada serviço que eu for utilizar."

> "Nunca pegue o que não tem o .pub, porque é essa parte aqui que você compartilha [...] você nunca tira isso aqui do seu computador."
