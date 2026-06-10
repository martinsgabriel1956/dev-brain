# Cinco Práticas de Segurança do Pragmatic Programmer

**Formato:** Transcrição de vídeo (YouTube)
**Idioma original:** Português (BR)
**Data de transcrição:** 2026-06-10
**Referência:** The Pragmatic Programmer

---

## Introdução

Segurança não é responsabilidade exclusiva do time de segurança — é cultura. A última palavra sobre segurança é do especialista, mas segurança não é uma feature, não é um conjunto de features, e não é algo que você contrata alguém para configurar e pronto.

Segurança é:
- Não clicar em e-mails e links duvidosos
- Usar multi-factor authentication nas contas importantes da empresa
- Não commitar a senha do banco de dados no GitHub

Este vídeo cobre cinco práticas tiradas diretamente do **The Pragmatic Programmer**.

---

## 1. Minimizar a Área de Superfície de Ataque

**Área de superfície** é o quanto de código existe, quantas partes há, como elas se conectam entre si e com o mundo externo.

### Fontes de superfície de ataque

**Complexidade de código**
1 milhão de linhas de código = 1 milhão de lugares onde pode morar um bug, exploit ou vulnerabilidade.

**Inputs do usuário**
Tudo que o usuário envia é um vetor de ataque em potencial. O exemplo clássico é a tira do xkcd — o estudante cujo nome era `Robert'; DROP TABLE students;--`. Se você executar esse input diretamente no banco, você tem uma injeção SQL.

Sanitize sempre: nome, e-mail, senha, uploads — qualquer coisa que venha do usuário.

**Endpoints públicos não autenticados**
Cada endpoint sem autenticação é um vetor para:
- DDoS (bots podem spammar)
- Varredura de dados disponíveis
- Exploits específicos por endpoint

Expor o mínimo possível ao público. Fechar endpoints não resolve DDoS por si só, mas reduz a superfície.

**Recursos com URL pública sem autenticação (ex: S3)**
URLs não são senhas. O browser não as trata como dado sensível:
- Ficam no histórico do browser
- Ficam no histórico do roteador
- Podem ser cacheadas em vários pontos da internet

Um bucket S3 com URLs públicas pode ser varrido por qualquer pessoa, além de gerar custos de DDoS. Sempre adicione autenticação a recursos sensíveis.

**IDs sequenciais expostos**
Endpoint como `/api/imagens/123` com ID sequencial permite varredura trivial: 124, 125, 126... A pessoa varre todos os registros sem qualquer autenticação.

**Serviços internos e backends**
Múltiplos backends se comunicando entre si são superfície de ataque. Chaves SSH vazadas, senhas fracas em `/admin`, credenciais antigas esquecidas — tudo isso é vetor de entrada.

**Outputs também são vetores**
Não são só os inputs. O que você loga pode ser vulnerabilidade:
- Logs com dados sensíveis
- Logs com senhas

**Timing attack**
Um exemplo sofisticado: um algoritmo que verifica senha letra a letra tem tempos de resposta ligeiramente diferentes dependendo de quantas letras já acertaram. Com medição precisa dos tempos de resposta, é possível descobrir a senha testando 26 + 26 + 26... combinações em vez de 26^n. O tempo de resposta do servidor pode ser informação suficiente para um atacante.

---

## 2. Princípio do Menor Privilégio

Cada serviço, funcionário ou usuário deve ter **exatamente** os privilégios necessários para sua função — e nada além.

### Exemplos práticos

**Backend com acesso read-only ao banco**
Se um backend antigo e vulnerável for comprometido, mas ele só tem permissão de leitura no banco, o dano é limitado — o atacante não consegue modificar nada.

**Usuários admin na empresa**
Não dar admin completo a todos. Mapear o que cada pessoa precisa fazer e dar só aquilo.

**Banco de dados fora da VPC**
Em quase todos os casos não existe motivo para o banco de dados ser acessível fora da VPC. O frontend jamais deveria ter acesso direto ao banco.

