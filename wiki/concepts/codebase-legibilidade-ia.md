---
type: concept
title: "Codebase Legibilidade para IA"
aliases: ["codebase para ia", "código legível ia", "qualidade código ia"]
date_created: 2026-05-04
date_updated: 2026-08-04
source_count: 5
tags: [ia-engineering, codebase-quality, acoplamento, context-engineering, coding-agents, comentarios]
skill: tech-mentor-backend
status: stable
---

# Codebase Legibilidade para IA

A qualidade do código que a IA vai interagir importa mais do que o prompt, o modelo ou a ferramenta utilizada. As mesmas técnicas que sempre tornaram código mais manutenível para humanos são as que tornam código mais legível para agentes.

> "Uma codebase boa legível para seres humanos também é uma codebase boa e legível para IAs."

## Por Que Isso Importa

Agentes de código trabalham com context window limitada. Cada arquivo aberto é tokens consumidos. Cada dependência escondida é uma chance de o agente perder contexto crítico.

Código fortemente acoplado numa god class de 20.000 linhas:
- Obriga o agente a manter muito mais contexto
- Torna impossível isolar a tarefa num módulo específico
- Aumenta a chance de o agente quebrar partes não relacionadas ao fazer uma mudança
- Dificulta o [[concepts/mental-alignment]] do dev sobre o que foi gerado

Ver [[concepts/navigation-paradox]] — agentes perdem ~25% dos arquivos críticos em arquiteturas com forte acoplamento via DI containers.

## O Que Torna Código Legível Para IA

| Característica | Bom para IA | Ruim para IA |
|---|---|---|
| Estrutura | Módulos com responsabilidade clara | God class que faz tudo |
| Acoplamento | Baixo — mudanças localizadas | Alto — mudança em A quebra B e C |
| Interfaces | Contratos explícitos (ports) | Dependências diretas e implícitas |
| Funções | Explícitas e nomeadas | Lógica inline repetida |
| Contexto por tarefa | 2–3 arquivos | 7–13 arquivos ou mais |

## Escala do Problema

Com 200 linhas, a IA entende qualquer estrutura. O problema começa quando:
- O projeto cresce para 10.000+ linhas
- Há múltiplos colaboradores (e agentes) fazendo PRs em paralelo
- Partes do sistema precisam ser substituídas
- O dev precisa voltar ao código dois meses depois

Para 200 linhas, uma god class é perfeitamente adequada. Para 20.000 linhas e quatro colaboradores, torna-se um problema real tanto para humanos quanto para modelos.

## Relação com Comprehension Debt

[[concepts/comprehension-debt]] é causado em parte por código de difícil leitura gerado por agentes. O ciclo:
1. Codebase ruim → agente gera código de baixa qualidade
2. Dev aprova sem entender completamente
3. Codebase piora
4. Próximo agente tem ainda mais dificuldade

Manter código legível quebra o ciclo na origem.

## Padrões que Ajudam

- [[concepts/hexagonal-architecture]] — ports e adapters localizam mudanças e reduzem contexto necessário por tarefa
- [[concepts/vertical-slice-architecture]] — feature-first em vez de camada-first reduz número de arquivos por feature
- [[concepts/single-responsibility-principle]] — uma razão para mudar = contexto mínimo para a IA

## MVC Monolítico como Anti-Padrão Específico

MVC com múltiplos services sem relação num diretório único é um dos piores cenários para IA: o agente precisa escanear tudo para entender qualquer coisa. Código modular por domínio (billing, identity, content) permite que o agente carregue só o módulo relevante.

Combinado com [[progressive-disclosure-ia]] — guidelines por diretório — o agente fica ainda mais focado: carrega as regras do módulo que está alterando, não de todos.

## Comentários no Código Como Sinal de Recuperação para Agentes

[[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] traz um ângulo que qualifica a tabela acima: comentários próximos ao código voltam a ter valor prático explicitamente por causa de como AI harnesses recuperam contexto. Como agentes buscam (via grep ou ferramenta equivalente) o arquivo específico que precisam alterar e então leem seu conteúdo sob demanda, um comentário explicando o quê e o porquê de um trecho é informação que o agente **efetivamente vai ler** no momento da tarefa — diferente de documentação externa (um README grande, por exemplo), que pode nunca ser recuperada na busca porque não está fisicamente perto do código sendo editado. O autor da fonte é explícito que isso o fez reconsiderar a posição clássica ("código autoexplicativo dispensa comentário") especificamente no contexto de agentes — ver [[wiki/concepts/comentarios-o-que-nao-o-como]] para a regra geral que essa observação qualifica, não substitui.

## Teto Prático de Tamanho de Arquivo: Ligado à Ferramenta, Não a Estilo

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] traz um número concreto que qualifica a linha "com 200 linhas, a IA entende qualquer estrutura" acima: o `Read` do Claude Code lê no máximo ~2000 linhas por tool call. Na prática, ~1000 linhas é considerado seguro, 2000 já é risco de leitura incompleta — independente de estilo ou de quantas funções cabem ali. A fonte é explícita que isso não é motivo para otimizar por arquivos de 50 linhas: se há uma responsabilidade só e o conteúdo pertence ali, um arquivo de 1000 linhas está OK. O problema oposto também é real e simétrico: um arquivo de 1000 linhas com **múltiplos assuntos** desperdiça a maior parte da leitura (~80%, na estimativa da fonte) em conteúdo irrelevante à tarefa — o mesmo custo por tool call, só que causado por falta de [[wiki/concepts/single-responsibility|responsabilidade única]] em vez de fragmentação excessiva.

Ver também [[wiki/concepts/codigo-grepavel]] — a mesma fonte separa dois motivos distintos para quebrar código: profundidade (estrutura interna, debate com [[wiki/entities/john-ousterhout]]) e buscabilidade (achar o arquivo/função certo de fora).

## Key Sources

- [[sources/ports-and-adapters-codebase-para-ia]]
- [[sources/navigation-paradox-2026]]
- [[wiki/sources/context-engineering-codebases-grandes-rpi]] — MVC god class vs. codebase modular; guidelines por diretório como mitigação
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — comentários próximos ao código como informação que agentes efetivamente recuperam via grep, ao contrário de documentação externa
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — teto prático de ~1000-2000 linhas por arquivo ligado ao limite de leitura por tool call, e custo simétrico de arquivo com múltiplos assuntos
