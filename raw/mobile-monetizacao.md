---
date: 2026-04-23
tags: [tech-mentor, mobile, monetização, storekit, google-play-billing, revenuecat, iap, subscriptions]
skill: tech-mentor-mobile/references/monetizacao
level: arquiteto
---

# Monetização Mobile — StoreKit 2, Google Play Billing, RevenueCat

## Contexto
Monetização in-app é regulada pelas stores: Apple leva 15–30% de todas as transações, Google também. As APIs são complexas, têm estados (purchasing, pending, restored) e diferenças significativas entre plataformas. RevenueCat abstrai essa complexidade e adiciona analytics de receita — para a maioria dos apps, é a escolha correta sobre implementar direto.

## Como Funciona

### RevenueCat — Abstração cross-platform (recomendado)

RevenueCat gerencia: verificação de recibos, estado de assinatura, webhooks, análise de churn, e experimentos de preço.

```typescript
// React Native — react-native-purchases
import Purchases, {
  PurchasesPackage,
  CustomerInfo,
  PURCHASES_ERROR_CODE
} from "react-native-purchases";

// Configuração
export async function setupPurchases(userId: string): Promise<void> {
  Purchases.configure({
    apiKey: Platform.select({
      ios: process.env.EXPO_PUBLIC_RC_IOS_KEY,
      android: process.env.EXPO_PUBLIC_RC_ANDROID_KEY
    })!,
    appUserID: userId // associar compras ao usuário
  });

  // Escutar mudanças de estado de assinatura
  Purchases.addCustomerInfoUpdateListener(handleCustomerInfoUpdate);
}

function handleCustomerInfoUpdate(info: CustomerInfo): void {
  const isActive = info.entitlements.active["premium"] !== undefined;
  useSubscriptionStore.getState().setIsPremium(isActive);
}
```

```typescript
// Listar produtos disponíveis
export async function getAvailablePackages(): Promise<PurchasesPackage[]> {
  const offerings = await Purchases.getOfferings();
  return offerings.current?.availablePackages ?? [];
}

// Realizar compra
export async function purchasePackage(pkg: PurchasesPackage): Promise<{
  success: boolean;
  customerInfo?: CustomerInfo;
  error?: string;
}> {
  try {
    const { customerInfo } = await Purchases.purchasePackage(pkg);
    return { success: true, customerInfo };
  } catch (err: unknown) {
    const error = err as { code: number; message: string };

    // Usuário cancelou — não é erro
    if (error.code === PURCHASES_ERROR_CODE.PURCHASE_CANCELLED_ERROR) {
      return { success: false };
    }

    return { success: false, error: error.message };
  }
}

// Restaurar compras (obrigatório pela App Store)
export async function restorePurchases(): Promise<boolean> {
  try {
    const customerInfo = await Purchases.restorePurchases();
    return Object.keys(customerInfo.entitlements.active).length > 0;
  } catch {
    return false;
  }
}

// Verificar acesso a feature premium
export function hasEntitlement(entitlementId: string): boolean {
  const info = Purchases.getCustomerInfoSync?.();
  return info?.entitlements.active[entitlementId] !== undefined;
}
```

```typescript
// Tela de paywall
export function PaywallScreen() {
  const [packages, setPackages] = useState<PurchasesPackage[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    getAvailablePackages().then(setPackages);
  }, []);

  async function handlePurchase(pkg: PurchasesPackage) {
    setIsLoading(true);
    const result = await purchasePackage(pkg);
    setIsLoading(false);

    if (result.success) {
      navigation.navigate("Home");
    } else if (result.error) {
      Alert.alert("Erro", result.error);
    }
  }

  return (
    <View>
      {packages.map(pkg => (
        <Pressable key={pkg.identifier} onPress={() => handlePurchase(pkg)}>
          <Text>{pkg.product.title}</Text>
          <Text>{pkg.product.priceString}</Text>
          {pkg.product.subscriptionPeriod && (
            <Text>/{formatPeriod(pkg.product.subscriptionPeriod)}</Text>
          )}
        </Pressable>
      ))}
      <Pressable onPress={restorePurchases}>
        <Text>Restaurar compras</Text>
      </Pressable>
    </View>
  );
}
```

