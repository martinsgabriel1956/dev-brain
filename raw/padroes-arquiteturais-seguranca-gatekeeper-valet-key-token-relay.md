# Padrões Arquiteturais de Segurança: Gatekeeper, Valet Key e Token Relay

**Autor:** Bernardo Lobato  
**Formato:** Transcrição de vídeo  
**Idioma original:** Português (BR)  
**Data de transcrição:** 2026-06-05  

---

## Introdução

Você já se deparou com uma aplicação ou API que precisa ser segura, mas o front precisa acessar, o parceiro externo precisa acessar, o mobile precisa acessar — e no fim você sente que está abrindo portas demais, e que quanto mais portas você abre, mais difícil fica saber quem pode entrar, por onde e até onde pode ir?

Este vídeo apresenta três padrões arquiteturais de segurança que visam resolver exatamente isso: o **Gatekeeper**, o **Valet Key** e o **Token Relay**.

---

## O Problema: Segurança como Problema Arquitetural

Quando falamos de segurança de APIs e aplicações, muitos desenvolvedores pensam imediatamente em código: qual lib usar, qual middleware instalar, qual header validar, etc. Só que na prática, quando ocorre um incidente de segurança, o problema nem sempre está naquela linha de código que valida o token. O problema pode estar muito antes disso — no **desenho do projeto**:

- Quem pode falar com quem
- Por onde a requisição passa
- Quais caminhos existem até o final do fluxo

Um erro comum é tentar remendar a segurança com soluções pontuais: colocar autenticação em todos os serviços, validar token em todo endpoint, adicionar headers, mais checagens, mais middlewares etc. Essas atividades são válidas, mas podem criar uma **falsa sensação de segurança** que não resolve a raiz do problema — porque no fundo você pode ter um **problema arquitetural**.

Pode ser que sua arquitetura esteja permitindo caminhos que nunca deveriam existir.

### Superfície de Ataque

Segurança robusta em APIs nasce quando você começa a pensar em termos de **superfície de ataque**:

- Quantos pontos de entrada o meu sistema tem?
- Quantos serviços estão expostos?
- Quantos lugares diferentes precisam saber fazer a segurança?

Quanto mais distribuída essa responsabilidade estiver, maior a chance de erro, inconsistência e brecha. Padrões arquiteturais de segurança são poderosos porque quando você enxerga a segurança como um problema de arquitetura, as perguntas passam a ser:

> *Por que esse serviço está acessível diretamente? Por que o cliente consegue falar com isso? Por que esse recurso precisa passar pela minha API?*

Esse tipo de pergunta tem o potencial de mudar o desenho da sua solução.

---

## Padrão 1: Gatekeeper

### Conceito

O **Gatekeeper** parte de uma ideia simples: seu sistema não deveria ter várias portas de entrada. Deve existir **um único ponto por onde todas as requisições externas obrigatoriamente passam**.

Esse componente intermediário é quem recebe os usuários externos. Seus serviços ficam protegidos dentro da arquitetura. O Gatekeeper pode:

- Autenticar e autorizar
- Aplicar rate limiting
- Registrar logs
- Bloquear o que for suspeito

Tudo isso antes de a requisição chegar à aplicação em si.

Com isso, os serviços internos deixam de se preocupar com essa exposição. Para eles, toda chamada já vem filtrada, vinda de uma fonte confiável e controlada.

### Ganhos

- Redução da superfície de ataque
- Centralização de responsabilidade em um único lugar arquitetural
- Serviços internos não precisam reimplementar segurança de borda

### Relação com API Gateway e BFF

Elementos como **API Gateway** e **BFF (Backend for Frontend)** são excelentes exemplos de implementação desse padrão.

### WAF (Web Application Firewall)

O **WAF** complementa o Gatekeeper, mas atua em um nível mais baixo — é um filtro de borda que inspeciona e bloqueia tráfego HTTP malicioso antes que chegue na aplicação. Normalmente é utilizado via serviços de nuvem como **AWS WAF**, **Azure Web Application Firewall** ou **Cloudflare WAF**.

Diferenças importantes:

| Gatekeeper | WAF |
|---|---|
| Sabe quem é o usuário | Não sabe quem é o usuário |
| Conhece os serviços internos | Não conhece os serviços internos |
| Aplica autorização contextual | Atua em padrões de ataque conhecidos |

O WAF atua em práticas como:
- Bloquear ataques conhecidos (OWASP Top 10, SQL Injection, XSS)
- Filtrar tráfego malicioso
- Prevenir DDoS
- Proteger contra padrões de ataque em geral

---

## Padrão 2: Valet Key

### Analogia

