---
type: concept
title: "Processo"
aliases: ["process", "PID", "process ID", "instância de programa"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [sistema-operacional, processo, concorrência, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# Processo

Instância em execução de um programa. Toda vez que você abre um programa, o SO cria um processo com identidade própria.

## Componentes

- **PID** (Process ID): número único de identificação
- **Estado**: ciclo de vida do processo
- **Espaço de memória isolado**: variáveis, código, pilha — separados de outros processos

## Ciclo de Vida

```
new → ready → running → waiting → terminated
         ↑_______________|
```

- **new**: processo sendo criado
- **ready**: preparado, aguardando CPU
- **running**: processador está executando suas instruções
- **waiting**: aguarda evento externo (leitura de disco, I/O)
- **terminated**: encerrado

## Isolamento de Memória

Navegador não consegue acessar a memória do editor de texto. Cada processo vive em seu próprio espaço de endereçamento (ver [[concepts/memoria-virtual]]).

Benefício: se um processo travar, em geral não derruba os outros.

## Processo vs Thread

| | Processo | Thread |
|---|---|---|
| Memória | Espaço separado | Compartilha com processo |
| Isolamento | Alto | Baixo |
| Custo de criação | Alto | Médio |
| Context switch | Mais caro | Menos caro |

Ver [[concepts/thread]] para a comparação completa.

## Ver também

- [[concepts/thread]] — unidade de execução dentro de um processo
- [[concepts/escalonador]] — decide qual processo roda e quando
- [[concepts/context-switch]] — troca de processo no processador
- [[concepts/memoria-virtual]] — como o espaço de memória é isolado
- [[concepts/syscall]] — como processos pedem serviços ao kernel

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
