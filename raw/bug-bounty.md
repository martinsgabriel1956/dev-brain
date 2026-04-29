---
date: 2026-04-23
tags: [tech-mentor, security, ofensivo, bug-bounty, vdp, hackerone]
skill: tech-mentor-security/references/bug-bounty
level: intermediário
---

# Bug Bounty

## Contexto

Bug bounty é um programa onde organizações pagam pesquisadores de segurança externos por vulnerabilidades encontradas e reportadas de forma responsável. Para a empresa: coverage de segurança que equipes internas nunca atingiriam. Para o pesquisador: monetização de habilidades, reconhecimento e experiência com sistemas reais.

Entender como programas funcionam é útil tanto para quem quer participar quanto para quem vai estruturar o programa do próprio produto.

## Como Funciona

### Tipos de Programa

| Tipo | Característica | Exemplos |
|---|---|---|
| **Bug Bounty** | Paga por finding válido | HackerOne, Bugcrowd, Intigriti |
| **VDP** (Vulnerability Disclosure Program) | Sem pagamento, só reconhecimento | security.txt, Hall of Fame |
| **Private Program** | Convite a pesquisadores selecionados | Alta maturidade, menores volumes |
| **Public Program** | Aberto a qualquer pesquisador | Maior volume, mais triagem |

### Plataformas

```
HackerOne:   maior plataforma, Fortune 500, bounties altos
Bugcrowd:    foco enterprise, managed triage
Intigriti:   forte na Europa, compliance com GDPR
Synack:      rede curada, pesquisadores vetados
YesWeHack:   europeia, compliance-friendly
```

### Ciclo de Vida de um Report

```
1. Pesquisador descobre vulnerabilidade
2. Redige relatório (estrutura abaixo)
3. Submete via plataforma
4. Triagem (triage): plataforma ou empresa valida
   → Duplicate: já reportado
   → Informative: não é vuln ou fora de escopo
   → N/A: não reproduzível
   → Valid: aceito, move para fix
5. Fix implementado + verificado pelo pesquisador
6. Bounty pago (se programa paga)
7. Disclosure coordenado (geralmente 90 dias)
```

### Estrutura de Report de Qualidade

```markdown
## Summary
SQL Injection em /api/v2/search permite extração completa do banco de dados
sem autenticação.

## Severity
Critical — CVSS 9.8
- Attack Vector: Network
- Privileges Required: None
- User Interaction: None
- Confidentiality Impact: High

## Steps to Reproduce
1. Acesse: GET /api/v2/search?q=test
2. Modifique o parâmetro: q=test' UNION SELECT username,password FROM users--
3. Resposta retorna hashes de senha de todos os usuários

## Proof of Concept
curl -i "https://target.com/api/v2/search?q=test%27%20UNION%20SELECT%20username%2Cpassword%20FROM%20users--"

[screenshot da resposta com dados sensíveis]

## Impact
Extração completa de credenciais de usuários. Com hashes fracos (MD5),
permite comprometimento de contas em massa.

## Recommended Fix
Usar prepared statements / ORM com parametrização. Nunca concatenar
input do usuário em queries SQL.

## References
- CWE-89: Improper Neutralization of Special Elements used in SQL Command
- OWASP A03:2021 – Injection
```

### Escopo — O Que Testar e O Que Não Testar

```
IN SCOPE (típico):
  - *.example.com
  - API endpoints documentados
  - Mobile apps (iOS/Android)
  - Autenticação e autorização

OUT OF SCOPE (típico):
  - DoS / DDoS
  - Social engineering de funcionários
  - Phishing
  - Sistemas de terceiros não controlados pela empresa
  - Issues requerendo acesso físico
  - Ataques que afetam outros usuários sem consentimento

REGRAS GERAIS:
  - Não exfiltrar dados reais de usuários
  - Não deletar ou modificar dados em produção
  - Parar ao provar impacto (não explorar mais do necessário)
  - Não divulgar publicamente antes do fix
```

### CVSS — Como Calcular Severidade

```
Base Score = f(AV, AC, PR, UI, S, C, I, A)

Attack Vector (AV):    Network(N) > Adjacent(A) > Local(L) > Physical(P)
Attack Complexity (AC): Low(L) > High(H)
Privileges Required (PR): None(N) > Low(L) > High(H)
User Interaction (UI):  None(N) > Required(R)
Scope (S):             Changed(C) > Unchanged(U)
Confidentiality (C):   High(H) > Low(L) > None(N)
Integrity (I):         High(H) > Low(L) > None(N)
Availability (A):      High(H) > Low(L) > None(N)

Critical: 9.0–10.0   → IDOR sem auth em dados financeiros, RCE
High:     7.0–8.9    → SQLi com auth, SSRF interno
Medium:   4.0–6.9    → XSS stored, IDOR com auth
Low:      0.1–3.9    → Information disclosure, rate limit missing
```

### Estruturando um Programa (Perspectiva da Empresa)

```
1. Definir escopo claro (o que está in/out)
2. Definir bounty table por severidade:
   Critical: $5.000–$50.000
   High:     $1.000–$5.000
   Medium:   $250–$1.000
   Low:      $50–$250
3. SLA de resposta: acknowledge em 24h, triage em 5 dias
4. Processo de triage com time de segurança
5. Safe harbor legal — proteção para pesquisadores de boa fé
6. VDP primeiro, bounty depois (quando processo maduro)
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Coverage externa | Pesquisadores com perspectiva zero | Volume alto de reports inválidos |
| Custo variável | Paga só por findings válidos | Findings críticos podem custar muito |
| VDP sem pagamento | Zero custo, feedback útil | Atrai menos pesquisadores qualificados |
| Private vs public | Menos ruído, pesquisadores selecionados | Menor diversidade de perspectivas |

## Quando Usar / Quando Evitar

**VDP (mínimo):** qualquer produto com usuários deveria ter um canal de disclosure. É custo zero e previne pesquisadores de divulgar publicamente sem aviso.

**Bug bounty:** quando o produto tem maturidade de segurança básica (SAST, pentest periódico) e capacidade de triage. Lançar bounty sem processo mata o time com volume.

**Sequência recomendada:** security.txt + VDP → private program → public program.

## Conceitos Relacionados

[[pentest-redteam]] · [[owasp-top10]] · [[threat-modeling]] · [[incident-response]] · [[api-security]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
