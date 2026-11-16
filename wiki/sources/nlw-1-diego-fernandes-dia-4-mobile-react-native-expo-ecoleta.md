---
type: source
title: "NLW #1 com Diego Fernandes, dia 4: app mobile do Ecoleta com React Native e Expo"
aliases: ["NLW 1 Diego dia 4", "Ecoleta mobile", "Ecoleta React Native", "NLW 1 trilha React Native dia 4"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [react-native, expo, mobile, typescript, react-navigation, stack-navigation, react-native-maps, expo-location, expo-mail-composer, linking, deep-link, metro-bundler, stylesheet, yoga, safe-area, keyboard-avoiding-view, densidade-de-pixels, expo-google-fonts, axios, frontend, rocketseat, ecoleta, iniciante]
skill: tech-mentor-mobile
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1 com Diego Fernandes, dia 4: app mobile do Ecoleta com React Native e Expo

## TL;DR

Quarta aula (cerca de 2h12) da trilha de [[wiki/entities/diego-fernandes]] na [[wiki/entities/next-level-week|NLW #1]]. O app mobile do Ecoleta, para Android e iOS, é feito com [[wiki/entities/react-native]] e [[wiki/entities/expo]] e consome a API do [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta|dia 2]]. A aula tem duas metades:

1. **Ambiente e diferenças.**
   - `expo-cli` global, `expo init mobile` (template *blank TypeScript*) e `npm start`.
   - O [[wiki/entities/metro-bundler]] e o QR code em modo LAN, aberto pelo app Expo no celular. Alternativas: emulador (com 8 GB de RAM) ou o Snack no navegador.
   - O que muda em relação ao ReactJS:
     - `View` e `Text` no lugar das tags HTML, sem semântica.
     - Estilo em objetos JS com `StyleSheet.create`, propriedades em camelCase e números sem `px`.
     - Tudo é flexbox por padrão (via Yoga), e não há cascata nem herança de estilos.
2. **O app.**
   - **Home:** `StatusBar` e fragment, imagens em 1x/2x/3x ([[wiki/concepts/densidade-de-pixels]]), Roboto e Ubuntu via Expo Google Fonts com `AppLoading` e `ImageBackground`.
   - **Botões e navegação:** `RectButton` do react-native-gesture-handler, `@expo/vector-icons`, e o [[wiki/entities/react-navigation]] com [[wiki/concepts/navegacao-em-pilha|navegação em pilha]] (`createStackNavigator`, `headerMode="none"`, `cardStyle`, `useNavigation`).
   - **Tela do mapa:** [[wiki/entities/react-native-maps]] com `initialRegion`/`latitudeDelta` e `Marker` customizado, itens em SVG via `SvgUri` num `ScrollView` horizontal, e o IP da máquina no lugar de `localhost` ([[wiki/concepts/endereco-ip]]).
   - **Tela de detalhe:** `SafeAreaView` ([[wiki/concepts/safe-area]]).
   - **Integração:**
     - Itens via [[wiki/entities/axios]] com seleção por estilos em array.
     - Posição pelo `expo-location`, com permissão e [[wiki/concepts/renderizacao-condicional]].
     - Pontos por `GET /points` com query params, e `route.params` para passar `point_id` e UF/cidade entre telas.
     - Detalhe com `MailComposer` e `Linking.openURL('whatsapp://send?...')` ([[wiki/concepts/mobile-deep-links]]).
     - UF e cidade em `TextInput` dentro de `KeyboardAvoidingView`. O select com o IBGE fica "como desafio".

## Key Claims

### Expo CLI e criação do projeto

- **`npm install -g expo-cli`** permite rodar `expo` "independente de onde a gente esteja". O projeto sai de `expo init mobile` com o template *blank (TypeScript)*; Diego recusa o Yarn porque usa npm na semana. A instalação aponta um aviso de segurança: "a gente deixa para o pessoal do Expo arrumar".
- **`npm start`** abre o Expo DevTools no navegador (porta 19002) com o QR code e o modo LAN, que exige o celular e o computador na mesma rede. O modo Tunnel funciona fora da rede, porém "mais lento".
- **[[wiki/entities/metro-bundler]]:** fica "ouvindo [...] todas as alterações" e monta "um código JavaScript totalmente minificado" para enviar ao celular. A primeira carga é lenta; as seguintes, "instantâneas".

### Celular, emulador ou Snack

- **O app Expo** (Expo Client no Android) lê o QR code, ou recebe `exp://192.168.1.13:19000` à mão. A recomendação é "use um dispositivo físico", pela sensação real e por não instalar nada além do Expo.
- **O emulador** exige "pelo menos 8 GB de memória RAM [...] um i3 de uma geração mais nova", e a Rocketseat tem um vídeo para isso. O **Snack** (`snack.expo.io`) é um editor online com emulador em fila (Appetize), para quem tem um "PC alimentado por um hamster".
- **Problemas comuns:** o repositório Expo Common Issues da Rocketseat, "com 900 stars". Depois de instalar pacote nativo, Diego reinicia o Expo e o app várias vezes na aula; ver as tensões.

### Diferenças entre React Native e ReactJS

- **O mesmo componente:** uma função que retorna JSX. "O resto é tudo igual": props, estado, [[wiki/concepts/componentizacao]] e [[wiki/concepts/imutabilidade]]. Ver [[wiki/concepts/jsx]].
- **Sem HTML:**
  - `View` faz o papel de `div`, `section`, `header` e `footer`; `Text` substitui `p`, `span`, `h1` e `strong`.
  - "No React Native nós não temos nenhum componente que ele tem um valor semântico [...] a gente não precisa de significado", porque na web o significado importa "pela questão de acessibilidade [...] indexação". Ver as tensões.
  - Nenhum elemento vem com estilo próprio: não há negrito automático.
- **Estilo em JavaScript:**
  - `style={styles.container}` e `StyleSheet.create({...})`, "como se fosse classes".
  - As propriedades são as do CSS, convertidas pelo **Yoga** do Facebook "para a estilização nativa".
  - Hífen vira camelCase (`backgroundColor`), números vão sem `px` e textos entre aspas. Ver [[wiki/concepts/css]].
- **Tudo é flex:** "todos os elementos são display flex por natureza". O máximo é `display: 'none'`. Ver [[wiki/concepts/flexbox]].
- **Sem cascata e sem herança:** não dá para estilizar "a text que tem dentro do meu container", e `color` na `View` não pinta os `Text` de dentro. "Não existe essa herança de estilos" também no Android e no iOS nativos. Ver [[wiki/concepts/cascata-css]].

### Home, StatusBar e fragment

- **Estrutura:** `src/pages/Home/index.tsx` com `const Home = () => <View />`, importado no `App.tsx`.
- **Dois elementos no `return`:** um componente não pode retornar dois irmãos. A saída é uma `View` em volta ou o **fragment** `<>...</>`, "uma div que ela não produz resultado".
- **`<StatusBar barStyle="dark-content" backgroundColor="transparent" translucent />`:** `backgroundColor` e `translucent` só valem no Android, e o `translucent` deixa o conteúdo passar por baixo da barra.

### Imagens em 1x, 2x e 3x

- **A regra:** "sempre que você for exportar uma imagem pra dentro do React Native [...] exportar ela em três tamanhos": `logo.png`, `logo@2x.png`, `logo@3x.png`. O Figma, o Sketch e o Adobe XD exportam assim. Ver [[wiki/concepts/densidade-de-pixels]].
- **O motivo:** densidade de pixel. Uma imagem de 44 px numa tela de densidade 3 "vai ficar embaçada"; o certo seria 132. O exemplo dado compara Galaxy S2 e iPhone 8, e está errado (ver as tensões).
- **Import x require:** `import logo from '../../assets/logo.png'` dá "cannot find module" no TypeScript. A saída é `source={require('...logo.png')}`, e o React Native escolhe o @2x/@3x sozinho. Ver [[wiki/concepts/arquivo-de-declaracao-de-tipos]].

### Fontes com Expo Google Fonts

- **Fontes customizadas:** "pergunta para qualquer desenvolvedor o trabalho que dá" para adicioná-las. O Expo Google Fonts, "bem recente", resolve com `expo install expo-font @expo-google-fonts/ubuntu @expo-google-fonts/roboto`. Ver [[wiki/entities/google-fonts]].
- **No `App.tsx`:** `const [fontsLoaded] = useFonts({ Roboto_400Regular, Roboto_500Medium, Ubuntu_700Bold })`, e `if (!fontsLoaded) return <AppLoading />`, que mantém a splash "girando uma bolinha".

### Layout da Home e ImageBackground

- **Textos:** "Seu marketplace de coleta de resíduos" e "Ajudamos pessoas a encontrarem pontos de coleta de forma eficiente". O `marginTop` de 64 ("os designers são tudo malucos por 8 pixels").
- **`ImageBackground`:** é "uma view, porém ela aceita uma imagem de background". Depois de tentar `resizeMode` (`contain`, `center`), a solução é `imageStyle={{ width: 274, height: 368 }}`, o tamanho exato do desenho. "Até porque eu não decoro todo o código possível."

### RectButton, React Navigation e ícones

- **Tipos de botão:** `TouchableHighlight`, `TouchableNativeFeedback` e `TouchableOpacity`, cada um com um efeito. Diego prefere o **`RectButton`** do `react-native-gesture-handler`, que tem "um efeito já pronto pra cada tipo de sistema operacional": ripple no Android, escurecer no iOS.
- **Dependências do [[wiki/entities/react-navigation]]:** `@react-navigation/native`, depois `expo install react-native-gesture-handler react-native-reanimated react-native-screens react-native-safe-area-context @react-native-community/masked-view`, mais `@react-navigation/stack`. Diego explica cada uma: gestos, animações, telas, áreas seguras e máscara.
- **`onPress`, não `onClick`,** "porque não existe mouse no React Native".
- **"Text strings must be rendered within a `<Text>` component":** todo texto precisa estar num `Text`. O erro costuma vir de um ponto e vírgula ou de uma tag fechada a mais dentro do JSX.
- **Ícones:** `@expo/vector-icons` já traz Feather (`<Icon name="arrow-right" />`), FontAwesome (o WhatsApp, que o Feather não tem), Ant e Material. Ver [[wiki/entities/feather-icons]].

### Navegação em pilha

- **`routes.tsx`:**
  - `NavigationContainer` "funciona mais ou menos [...] como a gente tinha aquele browser router" ([[wiki/entities/react-router]]).
  - `const AppStack = createStackNavigator()`, com `<AppStack.Navigator headerMode="none" screenOptions={{ cardStyle: { backgroundColor: '#f0f0f5' } }}>` e um `<AppStack.Screen name component />` por tela (Home, Points, Detail).
  - "A gente não tem endereço, não tem URL, então a gente coloca o nome".
- **Por que pilha:** "as telas anteriores, elas não deixam de existir, o usuário consegue voltar". Também existem abas e drawer ("o Google usa muito"). Ver [[wiki/concepts/navegacao-em-pilha]] e [[wiki/concepts/mobile-navegacao]].
- **`useNavigation()`:**
  - `navigation.navigate('Points')` avança e `navigation.goBack()` volta.
  - O iOS volta com gesto de arrastar para a esquerda.
  - A tela do mapa se chama `Points` "porque map é uma palavra reservada do JavaScript" (ver as tensões).
- **Detalhes:** `screenOptions` leva chave dupla, uma para o JS e outra para o objeto. O menu de desenvolvimento abre chacoalhando o celular, com Command D no simulador iOS ou Ctrl M no emulador Android.

### Página do mapa com react-native-maps

- **Instalação e cabeçalho:** `expo install react-native-maps` e `expo-constants` para `paddingTop: Constants.statusBarHeight`. O botão de voltar é um `TouchableOpacity` com `Feather` `arrow-left` na cor `#34cb79`. Títulos: "Bem-vindo." e "Encontre no mapa um ponto de coleta."
- **`View` com `mapContainer`,** porque "o borderRadius só funciona nas views". O mapa é `<MapView style={styles.map} />`. Ver [[wiki/entities/react-native-maps]].
- **Itens de coleta:**
  - São SVGs da API, desenhados com `SvgUri` (`react-native-svg`).
  - "Localhost na verdade ele não existe para o seu celular": a URL das imagens no `ItemsController` do back-end passa a ser `http://192.168.1.13:3333/uploads/...`, o IP da máquina mostrado pelo Expo.
  - No emulador Android, `10.0.2.2` também aponta para o localhost do computador. Ver [[wiki/concepts/endereco-ip]].
- **`ScrollView horizontal showsHorizontalScrollIndicator={false}`** com `contentContainerStyle={{ paddingHorizontal: 20 }}`, para o espaçamento ser "parte do conteúdo" e o item não ser cortado na borda.
- **`initialRegion`:** latitude e longitude copiadas do Google Maps, mais `latitudeDelta`/`longitudeDelta` = 0.014. "Não me peça para explicar isso aqui [...] é um cálculo [...] criado na Deep Web." Ver as tensões.
- **`<Marker coordinate onPress={handleNavigateToDetail}>`** com conteúdo próprio (`Image` com `source={{ uri }}` e um `Text`) no lugar do pino. A setinha embaixo do balão ficou de fora: "mó trabalheira, não vai anexar muito".

### Página de detalhe

- **Conteúdo:** imagem do ponto, nome, itens, endereço (cidade e UF) e um rodapé com dois `RectButton`, WhatsApp (FontAwesome) e E-mail (Feather `mail`).
- **[[wiki/concepts/safe-area|SafeAreaView]]** no lugar do fragment e do `paddingTop` manual. Ele "faz o padding automaticamente [...] do iPhone e também da status bar", e pede `style={{ flex: 1 }}`.

### Itens da API

- **`services/api.ts`** com `axios.create({ baseURL: 'http://192.168.1.13:3333' })`, "mesma coisa que a gente fez lá pra web". Ver [[wiki/entities/axios]].
- **`useEffect` + `useState<Item[]>`** com `interface Item { id; title; image_url }`, e `items.map(item => <TouchableOpacity key={String(item.id)} ...>)`. "No react-native [...] tem uma necessidade que a gente coloque sempre essa propriedade key [...] como sendo uma string" (ver as tensões). Ver [[wiki/concepts/useEffect]].
- **Seleção:**
  - O `handleSelectItem` (findIndex, filter, spread) vem copiado da web ([[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta|dia 3]]), e o `onPress` usa `() => handleSelectItem(item.id)`.
  - O destaque vem de estilos em array: `style={[styles.item, selectedItems.includes(item.id) ? styles.selectedItem : {}]}`.
  - O `activeOpacity={0.6}` reduz o "apagão" do `TouchableOpacity`.

### Localização do usuário com expo-location

- **`import * as Location from 'expo-location'`:** dentro do `useEffect`, uma `async function loadPosition()` chamada em seguida, "só para eu conseguir utilizar o async await".
- **Permissão:** `const { status } = await Location.requestPermissionsAsync()`. Se não for `'granted'`, aparece `Alert.alert('Ooops...', 'Precisamos de sua permissão para obter a localização')` e o código retorna. Senão, `getCurrentPositionAsync()` dá o `coords`, que vai para `setInitialPosition([latitude, longitude])`. Ver [[wiki/concepts/mobile-permissoes]] e [[wiki/concepts/geolocation-api]].
- **O bug do mapa azul:** com `initialRegion` em `[0, 0]`, o mapa abre no oceano e não se move depois. A solução é [[wiki/concepts/renderizacao-condicional]], `initialPosition[0] !== 0 && (<MapView ... />)`. "Quando eu não tenho o else [...] eu posso botar e-comercial." O `loadingEnabled` mostra um loading.
- **No simulador iOS** é preciso configurar Debug > Location > Custom Location, senão vale a localização da Apple ("lá no quinto dos infernos"). No emulador Android, a localização se define nas configurações.

### Pontos da API e parâmetros de rota

- **`api.get('points', { params: { city, uf, items } })`:** primeiro com valores fixos (Rio do Sul, SC, `[1, 2]`), depois com `route.params.city`, `route.params.uf` e `selectedItems`, e o efeito passa a depender de `[selectedItems]`. Sem item selecionado, não aparece nenhum ponto. Ver [[wiki/concepts/query-string]].
- **Interface `Point`:** `{ id, name, image, latitude, longitude }`. Diego primeiro cola o formato da rota de detalhe por engano: "isso aqui não era rota barra points [...] de listagem". O `map` gera os `Marker` com `key={String(point.id)}`.
- **Parâmetros entre telas:**
  - `navigation.navigate('Detail', { point_id: id })` manda o id, e `useRoute().params` o lê.
  - `const routeParams = route.params as Params` é uma asserção de tipo ("eu vou mandar ele confiar em mim"). Ver [[wiki/concepts/generics-typescript]].
  - A Home manda `{ uf, city }` para a tela Points do mesmo jeito.
- **Detalhe:**
  - `api.get(\`points/${routeParams.point_id}\`)` grava em `useState<Data>({} as Data)`, outra asserção ("burlar o sistema do TypeScript").
  - Com `if (!data.point) return null` no lugar de um loading.
  - Os itens viram texto com `data.items.map(item => item.title).join(', ')`.

### E-mail e WhatsApp: MailComposer e Linking

- **`expo-mail-composer`:** `MailComposer.composeAsync({ subject: 'Interesse na coleta de resíduos', recipients: [data.point.email] })`. Não funciona no emulador, e no celular de Diego também não, porque não havia app de e-mail nativo configurado ("mail service").
- **`Linking.openURL(\`whatsapp://send?phone=${data.point.whatsapp}&text=Tenho interesse sobre coleta de resíduos\`)`:** o *deep linking* abre o WhatsApp instalado. Como o número de teste não existia, abriu o app sem conversa. Ver [[wiki/concepts/mobile-deep-links]].

### UF e cidade na Home

- **Versão simples:** dois `TextInput` em vez do select com o [[wiki/entities/ibge]]. O desafio é fazer o select com `react-native-picker-select` e a API do IBGE, UF primeiro, "aqui está inverso".
- **`KeyboardAvoidingView`** com `behavior={Platform.OS === 'ios' ? 'padding' : undefined}` e `flex: 1`, mais uma `View` em volta dos textos para tudo subir junto. "Cada versão do Android ela funciona de uma maneira diferente."
- **Inputs:** `value={uf}`, `onChangeText={setUf}` (que "recebe diretamente já o texto digitado"), `maxLength={2}`, `autoCapitalize="characters"`, `autoCorrect={false}`. A dica: "digitar bem exatamente com a letra caixa alta e baixa conforme tu tinha usado no cadastro". Ver [[wiki/concepts/componente-controlado]].
- **Fechamento:** "umas sete horas" de código na semana; amanhã, "funcionalidades um pouquinho mais avançadas".

## Tensões e precisões

- **Ferramentas de 2020 que mudaram.** `[skill: tech-mentor-mobile]`
  - **Expo CLI:** a CLI global (`expo-cli`, `expo init`) foi substituída pela local, com `npx create-expo-app` e `npx expo start` `[external]` (https://docs.expo.dev/more/expo-cli/).
  - **`AppLoading`:** foi descontinuado; o padrão é `SplashScreen.preventAutoHideAsync()` com `hideAsync()` do `expo-splash-screen` `[external]` (https://docs.expo.dev/versions/latest/sdk/splash-screen/).
  - **React Navigation:** do v5 da aula (`headerMode="none"`, `@react-navigation/stack`, `masked-view`) para `screenOptions={{ headerShown: false }}` e o *native stack*. O template padrão do Expo hoje usa o **Expo Router**, roteamento por arquivos sobre o React Navigation.
  - **`Touchable*`:** o `Pressable` (RN 0.63, julho de 2020) é a API recomendada, e o `RectButton` continua útil para listas com gestos.
  - **Motor e arquitetura:** Hermes e a Nova Arquitetura são o padrão (ver [[wiki/entities/react-native]]). O app Expo Go serve para experimentar; projetos reais usam *development builds* ([[wiki/entities/expo]]).
  - **Permissão de localização:** `requestPermissionsAsync` virou `requestForegroundPermissionsAsync` no `expo-location` `[external]` (https://docs.expo.dev/versions/latest/sdk/location/).
- **O exemplo de densidade de pixels está errado.** O Galaxy S2 tinha 800×480, não 1920×1080. O iPhone 8 tem 1334×750 com densidade @2x (o 1920×1080 @3x é o do iPhone 8 Plus) `[external]` (https://developer.apple.com/design/human-interface-guidelines/layout). O princípio está certo; os números, não. Ver [[wiki/concepts/densidade-de-pixels]].
- **"Map é uma palavra reservada do JavaScript"** não procede. `map` não é reservada, e `Map` é um objeto global. Chamar um componente de `Map` sombreia o global, o que é má ideia, mas não é palavra reservada. Ver [[wiki/concepts/funcoes-javascript]].
- **"Sem semântica" não quer dizer sem acessibilidade.** No mobile, a semântica vai em props: `accessibilityRole="button"`, `accessibilityLabel`, `accessibilityState={{ selected }}`, `accessible`. Leitores de tela (VoiceOver, TalkBack) dependem delas. Na aula, os itens de coleta são `TouchableOpacity` sem papel nem estado, então o leitor não anuncia "selecionado", e as imagens não têm rótulo. O "a gente não precisa de significado" é o oposto do que vale para mobile `[skill: tech-mentor-mobile]`. Ver [[wiki/concepts/acessibilidade]].
- **Detalhes de estilo:**
  - Também há herança: `Text` dentro de `Text` herda o estilo do pai (só `View` → `Text` não herda) `[external]` (https://reactnative.dev/docs/text#limited-style-inheritance).
  - O flexbox do React Native começa com `flexDirection: 'column'`, ao contrário da web (`row`). É a diferença que mais confunde quem vem do CSS.
- **"key precisa ser string" é do `FlatList`, não do `.map`.** O `keyExtractor` do `FlatList` pede string. A `key` de elementos React aceita número ou string, então o `String(item.id)` é inofensivo, mas não obrigatório.
- **O `latitudeDelta` não tem nada de deep web.** É o tamanho da região visível em graus de latitude: 0,014° ≈ 1,5 km de altura na tela. O `longitudeDelta` é o mesmo para a longitude, que encolhe com o cosseno da latitude `[external]` (https://github.com/react-native-maps/react-native-maps/blob/master/docs/mapview.md). Ver [[wiki/entities/react-native-maps]].
- **IP fixo em dois lugares.** O `192.168.1.13` vai para o `baseURL` do app e para a `image_url` do back-end. Muda a rede, quebra tudo. Os caminhos melhores:
  - No app, derivar do `Constants.expoConfig?.hostUri` em desenvolvimento ou ler uma variável `EXPO_PUBLIC_API_URL`.
  - No servidor, montar a URL a partir do `Host` da requisição ou de configuração.
  - Ver [[wiki/concepts/variaveis-de-ambiente]] e [[wiki/concepts/endereco-ip]].
- **`items` chega como array por acaso.** O Axios serializa `{ items: [1, 2] }` como `items[]=1&items[]=2`. O parser `qs` do Express 4 transforma isso em `['1', '2']`, e o `String(items).split(',')` do dia 2 reconstrói `"1,2"`: funciona sem ninguém ter planejado. Com o parser simples do Express 5, a chave viria como `items[]` e o filtro quebraria. *Inferência a partir do comportamento padrão das duas bibliotecas.* Ver [[wiki/concepts/query-string]].
- **Permissão negada deixa o app sem mapa.** Com a recusa, `initialPosition` fica `[0, 0]` e a renderização condicional nunca mostra o `MapView`. Falta uma alternativa: centralizar na cidade escolhida ou deixar o usuário navegar. Ver [[wiki/concepts/mobile-permissoes]].
- **O link do WhatsApp e o `mailto`.**
  - O texto vai sem `encodeURIComponent`, e o telefone precisa estar no formato internacional (55 + DDD + número).
  - O link universal `https://wa.me/<número>?text=...` funciona sem o app e evita declarar o esquema `whatsapp` no iOS (`LSApplicationQueriesSchemes`) `[external]` (https://faq.whatsapp.com/5913398998672934).
  - Para o e-mail, `MailComposer.isAvailableAsync()` com `mailto:` de reserva resolveria o "mail service" que falhou na aula.
- **`SafeAreaView` do `react-native` só vale no iOS.** No Android, ele não faz nada, e foi descontinuado no React Native 0.81 em favor do `react-native-safe-area-context`, que a aula já tinha instalado com o React Navigation `[external]` (https://reactnative.dev/docs/safeareaview). Ver [[wiki/concepts/safe-area]].
- **As asserções `as Params` e `{} as Data`** calam o compilador sem garantir nada em runtime. Se o parâmetro não vier, `point_id` é `undefined` e a requisição vai para `points/undefined`.
- **A cidade digitada precisa bater byte a byte.** O back-end filtra por igualdade (`where('city', ...)`): "rio do sul" ou "Rio do sul" não acham nada, e acentos também contam. É o motivo real do desafio com o IBGE. Ver [[wiki/concepts/validacao-de-entrada]].
- **A mesma race condition da web.** Trocar de item rapidamente dispara várias `GET /points` sem cleanup. Ver [[wiki/concepts/race-condition]].
- **"Minificado" só em produção.** O bundle de desenvolvimento do Metro não é minificado (é transformado e servido com source maps). A minificação vem no build de release. Ver [[wiki/entities/metro-bundler]].

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/react-native]], [[wiki/entities/expo]]: plataforma do app
- [[wiki/entities/metro-bundler]]: bundler do React Native
- [[wiki/entities/react-navigation]]: navegação em pilha
- [[wiki/entities/react-native-maps]]: mapa nativo
- [[wiki/entities/axios]]: cliente HTTP com `baseURL`
- [[wiki/entities/react]], [[wiki/entities/typescript]]
- [[wiki/entities/feather-icons]]: via `@expo/vector-icons`
- [[wiki/entities/google-fonts]]: via Expo Google Fonts
- [[wiki/entities/ibge]]: desafio do select
- [[wiki/entities/react-router]]: comparação com o `NavigationContainer`
- [[wiki/entities/next-level-week]], [[wiki/entities/rocketseat]]

Citados sem página: Expo Snack, Appetize, react-native-gesture-handler, Reanimated, react-native-screens, react-native-safe-area-context, masked-view, react-native-svg, expo-constants, expo-location, expo-mail-composer, react-native-picker-select, Yoga, Figma, Sketch, Adobe XD, Font Awesome, WhatsApp, Galaxy S2, iPhone 8/11, Android Studio, Free Fire.

## Conceitos

[[wiki/concepts/navegacao-em-pilha]] · [[wiki/concepts/mobile-navegacao]] · [[wiki/concepts/densidade-de-pixels]] · [[wiki/concepts/safe-area]] · [[wiki/concepts/renderizacao-condicional]] · [[wiki/concepts/mobile-deep-links]] · [[wiki/concepts/mobile-permissoes]] · [[wiki/concepts/geolocation-api]] · [[wiki/concepts/endereco-ip]] · [[wiki/concepts/query-string]] · [[wiki/concepts/flexbox]] · [[wiki/concepts/css]] · [[wiki/concepts/cascata-css]] · [[wiki/concepts/jsx]] · [[wiki/concepts/componentizacao]] · [[wiki/concepts/imutabilidade]] · [[wiki/concepts/useEffect]] · [[wiki/concepts/componente-controlado]] · [[wiki/concepts/generics-typescript]] · [[wiki/concepts/arquivo-de-declaracao-de-tipos]] · [[wiki/concepts/funcoes-javascript]] · [[wiki/concepts/acessibilidade]] · [[wiki/concepts/variaveis-de-ambiente]] · [[wiki/concepts/validacao-de-entrada]] · [[wiki/concepts/race-condition]]

## Open Questions

- O dia 5 (upload de imagem e validação) está em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]].
- A legenda perdeu um trecho entre "O SVG é um vetor" e "Então, um componente para a gente conseguir colocar SVG", em que provavelmente vinha o `expo install react-native-svg`. Ficou sem marcação no raw porque não dá para saber o que foi dito.
- Data provável: 4 de junho de 2020 `[external, não verificado]`.
