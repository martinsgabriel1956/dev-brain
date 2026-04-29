---
date: 2026-04-23
tags: [tech-mentor, mobile, testes, detox, maestro, xcuitest, espresso, flutter-integration-test]
skill: tech-mentor-mobile/references/testes
level: intermediário
---

# Testes Mobile — Detox, Maestro, XCUITest, Espresso, integration_test

## Contexto
Testes mobile têm três camadas: unit (lógica pura), integration (componentes + estado), e E2E (app real em device/emulador). E2E é o mais valioso e o mais custoso — um bug de navegação não é detectado por unit tests. A escolha da ferramenta de E2E impacta flakiness, velocidade de CI e manutenção.

## Como Funciona

### React Native — Detox (E2E)

Detox é grey-box: controla o app e o device simultaneamente, aguarda idle state antes de interagir — elimina sleeps arbitrários.

```typescript
// e2e/login.test.ts
import { device, element, by, expect } from "detox";

describe("Login flow", () => {
  beforeAll(async () => {
    await device.launchApp({ newInstance: true });
  });

  beforeEach(async () => {
    await device.reloadReactNative();
  });

  it("should login with valid credentials", async () => {
    await element(by.id("email-input")).tap();
    await element(by.id("email-input")).typeText("user@example.com");
    await element(by.id("password-input")).typeText("Senha@123");
    await element(by.id("login-button")).tap();

    await expect(element(by.id("home-screen"))).toBeVisible();
  });

  it("should show error for invalid credentials", async () => {
    await element(by.id("email-input")).typeText("wrong@example.com");
    await element(by.id("password-input")).typeText("wrongpassword");
    await element(by.id("login-button")).tap();

    await expect(element(by.text("Credenciais inválidas"))).toBeVisible();
    await expect(element(by.id("home-screen"))).not.toBeVisible();
  });

  it("should navigate to forgot password", async () => {
    await element(by.id("forgot-password-link")).tap();
    await expect(element(by.id("forgot-password-screen"))).toBeVisible();
  });
});
```

```yaml
# .detoxrc.yml
testRunner:
  args:
    $0: jest
    config: e2e/jest.config.js
  jest:
    setupTimeout: 120000

devices:
  simulator:
    type: ios.simulator
    device: { type: "iPhone 15" }
  emulator:
    type: android.emulator
    device: { avdName: "Pixel_7_API_34" }

apps:
  ios:
    type: ios.app
    binaryPath: ios/build/Build/Products/Debug-iphonesimulator/MyApp.app
    build: xcodebuild -workspace ios/MyApp.xcworkspace -scheme MyApp -configuration Debug -sdk iphonesimulator
  android:
    type: android.apk
    binaryPath: android/app/build/outputs/apk/debug/app-debug.apk
    build: cd android && ./gradlew assembleDebug

configurations:
  ios.sim.debug:
    device: simulator
    app: ios
  android.emu.debug:
    device: emulator
    app: android
```

### Maestro (Cross-platform, YAML)

Maestro é a alternativa mais simples — flows em YAML, funciona em iOS/Android/RN/Flutter sem configuração de build.

```yaml
# flows/login.yaml
appId: com.yourcompany.app

---
- launchApp
- tapOn: "E-mail"
- inputText: "user@example.com"
- tapOn: "Senha"
- inputText: "Senha@123"
- tapOn: "Entrar"
- assertVisible: "Bem-vindo"
- takeScreenshot: login_success

---
# flows/product-search.yaml
appId: com.yourcompany.app

---
- launchApp
- runFlow: flows/login.yaml  # reuso de flows
- tapOn:
    id: "search-button"
- inputText: "tênis"
- assertVisible:
    text: "tênis"
    index: 0
- tapOn:
    id: "product-card-0"
- assertVisible: "Adicionar ao carrinho"
```

```bash
# Rodar
maestro test flows/login.yaml
maestro test flows/         # rodar todos

# CI
maestro cloud --apiKey $MAESTRO_KEY flows/
```

### iOS — XCUITest (Swift)

```swift
// LoginUITests.swift
import XCTest

final class LoginUITests: XCTestCase {

  var app: XCUIApplication!

  override func setUpWithError() throws {
    continueAfterFailure = false
    app = XCUIApplication()
    app.launchArguments = ["--uitesting"]       // desabilitar animações
    app.launchEnvironment = ["BASE_URL": "http://localhost:3001"]
    app.launch()
  }

  func test_login_withValidCredentials_navigatesToHome() throws {
    let emailField = app.textFields["email-input"]
    XCTAssertTrue(emailField.waitForExistence(timeout: 5))
    emailField.tap()
    emailField.typeText("user@example.com")

    let passwordField = app.secureTextFields["password-input"]
    passwordField.tap()
    passwordField.typeText("Senha@123")

    app.buttons["login-button"].tap()

    let homeScreen = app.otherElements["home-screen"]
    XCTAssertTrue(homeScreen.waitForExistence(timeout: 10))
  }

  func test_login_withInvalidCredentials_showsError() {
    app.textFields["email-input"].tap()
    app.textFields["email-input"].typeText("wrong@test.com")
    app.secureTextFields["password-input"].typeText("wrong")
    app.buttons["login-button"].tap()

    let errorLabel = app.staticTexts["Credenciais inválidas"]
    XCTAssertTrue(errorLabel.waitForExistence(timeout: 5))
  }
}
```

