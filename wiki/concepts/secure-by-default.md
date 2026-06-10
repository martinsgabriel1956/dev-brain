---
type: concept
title: "Secure by Default"
aliases: ["secure defaults", "defaults seguros", "fail-secure", "segurança por padrão"]
date_created: 2026-06-10
date_updated: 2026-06-10
source_count: 1
tags: [security, secure-defaults, appsec, ux-seguranca, defense-in-depth]
skill: tech-mentor-security
status: stable
---

# Secure by Default

O estado padrão de um sistema deve ser o mais seguro possível. O usuário pode explicitamente optar por uma configuração menos restritiva — mas o padrão nunca pode ser inseguro.

## O Princípio

**Fail-secure:** quando algo falha ou não está configurado, o comportamento padrão deve negar acesso, não permitir.

```
// ❌ Fail-open — se a autenticação falha, permite acesso
function authorize(token) {
  try { return verifyToken(token); }
  catch { return true; }  // erro → acesso liberado
}

// ✅ Fail-secure — se a autenticação falha, nega acesso
function authorize(token) {
  try { return verifyToken(token); }
  catch { return false; }  // erro → acesso negado
}
```

## Exemplos Concretos

**Campos de senha**
O padrão é mostrar `●●●●●●`. O usuário clica no ícone de olho para revelar. A ação insegura (mostrar) requer esforço explícito.

**Deleção de recursos críticos (AWS EC2, etc.)**
Clicar em "delete" não deleta imediatamente — abre modal exigindo digitar o nome exato do recurso. Ações destrutivas exigem confirmação explícita e não-ambígua.

**Onboarding de novos funcionários**
Boas empresas exigem troca de senha padrão + ativação de 2FA na primeira semana. Se a empresa não força isso, o padrão não é seguro o suficiente.

**S3 e recursos de storage**
O padrão de qualquer recurso de storage deve ser privado. Tornar público deve ser uma ação explícita e deliberada — não o default.

## Por Que Importa

Sistemas são operados por humanos que cometem erros. Quando o default é inseguro, o erro humano é o caminho de menor resistência. Quando o default é seguro, o erro humano precisa ir contra a corrente para criar a vulnerabilidade.

## Relação com Outros Conceitos

- [[defense-in-depth]] — defaults seguros são uma das camadas de controle
- [[principio-do-menor-privilegio]] — permissão mínima é um default seguro aplicado a acessos
- [[attack-surface]] — defaults inseguros aumentam a superfície passivamente

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — exemplos: campo de senha, deleção com confirmação, 2FA no onboarding
