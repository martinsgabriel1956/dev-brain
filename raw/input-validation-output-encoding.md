---
date: 2026-03-30
tags: [tech-mentor, security, appsec, input-validation, sanitization, xss, zod, dompurify]
skill: tech-mentor-security/references/appsec-owasp
level: fundamento
---

# Input Validation & Output Encoding

## Contexto

A maioria das vulnerabilidades de aplicação — SQL injection, XSS, path traversal, command injection — tem a mesma causa raiz: input não validado ou não sanitizado sendo usado diretamente. Não é uma questão de algoritmo criptográfico ou configuração de rede; é o código da aplicação tratando dados do usuário como confiáveis.

**Distinção fundamental**:
```
Validação:   rejeitar input que não corresponde ao formato esperado
Sanitização: transformar input para um formato seguro
```

Não são intercambiáveis. E a ordem importa:

```
Input → Sanitize (limpa) → Validate (verifica formato) → Use
```

Sanitizar depois de validar não faz sentido — você já usou o dado.

---

## Validação com Zod

Zod é a ferramenta certa para validação de dados estruturados no boundary da aplicação — entrada de requests, env vars, respostas de APIs externas.

### Schemas por tipo de dado

```typescript
import { z } from "zod";

// Dados estruturados com formato definido — rejeite se não bate
const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.number().int().min(0).max(150),
  role: z.enum(["user", "editor", "admin"]),
  website: z.string().url().optional()
});

// Resultado tipado — sem any
const result = createUserSchema.safeParse(req.body);
if (!result.success) {
  return res.status(400).json({ error: result.error.flatten() });
}
const user = result.data; // tipo inferido: { email: string, name: string, ... }
```

### Transforms — sanitizar e normalizar inline

```typescript
const userInputSchema = z.object({
  // Normaliza email: trim + lowercase
  email: z.string().email().transform(v => v.toLowerCase().trim()),

  // Nome: trim + colapsar espaços múltiplos
  name: z.string()
    .min(1).max(100)
    .transform(v => v.trim().replace(/\s+/g, " ")),

  // URL: garantir protocolo seguro
  redirectUrl: z.string()
    .url()
    .refine(url => url.startsWith("https://"), "Apenas HTTPS permitido")
    .optional()
});
```

`.transform()` é aplicado após a validação do tipo — o dado já passou na checagem de formato quando o transform roda.

### Validação de env vars na inicialização

```typescript
const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  NODE_ENV: z.enum(["development", "test", "production"]),
  PORT: z.coerce.number().int().min(1).max(65535).default(3000),
  CORS_ORIGIN: z.string().url()
});

// Falha na inicialização se env inválido — melhor do que falhar em runtime
export const env = envSchema.parse(process.env);
```

### Discriminated unions para payloads polimórficos

```typescript
const webhookSchema = z.discriminatedUnion("type", [
  z.object({ type: z.literal("payment.created"), amount: z.number() }),
  z.object({ type: z.literal("payment.refunded"), refundId: z.string() }),
  z.object({ type: z.literal("user.deleted"), userId: z.string().uuid() })
]);

// TypeScript infere o tipo correto em cada branch
const event = webhookSchema.parse(payload);
if (event.type === "payment.created") {
  console.log(event.amount); // TypeScript sabe que amount existe aqui
}
```

---

## Quando Validar vs Quando Sanitizar

| Tipo de dado | Estratégia | Por quê |
|---|---|---|
| Email, UUID, número, enum | Validar (rejeitar) | Formato completamente definido |
| Nome, descrição, mensagem | Sanitizar (normalizar) | Texto livre, rejeitar seria UX ruim |
| HTML de rich text (WYSIWYG) | Sanitizar com allowlist | Precisa manter formatação |
| Nome de arquivo | Sanitizar (sanitize-filename) | Muitos chars inválidos por OS |
| URL para server-side fetch | Validar + allowlist de domínio | SSRF se não validar |
| ORDER BY / table names | Allowlist explícita | Não pode ser parametrizado |

---

## Sanitização de HTML — DOMPurify

React escapa HTML automaticamente em JSX — `{userContent}` é sempre seguro. O risco está em três vetores específicos:

### 1. `dangerouslySetInnerHTML`

