# React 19 Memoization: Chega o Fim do useMemo e useCallback?

**Autor:** Komal Raut
**Publicação:** Front-end World (Medium)
**Data:** 25 de fevereiro de 2025
**Idioma original:** Inglês (traduzido para PT-BR)
**URL original:** https://medium.com/front-end-world/react-19-memoization-no-more-usememo-usecallback-3a09a986f9c7

---

## Introdução

Como desenvolvedores React, usamos `useMemo` e `useCallback` por anos para manter nossas aplicações eficientes e evitar re-renders desnecessários. É uma batalha constante entre saber quando otimizar e quando deixar o React fazer o trabalho dele. Mas com o React 19, esse cenário muda.

O novo **React Compiler** é uma inovação revolucionária. Ele leva a otimização a um novo nível porque o compilador vai cuidar dos otimizadores de performance sozinho, nos livrando de microgerenciar se devemos ou não fazer memoization.

Este artigo explora como a memoization funcionava antes do React 19, o que o React Compiler faz, e se ainda é necessário usar `useMemo` e `useCallback`.

---

## O Problema com Memoization Manual

### O que é Memoization no React?

Memoization é uma técnica de otimização que armazena o resultado de chamadas de função custosas e retorna o resultado em cache quando as mesmas entradas ocorrem novamente. No React, isso evita re-renders desnecessários de componentes e funções.

### Por que usávamos useMemo e useCallback?

Antes do React 19, o React recriava funções e recomputava valores a cada render, mesmo quando não era necessário. Para otimizar performance, era preciso usar manualmente:

- `useMemo` para memoizar cálculos custosos.
- `useCallback` para evitar recriação desnecessária de funções.

**Exemplo (antes do React 19):**

```jsx
import { useState, useMemo, useCallback } from "react";

function ExpensiveComponent({ num }) {
  const expensiveValue = useMemo(() => {
    console.log("Computing...!");
    return num * 2;
  }, [num]);

  const handleClick = useCallback(() => {
    console.log("Button clicked!");
  }, []);

  return (
    <div>
      <p>Computed Value: {expensiveValue}</p>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}
```

**Otimização feita manualmente:**
- Sem `useMemo`, `expensiveValue` seria recalculado a cada render.
- Da mesma forma, `useCallback` evita que `handleClick` seja recriado.

**O problema:**
- Envolver funções e valores manualmente aumenta a complexidade.
- Usar `useMemo` e `useCallback` em excesso pode, na verdade, tornar o código mais difícil de ler e manter.

---

## A Solução do React 19: Memoization Automática

Com o React 19, o novo **React Compiler** elimina a necessidade de memoization excessiva. Ele otimiza funções e valores automaticamente, reduzindo re-renders sem exigir `useMemo` e `useCallback`.

### Como o React Compiler funciona?

O React Compiler analisa os componentes e os otimiza automaticamente:

- Detectando re-renders desnecessários e pulando-os.
- Memoizando cálculos custosos por baixo dos panos.
- Garantindo referências de função estáveis para evitar que mudanças de props disparem re-renders.

**Exemplo (React 19 — sem useMemo e useCallback!):**

```jsx
function ExpensiveComponent({ num }) {
  function computeValue() {
    console.log("Computing...!");
    return num * 2;
  }

  function handleClick() {
    console.log("Button clicked!");
  }

  return (
    <div>
      <p>Computed Value: {computeValue()}</p>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}
```

**Sem memoization manual necessária:**
- O compilador otimiza automaticamente as chamadas de função e garante que `handleClick` não seja recriado desnecessariamente.

**Resultado:** código mais limpo, legível e eficiente sem trabalho extra.

---

## Ainda é preciso usar useMemo e useCallback?

Embora o React 19 reduza significativamente a necessidade de memoization manual, existem alguns casos de borda em que `useMemo` e `useCallback` ainda podem ser úteis:

### Quando ainda usar useMemo?
- Ao trabalhar com bibliotecas de terceiros que dependem de valores memoizados.
- Ao realizar cálculos extremamente custosos que as otimizações do React não capturam.

### Quando ainda usar useCallback?
- Ao passar funções para componentes que dependem de igualdade estrita de referência (ex.: componentes filhos memoizados com `React.memo`).

Na maioria dos casos, porém, eles não são mais necessários.

---

## Boas Práticas e Erros Comuns

**Boas práticas:**
- Escreva código simples primeiro e deixe o React otimizá-lo automaticamente.
- Use `useMemo` e `useCallback` com moderação, apenas quando realmente necessário.
- Teste a performance antes de otimizar — não assuma que algo está lento.

**Erros comuns:**
- Usar `useMemo` e `useCallback` em excesso sem necessidade, tornando o código mais complexo.
- Esquecer de atualizar para o React 19 antes de confiar nas otimizações automáticas.

---

## Conclusão

A memoization automática do React 19, via React Compiler, é um divisor de águas para otimização de performance. Ela simplifica o desenvolvimento eliminando re-renders desnecessários sem exigir memoization manual.

Se você ainda está otimizando tudo manualmente, é hora de atualizar e aproveitar um código React mais limpo e rápido.
