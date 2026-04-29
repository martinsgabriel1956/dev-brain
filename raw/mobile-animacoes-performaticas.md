---
date: 2026-04-23
tags: [tech-mentor, mobile, animações, reanimated, compose-animation, flutter-animation, performance]
skill: tech-mentor-mobile/references/animacoes
level: intermediário
---

# Animações Performáticas — Reanimated 3, Compose Animated, Flutter Implicit Animations

## Contexto
A regra de ouro de animações mobile: rodar na thread nativa, nunca na thread JavaScript/Dart/Kotlin. Animações na UI thread principal causam jank porque competem com a renderização. O modelo correto é declarar a animação uma vez, enviá-la para a thread nativa, e deixar o sistema executar frame a frame sem intervenção do JS/Dart.

## Como Funciona

### React Native — Reanimated 3

Reanimated executa toda a lógica de animação na UI thread via Worklets — funções JS que compilam para código nativo e rodam sem cruzar a bridge.

```typescript
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
  withTiming,
  withSequence,
  withRepeat,
  interpolate,
  Extrapolation,
  runOnJS,
  Easing
} from "react-native-reanimated";

// Shared value — estado que vive na UI thread
const scale = useSharedValue(1);
const opacity = useSharedValue(1);
const translateY = useSharedValue(0);

// Animated style — worklet executado na UI thread
const animatedStyle = useAnimatedStyle(() => ({
  transform: [
    { scale: scale.value },
    { translateY: translateY.value }
  ],
  opacity: opacity.value
}));

// Disparar animação — cross-thread safe
function handlePress() {
  scale.value = withSpring(0.95, { damping: 15, stiffness: 300 });
  setTimeout(() => {
    scale.value = withSpring(1);
  }, 100);
}
```

```typescript
// Animação de entrada de card
export function AnimatedCard({ children, index }: { children: React.ReactNode; index: number }) {
  const translateY = useSharedValue(50);
  const opacity = useSharedValue(0);

  useEffect(() => {
    const delay = index * 100;
    translateY.value = withTiming(0, { duration: 400, easing: Easing.out(Easing.cubic) });
    opacity.value = withTiming(1, { duration: 400 });
  }, []);

  const style = useAnimatedStyle(() => ({
    transform: [{ translateY: translateY.value }],
    opacity: opacity.value
  }));

  return <Animated.View style={[styles.card, style]}>{children}</Animated.View>;
}
```

```typescript
// Gesture + animação — react-native-gesture-handler + Reanimated
import { Gesture, GestureDetector } from "react-native-gesture-handler";

export function SwipeableCard({ onDismiss }: { onDismiss: () => void }) {
  const translateX = useSharedValue(0);
  const DISMISS_THRESHOLD = 150;

  const gesture = Gesture.Pan()
    .onUpdate(event => {
      translateX.value = event.translationX;
    })
    .onEnd(event => {
      if (Math.abs(event.translationX) > DISMISS_THRESHOLD) {
        translateX.value = withTiming(
          event.translationX > 0 ? 500 : -500,
          { duration: 300 },
          finished => { if (finished) runOnJS(onDismiss)(); }
        );
      } else {
        translateX.value = withSpring(0);
      }
    });

  const style = useAnimatedStyle(() => ({
    transform: [
      { translateX: translateX.value },
      {
        rotate: `${interpolate(
          translateX.value,
          [-200, 0, 200],
          [-15, 0, 15],
          Extrapolation.CLAMP
        )}deg`
      }
    ]
  }));

  return (
    <GestureDetector gesture={gesture}>
      <Animated.View style={[styles.card, style]} />
    </GestureDetector>
  );
}
```

```typescript
// Scroll animado — Animated.FlatList com header colapsável
export function CollapsingHeader() {
  const scrollY = useSharedValue(0);
  const HEADER_HEIGHT = 200;

  const scrollHandler = useAnimatedScrollHandler(event => {
    scrollY.value = event.contentOffset.y;
  });

  const headerStyle = useAnimatedStyle(() => ({
    height: interpolate(
      scrollY.value,
      [0, HEADER_HEIGHT],
      [HEADER_HEIGHT, 60],
      Extrapolation.CLAMP
    ),
    opacity: interpolate(scrollY.value, [0, HEADER_HEIGHT / 2], [1, 0], Extrapolation.CLAMP)
  }));

  return (
    <>
      <Animated.View style={[styles.header, headerStyle]}>
        <Text style={styles.title}>Produtos</Text>
      </Animated.View>
      <Animated.FlatList
        data={products}
        onScroll={scrollHandler}
        scrollEventThrottle={16}
        renderItem={({ item }) => <ProductCard product={item} />}
      />
    </>
  );
}
```

### Android Compose — Animate APIs