```typescript
import DOMPurify from "dompurify";

// ❌ XSS direto
return <div dangerouslySetInnerHTML={{ __html: userContent }} />;

// ✅ sanitizar antes — DOMPurify remove scripts, event handlers, etc.
return <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userContent) }} />;
```

### 2. Atributo `href` — React não sanitiza

```typescript
// ❌ javascript: protocol executa código
const url = "javascript:alert(document.cookie)";
return <a href={url}>Click</a>;  // XSS

// ✅ validar protocol antes de usar
function SafeLink({ href, children }: { href: string; children: React.ReactNode }) {
  const safeUrl = href.startsWith("https://") || href.startsWith("/") ? href : "#";
  return <a href={safeUrl} rel="noopener noreferrer">{children}</a>;
}
```

### 3. Rich text (editores WYSIWYG) — allowlist de tags e atributos

```typescript
import DOMPurify from "dompurify";

function sanitizeRichText(dirty: string): string {
  return DOMPurify.sanitize(dirty, {
    ALLOWED_TAGS: ["p", "br", "strong", "em", "u", "ul", "ol", "li", "a", "h2", "h3", "blockquote"],
    ALLOWED_ATTR: ["href", "rel"],
    FORBID_ATTR: ["style", "onclick", "onerror"],  // nenhum event handler
    FORCE_BODY: true
  });
}

// Adicionar rel="noopener noreferrer" automaticamente em todos os links
DOMPurify.addHook("afterSanitizeAttributes", node => {
  if (node.tagName === "A") {
    node.setAttribute("rel", "noopener noreferrer");
    node.setAttribute("target", "_blank");
  }
});
```

**DOMPurify no servidor (Node.js)**: DOMPurify precisa de DOM. Use `isomorphic-dompurify` ou execute no cliente. Para sanitização server-side pura, use `sanitize-html`.

```typescript
import sanitizeHtml from "sanitize-html";

const clean = sanitizeHtml(dirty, {
  allowedTags: ["p", "br", "strong", "em", "a"],
  allowedAttributes: { a: ["href", "rel"] },
  allowedSchemes: ["https"]  // bloqueia javascript:, data:, etc.
});
```

---

## Sanitização de Nomes de Arquivo

```typescript
import sanitizeFilename from "sanitize-filename";

// Remove: /, \, :, *, ?, ", <, >, |, null bytes, chars de controle
// Trunca para 255 chars (limite de maioria dos sistemas)
const safeFilename = sanitizeFilename(userFilename);

// Também verificar extensão em allowlist
const ALLOWED_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".pdf"];

function validateFileUpload(filename: string, mimetype: string): string {
  const safe = sanitizeFilename(filename);
  const ext = path.extname(safe).toLowerCase();

  if (!ALLOWED_EXTENSIONS.includes(ext)) {
    throw new Error(`Extension not allowed: ${ext}`);
  }

  return safe;
}
```

**Nunca confie no MIME type enviado pelo cliente** — é trivialmente forjável. Valide o conteúdo real do arquivo com `file-type`:

```typescript
import { fileTypeFromBuffer } from "file-type";

const type = await fileTypeFromBuffer(buffer);
if (!type || !["image/jpeg", "image/png", "image/webp"].includes(type.mime)) {
  throw new Error("Invalid file content");
}
```

---

## Output Encoding por Contexto

O mesmo dado pode precisar de encoding diferente dependendo de onde é inserido:

```
Contexto HTML:         &lt; &gt; &amp; &quot;
Contexto atributo HTML: escapes adicionais para aspas
Contexto URL:          encodeURIComponent()
Contexto JavaScript:   JSON.stringify() ou escape de string JS
Contexto CSS:          nunca inserir input do usuário diretamente
```

```typescript
// ✅ URL encoding
const searchParam = encodeURIComponent(userQuery);
const url = `https://api.exemplo.com/search?q=${searchParam}`;

// ✅ JSON context — JSON.stringify escapa corretamente
const script = `<script>const config = ${JSON.stringify(serverData)};</script>`;
// ATENÇÃO: ainda vulnerável a </script> no JSON — use serialização segura
const safeScript = JSON.stringify(serverData).replace(/<\/script>/gi, "<\\/script>");

