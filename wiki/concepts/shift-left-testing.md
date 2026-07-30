---
type: concept
title: "Shift-Left Testing"
aliases: ["shift left", "shift-left security", "teste antecipado"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_count: 1
tags: [devsecops, testing, sdlc, security-culture]
skill: tech-mentor-security
status: draft
---

# Shift-Left Testing

Abordagem que move testes (de segurança, qualidade ou ambos) para o início do ciclo de desenvolvimento — planejamento e código — em vez de deixá-los apenas para o fim, perto do deploy. O nome vem de representar o SDLC como uma linha do tempo da esquerda para a direita (planejamento → ... → produção): "shift left" significa literalmente empurrar a verificação para mais cedo nessa linha.

## Por Que Importa em DevSecOps

Numa pipeline puramente [[wiki/concepts/devsecops|DevOps]] sem essa prática, testes de conformidade e segurança costumam rodar isolados, muitas vezes via consultoria externa pontual, sem considerar todas as etapas do ciclo — o que os torna caros, lentos e fáceis de pular sob pressão de prazo. Shift-left integra a verificação a cada etapa (planejamento, código, build, deploy, operação), tornando segurança parte do fluxo normal de trabalho em vez de um gate externo de última hora.

## Categorias de Verificação Antecipada

- **Secret scanning** — escaneia repositórios em busca de credenciais vazadas antes que cheguem a produção.
- **SCA (Software Composition Analysis)** — analisa dependências de terceiros por vulnerabilidades conhecidas já no build.
- **[[wiki/concepts/sast]]** — análise estática de código antes da execução.
- **IAST (Interactive Application Security Testing)** — testes interativos de segurança de aplicação, combinando elementos de análise estática e dinâmica.

## Key Sources

- [[wiki/sources/devsecops-origem-cultura-manifesto]] — shift-left testing como abordagem promovida por guideline DevSecOps (fundação de segurança de software), com mapeamento de ferramentas por fase do ciclo

## Conceitos Relacionados

[[wiki/concepts/devsecops]] · [[wiki/concepts/sast]]
