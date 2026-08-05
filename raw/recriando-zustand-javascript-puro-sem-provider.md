# Recriando o Zustand com JavaScript Puro (sem Provider)

> Transcrição de vídeo (YouTube). Limpa de marcas de oralidade e erros de transcrição automática (ASR) mantendo o conteúdo técnico integral. Já em português — sem necessidade de tradução.

E se você desenvolve com React, possivelmente você conhece a lib dele chamada **Zustand** — uma lib que a gente usa bastante para evitar uma coisa chamada de **prop drilling**, ou seja, ficar passando propriedades durante a árvore do React até chegar num componente que precisa delas, de forma... bom, Zustand, Context API, Redux são soluções que se propõem a resolver essa questão do prop drilling.

Aqui nesse vídeo, hoje, a gente vai recriar o Zustand, na realidade, porém sem a necessidade de ficar usando um Provider. Dá para conseguir usar. A gente vai recriar ele de forma bem simples, usando só JavaScript e alguns macetes bons. Então fica até o final do vídeo, que eu tenho certeza que você vai gostar bastante de recriar essa funcionalidade do Zustand. Isso vai curtir para caramba esse vídeo. Valeu, roda a vinheta.

Fala, rapaziada! Pedro aqui. E, como eu falei, nesse vídeo a gente vai recriar o Zustand com JavaScript puro, sem a necessidade de ficar usando um Provider toda hora que a gente precisa usar ou criar um contexto dentro da nossa árvore, beleza?

Antes de a gente começar o vídeo, primeiro queria agradecer a vocês pelo feedback que vocês têm me dado, porque tem sido muito positivo criar os vídeos aqui para vocês. E pedir para vocês que continuem a me mandar comentários e feedback desse tipo, porque, cara, é muito valioso para mim saber que vocês estão gostando dos vídeos aqui do canal. Não esquece também de se inscrever no canal para que você possa continuar recebendo os nossos vídeos, que estão sendo lançados semana após semana, beleza?

Só que agora, sem mais delongas, vamos para o vídeo ver como a gente vai criar isso. É uma maneirinha bem fácil, tenho certeza que vocês vão gostar.

## Setup do projeto

E a galera, como vocês podem ver, eu tenho aqui uma estruturinha bem básica do `create-react-app`. Criei um projeto do zero, bem limpinho. Tenho simplesmente aqui um `App` com um `render` bem normal, sem segredo, beleza?

É aqui, nele, que a gente vai começar de fato a criar o nosso contexto. E para criar o nosso contexto, o que que eu vou fazer primeiro de tudo: eu vou dar um start aqui no meu projeto para vocês verem o que que tem atualmente nele. A gente abre aqui o browser e vamos ver que tem só um "Hello World" aqui, bem simples, bem básico — uma página em branco, sem nada demais. A gente vai começar a desenvolver aqui dentro, beleza?

## Passo 1 — `createDataSet`: o observer pattern

Primeiro de tudo, eu vou criar uma função chamada `createDataSet`. Essa função vai ser responsável por criar o nosso estado global, né — eu vou chamar de "data set" só para não confundir com o "Context do React". Beleza?

E o que que eu quero, para iniciar o nosso `DataSet`? Eu vou usar, para fazer esse gerenciamento de estado de forma global, um padrão chamado de **Observer Pattern** — o famoso pub/sub, onde a gente consegue escutar as modificações de um determinado valor e emitir modificações para esse novo valor usando os famosos **listeners**.

Dentro do meu `createDataSet` eu vou mostrar pra vocês como é que a gente faz, mas é bem simples. Primeiro eu vou criar uma função chamada `createSubscriber`. Essa função não vai receber nenhum parâmetro, e eu vou usar uma estrutura nativa do JavaScript, o **`Set`**, para criar uma estrutura de dados. Isso aqui é muito parecido com o `Array` — `Set` é uma estrutura do JavaScript muito parecida com `Array`, porém um pouco mais robusta e mais fácil de fazer gerenciamento (sem duplicados, `add`/`delete` diretos).

Então eu crio aqui os meus `listeners` como um `new Set()`. E dessa função `createSubscriber` eu vou retornar dois métodos:

- **`subscribe`**: recebe um `listener` (uma função, um callback).
- **`emit`**: recebe como parâmetro um `event` — o valor que vai ser o responsável por alterar o nosso estado.

O que eu faço: dentro de `subscribe`, eu adiciono o `listener` ao meu `Set` de `listeners` (`listeners.add(listener)`). E, como padrão dos observables, eu retorno uma função de `unsubscribe` — ou seja, quando eu executar a função que `subscribe` me retorna, eu removo aquele `listener` da minha lista (`listeners.delete(listener)`). É por isso que eu uso `Set` aqui: porque, como falei, `Set` é mais fácil de gerenciar remoção do que um `Array`.

