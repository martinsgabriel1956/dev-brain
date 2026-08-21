---
type: concept
title: "Coesão"
aliases: ["cohesion", "alta coesão", "baixa coesão"]
date_created: 2026-04-25
date_updated: 2026-08-18
source_count: 4
tags: [coesao, software-design, clean-code, arquitetura]
skill: tech-mentor-backend
status: stub
---

# Coesão

Coesão mede o **quanto as responsabilidades dentro de uma unidade (função, classe, módulo) estão relacionadas entre si**.

Alta coesão = tudo dentro da unidade serve ao mesmo propósito.  
Baixa coesão = a unidade mistura responsabilidades não relacionadas.

## Exemplo

```typescript
// baixa coesão — mistura parsing, validação e envio de e-mail
function processarFormulario(dados: string) {
  const parsed = JSON.parse(dados);
  if (!parsed.email) throw new Error("Email obrigatório");
  sendEmail(parsed.email, "Bem-vindo!");
}

// alta coesão — cada função tem um foco claro
function parseFormulario(dados: string): FormData { ... }
function validarFormulario(form: FormData): void { ... }
function enviarBoasVindas(email: string): void { ... }
```

## Relação com acoplamento

O alvo de design é **alta coesão dentro de módulos + baixo [[acoplamento]] entre módulos**. São conceitos complementares, não substitutos.

- Alta coesão garante que mudanças ficam localizadas dentro de um módulo
- Baixo acoplamento garante que mudanças em um módulo não afetam outros

## Relações

- [[acoplamento]] — complemento direto: coesão (interno) + acoplamento (externo)
- [[metricas-de-acoplamento]] — como o lado "acoplamento" desse par é quantificado (instabilidade I = Ce/(Ca+Ce), abstração, distância da sequência principal)
- [[single-responsibility]] — SRP é a diretriz que leva a alta coesão
- [[efeito-colateral]] — unidades com baixa coesão tendem a ter efeitos colaterais espalhados
- [[wiki/concepts/granularidade-de-mudanca]] — o mesmo critério de coesão aplicado a mudanças organizacionais e de processo, não só a código

## God Object e Data Clumps: Baixa Coesão em Dois Formatos Opostos

[[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] ilustra baixa coesão em duas direções opostas. Uma [[wiki/concepts/god-object|god object]] junta responsabilidades que deveriam estar separadas (autenticação + banco de dados + notificação na mesma classe) — coesão baixa por excesso de agrupamento indevido. Já um [[wiki/concepts/data-clumps|data clump]] é o oposto: variáveis que deveriam estar agrupadas (nome, e-mail, idade de um mesmo usuário) circulam soltas como parâmetros separados — coesão baixa por falta de agrupamento onde ele faria sentido. Os dois problemas usam o mesmo critério ("o que pertence junto deveria estar estruturalmente junto"), só que em direções contrárias.

## Além do Código: Coesão em Mudanças de Processo

O critério de coesão não se limita a funções e módulos. [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]] aplica o mesmo raciocínio a mudanças de processo ou tecnologia: ao separar uma mudança grande em partes menores, as partes precisam continuar fazendo sentido isoladamente — não é qualquer corte, é um corte coeso. Ver [[wiki/concepts/granularidade-de-mudanca]] para o desenvolvimento completo desse argumento.

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
- [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]] — coesão como critério para dividir mudanças de processo, não só código
- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] — god object (agrupamento indevido) e data clumps (falta de agrupamento devido) como baixa coesão em direções opostas