Você não entrega a chave da sua casa para alguém que vai só estacionar o carro. Você entrega apenas a chave da garagem, a chave do carro, a chave do portão. E essa chave só funciona por um tempo limitado e só dá acesso ao que é estritamente necessário.

### Conceito

Em APIs, a ideia é conceder acesso direto a um recurso específico com uma **credencial temporária e de escopo mínimo**, sem expor a aplicação principal.

Esse padrão é muito comum quando o cliente precisa interagir com um recurso pesado ou externo, como:
- Upload ou download de arquivos em storage
- Envio de mídias pesadas

Em vez de o cliente enviar tudo para a sua API — que então repassa ao destino (funcionando como um proxy) —, você gera uma credencial temporária que permite ao cliente acessar diretamente o recurso.

### Características da Valet Key

1. **Expira rapidamente** — credencial de curta duração
2. **Funciona apenas para um recurso específico** — escopo mínimo
3. **Não dá acesso à API como um todo** — sem elevação de privilégio

Mesmo que o token seja interceptado, o impacto é extremamente limitado no tempo e no escopo.

### Ganhos

- Reduz carga e surface de ataque na API
- Evita que a API vire um gargalo ou proxy desnecessário de alto tráfego
- A aplicação é responsável apenas por **autorizar** o acesso, não por **transportar** os dados
- Melhora a performance geral do sistema

### Exemplo Prático

Se você já precisou baixar um arquivo do **S3 da AWS** e criou um **Signed URL (Presigned URL)**, é exatamente disso que se trata.

### Fluxo

```
1. Cliente pede autorização para a API
2. API valida e gera a credencial temporária (valet key) com escopo restrito
3. Cliente recebe a chave
4. Cliente fala diretamente com o recurso usando essa chave
5. O recurso valida a chave e permite a operação — sem passar novamente pela API
```

---

## Padrão 3: Token Relay

### O Problema que Resolve

Como os serviços internos sabem quem é o usuário que iniciou aquela requisição?

Em arquiteturas com BFF, API Gateway e vários serviços interconectados, é fácil perder o contexto da identidade do usuário no meio do caminho — acabando por confiar demais apenas no componente anterior (o que chamou o endpoint), especialmente quando o serviço autentica somente outros serviços, e não o usuário comum.

### Conceito

Nesse padrão, a **identidade do usuário viaja junto com a requisição do início ao fim**.

O usuário se autentica, recebe um token, e esse token é validado na borda. A partir daí, em vez de serviços internos confiarem apenas em quem os está chamando (autenticando-se somente com chave de serviço), eles também recebem e validam **informações de identidade do próprio usuário**.

Isso permite que cada serviço aplique uma **autorização fina** baseada em papéis, atributos ou regras de negócio específicas — de forma independente do gateway.

### Por que é importante

Esse padrão é especialmente relevante para evitar problemas onde o sistema valida que o usuário está **autenticado** mas não valida se ele pode **acessar aquele recurso específico**.

Como a identidade está presente em todos os saltos, cada serviço pode fazer essa checagem individualmente, de acordo com suas próprias regras.

### Ganhos

- A segurança não fica concentrada apenas na borda da arquitetura
- A borda autentica, mas a **autorização acontece em todos os serviços**, em todos os níveis desejados
- Sempre considera o usuário real por trás da requisição

---

## Resumo Comparativo

| Padrão | Problema que resolve | Mecanismo principal |
|---|---|---|
| **Gatekeeper** | Muitos pontos de entrada e responsabilidade distribuída | Ponto único de entrada obrigatório |
| **Valet Key** | API como intermediário pesado e acesso excessivamente amplo | Credencial temporária de escopo mínimo |
| **Token Relay** | Perda de identidade do usuário entre serviços internos | Identidade viaja com a requisição end-to-end |

---

## Conclusão

Em nenhum momento falamos de framework, biblioteca ou linha de código específica. Falamos de **caminhos**, de **portas**, de **quem pode falar com quem**:

- O **Gatekeeper** reduz drasticamente os pontos de entrada da sua API
- O **Valet Key** evita que sua API vire um intermediário pesado e desnecessário, e ainda limita o acesso ao mínimo possível
- O **Token Relay** garante que mesmo lá no fundo da arquitetura, os serviços ainda saibam quem é o usuário de verdade por trás daquela chamada

Esses três padrões juntos podem mudar completamente a forma como você enxerga a segurança — saindo do escopo somente da aplicação e indo para o alto nível, para a arquitetura.

Você para de pensar em "como validar um token nesse endpoint" e começa a pensar em "**por que esse endpoint está exposto desse jeito**". E quando você tem a resposta para essa pergunta, o desenho da sua arquitetura pode mudar junto com ela.
