---
type: concept
title: "Testes Mobile"
aliases: ["detox react native", "maestro mobile testing", "xcuitest", "espresso android", "flutter integration test"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, testes, detox, maestro, xcuitest, espresso, integration-test, unit-test]
skill: tech-mentor-mobile
status: stable
---

# Testes Mobile

## Pirâmide Mobile

```
         E2E (Detox/Maestro/XCUITest/Espresso)
        ─── poucos, fluxos críticos, lentos ───
       Integration (Testing Library / Composable Tests)
      ──────── componentes com dependências ────────
   Unit Tests (ViewModel, UseCase, Domain Logic)
  ──────── muitos, rápidos, sem framework ─────────
```

## Unit Tests — ViewModel (Android)

```kotlin
@Test
fun `loadProduct emits success state`() = runTest {
    val fakeRepo = FakeProductRepository()
    fakeRepo.setProduct(productFixture)
    val viewModel = ProductViewModel(fakeRepo)

    viewModel.loadProduct("1")

    assertEquals(UiState.Success(productFixture), viewModel.uiState.value)
}
```

ViewModel testável sem Android framework — `Fake` em vez de `Mock`.

## E2E — Maestro (RN/Expo)

```yaml
# flow.yaml
appId: com.example.app
---
- launchApp
- tapOn: "Email"
- inputText: "user@example.com"
- tapOn: "Senha"
- inputText: "password123"
- tapOn: "Entrar"
- assertVisible: "Bem-vindo"
```

```bash
maestro test flow.yaml
maestro cloud --apiKey $KEY flow.yaml  # CI
```

YAML legível — não requer conhecimento de Detox/Appium.

## E2E — Detox (RN)

```js
it('should login successfully', async () => {
    await element(by.id('email-input')).typeText('user@test.com');
    await element(by.id('password-input')).typeText('password');
    await element(by.id('login-button')).tap();
    await expect(element(by.id('home-screen'))).toBeVisible();
});
```

Mais controle que Maestro — útil para gestos complexos e animações.

## Flutter — integration_test

```dart
testWidgets('checkout flow', (tester) async {
    await tester.pumpWidget(MyApp());
    await tester.tap(find.byKey(Key('product-1')));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Adicionar ao Carrinho'));
    expect(find.text('1 item'), findsOneWidget);
});
```

Roda no dispositivo real — acesso ao engine Flutter, sem mock de framework.

## Quando Usar Cada

- **Unit:** lógica de negócio, ViewModel, domain entities — sempre
- **Integration/Composable:** componentes com estado ou efeitos — frequentemente
- **E2E:** happy path dos 3-5 fluxos críticos (login, checkout, onboarding) — poucos

## Ver também

- [[piramide-de-testes]] — estratégia geral de testes
- [[mobile-cicd]] — integrar testes no pipeline

## Key Sources

- [[wiki/sources/mobile-testes]]