Com isso, minha função de `subscribe` já está pronta: já consigo inscrever e também remover um listener. Agora eu só preciso terminar a função de `emit`, que nada mais é do que fazer um `forEach` sobre todos os `listeners` quando essa função é executada, passando pra cada um o `event` recebido como parâmetro.

Com essas ~14 linhas de código a gente já tem uma estrutura básica de Observer pronta.

```javascript
function createSubscriber() {
  const listeners = new Set();

  function subscribe(listener) {
    listeners.add(listener);
    return () => listeners.delete(listener);
  }

  function emit(event) {
    listeners.forEach((listener) => listener(event));
  }

  return { subscribe, emit };
}
```

A gente vai usar essa função bastante aqui no código.

## Passo 2 — `createDataSet`: o estado global fora da árvore

Agora vamos para a segunda etapa: criar a nossa função principal, que vai ser exportada — a função `createDataSet`. Essa função vai criar o estado, o valor do nosso estado global, **fora da árvore do React**. Por isso ela recebe um parâmetro `initialValue`: um valor inicial para esse estado.

A outra estrutura que eu vou usar aqui é o **`Map`**, também nativo do JavaScript, para guardar os dados do meu estado. Dentro do escopo dessa função eu também crio o meu `subscriber`, usando o `createSubscriber` que a gente acabou de fazer. E, inicialmente, já quando eu crio meu estado, eu já faço o `set` do valor inicial dentro do meu `Map` — uma chave chamada `value`, por exemplo, guardando o `initialValue` recebido como parâmetro.

`Map`, assim como `Set`, é muito parecido com o objeto do JavaScript — a diferença é que ele é um pouco mais robusto, em algumas ocasiões mais performático, e tem uma API um pouco diferente (`get`/`set` em vez de acesso por colchete).

O que eu vou fazer é simplesmente retornar o `subscriber` criado e o `map`, os dois, na minha função `createDataSet`. Dessa forma eu tenho um estado — uma "memória de dados" — criada.

```javascript
function createDataSet(initialValue) {
  const map = new Map();
  const subscriber = createSubscriber();

  map.set("value", initialValue);

  return { map, subscriber };
}
```

## Passo 3 — `useDataSet`: sincronizando o estado externo com o React

Quando eu executo essa função, o que eu preciso agora é criar alguma maneira de usar esse estado, que é externo ao React, dentro do React. Como a gente vai fazer isso? A gente vai sincronizar, usando um **Hook** que a gente vai criar, um estado local com os valores que estão sendo atualizados dentro do nosso estado global. E para isso a gente usa a função de `subscribe`.

Qual é o parâmetro que eu vou receber na minha função `useDataSet`? Eu vou receber o `dataSet` como parâmetro. Para facilitar, eu já desestruturo ele aqui e pego `map` e `subscriber`, essas duas propriedades.

Como falei, a gente vai usar o `useState` mesmo, do React, para sincronizar o estado local do meu Hook com os dados do `DataSet`. Então eu pego o `useState` do React e, como valor inicial do `state`, eu já quero o valor atual do meu `DataSet` (`map.get("value")`).

Agora eu vou usar outro Hook do React, o `useEffect`, para que eu possa fazer um `subscribe` dentro do meu `DataSet` e, toda vez que mudar os dados dele, eu atualizar o meu estado local.

O que eu vou fazer: lembra que eu falei que o retorno da função de `subscribe` é um `unsubscribe`? Então eu pego o meu `subscriber` e faço `subscribe` nele, recebendo o parâmetro `event` que é sempre passado para o listener.

E o que eu quero, primeiro de tudo: eu quero pegar o valor atual do meu `DataSet` — uso o `map.get("value")` para isso — e guardar numa variável o **próximo** valor que vai ser passado para o estado.

Aqui a gente vai checar se esse `event` é uma função — para que ele possa ser usado como callback e retornar o valor atual do estado (padrão de "updater function" do `setState`), ou se ele é simplesmente um valor comum. Como eu faço isso: com `typeof event === "function"`. Se for uma função, eu executo essa função passando o valor atual do `DataSet` como argumento; senão, eu simplesmente uso o valor que veio no `event` como o próximo valor.

Depois eu faço `map.set("value", nextValue)` (o novo valor do `DataSet` como sendo o "corrente") e atualizo o meu estado local (`setState(nextValue)`) com esse valor. Como o `Map` executa em ordem, eu seto e depois pego ele aqui, mantendo sincronizado o estado local com o estado global.

A gente retorna a função de `unsubscribe` no `return` do `useEffect`, para que toda vez que o componente seja desmontado eu também remova o meu `listener` de dentro do `subscribe`, e ele não continue sendo escutado — não continue lá na minha memória. Removo toda vez que o componente é desmontado.