// ✅ SQL — parametrized queries, não encoding manual
// Encoding de SQL é complexo e propenso a erros — parametrize sempre
```

---

## Allowlist vs Denylist

**Allowlist** (lista de permitidos): define explicitamente o que é aceito. Tudo mais é rejeitado.

**Denylist** (lista de bloqueados): define o que é rejeitado. Tudo mais é aceito.

```
Allowlist → seguro por padrão, complexo de manter
Denylist  → inseguro por padrão, atacante encontra o que não está na lista
```

**Sempre prefira allowlist** para:
- Extensões de arquivo permitidas
- Tags HTML permitidas em rich text
- Campos aceitos em query strings (ORDER BY, filtros)
- Domínios permitidos para redirect ou server-side fetch
- Valores de enum

```typescript
// ❌ Denylist — fácil de contornar
function isSafeFilename(name: string): boolean {
  const blocked = [".php", ".exe", ".sh", ".bat"];
  return !blocked.some(ext => name.endsWith(ext));
  // Atacante usa .PHP, .PHP7, .phtml, etc.
}

// ✅ Allowlist — só o que é explicitamente permitido
const ALLOWED_EXTENSIONS = new Set([".jpg", ".jpeg", ".png", ".gif", ".pdf"]);

function isSafeFilename(name: string): boolean {
  return ALLOWED_EXTENSIONS.has(path.extname(name).toLowerCase());
}
```

---

## Normalização Unicode e Homoglyph Attacks

Caracteres Unicode visualmente idênticos podem ter code points diferentes:

```
"аdmin" ← o 'а' é cirílico (U+0430), não ASCII 'a'
"pаypal.com" ← ataque de homoglyph em domínio
```

```typescript
// Normalizar para NFC/NFKC antes de validar — colapsa equivalências Unicode
const normalized = userInput.normalize("NFKC").trim();

// Para domínios — usar Punycode para detectar IDN homoglyphs
import { toASCII } from "punycode";
const domain = toASCII(hostname); // "xn--pypal-4ve.com" expõe o ataque
```

---

## Prototype Pollution

Específico para JavaScript — input malicioso contamina `Object.prototype`, afetando todos os objetos da aplicação.

```typescript
// ❌ merge sem proteção
const payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
Object.assign(target, payload); // contamina Object.prototype

// ✅ verificar keys perigosas antes de merge
function safeMerge<T>(target: T, source: Record<string, unknown>): T {
  for (const [key, value] of Object.entries(source)) {
    if (key === "__proto__" || key === "constructor" || key === "prototype") {
      continue; // ignorar — nunca mesclar
    }
    (target as Record<string, unknown>)[key] = value;
  }
  return target;
}

// ✅ ou usar Object.create(null) para objetos sem prototype
const safe = Object.create(null);
```

Validar com Zod previne prototype pollution — Zod constrói um objeto novo com as keys definidas no schema, sem copiar keys extras do input.

---

## Checklist por Tipo de Input

```
Campos de formulário (email, nome, número):
  [ ] Schema Zod com tipos e constraints corretos
  [ ] .transform() para normalização (trim, lowercase)
  [ ] Validar no backend — nunca confiar na validação do frontend

Rich text (WYSIWYG, markdown):
  [ ] DOMPurify com ALLOWED_TAGS e ALLOWED_ATTR explícitos
  [ ] FORBID_ATTR para style e event handlers
  [ ] rel="noopener noreferrer" em links

Upload de arquivo:
  [ ] sanitize-filename no nome
  [ ] Allowlist de extensões
  [ ] Validar magic bytes com file-type (não confiar no MIME do cliente)
  [ ] Armazenar fora do webroot ou no S3

URLs (redirect, server-side fetch):
  [ ] Allowlist de domínios ou validação de protocolo
  [ ] Bloquear IPs privados se usado para fetch server-side (SSRF)

ORDER BY / campos dinâmicos em queries:
  [ ] Allowlist explícita — nunca interpolar diretamente
```

---

## Conceitos Relacionados

[[owasp-top10]] · [[autenticacao-segura]] · [[criptografia-fundamentos]] · [[secrets-management]] · [[api-security]]

---

*Fonte: tech-mentor skill · tech-mentor-security · 2026-03-30*
