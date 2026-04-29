---
type: concept
title: "Compound Components"
aliases: ["componentes compostos", "compound pattern React"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_count: 1
tags: [react, padrões, composição, context, design-patterns]
skill: tech-mentor-frontend
status: stable
---

# Compound Components

Padrão onde **componentes filhos compartilham estado implicitamente** com o pai via Context — sem prop drilling. API estilo `<Select.Trigger>`, `<Select.Options>`.

## Estrutura

```typescript
const SelectContext = createContext<SelectContextValue | null>(null);

function Select({ value, onChange, children }: SelectProps) {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <SelectContext.Provider value={{ value, onChange, isOpen, toggle: () => setIsOpen(o => !o) }}>
      <div>{children}</div>
    </SelectContext.Provider>
  );
}

Select.Trigger = function Trigger({ children }: { children: React.ReactNode }) {
  const { toggle, isOpen } = useContext(SelectContext)!;
  return <button onClick={toggle} aria-expanded={isOpen}>{children}</button>;
};

Select.Options = function Options({ children }: { children: React.ReactNode }) {
  const { isOpen } = useContext(SelectContext)!;
  return isOpen ? <ul role="listbox">{children}</ul> : null;
};
```

## Uso

```typescript
<Select value={status} onChange={setStatus}>
  <Select.Trigger>{status || "Selecione"}</Select.Trigger>
  <Select.Options>
    <Select.Option value="pending">Pendente</Select.Option>
  </Select.Options>
</Select>
```

## Quando usar

✅ Componentes de UI complexos com múltiplas partes coordenadas (Select, Tabs, Accordion, Modal)
✅ Quando a composição flexível é mais importante que uma API simples
❌ Componentes simples sem subpartes — over-engineering

## Ver também

- [[context-api]] — mecanismo subjacente
- [[custom-hooks]] — alternativa para compartilhar lógica sem subcomponentes

## Key Sources

- [[wiki/sources/react-tudo-que-voce-precisa-saber]]
