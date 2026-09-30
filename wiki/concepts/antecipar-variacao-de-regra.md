---
type: concept
title: "Antecipar Variação de Regra de Negócio"
aliases: ["projetar para mudança de regra", "modelar para evolução", "desconto VIP ouro prata"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [design, evolucao, regra-de-negocio, open-closed, strategy, yagni]
skill: tech-mentor-leadership
status: draft
---

# Antecipar Variação de Regra de Negócio

Hábito atribuído ao pleno: perceber que uma regra hoje binária (VIP 15% / demais 5%) provavelmente se multiplicará (ouro, prata, sazonalidade), de modo que um `if/else` simples tende a virar cascata. Soluções clássicas: [[wiki/concepts/strategy-pattern]] / polimorfismo e [[wiki/concepts/open-closed-principle]] (aceitar novas regras sem alterar as existentes). O vídeo não mostra a modelagem escolhida.

**Tensão [external]:** antecipar não é implementar todas as variações agora (YAGNI). O equilíbrio usual é manter o ponto de extensão barato — regra isolada em um lugar, nome claro — e só generalizar quando a segunda ou terceira variação aparece. Ver [[wiki/concepts/abstraction-bloat]] para o risco oposto. Dinheiro: o autor cita `double`, mas admite `BigDecimal` [external: `double` é inadequado para valores monetários].

## Key Sources

- [[wiki/sources/o-que-diferencia-pleno-de-junior-decisoes-legibilidade-modelagem]] — exemplo `calcularDesconto` e a previsão de novas faixas de cliente
