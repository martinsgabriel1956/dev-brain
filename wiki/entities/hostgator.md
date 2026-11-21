---
type: entity
title: "HostGator"
aliases: ["HostGator", "HostGator VPS"]
date_created: 2026-07-20
date_updated: 2026-11-21
source_count: 11
tags: [empresa, hosting, vps, infra, patrocinio]
skill: tech-mentor-infra
status: stub
---

# HostGator

Provedora de hospedagem/VPS, patrocinadora da demo de [[wiki/concepts/blue-green-deploy|deploy blue/green]] de [[wiki/entities/augusto-galego]]. Oferece planos de VPS com servidores localizados no Brasil (latência menor para público local) e terminal web integrado além de acesso via SSH.

## Contexto de uso na demo

- Plano de VPS mais barato usado como ambiente de teste — suficiente para rodar [[wiki/concepts/reverse-proxy|Nginx]] + duas instâncias Node em paralelo.
- Apresentado como opção viável tanto para aprendizado quanto para produção real (SaaS/site próprio), com upgrade de plano disponível se a carga crescer.

## Segunda Aparição: Deploy Contínuo via SSH e VPS com Claude Code Pré-instalado

Citada novamente (bloco patrocinado) em [[wiki/sources/continuous-integration-delivery-deploy-vs-release]], desta vez como alvo de deploy contínuo via GitHub Actions + SSH, não deploy manual blue/green. Planos a partir de R$ 21,70/mês, servidores em São Paulo, opções de OS (Ubuntu, Alma Linux, Rocky Linux, com/sem cPanel) e instaladores prontos para N8N, WordPress, Docker. Destaque adicional: oferta de VPS com [[wiki/entities/claude-code]] pré-instalado, promovida como alternativa a manter o computador local sempre ligado. *Nota de desambiguação:* não confundir com [[wiki/entities/hostinger]], provedora de VPS diferente já documentada em outras fontes da wiki — risco de confusão de nome, já que a transcrição desta fonte grafa o nome como "Host Gator" (dois termos), possível artefato de transcrição automática.

## Terceira Aparição: "Allstack" — Agregador de Assinaturas de IA

Citada em [[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]] como patrocinadora de um produto novo, "Allstack" (nome falado, grafia não confirmada): passe único que centraliza várias assinaturas de IA (chat com roteamento entre modelos como Claude, GPT, Gemini, Grok, e agentes pré-configurados ou customizáveis), com planos diferenciados incluindo um foco em privacidade/modo anônimo. Proposta de valor: reduzir troca de contexto e custo agregando assinaturas num único lugar.

## Key Sources

- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]]
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — segunda aparição, agora como alvo de deploy contínuo via GitHub Actions; oferta de VPS com Claude Code pré-instalado
- [[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]] — terceira aparição, produto "Allstack" de agregação de assinaturas de IA

## FrontPUSH, hospedagem aula 01

Em [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]], primeiro exemplo do "método tradicional"; no slide de "Pagos" leva uma estrela não explicada (talvez a que o autor usa; inferência).

## FrontPUSH, hospedagem aula 02

Em [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: frontpush.com.br resolve para `162.241.61.29`, e FrontPUSH, CreatorPUSH e o domínio do autor estão "todos [...] no mesmo servidor que é na HostGator". Confirma a estrela do slide da aula 01.

## FrontPUSH, hospedagem aula 03

Em [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]], HostGator e Hostinger "já vem com [o Apache] instalado, configurado na porta 80"; o FrontPUSH em PHP e o CreatorPUSH estático vão para a HostGator na próxima aula.

## FrontPUSH, hospedagem aula 04

Em [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]: planos P, M e Turbo; o autor assinou o Turbo (SSD "na época", SSL grátis, mais processamento). O e-mail técnico traz `nspro34`/`nspro35.hostgator.com.br`, IP do servidor e acesso ao [[wiki/entities/cpanel]]. Acha a Hostinger melhor hoje, mas o plano "já está pago".

## FrontPUSH, hospedagem aula 05

Em [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: tour pelo cPanel da conta do autor (80 MB em `public_html`, três domínios, SSL nos três, e-mail próprio). Para quem usa PHP ou WordPress, "eu indico" esse tipo de serviço.

## FrontPUSH, hospedagem aula 06

Em [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: o portfólio do autor em `public_html`, FrontPUSH (PHP) e CreatorPUSH (estático) como domínios adicionais, `/Nubank` e `/Spider-Man` como subpastas, AutoSSL em todos. O PHP roda sem configurar porque "a HostGator já deixa pré-configurado e instalado o Apache". FileZilla "indicado pelo próprio pessoal do HostGator".

## Key sources (adição 2026-10-30)

- [[wiki/sources/no-robots-in-the-gym-ia-tarefas-de-academia-ler-e-escrever]] — quarta aparição como patrocinadora (VPS para site, SaaS, n8n ou OpenClaw)
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — citada como exemplo de mascote de marca (aula de UI, não patrocínio)
- [[wiki/sources/frontpush-introducao-hospedagem-de-websites-url-localhost-porta]]: FrontPUSH, hospedagem aula 01: hospedagem tradicional, com estrela no slide
- [[wiki/sources/frontpush-ip-e-dns-ipv4-ipv6-ip-publico-privado-registro-br]]: FrontPUSH, hospedagem aula 02: servidor dos três domínios do autor
- [[wiki/sources/frontpush-website-estatico-vs-aplicacao-web-php-apache-xampp-react]]: FrontPUSH, hospedagem aula 03: Apache/PHP prontos no compartilhado
- [[wiki/sources/frontpush-hostgator-parte-1-plano-turbo-name-servers-registro-br]]: FrontPUSH, hospedagem aula 04: plano Turbo, e-mail técnico, name servers
- [[wiki/sources/frontpush-hostgator-parte-2-cpanel-recursos-ftp-ssl-email]]: FrontPUSH, hospedagem aula 05: cPanel da conta do autor
- [[wiki/sources/frontpush-hostgator-parte-3-upload-public-html-filezilla-dominios-adicionais-autossl]]: FrontPUSH, hospedagem aula 06: três sites no mesmo plano