Para migrations e tarefas que precisam de acesso direto: use um bastion host (uma EC2 dentro da VPC). O dev acessa a EC2 via SSH e de lá acessa o banco. O banco nunca fica exposto fora da VPC.

---

## 3. Defaults Seguros

O estado padrão deve ser o mais seguro possível. O usuário pode explicitamente abrir mão dessa segurança, mas o padrão não pode ser inseguro.

### Exemplos

- **Campos de senha:** mostram `●●●●●●` por padrão. O usuário clica no olhinho para ver.
- **Deleção na AWS:** clicar em "delete" não deleta imediatamente — abre um modal que exige digitar o nome do recurso para confirmar. Ação destrutiva com confirmação explícita.
- **Onboarding de funcionários:** boas empresas exigem que na primeira semana o funcionário troque a senha padrão e ative 2FA. Se a empresa não força isso, o padrão não é seguro o suficiente.

---

## 4. Criptografar Dados Sensíveis

Dados bancários, PII (Personally Identifiable Information) e outras informações sensíveis armazenadas no banco de dados devem ser criptografadas.

- Use algoritmos de hash e padrões estabelecidos de criptografia
- **Não invente criptografia própria**
- Use as ferramentas e bibliotecas consolidadas pelo mercado

---

## 5. Aplicar Updates de Segurança o Mais Rápido Possível

Use ferramentas que alertam sobre vulnerabilidades em dependências:

- **Dependabot (GitHub):** monitora dependências e avisa quando uma versão usada tem CVE conhecida
- **SAST — Static Application Security Testing:** análise estática do código-fonte

### SonarQube

O SonarQube é um dos SASTs mais usados. Faz análise estática e pode alertar para:
- Possíveis injeções SQL no código
- Vulnerabilidades XSS (Cross-Site Scripting)
- Outras vulnerabilidades conhecidas por padrão de código

**Limitação:** SAST é análise estática — não resolve tudo. Deve ser combinado com outras camadas.

### WAF — Web Application Firewall

SAST e WAF são ferramentas diferentes para propósitos diferentes. Ambas contribuem para a cultura de segurança, mas nenhuma substitui a outra. Segurança não é uma ferramenta isolada.

---

## Dica Bônus: Credenciais Nunca no Código

Jamais commite senhas, API keys ou qualquer credencial na codebase.

**Se você commitou uma credencial: altere essa credencial imediatamente.**

### Como gerenciar credenciais localmente

```
.env              # variáveis locais (NUNCA commitado)
.env.example      # template sem valores reais (pode commitar)
.gitignore        # deve incluir .env
```

Exemplo de `.env`:
```
DB_PASSWORD=...
OPENAI_API_KEY=...
```

### Como gerenciar credenciais em produção

Ferramentas de secrets management injetam as variáveis na aplicação em tempo de execução, sem que fiquem visíveis após configuradas:

- **GitHub Secrets** — injetado no CI/CD durante o deploy
- **AWS Secrets Manager** — gerenciamento centralizado de segredos
- **HashiCorp Vault** — alternativa open-source

---

## História (Puramente Fictícia)

Uma empresa tinha um CTO técnico mas com práticas de segurança questionáveis. O dev principal contratado foi notando problemas progressivamente piores:

1. `.env` commitado na codebase com credenciais do banco → ruim
2. Credenciais hardcoded em múltiplos pontos do backend → muito pior
3. Credenciais hardcoded **no frontend**, que fazia requisições **direto ao banco de dados**, retornando dados direto para o browser do usuário → catastrófico

O resultado: o CTO foi demitido. O dev principal foi promovido a CTO e teve que montar uma equipe para reescrever o backend deixado pelo anterior.

Isso nunca acontece na prática. É uma história puramente fictícia.

---

## Conceitos-chave

- [[attack-surface]]
- [[principio-do-menor-privilegio]]
- [[secure-by-default]]
- [[defense-in-depth]]
- [[sql-injection]]
- [[xss]]
- [[timing-attack]]
- [[waf]]
- [[sast]]
- [[secrets-management]]
- [[env-variables]]
- [[vpc]]
- [[ddos]]
