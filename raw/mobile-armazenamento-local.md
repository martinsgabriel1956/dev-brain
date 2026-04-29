---
date: 2026-04-23
tags: [tech-mentor, mobile, storage, mmkv, asyncstorage, sqlite, hive, room, sharedpreferences]
skill: tech-mentor-mobile/references/armazenamento
level: intermediário
---

# Armazenamento Local — Mobile

## Contexto
Todo app mobile precisa persistir dados localmente: preferências de usuário, cache de sessão, dados offline. A escolha da solução impacta performance de I/O (síncrono vs assíncrono), tamanho do dado, criptografia e capacidade de query. Usar AsyncStorage para tudo é o erro mais comum — para dados frequentemente lidos, MMKV é 30x mais rápido.

## Como Funciona

### React Native — MMKV (key-value rápido)

MMKV é síncrono e escrito em C++ — ideal para tokens, preferências, feature flags.

```typescript
import { MMKV } from "react-native-mmkv";

// Instância global (pode ter múltiplas com IDs diferentes)
export const storage = new MMKV({
  id: "app-storage",
  encryptionKey: process.env.EXPO_PUBLIC_STORAGE_KEY // opcional: criptografia AES
});

// Operações síncronas
storage.set("theme", "dark");
const theme = storage.getString("theme"); // "dark"

storage.set("isOnboarded", true);
const isOnboarded = storage.getBoolean("isOnboarded"); // true

storage.set("userId", 42);
const userId = storage.getNumber("userId"); // 42

storage.delete("userId");
storage.clearAll();

// Integração com Zustand persist
import { StateStorage } from "zustand/middleware";

const mmkvStorage: StateStorage = {
  getItem: key => storage.getString(key) ?? null,
  setItem: (key, value) => storage.set(key, value),
  removeItem: key => storage.delete(key)
};

export const useAuthStore = create<AuthState>()(
  persist(authSlice, {
    name: "auth",
    storage: createJSONStorage(() => mmkvStorage)
  })
);
```

### React Native — AsyncStorage (legacy / dados maiores)

```typescript
import AsyncStorage from "@react-native-async-storage/async-storage";

// Sempre serializar objetos
async function saveUser(user: User): Promise<void> {
  await AsyncStorage.setItem("user", JSON.stringify(user));
}

async function getUser(): Promise<User | null> {
  const raw = await AsyncStorage.getItem("user");
  if (!raw) return null;
  return JSON.parse(raw) as User;
}

// Batch operations — mais eficiente
await AsyncStorage.multiSet([
  ["key1", "value1"],
  ["key2", "value2"]
]);

const results = await AsyncStorage.multiGet(["key1", "key2"]);
```

### React Native — SQLite (dados estruturados/relacionais)

```typescript
import * as SQLite from "expo-sqlite";

const db = SQLite.openDatabaseSync("app.db");

// Migrations
db.execSync(`
  CREATE TABLE IF NOT EXISTS messages (
    id TEXT PRIMARY KEY,
    conversation_id TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at INTEGER NOT NULL,
    synced INTEGER DEFAULT 0
  );
  CREATE INDEX IF NOT EXISTS idx_messages_conversation ON messages(conversation_id);
`);

// CRUD tipado
type Message = {
  id: string;
  conversationId: string;
  content: string;
  createdAt: number;
  synced: boolean;
};

function saveMessage(msg: Message): void {
  db.runSync(
    "INSERT OR REPLACE INTO messages VALUES (?, ?, ?, ?, ?)",
    [msg.id, msg.conversationId, msg.content, msg.createdAt, msg.synced ? 1 : 0]
  );
}

function getMessagesByConversation(conversationId: string): Message[] {
  return db.getAllSync<Message>(
    "SELECT * FROM messages WHERE conversation_id = ? ORDER BY created_at DESC",
    [conversationId]
  );
}

function markAsSynced(ids: string[]): void {
  db.runSync(
    `UPDATE messages SET synced = 1 WHERE id IN (${ids.map(() => "?").join(",")})`,
    ids
  );
}
```

### Flutter — Hive (key-value rápido)

