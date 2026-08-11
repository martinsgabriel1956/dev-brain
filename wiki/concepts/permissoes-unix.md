---
type: concept
title: "Permissões Unix (chmod, sudo)"
aliases: ["permissões", "chmod", "sudo", "rwx", "permissão negada", "file permissions"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [linux, unix, permissoes-unix, chmod, sudo, seguranca, tech-mentor-infra]
skill: tech-mentor-infra
status: stub
---

# Permissões Unix (chmod, sudo)

Todo arquivo Unix carrega permissões de **read (`r`)**, **write (`w`)** e **execute (`x`)** para três classes: dono, grupo e outros. `ls -l` exibe essas permissões (ex.: `-rwxr-xr--`), o tipo (`-` arquivo, `d` diretório, `l` link) e o dono.

## O erro clássico: "permissão negada"

Segundo [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]], tentar executar um script (`./hello.sh`) que tem `r` e `w` mas **não** tem `x` resulta em "permissão negada". A correção é dar a permissão de execução:

```bash
chmod +x hello.sh    # adiciona x; agora ./hello.sh roda
```

É a origem daquele conselho "dá um `chmod` que resolve" que IA e Stack Overflow dão: o arquivo simplesmente não tinha permissão de execução.

> Notação octal (referência): `r=4, w=2, x=1` → `chmod 750 script.sh` = dono rwx, grupo r-x, outros ---. `[skill: tech-mentor-infra — linux-essentials]`

## sudo

`sudo` roda um comando como **super user / admin**, permitindo forçar operações que o usuário atual não tem permissão de fazer (pede a senha de admin). Usar com cuidado — combina mal com comandos destrutivos como `rm -rf` (ver [[wiki/concepts/comandos-basicos-linux]]).

## Relação com outros conceitos

- [[wiki/concepts/comandos-basicos-linux]] — `chmod`/`sudo` no conjunto básico de comandos.
- [[wiki/concepts/permissoes-de-arquivo]] — `[[link marcador; criar se necessário]]`.
- [[wiki/concepts/principio-do-menor-privilegio]] — `sudo` é o oposto: elevar privilégio; usar só quando preciso.

## Key Sources

- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
