---
type: source
title: "NLW #2 com Diego Fernandes, dia 5: listagem, filtros, API e favoritos no app mobile do Proffy"
aliases: ["NLW 2 Diego dia 5", "Proffy mobile favoritos", "Proffy AsyncStorage", "NLW 2 trilha React dia 5"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [react-native, expo, mobile, typescript, scrollview, textinput, axios, endereco-ip, async-storage, favoritos, linking, deep-link, whatsapp, useFocusEffect, useState, estado-derivado-de-prop, react-node, context-api, react-navigation, gesture-handler, desafios, frontend, tech-mentor-frontend, rocketseat, proffy, iniciante]
skill: tech-mentor-mobile
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2 com Diego Fernandes, dia 5: listagem, filtros, API e favoritos no app mobile do Proffy

## TL;DR

Última aula (cerca de 1h34) da trilha de [[wiki/entities/diego-fernandes]] na [[wiki/entities/next-level-week|NLW #2]]. Ela termina o app do [[wiki/sources/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy|dia 4]] e o liga à API do [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy|dia 2]], reaproveitando o código web do [[wiki/sources/nlw-2-diego-fernandes-dia-3-formulario-estado-axios-proffy|dia 3]] quase linha a linha ("é muito igual ao React"):

1. **A interface.**
   - `TeacherItem` com avatar remoto (`source={{ uri }}`, com largura e altura obrigatórias), bio, preço e dois `RectButton` (favoritar, em vermelho quando ativo, e "Entrar em contato").
   - Lista em `ScrollView` com `contentContainerStyle`.
   - Filtros por `TextInput` dentro do `PageHeader` (`children`), escondidos atrás de um ícone Feather passado como `headerRight: ReactNode`.
2. **A API.**
   - [[wiki/entities/axios]] com o IP da máquina na rede, e não `localhost` ([[wiki/concepts/endereco-ip]]).
   - Total de conexões copiado da web.
   - `onChangeText` no lugar de `onChange`, e `api.get('classes', { params })`.
   - Contato com `Linking.openURL('whatsapp://send?phone=...')` ([[wiki/concepts/mobile-deep-links]]) e `post('connections')`.
3. **Favoritos em [[wiki/concepts/mobile-armazenamento-local|AsyncStorage]].**
   - JSON com os professores, ids para marcar a lista e `useState(favorited)` no item.
   - Adicionar com `push`, remover com `findIndex` + `splice`.
   - A aba Favoritos usa `useFocusEffect`.
   - Sobra um caso desatualizado entre abas, que Diego deixa para a [[wiki/concepts/context-api]].

A aula fecha com a "versão 2.0" de desafios (login, cadastro, perfil, upload, paginação infinita, onboarding, picker, cadastro de aulas no app).

## Key Claims

### TeacherItem e a lista

- **Componente compartilhado** entre Proffys e Favoritos, como na web. Ver [[wiki/concepts/componentizacao]].
- **Imagem remota:** `source={{ uri: 'https://github.com/diego3g.png' }}`. As chaves duplas são "JavaScript" + "objeto". Imagens externas "não são exibidas em tela até a gente colocar uma largura e altura nelas" (64 × 64). Um `backgroundColor` no avatar "dá uma sensação que está carregando".
- **Bordas sem atalho:** no RN "a gente não tem a propriedade border", então são `borderWidth` e `borderColor` separados. O `overflow: 'hidden'` faz o rodapé colorido respeitar o `borderRadius`.
- **Detalhes de texto:** espaçamento com `{'   '}` em vez de `marginLeft`, e o preço como `Text` aninhado. O favoritar tem fundo roxo (vermelho `#E33D3D` quando favoritado, por um estilo extra no array) e o contato tem fundo verde com `flex: 1`.
- **Lista:** `ScrollView` "da maneira mais fácil possível", com "formas mais avançadas" para depois. `marginTop: -40` sobe a lista sobre o header, e `contentContainerStyle={{ paddingHorizontal: 16, paddingBottom: 16 }}`, porque o padding no `style` "não manteve o padding embaixo". Ver [[wiki/concepts/mobile-performance-listas]].

### Filtros no cabeçalho

- **Os campos são obrigatórios, não filtro:** Diego não mostra todos os professores para depois filtrar. "O usuário precisa preencher para daí mostrar a lista." Por isso o botão "Filtrar por dia, hora e matéria" do layout sai ("eu acabei não repassando isso para o Thiago").
- **`children` no `PageHeader`,** como na web, com label (Poppins), `TextInput` de altura 54 com `placeholderTextColor` e dia e horário lado a lado com `48%` e `space-between`.
- **Texto em vez de select:** "matéria", "segunda-feira", "9:00" digitados, porque bibliotecas externas "acabam atualizando e depreciando". A recomendação para depois é o `@react-native-picker/picker`, com rolagem num modal no iOS. Ver as tensões.
- **Mostrar e esconder:**
  - `const [isFiltersVisible, setIsFiltersVisible] = useState(false)` e `{isFiltersVisible && (<View>...</View>)}` ([[wiki/concepts/renderizacao-condicional]]).
  - O botão é um ícone `Feather name="filter"` num `BorderlessButton`, passado ao header por uma prop nova, `headerRight?: ReactNode`: "eu posso receber um componente como uma propriedade". Ver [[wiki/concepts/props-react]].
  - O toggle é `setIsFiltersVisible(!isFiltersVisible)`, e depois do submit a lista fecha os filtros.

### Conexão com a API

- **`services/api.ts`** com `axios.create({ baseURL: 'http://192.168.x.x:3333' })`: o IP do painel do Expo, sem o `exp://` e com a porta do Node. "No emulador o localhost não vai funcionar [...] e no seu dispositivo físico também." Ver [[wiki/entities/axios]], [[wiki/concepts/endereco-ip]] e [[wiki/concepts/mobile-chamadas-http]].
- **Total de conexões:** o `useState` + `useEffect` do front web é colado na landing e funciona igual. "A gente usou a mesma sintaxe de código que a gente usa na web."
- **Inputs controlados:** `value` + `onChangeText={text => setSubject(text)}`, que "vai receber diretamente o texto digitado", ao contrário do `e.target.value` da web. Ver [[wiki/concepts/componente-controlado]].
- **A busca que "não aconteceu":** "eu sou uma batata". O back-end espera `week_day` numérico (0 a 6), e o campo de texto mandava "segunda-feira". Com "1", a busca funciona. Ver [[wiki/concepts/validacao-de-entrada]].
- **Renderização:** `teachers.map((teacher: Teacher) => <TeacherItem key={teacher.id} teacher={teacher} />)`, com a `interface Teacher` copiada da web e `React.FC<TeacherItemProps>`. "Seria legal a gente colocar uma mensagem de vazio."

### Contato pelo WhatsApp

- **Deep linking** é "basicamente uma aplicação abrir outra", e a "grande maioria das aplicações comerciais" tem uma URL. O código faz `Linking.openURL(`whatsapp://send?phone=${teacher.whatsapp}`)`.
- **Teste no celular físico,** porque no emulador não há WhatsApp. O app abre (o número do Vini é falso de propósito). Ver [[wiki/concepts/mobile-deep-links]].
- **Conexão no clique:** `api.post('connections', { user_id: teacher.id })` em `handleLinkToWhatsapp`. No emulador, sem WhatsApp, aparece "um errinho", mas o contador sobe de 8 para 9.

### Favoritos

- **AsyncStorage** (`expo install @react-native-community/async-storage`) não é "um banco relacional [...] a única coisa que eu posso salvar nele são dados em texto", então a lista vira JSON (`JSON.stringify`/`JSON.parse`) sob a chave `favorites`. Ver [[wiki/concepts/mobile-armazenamento-local]] e [[wiki/concepts/json]].
- **Marcar os favoritos na lista:**
  - O `TeacherList` lê o storage, guarda só os ids (`favoritedTeachers.map(t => t.id)`, com `useState<number[]>`) e passa `favorited={favorites.includes(teacher.id)}`.
  - A leitura vai para `loadFavorites()` chamado no submit, porque no `useEffect([])` a lista ficava velha.
- **Toggle no item:**
  - `const [isFavorited, setIsFavorited] = useState(favorited)`. "Sempre que alguma coisa pode mudar e ela precisa ser manipulada pelo usuário, isso precisa estar no estado"; a prop "eu não posso [...] modificar o valor dela diretamente". Ver [[wiki/concepts/useState]] e as tensões.
  - `handleToggleFavorite` é `async`: lê `favorites`, faz `JSON.parse`, depois `push(teacher)` para adicionar ou `findIndex(t => t.id === teacher.id)` + `splice(index, 1)` para remover, e salva com `setItem(..., JSON.stringify(...))`. A lógica foi feita "totalmente do zero agora".
  - Ícone e estilo mudam por ternário.
- **Aba Favoritos:** carrega objetos inteiros, e não ids ("eu preciso mostrar todos os dados deles"), com `<TeacherItem favorited />`. Diego explica o booleano assim: "se eu quero botar alguma coisa true no React, é só não passar nada" (ver as tensões).
- **Abas não remontam:** "as abas meio que elas já existem desde o começo", então o `useEffect` não roda de novo. A saída é `useFocusEffect` (`@react-navigation/native`), "executado toda vez que a tela entrar em foco". Ver [[wiki/concepts/mobile-navegacao]].
- **Sobra um caso:** tirar dos favoritos na aba Favoritos não atualiza o coração já desenhado na aba Proffys, nem com um `useFocusEffect` lá. "Eu não vou conseguir fazer isso aqui sem utilizar contexto no React" (Context API, Redux, "biblioteca de gerenciamento de estado"). Ver [[wiki/concepts/context-api]] e [[wiki/concepts/mobile-state-management-global]].

### Versão 2.0 (desafios)

- **Web:** login com e-mail e senha (mostrar senha, "lembrar" na sessão ou persistente), cadastro, esqueci minha senha (link por e-mail), avatar e "sair" no topo, um mesmo usuário podendo ser aluno e professor, upload de avatar, perfil editável que preenche o cadastro de aula (com bio por aula), total de professores, horários no card e paginação infinita ("esses são todos os resultados"). Ver [[wiki/concepts/infinite-query]].
- **Mobile:** splash screen, onboarding só na primeira vez, login com `KeyboardAvoidingView`, cadastro em duas etapas, header com título, horários no card, contadores, picker nos filtros, perfil e cadastro de aulas no app.
- **Material:** um Notion com os requisitos, o layout no Figma e os conteúdos da Rocketseat para cada funcionalidade, "sem prazo".

## Tensões e precisões

- **`useState(favorited)` explica o bug que sobrou.** O valor inicial do `useState` só vale na montagem. Quando o `TeacherList` recarrega `favorites` (no submit ou no `useFocusEffect`), o `TeacherItem` já montado recebe a prop nova e ignora, porque `isFavorited` continua com o valor antigo. Era isso que o "ele deveria ter tirado" esbarrava, antes de precisar de Context.
  - Saída simples: uma fonte de verdade só, com o `TeacherList` dono dos ids e o item recebendo `favorited` + `onToggle` ([[wiki/concepts/levantamento-de-estado]]).
  - Para sincronizar entre abas: Context ou um store (Zustand) sobre o AsyncStorage `[skill: tech-mentor-mobile]`.
  - Ver [[wiki/concepts/useState]] e [[wiki/concepts/props-react]].
- **`useFocusEffect` sem `useCallback`.** A documentação pede `useFocusEffect(React.useCallback(() => { ... }, []))`, porque o hook roda de novo sempre que a função muda `[external]` (https://reactnavigation.org/docs/use-focus-effect/). Com uma função nova a cada render, e o `loadFavorites` chamando `setFavorites` com array novo, a tela tende a reler o storage em laço enquanto estiver em foco `[inferência, não testado]`. Ver [[wiki/concepts/useEffect]].
- **`splice(-1, 1)` apaga o último.** Se `findIndex` não acha o professor (storage e estado fora de sincronia, como no caso entre abas), devolve −1, e `splice(-1, 1)` remove o último favorito da lista, outro professor. O certo é `filter(t => t.id !== teacher.id)`. Ver [[wiki/concepts/imutabilidade]].
- **Guardar o objeto inteiro deixa o favorito desatualizado.** Preço, bio e WhatsApp ficam congelados no momento em que o professor foi favoritado. Guardar ids e buscar os dados na API (ou revalidar) evita isso. Também não há `try/catch` no `JSON.parse` nem proteção contra dois toques rápidos (ler, alterar, gravar). Ver [[wiki/concepts/mobile-armazenamento-local]] e [[wiki/concepts/server-state]].
- **`ScrollView` renderiza tudo.** Para listas que crescem (e a 2.0 pede paginação infinita), `FlatList` ou FlashList virtualizam e só montam o que está visível `[skill: tech-mentor-mobile]`. Ver [[wiki/concepts/mobile-performance-listas]].
- **"Não passar nada" não é `true`.** Escrever só o nome da prop (`<TeacherItem favorited />`) é o atalho booleano do JSX e vale `true`. Omitir a prop é `undefined`. A frase da aula diz o contrário do que o código faz.
- **Deep link sem verificação.** `Linking.openURL` rejeita se o WhatsApp não estiver instalado, e o "errinho" é uma promise rejeitada sem `catch`.
  - `Linking.canOpenURL` exige declarar o esquema (`LSApplicationQueriesSchemes` no iOS, `<queries>` no Android 11+).
  - A alternativa mais robusta é o link universal `https://wa.me/<número>`, que cai no navegador se o app não existir (o "click to chat" da documentação do WhatsApp) `[external, não verificado nesta sessão]`.
  - O número também precisa estar normalizado (DDI e só dígitos), a mesma lacuna da web.
  - Ver [[wiki/concepts/mobile-deep-links]].
- **A conexão conta tentativas.** O `post('connections')` vai antes de saber se o WhatsApp abriu: no emulador, o contato falhou e o contador subiu.
- **O IP fixo no código** muda a cada rede (e a cada pessoa da equipe). O emulador Android também alcança o host por `10.0.2.2`. A forma usual é tirar o host de variável de ambiente ou do `expo-constants` (`hostUri`). Ver [[wiki/concepts/endereco-ip]] e [[wiki/concepts/variaveis-de-ambiente]].
- **Filtro em texto livre** quebra com "segunda-feira", "Geografia" sem acento ou "9h". O próprio Diego tropeça nisso. Picker (ou ao menos `keyboardType` e máscara) e validação no back-end são a correção. Ver [[wiki/concepts/validacao-de-entrada]].
- **APIs que mudaram.** O pacote `@react-native-community/async-storage` virou `@react-native-async-storage/async-storage` `[external]` (https://react-native-async-storage.github.io/async-storage/docs/install/). O `useFocusEffect` continua, e o `React.FC` tem as ressalvas de sempre.
- **Busca e lista sem estados de interface:** sem loading, sem erro (o `await` sem `catch` volta a aparecer) e sem lista vazia. O próprio Diego aponta a falta da "mensagem de vazio".
- **Positivos:** reaproveitamento explícito do código web, prop `ReactNode` para compor o header, `contentContainerStyle` explicado, a regra "o que o usuário altera vai para o estado", toggle de favorito com persistência e o reconhecimento honesto do limite sem estado global.

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/react-native]]: ScrollView, TextInput, Linking
- [[wiki/entities/expo]]: `expo install`, painel com IP e Metro
- [[wiki/entities/react-navigation]]: `useFocusEffect`
- [[wiki/entities/axios]]: cliente HTTP com o IP da máquina
- [[wiki/entities/insomnia]]: conferir que o servidor está de pé
- [[wiki/entities/figma]]: layout da versão 2.0
- [[wiki/entities/next-level-week]], [[wiki/entities/rocketseat]]

Citados sem página: AsyncStorage (`@react-native-community/async-storage`), React Native Gesture Handler (RectButton, BorderlessButton), Feather Icons e Ionicons (`@expo/vector-icons`), React Native Picker, Modal, Context API, Redux, KeyboardAvoidingView, WhatsApp, Vini Fraga, Thiago/Tiago (designer), Joseph, Giovana, OBS, Vivaldi.

## Conceitos

[[wiki/concepts/mobile-armazenamento-local]] · [[wiki/concepts/mobile-deep-links]] · [[wiki/concepts/mobile-performance-listas]] · [[wiki/concepts/mobile-chamadas-http]] · [[wiki/concepts/mobile-navegacao]] · [[wiki/concepts/mobile-state-management-global]] · [[wiki/concepts/context-api]] · [[wiki/concepts/levantamento-de-estado]] · [[wiki/concepts/useState]] · [[wiki/concepts/useEffect]] · [[wiki/concepts/props-react]] · [[wiki/concepts/componentizacao]] · [[wiki/concepts/componente-controlado]] · [[wiki/concepts/renderizacao-condicional]] · [[wiki/concepts/imutabilidade]] · [[wiki/concepts/json]] · [[wiki/concepts/endereco-ip]] · [[wiki/concepts/variaveis-de-ambiente]] · [[wiki/concepts/validacao-de-entrada]] · [[wiki/concepts/server-state]] · [[wiki/concepts/infinite-query]]

## Open Questions

- **Fecha a trilha da NLW #2:** dias 1 a 5 ingeridos (web, API, front conectado, app mobile em duas partes). A comparação das duas trilhas da NLW #2 está em [[wiki/questions/nlw-2-duas-trilhas-proffy-comparacao]]. Segue sem página a comparação das duas edições do Diego (Ecoleta × Proffy).
- O laço do `useFocusEffect` sem `useCallback` é inferido pela documentação; não aparece na gravação.
- A legenda trocou `headerRight` por "HeaderWrite" e "pickers" por "speakers"; o raw corrigiu. "Diego Química" e "No word dele é unfavorite" (o corretor ortográfico do editor) ficaram como dito.
- Data provável: 7 de agosto de 2020 `[external, não verificado]`.