Dessa forma, através do `useEffect`, a gente consegue escutar as modificações do estado global no estado local.

E a gente cria um outro cara chamado `setValue` (o vídeo fala "render" pela pronúncia, mas o papel dele é de setter). Esse cara vai receber um valor e vai simplesmente, no `subscriber`, dar um `emit` desse valor. Essa função vai ser a responsável por atualizar o estado global.

E aí, o que eu quero: eu vou seguir o padrão do `useState` do React para retornar o valor atual do estado, que está sendo sincronizado com o estado global, e também essa função de atualização (`setValue`) do estado global.

```javascript
function useDataSet(dataSet) {
  const { map, subscriber } = dataSet;
  const [state, setState] = useState(map.get("value"));

  useEffect(() => {
    return subscriber.subscribe((event) => {
      const currentValue = map.get("value");
      const nextValue =
        typeof event === "function" ? event(currentValue) : event;

      map.set("value", nextValue);
      setState(nextValue);
    });
  }, [map, subscriber]);

  function setValue(value) {
    subscriber.emit(value);
  }

  return [state, setValue];
}
```

Como vocês podem ver, com simples ~43 linhas de código, a gente recriou o Zustand de uma maneira bem simples, só com JavaScript puro.

## Exemplo prático: color picker sincronizado em toda a árvore

Para criar um exemplo legal de como esse "gritinho" da fita funciona, eu adicionei uma lib chamada `react-color`, e a gente vai fazer uma espécie de color picker dentro da aplicação. Eu crio um componente `ColorPicker`:

```javascript
import { SketchPicker } from "react-color";
import { createDataSet, useDataSet } from "./data-set";

export const colorDataSet = createDataSet("#ff7f0e"); // laranja

export function ColorPicker() {
  const [color, setColor] = useDataSet(colorDataSet);

  return (
    <SketchPicker
      color={color}
      onChange={(newColor) => setColor(newColor.hex)}
    />
  );
}
```

Importei um pequeno componente de picker do `react-color`, usei as nossas duas funções — `createDataSet` e `useDataSet` — para criar o estado global. Crio a variável `colorDataSet`, que é um `DataSet`, passando como valor inicial uma cor (laranja). Dentro do componente `ColorPicker` eu uso o `useDataSet`, passando `colorDataSet` como parâmetro, e recebo o valor da cor e o handler para atualizar toda vez que a cor mudar.

**Teste 1 — no próprio componente:** uso o `ColorPicker` direto no `App`. Atualizo a cor e ela muda — beleza, sabemos que pelo menos em um componente o estado está funcionando.

**Teste 2 — em outra parte da árvore:** crio um componente `ColorView`, que só usa `useDataSet(colorDataSet)` para pegar `colorData` e escrever o valor da cor (texto puro), para checar se bate com a outra cor:

```javascript
export function ColorView() {
  const [color] = useDataSet(colorDataSet);
  return <div>{color}</div>;
}
```

Coloco ele na árvore do React e faço o teste: mudo a cor no `ColorPicker` e o `ColorView` atualiza em tempo real — as duas cores ficam sincronizadas. Tenho um estado global compartilhado entre dois componentes, só através do Hook, sem a necessidade de criar nenhum Provider.

**Teste 3 — no topo da árvore:** será que funciona lá também? Uso `colorData` no componente raiz para mudar o `background` de uma `div`, usando a mesma cor. E funciona — o background muda junto com o color picker e o color view.

## Conclusão

Como vocês podem ver, a gente conseguiu replicar, de forma bem fácil e bem tranquila, o Zustand só com JavaScript puro, sem usar Provider. Espero que vocês tenham aprendido pelo menos um pouco sobre **Observer Pattern** e um pouco de como funciona essa estrutura de Hooks — `useState` e `useEffect` — sincronizando estado externo com estado local do React.

E também que vocês possam entender que é possível, sim, criar soluções às vezes de forma bem básica, sem muito código, e até mesmo com JavaScript puro, quando a gente pensa um pouco fora da caixa. Claro que talvez a solução não seja a melhor do mundo — você não conseguiria criar apps gigantes com ela sem cuidado. Tem alguns probleminhas: talvez concorrência (race conditions em updates simultâneos) ou alguns problemas de re-render que você pode enfrentar. Mas dá pra ver que é possível criar soluções, e às vezes é assim que nasce um projeto open-source: de uma ideia de algo que a gente pensa fora da caixa.

Comenta aqui se vocês gostaram ou não dessa solução, se vocês veem algum problema nisso, ou se, de alguma forma, gostariam de usar essa solução num projeto pra vocês. O feedback de vocês vai me ajudar muito. Não esquece de se inscrever no canal para continuar recebendo nossos vídeos. Valeu, galera, espero vocês no próximo vídeo. E é nós!
