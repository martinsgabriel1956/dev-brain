---
date: 2026-04-23
tags: [tech-mentor, mobile, offline-first, sync, queue, reconciliacao, react-native, flutter]
skill: tech-mentor-mobile/references/offline-first
level: intermediário
---

# Offline-First Básico — Queue de Operações + Reconciliação

## Contexto
Apps mobile precisam funcionar sem internet — por design, não como fallback. Offline-first básico significa: o usuário pode criar/editar dados offline, e esses dados são sincronizados quando a conexão retorna. A complexidade está na fila de operações pendentes e na reconciliação quando o servidor tem a versão canônica dos dados.

## Como Funciona

### Estratégia core

```
Escrita: persiste local (SQLite/MMKV) → adiciona à fila de sync → retorna imediatamente
Leitura: lê do cache local sempre (sem loading state para dados cacheados)
Sync: quando online → processa fila em ordem → atualiza cache com resposta do servidor
Conflito: última escrita vence (LWW) na versão básica
```

### React Native — NetInfo + fila no SQLite

```typescript
import NetInfo from "@react-native-community/netinfo";

// Monitor de conectividade
export class ConnectivityService {
  private isConnected = true;
  private listeners: Set<(online: boolean) => void> = new Set();

  constructor() {
    NetInfo.addEventListener(state => {
      const online = state.isConnected === true && state.isInternetReachable === true;
      if (online !== this.isConnected) {
        this.isConnected = online;
        this.listeners.forEach(fn => fn(online));
      }
    });
  }

  getIsConnected() { return this.isConnected; }

  onConnectivityChange(fn: (online: boolean) => void) {
    this.listeners.add(fn);
    return () => this.listeners.delete(fn);
  }
}

export const connectivity = new ConnectivityService();
```

```typescript
// Fila de operações pendentes no SQLite
type SyncOperation = {
  id: string;
  type: "create" | "update" | "delete";
  entity: string;
  payload: string; // JSON
  createdAt: number;
  retryCount: number;
};

const MAX_RETRIES = 3;

class SyncQueue {
  constructor(private db: SQLiteDatabase) {
    this.db.execSync(`
      CREATE TABLE IF NOT EXISTS sync_queue (
        id TEXT PRIMARY KEY,
        type TEXT NOT NULL,
        entity TEXT NOT NULL,
        payload TEXT NOT NULL,
        created_at INTEGER NOT NULL,
        retry_count INTEGER DEFAULT 0
      )
    `);
  }

  enqueue(op: Omit<SyncOperation, "id" | "createdAt" | "retryCount">): void {
    this.db.runSync(
      "INSERT INTO sync_queue VALUES (?, ?, ?, ?, ?, 0)",
      [crypto.randomUUID(), op.type, op.entity, op.payload, Date.now()]
    );
  }

  dequeue(): SyncOperation[] {
    return this.db.getAllSync<SyncOperation>(
      "SELECT * FROM sync_queue ORDER BY created_at ASC LIMIT 50"
    );
  }

  markDone(id: string): void {
    this.db.runSync("DELETE FROM sync_queue WHERE id = ?", [id]);
  }

  incrementRetry(id: string): void {
    this.db.runSync("UPDATE sync_queue SET retry_count = retry_count + 1 WHERE id = ?", [id]);
  }

  removeFailed(): void {
    this.db.runSync("DELETE FROM sync_queue WHERE retry_count >= ?", [MAX_RETRIES]);
  }
}
```

```typescript
// SyncManager — processa fila quando online
class SyncManager {
  private isSyncing = false;

  constructor(
    private queue: SyncQueue,
    private apiClient: ApiClient
  ) {
    connectivity.onConnectivityChange(online => {
      if (online) this.processQueue();
    });
  }

  async processQueue(): Promise<void> {
    if (this.isSyncing || !connectivity.getIsConnected()) return;

    this.isSyncing = true;
    try {
      const operations = this.queue.dequeue();

      for (const op of operations) {
        try {
          await this.executeOperation(op);
          this.queue.markDone(op.id);
        } catch (err) {
          this.queue.incrementRetry(op.id);
          console.log({ message: "Sync operation failed", opId: op.id, error: err });
        }
      }

      this.queue.removeFailed();
    } finally {
      this.isSyncing = false;
    }
  }

  private async executeOperation(op: SyncOperation): Promise<void> {
    const payload = JSON.parse(op.payload);

    switch (op.type) {
      case "create":
        await this.apiClient.post(`/${op.entity}`, payload);
        break;
      case "update":
        await this.apiClient.patch(`/${op.entity}/${payload.id}`, payload);
        break;
      case "delete":
        await this.apiClient.delete(`/${op.entity}/${payload.id}`);
        break;
    }
  }
}
```