### StoreKit 2 — iOS Nativo (Swift)

```swift
import StoreKit

class StoreManager: ObservableObject {
  @Published var products: [Product] = []
  @Published var purchasedProductIds: Set<String> = []

  private var updateListenerTask: Task<Void, Error>?

  init() {
    updateListenerTask = listenForTransactions()
    Task { await loadProducts() }
  }

  deinit {
    updateListenerTask?.cancel()
  }

  func loadProducts() async {
    do {
      // IDs configurados no App Store Connect
      products = try await Product.products(for: [
        "com.yourapp.premium.monthly",
        "com.yourapp.premium.yearly",
        "com.yourapp.lifetime"
      ])
    } catch {
      print("Erro ao carregar produtos: \(error)")
    }
  }

  func purchase(_ product: Product) async throws -> Transaction? {
    let result = try await product.purchase()

    switch result {
    case .success(let verification):
      let transaction = try checkVerified(verification)
      await updatePurchasedProducts()
      await transaction.finish()
      return transaction

    case .userCancelled:
      return nil

    case .pending:
      // Transação pendente (ex: compra de criança aguardando aprovação parental)
      return nil

    @unknown default:
      return nil
    }
  }

  private func checkVerified<T>(_ result: VerificationResult<T>) throws -> T {
    switch result {
    case .unverified:
      throw StoreError.failedVerification
    case .verified(let safe):
      return safe
    }
  }

  func updatePurchasedProducts() async {
    var purchased: Set<String> = []
    for await result in Transaction.currentEntitlements {
      if case .verified(let transaction) = result {
        purchased.insert(transaction.productID)
      }
    }
    purchasedProductIds = purchased
  }

  private func listenForTransactions() -> Task<Void, Error> {
    Task.detached {
      for await result in Transaction.updates {
        if case .verified(let transaction) = result {
          await self.updatePurchasedProducts()
          await transaction.finish()
        }
      }
    }
  }

  func restorePurchases() async {
    try? await AppStore.sync()
    await updatePurchasedProducts()
  }
}

// SwiftUI
struct PremiumView: View {
  @StateObject private var store = StoreManager()

  var body: some View {
    ForEach(store.products) { product in
      Button(action: { Task { try? await store.purchase(product) } }) {
        VStack {
          Text(product.displayName)
          Text(product.displayPrice)
        }
      }
    }
  }
}
```

### Google Play Billing — Android Nativo (Kotlin)

