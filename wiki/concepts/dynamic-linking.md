---
type: concept
title: "Dynamic Linking"
aliases: ["linkagem dinâmica", "shared library", "biblioteca dinâmica", ".so", ".dll"]
date_created: 2026-05-02
date_updated: 2026-05-02
source_count: 1
tags: [linking, compilacao, sistemas]
skill: lang-systems
status: stable
---

# Dynamic Linking

Estratégia de linking onde o executável não copia o código das bibliotecas — apenas registra **referências** a elas. Em runtime, o sistema operacional carrega as funções necessárias no address space do processo sob demanda.

## Arquivos envolvidos

- **Unix/Linux:** Dynamic Shared Libraries com extensão `.so` (Shared Object)
- **Windows:** Dynamic Link Libraries com extensão `.dll`

Esses arquivos contêm código executável mas **não têm entry point** (sem função `main`) — não iniciam execução por conta própria.

## Como funciona em runtime

```
Processo inicia
      │
      ▼
SO lê a lista de dependências no executável
      │
      ▼
Para cada .so referenciado:
  - Se já está mapeado em memória por outro processo → compartilha o mesmo segmento físico
  - Se não está → carrega do disco, mapeia no address space do processo
      │
      ▼
Resolve os endereços (GOT/PLT — tabelas de indireção)
      │
      ▼
Processo chama a função normalmente
```

## Vantagens

- **Economia de memória:** 100 processos usando a mesma lib compartilham uma única cópia física na RAM
- **Atualização sem recompilação:** corrigir uma vuln na libc atualiza todos os programas que a usam instantaneamente
- **Binários menores:** o executável não carrega código das bibliotecas

## Desvantagens

- **"DLL Hell":** incompatibilidades de versão entre o que foi compilado e o que está instalado
- **Startup ligeiramente mais lento:** resolução de símbolos em runtime
- **Dependência de ambiente:** o binário não roda sem as libs instaladas

## Casos de uso

- Bibliotecas do sistema (libc, libssl) usadas por centenas de programas
- Plugins carregados em runtime (`dlopen()` em C, `LoadLibrary()` no Windows)
- Bibliotecas Python de C extension (`.so` carregados pelo CPython)

## Contraste

Ver [[concepts/static-linking]] para a alternativa autocontida.

## Key Sources

- [[sources/como-multiplas-linguagens-vivem-num-unico-binario]]
