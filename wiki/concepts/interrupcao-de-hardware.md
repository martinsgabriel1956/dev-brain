---
type: concept
title: "Interrupção de Hardware"
aliases: ["interrupt", "hardware interrupt", "IRQ", "timer interrupt"]
date_created: 2026-04-22
date_updated: 2026-08-27
source_count: 3
tags: [sistema-operacional, hardware, cs-fundamentals, lang-systems, embarcados]
skill: cs-fundamentals
status: stable
---

# Interrupção de Hardware

Sinal elétrico enviado por um dispositivo de hardware que para o que o processador está fazendo e transfere controle ao sistema operacional.

## Como funciona

```
1. Hardware dispara sinal de interrupção (IRQ)
2. CPU termina a instrução atual
3. CPU salva estado atual (program counter, registradores)
4. CPU salta para o interrupt handler do SO (ISR — Interrupt Service Routine)
5. SO processa o evento
6. SO retoma o processo anterior (ou decide trocar — context switch)
```

## Fontes comuns

| Fonte | Evento |
|---|---|
| Timer de hardware | A cada N ms — base do escalonador preemptivo |
| Teclado | Tecla pressionada |
| Disco/SSD | Leitura/escrita concluída |
| Placa de rede | Pacote recebido |
| Mouse | Movimento ou clique |

## Por que é fundamental para o SO

Sem interrupções, o SO não teria como retomar o controle de um processo em execução. Um processo poderia monopolizar o processador para sempre.

O [[concepts/escalonador]] preemptivo depende do timer interrupt para funcionar: a cada fatia de tempo, o timer dispara, o SO assume e decide quem roda em seguida.

## Software interrupt (syscall)

Além das interrupções de hardware, existe o **software interrupt** (trap): o processo voluntariamente chama o SO via [[concepts/syscall]] para pedir um serviço. O mecanismo é similar — CPU troca de modo e transfere controle ao kernel.

## Interrupções customizadas em sistemas embarcados

Em [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]], interrupções aparecem como um dos motivos concretos para se aprofundar em [[wiki/concepts/arquitetura-de-computadores]]: em [[wiki/concepts/sistemas-embarcados|sistemas embarcados]] e críticos, é comum precisar definir **interrupções customizadas** com base na leitura de sensores, o que exige entender clocks de interrupção e como configurar a **tabela de interrupções** específica do processador — o exemplo dado é o **NVIC** (Nested Vectored Interrupt Controller) do ARM. Diferente de um SO de propósito geral, onde boa parte da arquitetura pode ser abstraída, em embarcados isso não é opcional.

## Ver também

- [[concepts/escalonador]] — usa timer interrupt para preempção
- [[concepts/context-switch]] — disparado pela interrupção do timer
- [[concepts/syscall]] — interrupt voluntário do software para o kernel
- [[concepts/kernel]] — recebe controle quando a interrupção ocorre

## Key Sources

- [[sources/sistema-operacional-por-baixo-dos-panos]]
- [[sources/como-sistemas-operacionais-funcionam]]
- [[wiki/sources/guia-programacao-baixo-nivel-c-arquitetura-so-embarcados]] — interrupções customizadas em embarcados; tabela de interrupções (NVIC do ARM)
