---
type: concept
title: "Degradação de Contexto"
aliases: ["context degradation", "lost in the middle", "degradação janela contexto"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [contexto, degradacao, janela-de-contexto, llm, qualidade]
skill: tech-mentor-ai
status: stable
---

# Degradação de Contexto

Fenômeno em que a qualidade das respostas do LLM cai significativamente quando a [[wiki/concepts/janela-de-contexto]] está muito preenchida. Todos os modelos de 1M de tokens degradam consideravelmente após ~400k tokens, independente dos claims dos fabricantes.

## Mecanismo

O Transformer usa **mecanismo de atenção**: cada token presta atenção a todos os outros no contexto. Com muita informação acumulada — especialmente informação irrelevante ou de múltiplas threads misturadas — o modelo começa a "confundir" contextos, como uma pessoa tentando ouvir três conversas simultâneas.

**Lost in the Middle**: informações no meio de um contexto longo recebem menos atenção que as extremidades (início e fim). Isso é um efeito de pesquisa já documentado. Ver referências de LLM context explosion.

## Números Práticos

- Limiar crítico (2026): **~400k tokens** — após esse ponto, todos os modelos de 1M degradam "consideravelmente"
- Exemplo: modelo com qualidade basal 92% → após degradação severa pode cair para ~65%, pior que muitos modelos open source
- Anthropic publicou research afirmando que o Opus não degrada — Pedro Nauke contesta por experiência prática

## Consequências

1. **Custo**: cada requisição manda o contexto inteiro ao provider; tokens acumulados = custo acumulado
2. **Qualidade**: respostas menos precisas, mais alucinações, contradições internas
3. **Loop infinito**: modelo pode entrar em loop de tool calls desnecessários tentando re-encontrar informações que já tinha

## Mitigações

### Auto-compact
Configurar o harness para compactar automaticamente ao atingir ~400k tokens. O harness gera um resumo do contexto, descartando o histórico detalhado.

```
# Claude Code — ajuste em settings
compact_threshold: 400000
```

### Skills e Templates
Em vez de manter um contexto longo com instruções repetitivas, criar uma [[wiki/concepts/harness#skills|skill]] que é carregada em cada sessão nova. Exemplo: Branas fez isso para criar slides — em vez de reiterar estilo em cada prompt, criou uma skill de "criar slide" com todos os modelos.

### `/clear` + Nova Sessão
Limpar o contexto antes de mudar de tarefa, mesmo que ainda haja tokens disponíveis. O contexto sobrando não compensa a degradação de atenção.

### Contexto Enxuto
Não carregar todo o código-fonte. Carregar só os arquivos relevantes para a tarefa atual. Contexto irrelevante não ajuda — atrapalha.

## Antipadrão: "Tenho 1M de tokens, vou usar todos"

Ter uma janela grande não significa que devo preenchê-la. Quanto mais informação irrelevante, menor a qualidade. A janela grande é uma rede de segurança para tarefas longas, não uma licença para acumular lixo.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
