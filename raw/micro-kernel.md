---
date: 2026-04-17
tags: [tech-mentor, arquitetura, estilos-arquiteturais]
skill: tech-mentor-system-design/references/architecture-styles
level: intermediário
---

# Micro-Kernel Architecture

## Contexto
Também chamado de **Plugin Architecture**, é o estilo onde um **core mínimo e estável** concentra apenas a lógica essencial do sistema, e toda funcionalidade adicional chega via **plugins registrados dinamicamente**. Comum em IDEs (VS Code, IntelliJ), browsers, sistemas de pagamento com múltiplos provedores e plataformas extensíveis.

A questão central que esse estilo resolve: como entregar um sistema extensível sem que o núcleo quebre a cada nova funcionalidade?

## Como Funciona

```
┌─────────────────────────────────┐
│          Plugin Registry        │
│  plugin-a | plugin-b | plugin-c │
└──────────────┬──────────────────┘
               │ register / discover
┌──────────────▼──────────────────┐
│           Core System           │
│  - Plugin contract (interface)  │
│  - Lifecycle management         │
│  - Routing / dispatch           │
│  - Shared services              │
└─────────────────────────────────┘
```

O **Core** define:
- A interface/contrato que todo plugin deve implementar
- O mecanismo de registro (dinâmico em runtime ou estático em build)
- Ciclo de vida: `init → execute → teardown`

Os **Plugins** encapsulam feature completa e são independentes entre si. Comunicam com o core, nunca diretamente entre si — isso evita acoplamento cruzado.

## Código de Referência

```typescript
// Contrato do plugin
type Plugin = {
  name: string;
  version: string;
  execute: (context: PluginContext) => Promise<void>;
  teardown?: () => Promise<void>;
};

type PluginContext = {
  config: Record<string, unknown>;
  logger: Logger;
  emitEvent: (event: string, payload: unknown) => void;
};

// Core system
class PluginCore {
  private plugins = new Map<string, Plugin>();

  register(plugin: Plugin) {
    if (this.plugins.has(plugin.name)) {
      throw new Error(`Plugin ${plugin.name} already registered`);
    }
    this.plugins.set(plugin.name, plugin);
  }

  async run(context: PluginContext) {
    for (const plugin of this.plugins.values()) {
      await plugin.execute(context);
    }
  }

  async shutdown() {
    for (const plugin of this.plugins.values()) {
      await plugin.teardown?.();
    }
  }
}

// Plugin de exemplo: provider de pagamento
const stripePlugin: Plugin = {
  name: "stripe-payment",
  version: "1.0.0",
  async execute(ctx) {
    ctx.logger.info({ message: "Stripe plugin initialized" });
    ctx.emitEvent("payment.provider.ready", { provider: "stripe" });
  }
};

const core = new PluginCore();
core.register(stripePlugin);
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Extensibilidade | Adiciona feature sem tocar no core | Contrato do plugin é difícil de evoluir |
| Isolamento | Plugins falham de forma isolada | Debug cross-plugin é complexo |
| Deploy | Plugin pode ser entregue independente | Compatibilidade de versão vira problema |
| Testabilidade | Core testável sem plugins; plugins mockáveis | Testes de integração precisam do core |
| Complexidade | Core permanece pequeno e estável | Registry e lifecycle adicionam indireção |

## Quando Usar / Quando Evitar

**Usar quando:**
- O produto precisa ser extensível por terceiros (marketplace de integrações)
- Há múltiplas variantes de uma funcionalidade que não podem coexistir no core (ex: N provedores de pagamento)
- Times diferentes mantêm partes diferentes do sistema com contratos bem definidos

**Evitar quando:**
- O sistema tem features fixas e o conjunto de funcionalidades muda raramente
- A performance é crítica — o overhead de dispatch e registro pode ser relevante
- Não há maturidade suficiente para definir e manter contratos estáveis

## Conceitos Relacionados
[[hexagonal-architecture]] · [[clean-architecture]] · [[design-patterns-gof]] · [[microsservicos]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
