---
type: source
title: "XSS Attack — Dicionário do Programador (Código Fonte TV)"
aliases: ["xss attack dicionario do programador", "xss cross site scripting codigo fonte tv", "loja do bob xss"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/xss-attack-dicionario-programador-codigo-fonte-tv.md
source_url: ""
author: "Código Fonte TV"
date_published: ""
date_ingested: 2026-09-01
source_count: 0
tags: [xss, appsec, owasp, dicionario-do-programador, csrf, engenharia-social, csp, httponly, sql-injection]
skill: tech-mentor-security
status: stable
---

# XSS Attack — Dicionário do Programador (Código Fonte TV)

## TL;DR

Episódio da série "Dicionário do Programador" do [[wiki/entities/codigo-fonte-tv]], patrocinado por [[wiki/entities/alura]], introduzindo XSS (Cross-Site Scripting) do zero para quem nunca ouviu falar do termo. Usa um estudo de caso narrativo (loja de produtos para cachorro do "Bob", atacante fictícia "Cecília") para explicar reflected vs. stored XSS, fecha com estatísticas de mercado (74% dos ataques documentados em 2019 ligados a XSS; 60%+ dos sites ainda vulneráveis) e uma checklist de mitigação. É uma fonte introdutória/didática — sobrepõe-se em definição com [[wiki/sources/xss-cross-site-scripting-luiz-viana]], mas sem a demonstração técnica em laboratório (DVWA); contribui principalmente com a narrativa de engenharia social do reflected XSS e as estatísticas de mercado.

## Key Claims

**Claim:** XSS refletido (não persistente) exige um vetor de engenharia social — o payload não fica armazenado no servidor, então precisa ser entregue manualmente a cada vítima (ex.: link malicioso compartilhado).
**Evidence:** Estudo de caso completo: Cecília descobre que o parâmetro de busca da loja do Bob é refletido sem sanitização na resposta HTML, testa com `<script>alert('oi')</script>`, confirma a execução, hospeda um script de roubo de cookie em domínio próprio, ofusca o payload, encurta o link e o distribui em grupos temáticos para induzir cliques.
**Confidence:** alta — consistente com a definição de reflected XSS já documentada em [[wiki/concepts/xss]] e em `references/appsec-attacks-deep.md` da skill `tech-mentor-security`.

**Claim:** XSS persistente (armazenado) é mais perigoso que o refletido porque dispensa qualquer vetor humano — o próprio site entrega o script malicioso a quem visualiza o conteúdo afetado.
**Evidence:** Exemplo histórico de fóruns (~2000–2015): um usuário cria um tópico com título chamativo e embute `<script>` no corpo do texto; qualquer visitante do tópico executa o payload automaticamente, sem precisar clicar em link externo.
**Confidence:** alta — consistente com a definição de stored XSS já documentada em [[wiki/concepts/xss]].

**Claim:** De todos os ataques documentados em 2019, cerca de 74% estavam de alguma forma relacionados a XSS; mais de 60% dos sites existentes permanecem vulneráveis a algum ataque desse tipo.
**Evidence:** Estatística citada no vídeo sem fonte primária nomeada (ex.: relatório específico da OWASP ou de uma empresa de segurança).
**Confidence:** baixa/média — número plausível e direcionalmente consistente com XSS aparecer historicamente no OWASP Top 10, mas sem fonte primária citada nesta transcrição; não verificado nesta ingestão.

**Claim:** O nome "cross-site scripting" vem do fato de o script executado ter origem em outro site/domínio, e o navegador não ter como distinguir sozinho qual domínio é "válido".
**Evidence:** Explicação dada diretamente no vídeo ao fechar a demonstração do caso Bob/Cecília.
**Confidence:** alta — consistente com a etimologia do termo já registrada implicitamente em [[wiki/concepts/xss]].

**Claim:** O mesmo mecanismo de payload embutido na URL usado no reflected XSS também é a base de outro tipo de vulnerabilidade citada como "CSRF" (Cross-Site Request Forgery), mencionada como assunto de outro episódio da série.
**Evidence:** Trecho de áudio de transcrição incerta ("skellen Jackson") — interpretado como referência a CSRF dado o contexto (payload/estado carregado via URL, mesma superfície de exploração). Ver Open Questions.
**Confidence:** baixa — nome da vulnerabilidade citada no áudio original é foneticamente ambíguo; a normalização para "CSRF" foi uma inferência do ingest, não uma transcrição literal confiável.

**Claim:** Um checklist prático de mitigação para o cenário da loja do Bob inclui: sanitizar a entrada de busca, detectar sessões duplicadas/login simultâneo e invalidar a sessão suspeita, armazenar/exibir só os últimos dígitos do cartão, reconfirmar senha antes de alterar dados de pagamento, aplicar Content Security Policy (CSP) e marcar o cookie de sessão como `HttpOnly`.
**Evidence:** Lista de recomendações apresentada no fechamento do vídeo como resposta direta às falhas do cenário fictício.
**Confidence:** alta para os itens já triangulados na wiki (CSP, `HttpOnly`, sanitização de input — ver [[wiki/concepts/xss]]); média para os itens específicos de e-commerce (detecção de sessão duplicada, mascaramento de cartão, reconfirmação de senha), que não têm triangulação prévia na wiki de segurança.

## Entities & Concepts Touched

- [[wiki/concepts/xss]]
- [[wiki/entities/codigo-fonte-tv]]
- [[wiki/entities/alura]]
- [[wiki/concepts/sql-injection]] (mencionado como próximo episódio da série)
- [[wiki/concepts/sessoes-http-cookies]] (roubo de cookie de sessão, `HttpOnly`)
- [[wiki/concepts/confiar-no-frontend]] (princípio "nunca confie no usuário")
- [[wiki/concepts/attack-surface]]
- [[wiki/concepts/bug-bounty]] (contexto de descoberta responsável vs. maliciosa de vulnerabilidades)

## Open Questions

- A estatística "74% dos ataques em 2019 relacionados a XSS" e "60%+ dos sites vulneráveis" não cita fonte primária no vídeo — vale investigar um relatório específico (ex.: Positive Technologies, Acunetix, OWASP) numa ingestão futura dedicada a dados de mercado de vulnerabilidades.
- O nome da vulnerabilidade citada como decorrência do mesmo mecanismo de URL (transcrito foneticamente como "skellen Jackson") não pôde ser confirmado como CSRF com certeza — a transcrição automática do áudio original é ambígua nesse trecho específico. Fica como open question até uma fonte que trate CSRF explicitamente ser ingerida.
- Nenhuma página de conceito dedicada existe ainda para CSP ou CSRF na wiki — ambos aparecem aqui e em [[wiki/concepts/xss]] apenas como menção lateral dentro de outras páginas, candidatos a stub numa ingestão futura focada neles.

## Raw Quotes

> "A ideia principal do XSS é baixar algum script malicioso de uma outra fonte e executar dentro de um determinado site, de uma forma que seja compartilhável."

> "Por que chamamos de cross-site scripting? Porque o script que a gente vai executar está vindo de outro site ou de outro domínio, e o navegador não tem como saber qual é o domínio válido ou não."

> "Apesar de perigoso, é fácil de evitar: é só não confiar em nada que é enviado pelo usuário e sempre manter o controle máximo das suas aplicações."

## Key Sources (páginas que citam esta fonte)

- [[wiki/concepts/xss]]
- [[wiki/entities/codigo-fonte-tv]]
- [[wiki/entities/alura]]
- [[wiki/concepts/sql-injection]]