```kotlin
class BillingManager(
  private val context: Context,
  private val onPurchaseUpdated: (Purchase) -> Unit
) {
  private lateinit var billingClient: BillingClient

  fun initialize() {
    billingClient = BillingClient.newBuilder(context)
      .setListener { billingResult, purchases ->
        if (billingResult.responseCode == BillingResponseCode.OK && !purchases.isNullOrEmpty()) {
          purchases.forEach { purchase ->
            if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED) {
              onPurchaseUpdated(purchase)
            }
          }
        }
      }
      .enablePendingPurchases()
      .build()

    billingClient.startConnection(object : BillingClientStateListener {
      override fun onBillingSetupFinished(result: BillingResult) {
        if (result.responseCode == BillingResponseCode.OK) {
          loadProducts()
        }
      }

      override fun onBillingServiceDisconnected() {
        // Reconectar
      }
    })
  }

  suspend fun querySubscriptions(): List<ProductDetails> {
    val params = QueryProductDetailsParams.newBuilder()
      .setProductList(listOf(
        QueryProductDetailsParams.Product.newBuilder()
          .setProductId("premium_monthly")
          .setProductType(ProductType.SUBS)
          .build()
      ))
      .build()

    val result = billingClient.queryProductDetails(params)
    return result.productDetailsList ?: emptyList()
  }

  fun launchPurchaseFlow(activity: Activity, productDetails: ProductDetails): Boolean {
    val offerToken = productDetails.subscriptionOfferDetails?.firstOrNull()?.offerToken ?: return false

    val params = BillingFlowParams.newBuilder()
      .setProductDetailsParamsList(listOf(
        BillingFlowParams.ProductDetailsParams.newBuilder()
          .setProductDetails(productDetails)
          .setOfferToken(offerToken)
          .build()
      ))
      .build()

    val result = billingClient.launchBillingFlow(activity, params)
    return result.responseCode == BillingResponseCode.OK
  }

  // OBRIGATÓRIO: confirmar compra com o servidor antes de acknowledgeRechase
  suspend fun acknowledgePurchase(purchase: Purchase, serverVerified: Boolean) {
    if (!serverVerified) return // não confirmar sem verificação do servidor

    if (!purchase.isAcknowledged) {
      val params = AcknowledgePurchaseParams.newBuilder()
        .setPurchaseToken(purchase.purchaseToken)
        .build()
      billingClient.acknowledgePurchase(params)
    }
  }
}
```

### Verificação de recibo no backend — crítico para segurança

```typescript
// Backend — verificar antes de liberar acesso
// NUNCA confiar apenas na confirmação do cliente

// iOS — verificar com servidor da Apple (StoreKit 2 usa JWS)
async function verifyAppleReceipt(transactionId: string): Promise<boolean> {
  const response = await fetch(
    `https://api.storekit.itunes.apple.com/inApps/v1/transactions/${transactionId}`,
    {
      headers: {
        Authorization: `Bearer ${await generateAppleJWT()}`
      }
    }
  );

  if (!response.ok) return false;

  const data = await response.json();
  return data.inAppOwnershipType === "PURCHASED";
}

// Android — verificar com Google Play Developer API
async function verifyGooglePurchase(
  packageName: string,
  productId: string,
  purchaseToken: string
): Promise<boolean> {
  const auth = new GoogleAuth({ scopes: ["https://www.googleapis.com/auth/androidpublisher"] });
  const client = await auth.getClient();
  const token = await client.getAccessToken();

  const response = await fetch(
    `https://androidpublisher.googleapis.com/androidpublisher/v3/applications/${packageName}/purchases/subscriptions/${productId}/tokens/${purchaseToken}`,
    { headers: { Authorization: `Bearer ${token.token}` } }
  );

  if (!response.ok) return false;

  const data = await response.json();
  return data.paymentState === 1; // 1 = received
}
```

## Trade-offs

| Aspecto | RevenueCat | StoreKit 2 direto | BillingClient direto |
|---|---|---|---|
| Setup | Baixo | Alto | Alto |
| Cross-platform | Sim | iOS only | Android only |
| Analytics de receita | Built-in | Manual | Manual |
| Custo | 1% da receita acima de $2.5k/mês | Grátis | Grátis |
| Controle | Médio | Total | Total |
| Webhooks | Built-in | Manual | Manual |

## Quando Usar / Quando Evitar

**RevenueCat** para a maioria dos apps — o valor de analytics, cross-platform, e abstração de edge cases supera o custo de 1%.

**StoreKit 2 / BillingClient diretos** quando: app iOS-only ou Android-only com time experiente em billing, requisito de zero dependency externa, ou volume de transações onde 1% é significativo.

**Sempre verificar no servidor** — nunca liberar acesso premium baseado apenas no callback do cliente. Receipts podem ser forjados.

**Sempre implementar "Restaurar compras"** — é obrigatório pela política da App Store.

## Conceitos Relacionados
[[mobile-seguranca]] · [[mobile-feature-flags]] · [[mobile-monitoramento]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
