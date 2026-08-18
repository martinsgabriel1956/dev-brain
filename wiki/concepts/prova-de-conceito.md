---
type: concept
title: "Prova de Conceito (PoC)"
aliases: ["proof of concept", "PoC", "protótipo técnico", "spike"]
date_created: 2026-04-22
date_updated: 2026-08-18
source_count: 3
tags: [processo, tecnologia, inovação, risco, protótipo]
skill: tech-mentor-leadership
status: stable
---

# Prova de Conceito (PoC)

Projeto pequeno e isolado para **testar uma tecnologia ou abordagem nova antes de adotá-la em produção**. Mata a ansiedade de "quero usar isso" sem colocar sistemas consolidados em risco.

## O problema que resolve

Devs tendem a querer usar tecnologias novas por ansiedade, não por necessidade do cliente. Adotar tecnologia em beta ou recém-lançada em projetos grandes e consolidados é amadorismo — o produto tem muito a perder.

```
❌ Usar tecnologia nova diretamente em produção consolidada
   Motivo real: ansiedade de usar algo novo
   Resultado: instabilidade, bugs de borda, legado difícil de manter

✅ PoC isolada primeiro
   Resultado: ansiedade saciada, aprendizado real, decisão informada
```

## Quando uma tecnologia vai de PoC para produção

- PoC funcionou e os trade-offs são aceitáveis
- A tecnologia saiu de beta / tem histórico de estabilidade
- O ganho para o cliente/produto é claro e mensurável
- O time tem capacidade de manter

## Formato de uma boa PoC

1. **Escopo mínimo** — problema específico, não reescrever tudo
2. **Timeboxed** — 1-3 dias, não semanas
3. **Critérios de sucesso definidos antes** — o que você quer validar?
4. **Descartável por padrão** — código de PoC raramente vai para produção diretamente

## Conexão com flexibilidade técnica

Fazer PoCs regularmente evita virar o dev que "sempre usa X" porque nunca experimentou alternativas — ver [[flexibilidade-tecnica]].

## Escala Realista Também é Escopo Mínimo — POC de Migração de Arquitetura

[[wiki/sources/ciclo-de-mudanca-de-arquitetura]] adiciona uma restrição específica para PoCs que validam mudança de arquitetura (troca de banco, novo padrão de mensageria, etc.): "escopo mínimo" não pode significar "escala irrealista". Se o sistema precisa suportar 10.000 transações por segundo, testar a PoC com 500 TPS e considerar validado é um teste inválido — o comportamento sob carga real (principalmente na camada de dados) é frequentemente o próprio objeto do teste. A fonte recomenda me aproximar do volume real esperado (1.000, 5.000, 10.000, e se possível acima) para revelar como o comportamento muda, sem exigir cobertura de 100% dos cenários. Essa mesma fonte também reforça a ordem já implícita nesta página: PoC vem antes do MVP, não o contrário — MVP é a entrega incremental que só começa depois que a PoC validou a abordagem.

## PoC Como Pré-Requisito de Estimativa (Não Só de Adoção de Tecnologia)

[[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] usa a PoC num contexto ligeiramente diferente das seções acima: não para decidir se adotar uma tecnologia nova, mas para **tornar uma estimativa possível** quando parte do sistema envolve algo desconhecido. Antes de estimar uma feature com incerteza real (ex.: gerar PDFs em escala para 1 milhão de clientes), a fonte recomenda uma PoC isolada em cada presunção desconhecida (a lib de PDF resolve o formato desejado? o banco de dados aguenta a carga de leitura?) — sem isso, qualquer número dado é um chute disfarçado de estimativa. A fonte também nota que uma PoC nem sempre precisa ser código executado: ler relatos de terceiros que já resolveram um problema semelhante pode dar ~95% de confiança de viabilidade, funcionando como um substituto mais barato da PoC quando o objetivo é só reduzir incerteza, não validar uma decisão de adoção de longo prazo. Ver [[wiki/concepts/reducao-de-incerteza-antes-de-estimar]] para o método completo.

## Key Sources

- [[wiki/sources/desenvolvedor-acima-da-media-10-itens]]
- [[wiki/sources/ciclo-de-mudanca-de-arquitetura]] — PoC de migração de arquitetura precisa ser testada na escala real esperada, não numa fração dela
- [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] — PoC como redução de incerteza pré-estimativa, não só validação de tecnologia nova