```dart
// pubspec.yaml: hive_flutter: ^1.1.0, hive_generator: ^2.0.1

// Inicialização
await Hive.initFlutter();
await Hive.openBox<String>("settings");
await Hive.openBox<User>("users");

// TypeAdapter para objetos custom
@HiveType(typeId: 0)
class UserModel extends HiveObject {
  @HiveField(0) late String id;
  @HiveField(1) late String name;
  @HiveField(2) late String email;
}

// Uso
final settingsBox = Hive.box<String>("settings");
settingsBox.put("theme", "dark");
final theme = settingsBox.get("theme", defaultValue: "light");

final userBox = Hive.box<UserModel>("users");
userBox.put("me", UserModel()..id = "1"..name = "João");
final me = userBox.get("me");
```

### Flutter — SharedPreferences (preferências simples)

```dart
final prefs = await SharedPreferences.getInstance();

// Escrever
await prefs.setString("token", "abc123");
await prefs.setBool("hasSeenOnboarding", true);
await prefs.setInt("badgeCount", 5);

// Ler
final token = prefs.getString("token");
final hasSeenOnboarding = prefs.getBool("hasSeenOnboarding") ?? false;
```

### Flutter / Android — SQLite com sqflite

```dart
Database? _db;

Future<Database> get database async {
  _db ??= await openDatabase(
    join(await getDatabasesPath(), "app.db"),
    version: 1,
    onCreate: (db, version) async {
      await db.execute("""
        CREATE TABLE messages (
          id TEXT PRIMARY KEY,
          content TEXT NOT NULL,
          created_at INTEGER NOT NULL,
          synced INTEGER DEFAULT 0
        )
      """);
    },
  );
  return _db!;
}

Future<void> insertMessage(Message msg) async {
  final db = await database;
  await db.insert("messages", msg.toMap(), conflictAlgorithm: ConflictAlgorithm.replace);
}

Future<List<Message>> getUnsyncedMessages() async {
  final db = await database;
  final results = await db.query("messages", where: "synced = ?", whereArgs: [0]);
  return results.map(Message.fromMap).toList();
}
```

### Android — Room (ORM sobre SQLite)

```kotlin
@Entity(tableName = "messages")
data class MessageEntity(
  @PrimaryKey val id: String,
  val content: String,
  val createdAt: Long,
  val synced: Boolean = false
)

@Dao
interface MessageDao {
  @Query("SELECT * FROM messages WHERE synced = 0")
  fun getUnsyncedMessages(): Flow<List<MessageEntity>>

  @Insert(onConflict = OnConflictStrategy.REPLACE)
  suspend fun insert(message: MessageEntity)

  @Query("UPDATE messages SET synced = 1 WHERE id IN (:ids)")
  suspend fun markAsSynced(ids: List<String>)
}
```

## Trade-offs

| Solução | Tipo | Sync | Criptografia | Query | Ideal para |
|---|---|---|---|---|---|
| MMKV | Key-value | Síncrono | AES nativo | Não | Tokens, flags, prefs |
| AsyncStorage | Key-value | Assíncrono | Não | Não | Dados leves, legacy |
| SQLite (expo-sqlite) | Relacional | Síncrono | SQLCipher | SQL completo | Offline-first |
| Hive | Key-value | Assíncrono | Nativo | Não | Flutter key-value |
| SharedPreferences | Key-value | Assíncrono | Não | Não | Flutter prefs simples |
| Room | Relacional (ORM) | Assíncrono | SQLCipher | SQL + Flow | Android offline |

## Quando Usar / Quando Evitar

**MMKV** para qualquer dado lido com frequência (token, tema, config) — a diferença de performance vs AsyncStorage é perceptível.

**SQLite/Room** quando tiver relações entre entidades, necessidade de queries complexas, ou dados de offline-first.

**Evite AsyncStorage** para objetos grandes ou dados acessados em cada render — use MMKV ou SQLite.

**Criptografia:** use `encryptionKey` no MMKV ou SQLCipher para dados sensíveis (tokens, PII) — dados em texto plano no storage são acessíveis via backup do Android.

## Conceitos Relacionados
[[mobile-offline-first-basico]] · [[mobile-offline-first-avancado]] · [[mobile-seguranca]] · [[mobile-biometria]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