```kotlin
// Animação de estado — animateFloatAsState
@Composable
fun LikeButton(isLiked: Boolean, onToggle: () -> Unit) {
  val scale by animateFloatAsState(
    targetValue = if (isLiked) 1.2f else 1f,
    animationSpec = spring(dampingRatio = Spring.DampingRatioMediumBouncy),
    label = "like_scale"
  )

  val tint by animateColorAsState(
    targetValue = if (isLiked) Color.Red else Color.Gray,
    animationSpec = tween(durationMillis = 200),
    label = "like_color"
  )

  Icon(
    imageVector = Icons.Default.Favorite,
    contentDescription = null,
    tint = tint,
    modifier = Modifier
      .scale(scale)
      .clickable { onToggle() }
  )
}
```

```kotlin
// Animação de visibilidade
@Composable
fun AnimatedPanel(visible: Boolean, content: @Composable () -> Unit) {
  AnimatedVisibility(
    visible = visible,
    enter = slideInVertically(
      initialOffsetY = { it },
      animationSpec = spring(stiffness = Spring.StiffnessMediumLow)
    ) + fadeIn(),
    exit = slideOutVertically(targetOffsetY = { it }) + fadeOut()
  ) {
    content()
  }
}
```

```kotlin
// Transição de layout com animateContentSize
Card(
  modifier = Modifier
    .fillMaxWidth()
    .animateContentSize(
      animationSpec = spring(
        dampingRatio = Spring.DampingRatioMediumBouncy,
        stiffness = Spring.StiffnessLow
      )
    )
    .clickable { expanded = !expanded }
) {
  Column(modifier = Modifier.padding(16.dp)) {
    Text(title)
    if (expanded) Text(description) // anima automaticamente a mudança de tamanho
  }
}
```

```kotlin
// Animação de lista — animateItem (Compose 1.7+)
LazyColumn {
  items(items = products, key = { it.id }) { product ->
    ProductCard(
      product = product,
      modifier = Modifier.animateItem(
        fadeInSpec = tween(durationMillis = 250),
        placementSpec = spring(stiffness = Spring.StiffnessMediumLow)
      )
    )
  }
}
```

### Flutter — Implicit + Explicit Animations

```dart
// Implicit — AnimatedContainer, AnimatedOpacity, AnimatedAlign
// O Flutter calcula a interpolação automaticamente quando o valor muda
class ExpandableCard extends StatefulWidget {
  @override
  State<ExpandableCard> createState() => _ExpandableCardState();
}

class _ExpandableCardState extends State<ExpandableCard> {
  bool _expanded = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => setState(() => _expanded = !_expanded),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 300),
        curve: Curves.easeInOut,
        height: _expanded ? 200 : 80,
        decoration: BoxDecoration(
          color: _expanded ? Colors.blue.shade100 : Colors.white,
          borderRadius: BorderRadius.circular(12),
        ),
        child: const Padding(
          padding: EdgeInsets.all(16),
          child: Text("Toque para expandir"),
        ),
      ),
    );
  }
}
```

```dart
// Explicit — AnimationController para controle total
class PulsingButton extends StatefulWidget {
  @override
  State<PulsingButton> createState() => _PulsingButtonState();
}

class _PulsingButtonState extends State<PulsingButton>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _scaleAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 800),
    )..repeat(reverse: true);

    _scaleAnimation = Tween<double>(begin: 1.0, end: 1.1).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeInOut),
    );
  }

  @override
  void dispose() {
    _controller.dispose(); // SEMPRE fazer dispose
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return ScaleTransition(
      scale: _scaleAnimation,
      child: ElevatedButton(onPressed: () {}, child: const Text("Clique")),
    );
  }
}
```

## Trade-offs

| Solução | Thread | Gesture support | Complexidade | Ideal para |
|---|---|---|---|---|
| Reanimated 3 | UI thread | Excelente | Média | RN: qualquer animação |
| Animated API (RN core) | JS thread | Limitado | Baixa | Animações simples legadas |
| Compose Animated APIs | Compositor | Integrado | Baixa | Android: state-driven |
| Flutter Implicit | Rasterizer | Via GestureDetector | Muito baixa | Transições de estado simples |
| Flutter Explicit | Rasterizer | Via GestureDetector | Alta | Animações complexas/loop |

## Quando Usar / Quando Evitar

**Reanimated sobre Animated API (RN):** sempre para animações de gesture, scroll, ou qualquer coisa que precise de 60fps. A Animated API JS é suficiente apenas para animações de entrada/saída sem interação.

**Implicit Animations (Flutter)** para mudanças de estado simples — zero boilerplate. **Explicit** quando precisar de loop, controle de play/pause, ou animações sequenciais complexas.

**Sempre fazer `dispose()` de AnimationController** no Flutter — leak de controller é causa comum de crash após navegação.

**Nunca:** fazer cálculos pesados dentro de `useAnimatedStyle` sem `useDerivedValue` — o worklet deve ser o mais leve possível.

## Conceitos Relacionados
[[mobile-metricas-criticas]] · [[mobile-profiling]] · [[mobile-performance-listas]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