```swift
// Helper para acessibilidade (testabilidade)
// No componente SwiftUI, adicionar accessibilityIdentifier
TextField("E-mail", text: $email)
  .accessibilityIdentifier("email-input")

Button("Entrar") { login() }
  .accessibilityIdentifier("login-button")
```

### Android — Espresso

```kotlin
// LoginInstrumentedTest.kt
@RunWith(AndroidJUnit4::class)
@LargeTest
class LoginInstrumentedTest {

  @get:Rule
  val activityRule = ActivityScenarioRule(MainActivity::class.java)

  @Test
  fun login_withValidCredentials_navigatesToHome() {
    onView(withId(R.id.email_input))
      .perform(typeText("user@example.com"), closeSoftKeyboard())

    onView(withId(R.id.password_input))
      .perform(typeText("Senha@123"), closeSoftKeyboard())

    onView(withId(R.id.login_button)).perform(click())

    // Aguardar navegação
    onView(withId(R.id.home_screen)).check(matches(isDisplayed()))
  }

  @Test
  fun login_withInvalidCredentials_showsError() {
    onView(withId(R.id.email_input)).perform(typeText("wrong@test.com"))
    onView(withId(R.id.password_input)).perform(typeText("wrong"))
    onView(withId(R.id.login_button)).perform(click())

    onView(withText("Credenciais inválidas")).check(matches(isDisplayed()))
  }
}

// Compose UI Testing
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun productCard_displayed_correctly() {
  val product = createTestProduct()

  composeTestRule.setContent {
    ProductCard(product = product)
  }

  composeTestRule.onNodeWithText(product.name).assertIsDisplayed()
  composeTestRule.onNodeWithText(formatCurrency(product.price)).assertIsDisplayed()
  composeTestRule.onNodeWithContentDescription("Adicionar ao carrinho").assertIsDisplayed()
}
```

### Flutter — integration_test

```dart
// integration_test/login_test.dart
import "package:flutter_test/flutter_test.dart";
import "package:integration_test/integration_test.dart";
import "package:myapp/main.dart" as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  group("Login flow", () {
    testWidgets("login with valid credentials", (tester) async {
      app.main();
      await tester.pumpAndSettle();

      // Encontrar campos por key ou texto
      await tester.enterText(find.byKey(const Key("email-field")), "user@example.com");
      await tester.enterText(find.byKey(const Key("password-field")), "Senha@123");
      await tester.tap(find.byKey(const Key("login-button")));
      await tester.pumpAndSettle(const Duration(seconds: 3));

      expect(find.byKey(const Key("home-screen")), findsOneWidget);
    });

    testWidgets("shows error for invalid credentials", (tester) async {
      app.main();
      await tester.pumpAndSettle();

      await tester.enterText(find.byKey(const Key("email-field")), "wrong@test.com");
      await tester.enterText(find.byKey(const Key("password-field")), "wrong");
      await tester.tap(find.byKey(const Key("login-button")));
      await tester.pumpAndSettle();

      expect(find.text("Credenciais inválidas"), findsOneWidget);
    });
  });
}
```

```bash
# Rodar no device/emulador
flutter test integration_test/login_test.dart -d emulator-5554

# Firebase Test Lab
gcloud firebase test android run \
  --type instrumentation \
  --app build/app/outputs/apk/debug/app-debug.apk \
  --test build/app/outputs/apk/debug/app-debug-androidTest.apk
```

## Trade-offs

| Ferramenta | Plataforma | Setup | Flakiness | Manutenção | Ideal para |
|---|---|---|---|---|---|
| Detox | RN | Alta | Baixa (idle wait) | Média | RN apps grandes |
| Maestro | Todas | Baixíssima | Média | Baixa | MVP, cross-platform |
| XCUITest | iOS | Média | Média | Média | iOS nativo |
| Espresso | Android | Média | Baixa | Média | Android nativo |
| integration_test | Flutter | Baixa | Média | Baixa | Flutter apps |

## Quando Usar / Quando Evitar

**Maestro** para começar rápido e testar flows críticos cross-platform — YAML é mais fácil de manter do que código.

**Detox** quando precisar de controle fino, mocks de rede, e equipe com tempo para setup.

**XCUITest/Espresso** para apps nativos onde a ferramenta nativa é a opção óbvia e tem melhor integração com IDE.

**Estratégia recomendada:** unit tests para lógica de negócio (100%), integration tests para componentes complexos, E2E apenas para os 5–10 flows mais críticos (login, checkout, onboarding).

## Conceitos Relacionados
[[mobile-metricas-criticas]] · [[mobile-cicd]] · [[mobile-profiling]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
