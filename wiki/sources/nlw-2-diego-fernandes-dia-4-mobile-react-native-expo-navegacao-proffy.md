---
type: source
title: "NLW #2 com Diego Fernandes, dia 4: app mobile do Proffy com React Native, Expo e React Navigation"
aliases: ["NLW 2 Diego dia 4", "Proffy mobile", "Proffy React Native", "NLW 2 trilha React dia 4"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [react-native, expo, mobile, typescript, react-navigation, stack-navigation, bottom-tabs, navegacao-encadeada, stylesheet, yoga, flexbox, densidade-de-pixels, expo-google-fonts, apploading, rect-button, gesture-handler, image-background, vector-icons, ionicons, fragment, async-storage, frontend, tech-mentor-frontend, rocketseat, proffy, iniciante]
skill: tech-mentor-mobile
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-2-diego-fernandes-dia-4-mobile-react-native-expo-navegacao-proffy.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #2 com Diego Fernandes, dia 4: app mobile do Proffy com React Native, Expo e React Navigation

## TL;DR

Quarta aula (cerca de 1h40) da trilha de [[wiki/entities/diego-fernandes]] na [[wiki/entities/next-level-week|NLW #2]]: a interface do app mobile do Proffy. No app, o aluno só procura professor; o cadastro de professor fica na web. Boa parte repete o [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta|dia 4 da NLW #1]] (Expo, `View`/`Text`, `StyleSheet`, imagens @2x/@3x, Expo Google Fonts, `RectButton`, React Navigation). As novidades são três:

1. **Navegação encadeada:** abas ([[wiki/concepts/mobile-navegacao|bottom tabs]]) dentro de uma rota da [[wiki/concepts/navegacao-em-pilha|pilha]]. O `NavigationContainer` aparece uma vez só.
2. **Ícones por fonte** (`@expo/vector-icons`, Ionicons), que recebem a cor da aba ativa.
3. **A tela "dar aulas"** com `ImageBackground`, e um `PageHeader` com botão de voltar sem fundo (`BorderlessButton`) que força a volta para a landing.

A listagem, os filtros, a conexão com a API e os favoritos em [[wiki/concepts/mobile-armazenamento-local|AsyncStorage]] ficam para o dia 5.

## Key Claims

### Projeto e ambiente

- **`expo init mobile`** com o template **blank (TypeScript)**, "muito em branco", "porque nós queremos fazer tudo do zero". O `yarn start` abre o painel do Expo, "como se fosse o webpack", com QR code e endereço na rede local (`192.168.1.13`). Ver [[wiki/entities/expo]].
- **Expo Client** no celular, pela câmera ou pelo app, com celular e computador "na mesma rede". Redes de empresa com proxy ou firewall podem bloquear, e o repositório **Expo Common Issues** da Rocketseat reúne os problemas comuns.
- **Emulador:** "não recomendo se você tiver menos do que 8 GB de memória" ou um processador abaixo de um i3 recente. O vídeo da Rocketseat ensina a instalar no iOS e no Android.
- **Fast refresh** recarrega a cada salvamento. O menu de desenvolvedor abre chacoalhando o aparelho, ou com Ctrl+M (Android) e Cmd+D (iOS), e traz reload, debug e monitor de performance ("se ela está rodando em 60 fps").

### React Native × React web

- **"90%, se não mais"** do conhecimento de React web é reaproveitado: componentes, [[wiki/concepts/jsx]], estado e props. Ver [[wiki/entities/react-native]].
- **Sem tags HTML:**
  - `View` é "tudo o que representa um bloco", e `Text` é "tudo o que for um texto", porque "no mobile nós não temos elementos com resultado semântico".
  - "Aqui não tem a parte de SEO", e a acessibilidade "é tratada de uma outra forma".
  - Ver as tensões e [[wiki/concepts/html-semantico]].
- **`StyleSheet.create`:** é "como se fosse o objeto no JavaScript", com propriedades em camelCase ("tirar o hífen, pega a próxima letra e bota maiúscula") e valores de cor entre aspas.
- **Sem herança de estilos:** o `color` no container não chega ao texto, então "cada estilo no seu elemento". A exceção é `Text` dentro de `Text`, que herda cor e fonte. Ver [[wiki/concepts/heranca-css]].
- **CSS "um pouquinho mais limitado":** transforms (`rotateZ`) existem; grid, gradientes e animações por CSS não.
- **Flexbox:** "todos os elementos já vêm com o display flex por padrão", e o `flexDirection` padrão é `column`, porque o celular é "muito mais alto do que largo". Ver [[wiki/concepts/flexbox]].

### Landing page

- **Imagens em PNG,** porque o React Native "não lê SVG" sem `react-native-svg`. Elas são exportadas em 1x, @2x e @3x, e o RN escolhe a certa sozinho.
  - O exemplo do Diego: o iPhone X tem densidade 3, então "mil pixels de largura" viram "3 mil".
  - Ver [[wiki/concepts/densidade-de-pixels]], [[wiki/concepts/formato-svg]] e as tensões.
- **Estrutura:** `src/pages/Landing/index.tsx` + `styles.ts`, e o `App.tsx` retorna `<><Landing /><StatusBar style="light" /></>`. O fragment (`<>...</>`) agrupa "sem produzir nada visual" no resultado, enquanto uma `View` criaria um elemento a mais.
- **`declare module '*.png'`** em `src/@types/index.d.ts`, "lido somente pelo TypeScript", para o `import landingImg from '...png'` não dar erro. Ver [[wiki/concepts/arquivo-de-declaracao-de-tipos]].
- **Imagem:** `style={{ width: '100%' }}` com `resizeMode="contain"` (que "não existe no CSS"). O `contain` mantém tudo visível; o `cover` cortaria.
- **Textos:** quebra de linha com `{'\n'}`, porque "eu não tenho o br". O negrito vem de um `Text` aninhado ("Seja bem-vindo, / **O que deseja fazer?**"). O espaço antes do coração é `{' '}`.
- **Fontes:**
  - `expo install expo-font @expo-google-fonts/archivo @expo-google-fonts/poppins`.
  - `useFonts({ Archivo_400Regular, Archivo_700Bold, Poppins_400Regular, Poppins_600SemiBold })` e `AppLoading` enquanto `!fontsLoaded`: "para o usuário vai parecer que o app ainda está carregando".
  - O negrito é outro `fontFamily`, e não `fontWeight`.
  - Ver [[wiki/entities/google-fonts]] e [[wiki/concepts/renderizacao-condicional]].
- **Botões:**
  - Dois estilos num array (`style={[styles.button, styles.buttonPrimary]}`), `width: '48%'` com `space-between` para sobrar espaço "sem margem right, left", `height: 150` e cores `#9871F5`/`#04D361`.
  - "Text strings must be rendered within a text component" aparece quando sobra um ponto e vírgula solto no JSX.
- **Variáveis:** sem variáveis de CSS no RN. Daria para usar constantes de JavaScript, mas Diego prefere Styled Components com tema "quando eu vou criar aplicações mais avançadas". Ver [[wiki/concepts/variaveis-css]].

### Navegação em pilha

- **Três tipos:** stack ("quando geralmente eu tenho um botão de voltar"; "a tela anterior ela não deixa de existir"), abas e drawer ("aquele menu [...] hambúrguer"). Ver [[wiki/concepts/mobile-navegacao]] e [[wiki/concepts/navegacao-em-pilha]].
- **`routes/AppStack.tsx`:** `NavigationContainer` (o equivalente ao `BrowserRouter` da web) com `createStackNavigator()` devolvendo `Navigator` e `Screen`, e `<Screen name="Landing" component={Landing} />`.
  - O cabeçalho automático ("App Bar", segue o Material Design e muda entre iOS e Android) sai com `screenOptions={{ headerShown: false }}`. As chaves duplas são "a primeira [para] JavaScript [...] a segunda [para] um objeto".
  - Ver [[wiki/entities/react-navigation]] e [[wiki/entities/material-design]].
- **`useNavigation()` + `navigate('GiveClasses')`:** "não existe onClick no React Native, porque não tem mouse": é `onPress`. Os nomes das funções são longos de propósito, "quem olhar o nome da função vai saber exatamente o que ela faz".
- **`RectButton`** do `react-native-gesture-handler` (instalado com a navegação) no lugar do `TouchableOpacity`, porque "vai adaptar o efeito do clique ao sistema operacional": no Android aparece o *ripple*.

### A tela "dar aulas"

- **`ImageBackground`** "aceita que tenha filhos", exige tamanho (`flex: 1`) e usa `resizeMode="contain"` como prop (Diego achou que não funcionava pelo estilo).
- **Conteúdo:** "Quer ser um Proffy? Para começar, você precisa se cadastrar como professor na nossa plataforma web", e o botão "Tudo bem" com `navigation.goBack()`, que "volta para a tela anterior independente de onde ele veio". A função fica separada "para um dia se a gente quiser mexer".

### Navegação encadeada e abas

- **O problema:** de "Favoritos", o voltar deve ir para a landing, e não para "Proffys". "Eu tenho uma navegação de abas dentro de uma outra navegação", e a rota `Study` da pilha é o conjunto das duas abas.
- **`routes/StudyTabs.tsx`:** `createBottomTabNavigator()` com `TeacherList` e `Favorites`, sem `NavigationContainer`, porque ele "só precisa aparecer uma vez [...] por volta do nosso app todo". Na pilha entra `<Screen name="Study" component={StudyTabs} />`.
- **`tabBarOptions`:**
  - `style` com `elevation: 0` ("no Android a gente não tem box shadow") e `shadowOpacity: 0` (iOS), `height: 64`.
  - `tabStyle` com `flexDirection: 'row'` para ícone e texto lado a lado, e `iconStyle` com `flex: 0` e 20 × 20.
  - `labelStyle` com Archivo 700 e 13.
  - Cores de fundo e de texto para aba ativa e inativa.
- **Ícones por fonte:** `@expo/vector-icons` já vem no Expo, com Font Awesome, Material Icons, Feather e Ionicons. A escolha é ícone por fonte, e não PNG, porque é preciso trocar a cor da aba selecionada.
  - `options={{ tabBarLabel: 'Proffys', tabBarIcon: ({ color, size, focused }) => <Ionicons name="ios-easel" size={size} color={focused ? '#8257E5' : color} /> }}`, e `ios-heart` em Favoritos.
  - Os ícones *outline* do layout não estavam no pacote: "provavelmente deve ser [...] uma versão mais nova do Ionicons". Ver [[wiki/concepts/icones-em-interfaces]] e as tensões.

### PageHeader

- **`components/PageHeader`:** barra com `BorderlessButton` ("quando o botão não tem fundo [...] eu não uso o RectButton") para voltar, logo à direita (`space-between`) e `title: string` tipado por `React.FC<PageHeaderProps>`, com padding 40 e fundo roxo. Ver [[wiki/concepts/props-react]] e [[wiki/concepts/componentizacao]].
- **O voltar vai sempre para a landing:** `goBack()` voltaria para a aba anterior, então o header usa `navigate('Landing')`: "não interessa se eu troco de aba".
- **Títulos:** "Proffys disponíveis" e "Meus proffys favoritos". O `children` para os filtros "vai ser muito semelhante com o que a gente tinha lá na web".
- **Dica do VS Code:** criar pasta e arquivo juntos digitando `favorites/index.tsx` no "new file". Ver [[wiki/entities/vs-code]].

## Tensões e precisões

- **APIs de 2020 que mudaram,** as mesmas registradas no [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta|dia 4 da NLW #1]]. `[skill: tech-mentor-mobile]`
  - `expo init` virou `npx create-expo-app`, e o Expo Client virou Expo Go.
  - `AppLoading` foi descontinuado em favor de `expo-splash-screen` (`preventAutoHideAsync`/`hideAsync`) `[external]` (https://docs.expo.dev/versions/latest/sdk/splash-screen/).
  - O `Pressable` substitui os `Touchable*`.
  - O template padrão usa o Expo Router, que roda sobre o React Navigation.
- **`tabBarOptions` saiu no React Navigation 6.** As opções viraram `screenOptions` (`tabBarStyle`, `tabBarItemStyle`, `tabBarLabelStyle`, `tabBarActiveTintColor`...) `[external]` (https://reactnavigation.org/docs/6.x/upgrading-from-5.x/#tabbaroptions-is-replaced-by-options-on-screen). Ver [[wiki/entities/react-navigation]].
- **Os ícones "que faltavam" eram questão de versão, mas ao contrário.** O Ionicons 5 (2020) tirou os prefixos `ios-`/`md-` e passou a ter `easel`, `easel-outline`, `heart-outline`. O `@expo/vector-icons` da época ainda trazia o Ionicons 4, por isso os *outline* do layout não existiam com aqueles nomes `[external, não verificado nesta sessão]`. Nas versões atuais, `ios-easel` não existe mais.
- **Densidade de pixels: pontos não são pixels.** A conta "mil pixels × 3 = 3 mil" mistura as unidades. O iPhone X tem 375 pontos de largura e 1125 pixels físicos (375 × 3). É em pontos que o React Native mede `width` e `height`, e a imagem @3x precisa ter 3× o tamanho em pontos `[external]` (https://developer.apple.com/design/human-interface-guidelines/layout). Mesmo tipo de erro numérico da NLW #1. Ver [[wiki/concepts/densidade-de-pixels]].
- **"Sem semântica" de novo.** No mobile, a semântica vai em props: `accessibilityRole`, `accessibilityLabel`, `accessibilityState`.
  - O `BorderlessButton` só com a imagem de voltar não tem rótulo, e o leitor de tela anuncia só "botão".
  - As imagens decorativas não são marcadas como tal.
  - As abas, ao contrário, ganham rótulo do `tabBarLabel`.
  - `[skill: tech-mentor-mobile]` Ver [[wiki/concepts/acessibilidade]].
- **"AsyncStorage funciona da mesma forma que o localStorage"** só vale para o modelo chave-valor de strings. A API é assíncrona (promises), não é criptografada e tem limites de tamanho por plataforma. Para dado sensível, o caminho é `expo-secure-store` (Keychain/Keystore). Ver [[wiki/concepts/mobile-armazenamento-local]].
- **Flexbox do RN não é idêntico ao da web.** O `flexDirection` padrão é `column`, e também `alignContent: 'flex-start'` e `flexShrink: 0` são padrões, o que muda o encolhimento em relação ao navegador. `flex: 1` no RN é um atalho próprio (cresce e encolhe a partir de 0), e não o `1 1 0%` exato da web `[external]` (https://reactnative.dev/docs/flexbox). Ver [[wiki/concepts/flexbox]].
- **"Não tem animações"** se refere a CSS. O RN tem a API `Animated` e o Reanimated, e gradiente vem de `expo-linear-gradient`. Ver [[wiki/concepts/mobile-animacoes-performaticas]].
- **Fragment "não é repassado para o HTML":** no RN não há HTML. O fragment só não cria view nativa. É a mesma ideia, com o alvo errado.
- **`React.FC`** de novo, com as ressalvas dos dias 1 e 3.
- **Expo e redes restritas:** além do "Expo Common Issues", o modo `tunnel` do Expo contorna rede de empresa e isolamento de clientes no Wi-Fi.
- **Positivos:** explicação da navegação encadeada e de por que o container aparece uma vez, voltar sempre para a landing (decisão de UX consciente), `fontFamily` por peso (no Android, `fontWeight` não escolhe arquivo de fonte personalizada), `Text` aninhado como única herança, ícones por fonte para tingir a aba ativa.

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/react-native]]: o app
- [[wiki/entities/expo]]: CLI, Expo Client, `expo-font`, `@expo/vector-icons`, `AppLoading`
- [[wiki/entities/react-navigation]]: stack + bottom tabs
- [[wiki/entities/google-fonts]]: Archivo e Poppins via `@expo-google-fonts`
- [[wiki/entities/material-design]]: o App Bar padrão do Android
- [[wiki/entities/vs-code]]: criar pasta e arquivo juntos
- [[wiki/entities/next-level-week]], [[wiki/entities/rocketseat]]

Citados sem página: React Native Gesture Handler (RectButton, BorderlessButton), Ionicons, Font Awesome, Feather Icons, Material Icons, AsyncStorage, react-native-svg, Styled Components, Netflix (splash), Notion, Vivaldi, Thiago/Tiago (designer), Expo Common Issues.

## Conceitos

[[wiki/concepts/mobile-navegacao]] · [[wiki/concepts/navegacao-em-pilha]] · [[wiki/concepts/densidade-de-pixels]] · [[wiki/concepts/formato-svg]] · [[wiki/concepts/flexbox]] · [[wiki/concepts/heranca-css]] · [[wiki/concepts/html-semantico]] · [[wiki/concepts/acessibilidade]] · [[wiki/concepts/jsx]] · [[wiki/concepts/componentizacao]] · [[wiki/concepts/props-react]] · [[wiki/concepts/arquivo-de-declaracao-de-tipos]] · [[wiki/concepts/renderizacao-condicional]] · [[wiki/concepts/icones-em-interfaces]] · [[wiki/concepts/variaveis-css]] · [[wiki/concepts/mobile-armazenamento-local]] · [[wiki/concepts/mobile-animacoes-performaticas]]

## Open Questions

- A listagem, os filtros (com `children` e `headerRight` no `PageHeader`), a API via Axios com IP e os favoritos em AsyncStorage estão em [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].
- A legenda trocou "hífen" por "if" quatro vezes, e o raw corrigiu. Os nomes Giovana e Giovanna, ditos no meio da aula, ficaram literais.
- Data provável: 6 de agosto de 2020 `[external, não verificado]`.
