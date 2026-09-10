# Como um Painel Admin Vibe Coded é Invadido em Segundos (Burp, ffuf, Hydra)

**Formato:** Transcrição de vídeo (autor/canal não identificados no texto fornecido — menções a "meu curso" de pentest em Early Access sugerem criador de conteúdo de segurança ofensiva/pentest em pt-BR).
**Contexto declarado:** Laboratório de teste autorizado ("lembre-se sempre de testar sistemas que você tem autorização para testar, monte o seu laboratório").

## Cenário

O vídeo abre com um cenário hipotético: alguém decide tirar do papel uma pizzaria estilo tradicional/família e, para economizar tempo, usa uma ferramenta de IA generativa pedindo "cria um site de pizzaria clássico para mim com painel para eu gerenciar meus pedidos". Em menos de um minuto o site está no ar, bonito e funcional. O autor comenta que a IA entrega literalmente o que foi pedido — não necessariamente o que o negócio precisava — e que o código gerado tende a ser "educado demais com estranhos": ele não sabe recusar más intenções, só sabe responder ao que o protocolo HTTP pede.

O alvo do laboratório é esse site fictício de pizzaria, incluindo um pedido especial chamado "hacker special".

## Fase 1 — Reconhecimento (assumido como já feito)

O autor assume que boa parte do reconhecimento já ocorreu (enumeração de subdomínios, fingerprint de tecnologias) e foca na próxima etapa: fuzzing de diretórios e arquivos.

**Wordlists:** recomenda o pacote SecLists (`sudo apt install seclists` ou equivalente), que traz wordlists prontas para usuário, senha e fuzzing de diretórios/arquivos.

**Ferramenta usada:** dirsearch (alternativas citadas: Gobuster, ffuf — "fica à sua escolha").

Comando (reconstituído do áudio):
```
dirsearch -u <URL_ALVO> -w /usr/share/seclists/Discovery/Web-Content/<wordlist>.txt
```
Wordlist usada: uma da categoria "directories", tamanho "medium" (o autor promete indicar no fim do vídeo quais wordlists usa no dia a dia — não retomado explicitamente na transcrição fornecida).

**Resultado do dirsearch:** dois diretórios encontrados — `admin` e `dashboard`.

**Como o dirsearch funciona (explicação do autor):** para cada entrada da wordlist, a ferramenta monta uma URL testando aquele valor como path e envia a requisição, reportando o status code (200, 301, 302, 404 etc.), permitindo identificar de forma automatizada quais caminhos existem na aplicação — mesmo sem estarem linkados em nenhuma página visível.

Testando manualmente: `/dashboard` redireciona para `/admin`. O painel administrativo está exposto publicamente, sem estar linkado no site.

## Fase 2 — Reconhecimento do comportamento de login

Antes de automatizar qualquer ataque, o autor destaca a importância de entender como a aplicação reage a tentativas de login: existe MFA? Existe CAPTCHA contra automação? Existe bloqueio de conta (account lockout)?

**Teste manual:**
- Usuário `teste` + senha qualquer → resposta: "usuário não encontrado"
- Usuário `admin` (sugerido por um placeholder no campo) + senha qualquer → resposta: "senha incorreta"

**Vulnerabilidade identificada: User Enumeration.** As duas mensagens de erro são diferentes — uma diz explicitamente que o usuário não existe, a outra confirma que o usuário existe mas a senha está errada. Isso permite a um atacante enumerar quais usuários existem no sistema antes mesmo de tentar quebrar a senha. Num cenário real, o passo seguinte seria rodar um brute-force no campo de usuário para mapear contas válidas via diferença de resposta; no laboratório, o usuário `admin` já é assumido como válido.

## Fase 3 — Brute Force de senha (três ferramentas demonstradas)

### Ferramenta 1 — Burp Suite (Intruder)

Observação do autor: a demonstração usa Burp Community Edition, que é mais lento que o Burp Pro (recomendado para quem trabalha profissionalmente como pentester).

Passos:
1. Capturar a requisição de login (`admin` + senha qualquer) no proxy do Burp.
2. Enviar (`Send to Intruder`) para o módulo Intruder.
3. Marcar como posição de ataque (payload position) apenas o parâmetro `password` — o usuário `admin` já é fixo/conhecido.
4. Carregar uma wordlist de senhas como payload (`Sniper` attack, um único parâmetro variando).
5. Configurar **Grep - Extract** (ou Grep Match) procurando pela string "senha incorreta"/"senha inválida" na resposta, para que o Burp marque automaticamente quais respostas contêm essa frase.
6. Rodar o ataque (`Start attack`).

