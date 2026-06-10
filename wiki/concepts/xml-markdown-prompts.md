---
type: concept
title: "XML + Markdown em Prompts"
aliases: ["xml markdown prompts", "structured prompts", "template xml markdown"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [prompt-engineering, xml, markdown, template, estruturacao]
skill: tech-mentor-ai
status: draft
---

# XML + Markdown em Prompts

Técnica de estruturação de prompts que combina **tags XML** (para delimitar blocos e criar referências) com **Markdown** (para hierarquia e formatação). Recomendada por pesquisas da Anthropic e OpenAI para tarefas complexas. Funciona melhor que Markdown puro ou XML puro para prompts de spec-driven.

## Por que Não Markdown Puro?

Markdown não permite criar referências entre seções. Se quero mencionar "a tarefa" em cinco lugares diferentes, precisaria repetir o nome da tarefa cinco vezes — ou criar alguma gambiarra. Com XML, defino `<task>Nome da Tarefa</task>` uma vez e referencio a tag nas outras seções.

## Por que Não XML Puro?

XML aninhado fica ilegível e remete ao trauma de SOAP/EJB. O objetivo é leveza estrutural, não serialização de dados. Markdown resolve a legibilidade.

## A Combinação

```xml
<task>Painel de Clima com Geolocalização</task>

## Requirements
- O usuário pode pesquisar por cidade
- Dados obtidos via OpenMeteo API (gratuita)
- Backend faz o proxy; frontend não acessa API diretamente
- Suporte a geolocalização automática

## API Contract
### GET /weather?city={city}
Response: { temperature, humidity, wind_speed, forecast_7days }

## UI/UX
- Layout responsivo, mobile-first
- Background gradiente dinâmico conforme temperatura/clima
- Ícones representando condição climática

## Constraints
- **Faça**: separar cada componente React em arquivo próprio
- **Nunca faça**: acessar OpenMeteo diretamente no frontend
- **Nunca faça**: componentes > 150 linhas

## Acceptance Criteria
- [ ] Cidade pesquisada retorna temperatura atual
- [ ] Previsão de 7 dias exibe min/máx
- [ ] Geolocalização detecta cidade automaticamente
```

## Regras da Técnica

1. **Tags não precisam ser fechadas**: é probabilístico, não sintático — o modelo entende igual
2. **Nomes de tags são livres**: `<task>`, `<context>`, `<erro>` — pode ser em qualquer idioma
3. **Não é XML compilado**: nenhum parser vai validar; funciona como delimitador semântico
4. **Hierarquia**: use Markdown headings (##, ###) dentro das seções XML
5. **Referência**: `<task>` definido no topo pode ser mencionado em qualquer seção para criar coesão

## Workflow de Geração

Em vez de escrever o template do zero, use o próprio LLM:

1. Escrever prompt inicial simples (vago)
2. Criar template com as seções desejadas (placeholders)
3. Pedir: "converta o prompt na estrutura do template e salve em prompt2.md"
4. Iterar sobre o arquivo gerado: adicionar seções, refinar restrições
5. Executar a spec resultante em sessão limpa

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
