---
type: concept
title: "FTP, SFTP e FTPS"
aliases: ["ftp", "file transfer protocol", "sftp", "ftps", "conta ftp"]
date_created: 2026-11-21
date_updated: 2026-11-21
source_count: 3
tags: [ftp, sftp, ftps, protocolo, deploy, hospedagem, seguranca, networking]
skill: tech-mentor-networking
status: stub
---

# FTP, SFTP e FTPS

**FTP** (File Transfer Protocol, RFC 959) transfere arquivos entre cliente e servidor por duas conexões TCP (controle na porta 21, dados em outra porta). Manda usuário, senha e arquivos **em texto claro** `[external]` (https://www.rfc-editor.org/rfc/rfc959). Duas saídas seguras:

- **SFTP**: subsistema do SSH (porta 22), um só canal cifrado; não é "FTP com S" ([[wiki/concepts/ssh]]).
- **FTPS**: FTP com TLS (explícito via `AUTH TLS` ou implícito na 990).

Clientes como FileZilla falam os três. Na [[wiki/concepts/hospedagem-de-sites|hospedagem compartilhada]], o [[wiki/entities/cpanel]] cria contas FTP e oferece o gerenciador de arquivos pelo navegador (HTTPS) como alternativa.

## No FrontPUSH

- Aula 01 ([[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]): o Netlify dispensa "entrar no servidor [...] por meio de um FTP"; dá para "colocar os arquivos direto pelo Git".
- Aula 05 ([[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]): "o FTP, pessoal, é um protocolo de transferência de arquivos"; cria-se uma conta FTP "ou você pode puxar daqui diretamente". A aula não fala da falta de criptografia.

O deploy por Git (push → build → publicação) substitui o upload manual nas plataformas modernas ([[wiki/concepts/deploy-strategies]]).

## FrontPUSH, hospedagem aula 06

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: upload pelo [[wiki/entities/filezilla]] com IP, usuário e senha; o aviso de segurança aparece porque o FTP "não é criptografado", "é só você clicar em sim"; para criptografar, "SFTP, basicamente só muda isso, mas é o mesmo protocolo". Não é: SFTP é do SSH; FTP com TLS é FTPS. Clicar em sim manda a senha do cPanel em claro.

## Key sources

- [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]: deploy pelo Git em vez de FTP (Netlify)
- [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: conta FTP no cPanel × upload pelo gerenciador de arquivos
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: FileZilla, aviso de FTP sem criptografia, SFTP ≠ FTPS