```typescript
// Repository com offline-first
class MessageRepository {
  constructor(
    private db: SQLiteDatabase,
    private queue: SyncQueue
  ) {}

  // Escrita: local imediato + enfileira sync
  createMessage(conversationId: string, content: string): Message {
    const message: Message = {
      id: crypto.randomUUID(),
      conversationId,
      content,
      createdAt: Date.now(),
      synced: false
    };

    this.db.runSync(
      "INSERT INTO messages VALUES (?, ?, ?, ?, ?)",
      [message.id, conversationId, content, message.createdAt, 0]
    );

    this.queue.enqueue({
      type: "create",
      entity: "messages",
      payload: JSON.stringify(message)
    });

    return message; // retorna imediatamente, sem esperar o servidor
  }

  // Leitura: sempre do cache local
  getMessages(conversationId: string): Message[] {
    return this.db.getAllSync<Message>(
      "SELECT * FROM messages WHERE conversation_id = ? ORDER BY created_at DESC",
      [conversationId]
    );
  }

  // Reconciliação: quando servidor retorna dados, atualiza cache
  async syncFromServer(conversationId: string): Promise<void> {
    if (!connectivity.getIsConnected()) return;

    const serverMessages = await apiClient.get<Message[]>(`/conversations/${conversationId}/messages`);

    this.db.runSync("BEGIN TRANSACTION");
    try {
      // Atualizar mensagens do servidor (last write wins básico)
      for (const msg of serverMessages) {
        this.db.runSync(
          "INSERT OR REPLACE INTO messages VALUES (?, ?, ?, ?, 1)",
          [msg.id, msg.conversationId, msg.content, msg.createdAt]
        );
      }
      this.db.runSync("COMMIT");
    } catch {
      this.db.runSync("ROLLBACK");
    }
  }
}
```

### Flutter — Fila com Hive + dio_retry

```dart
class OfflineQueue {
  late Box<Map> _box;

  Future<void> initialize() async {
    _box = await Hive.openBox<Map>("sync_queue");
  }

  Future<void> enqueue(String type, String entity, Map<String, dynamic> payload) async {
    final op = {
      "id": const Uuid().v4(),
      "type": type,
      "entity": entity,
      "payload": payload,
      "createdAt": DateTime.now().millisecondsSinceEpoch,
      "retryCount": 0,
    };
    await _box.add(op);
  }

  List<Map<dynamic, dynamic>> getAll() => _box.values.toList();

  Future<void> remove(String id) async {
    final key = _box.keys.firstWhere(
      (k) => _box.get(k)?["id"] == id,
      orElse: () => null,
    );
    if (key != null) await _box.delete(key);
  }
}

// Connectivity com connectivity_plus
class SyncService {
  final OfflineQueue _queue;
  final Dio _dio;

  SyncService(this._queue, this._dio) {
    Connectivity().onConnectivityChanged.listen((result) {
      if (result != ConnectivityResult.none) processQueue();
    });
  }

  Future<void> processQueue() async {
    final ops = _queue.getAll();
    for (final op in ops) {
      try {
        await _executeOp(op);
        await _queue.remove(op["id"] as String);
      } catch (e) {
        console.log({ "message": "Sync failed", "op": op["id"], "error": e });
      }
    }
  }
}
```

## Indicadores de UI para estado offline

```typescript
// Banner de status de conectividade
export function OfflineBanner() {
  const [isOnline, setIsOnline] = useState(true);

  useEffect(() => {
    const unsub = connectivity.onConnectivityChange(online => setIsOnline(online));
    return unsub;
  }, []);

  if (isOnline) return null;

  return (
    <View style={styles.banner}>
      <Text style={styles.text}>Sem conexão — alterações serão sincronizadas quando online</Text>
    </View>
  );
}
```

## Trade-offs

| Aspecto | Offline-first | Online-first com cache |
|---|---|---|
| UX sem internet | Funciona normalmente | Tela de erro |
| Complexidade | Alta | Baixa |
| Conflitos | Precisa resolver | Não tem |
| Dados garantidos | Eventual | Imediato |
| Tamanho local | Grande | Pequeno |

## Quando Usar / Quando Evitar

**Use offline-first quando:** app de campo (inspeções, entregas, vendas), chat, notas, qualquer funcionalidade core que não pode depender de conexão.

**Evite para:** transações financeiras (integridade requer servidor), dados em tempo real (preços, estoque), conteúdo muito grande para cache local.

**Prioridade de conflito básica (LWW):** quem escreveu por último ganha. Suficiente para 90% dos casos. Para colaboração em tempo real, veja [[mobile-offline-first-avancado]] (CRDT).

## Conceitos Relacionados
[[mobile-offline-first-avancado]] · [[mobile-armazenamento-local]] · [[mobile-chamadas-http]] · [[mobile-state-management-global]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