**Resultado:** todas as requisições retornam status code 200 com a frase "senha incorreta" — exceto uma, que retorna status code **302** (redirecionamento, típico de login bem-sucedido) sem a frase de erro. Essa é a senha correta.

Login confirmado com `admin` + a senha encontrada na wordlist → acesso total ao painel administrativo, incluindo faturamento, usuários e demais funcionalidades administrativas da aplicação.

### Ferramenta 2 — ffuf

Fluxo:
1. Capturar a requisição de login no Burp e usar "Copy to file" para salvar como um arquivo de requisição bruta (`hack.txt`), reaproveitando a requisição já mapeada anteriormente.
2. Editar o arquivo, substituindo o valor do campo de senha pela palavra-chave `FUZZ` (é o marcador padrão esperado pelo ffuf).
3. Rodar o ffuf apontando para esse arquivo de requisição:

```
ffuf -request hack.txt -request-proto http -w <wordlist_senhas.txt> -fr "senha incorreta"
```

- `-request`: usa a requisição salva como template.
- `-request-proto`: protocolo (http, ou https se a aplicação estivesse em TLS).
- `-w`: wordlist de senhas a testar no ponto marcado com `FUZZ`.
- `-fr`: filtra (oculta) da saída qualquer resposta que contenha a frase indicada — nesse caso, a mensagem de erro de senha incorreta. Assim, só aparece na saída a(s) resposta(s) que **não** contêm o erro, ou seja, o login bem-sucedido.

**Resultado:** ffuf reporta a senha correta, e o login com `admin` + essa senha confirma acesso ao painel.

### Ferramenta 3 — Hydra

Comando (reconstituído do áudio):
```
hydra -l admin -P <wordlist_senhas.txt> -s 8080 127.0.0.1 http-post-form \
"/admin:username=^USER^&password=^PASS^:senha incorreta"
```

Explicação parâmetro a parâmetro:
- `-l` (minúsculo): um único usuário fixo a testar (`admin`), em vez de uma lista de usuários.
- `-P` (maiúsculo): uma wordlist de senhas a testar.
- `-s`: porta não padrão (8080, no laboratório).
- IP alvo: `127.0.0.1` (laboratório local).
- `http-post-form`: informa ao Hydra que a autenticação é feita via requisição POST de formulário, com três campos separados por `:`:
  1. O path da página de login (`/admin`).
  2. O corpo da requisição, com os parâmetros reais (copiados do Burp) e os placeholders `^USER^` e `^PASS^` marcando onde o Hydra deve inserir, respectivamente, o valor de `-l` e cada linha de `-P`.
  3. A string que identifica uma tentativa de login **falha** (nesse caso, a mensagem "senha incorreta", também copiada da resposta real do servidor) — o Hydra usa essa string como critério de falha/sucesso.

**Resultado:** Hydra reporta usuário `admin` e a senha correta encontrada na wordlist, confirmando a mesma vulnerabilidade pelas três ferramentas.

## Fase 4 — Mitigações recomendadas

O autor fecha com cinco recomendações de defesa contra brute force de login:

1. **Rate limiting** — bloquear ou desacelerar requisições de um mesmo IP acima de um limiar de frequência (por segundo/minuto), calibrado pela regra de negócio.
2. **Account lockout** — bloquear a conta após um número determinado de tentativas de login falhas, impedindo brute-force contínuo mesmo com rotação de IP.
3. **CAPTCHA** — dificulta (não impede completamente — o autor reconhece que dá para contornar "na maioria das vezes") automações; usar sempre que possível.
4. **Respostas de erro genéricas** — não diferenciar "usuário não encontrado" de "senha incorreta"; usar sempre uma mensagem única do tipo "usuário ou senha incorretos" para dificultar user enumeration (o autor reconhece que isso não impede enumeração por outras vias, mas dificulta).
5. **MFA sempre que possível** — protege o usuário final mesmo que usuário e senha sejam comprometidos, pois o segundo fator está sob controle exclusivo do dono da conta.
6. **Política de senha forte** — impor complexidade mínima na criação/troca de senha, já que usuários tendem a escolher senhas fracas por conta própria.

## Encerramento

O vídeo termina indicando um próximo vídeo da mesma série sobre XSS — roubo de cookie de sessão de administrador para login sem necessidade de senha.
