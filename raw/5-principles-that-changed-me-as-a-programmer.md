# 5 Princípios Que Vão Mudar Você Como Programador

> Transcrição de vídeo sobre 5 princípios aprendidos na prática — não em faculdade.
> O fio condutor: **realidade vs. teoria**. O que importa em produção diverge do que se ensina em cursos.

---

## Princípio 1 — Logs São Mais Importantes Que o Seu Código

Quando comecei, achei que logs eram para outras pessoas. Eu escrevia código, funcionava na minha máquina, e era o suficiente.

Aí fiz deploy em produção. Algo quebrou. Sem logs. Só usuários irritados e uma tela de erro em branco.

Passei **6 horas** entrando via SSH em servidores, adicionando print statements, fazendo redeploy. 6 horas porque estava com preguiça de adicionar 5 linhas de logging.

**A realidade:** seu código vai quebrar em produção. Sempre. E quando acontecer — às 3h da manhã — você precisa saber o que *de fato* aconteceu. Não o que você *acha* que aconteceu.

Bons logs são a diferença entre "vejo o problema" e "vou ficar 3 horas chutando".

**Regra prática:** logue tudo que importa — inputs, outputs, erros — sempre com contexto.

```python
# RUIM
print("erro")

# BOM
logger.error("Falha ao processar pagamento", extra={
    "user_id": user.id,
    "amount": amount,
    "payment_method": method,
    "error": str(e)
})
```

---

## Princípio 2 — Usuários Vão Quebrar Tudo Que Você Não Testou

Construí um formulário. Simples: nome, email, enviar. Testei. Funcionou perfeitamente.

Fiz deploy. O primeiro usuário quebrou imediatamente.

**Como?** Emoji no campo de nome. Nunca pensei em testar isso. Acontece que muita gente faz isso.

Usuários são criativos de formas que você não consegue imaginar:
- Strings vazias
- Números negativos
- `null`
- SQL injection
- Spam de 50 cliques porque não respondeu em 0,2 segundos
- Internet Explorer em 2026

Toda suposição que você faz está errada. Eles vão encontrar o edge case que você não pensou e quebrar tudo.

> *"O impossível se torna possível no segundo em que alguém chamado Dave começa a digitar."*

**Regra prática:** teste para o impossível — especialmente inputs inválidos, vazios, gigantes, com caracteres especiais e comportamento concorrente.

---

## Princípio 3 — Tech Debt Não É um Pecado, É uma Ferramenta

Eu achava que atalhos eram ruins. Então passava semanas arquitetando soluções perfeitas — clean architecture, abstrações corretas, design patterns lindos.

Aí o negócio pivotava. A feature que eu passei 3 semanas perfeiçoando era descartada.

Às vezes você deveria tomar atalhos. Hardcodar valores. Copiar e colar código. Não porque você é preguiçoso — porque **velocidade importa mais que perfeição** na fase de validação.

Tech debt deixa você validar ideias rapidamente:
- Se a feature funcionar e os usuários amarem → refatore depois
- Se não funcionar → você economizou 3 semanas

**A maioria das features falha.** Não construa um palácio para algo que pode ser demolido no mês que vem.

Faça o deploy com debt. Pague depois. **Se** sobreviver. Palavra-chave: *se*.

**Referência:** Quadrante de Fowler — o único debt aceitável é Prudente + Deliberado.

---

## Princípio 4 — Dar Nome às Coisas É de Fato a Parte Mais Difícil

Eu achava que isso era meme. Não é.

Já passei 30 minutos nomeando uma única variável. Porque nomes importam.

Herded código com uma função chamada `doStuff`. Ótimo — ela faz *alguma coisa*. Passei 2 horas descobrindo que ela processava payment webhooks. Por que não chamar de `processPaymentWebhook`?

Toda vez que você nomeia algo `data`, `info`, `manager`, `handler` — você está tornando a vida mais difícil. Inclusive a sua, daqui a 6 meses.

Você não vai lembrar o que `data2` significa. Mas se você chamar de `validatedUserInput`, você vai saber exatamente o que é.

**Regra prática:** gaste 5 minutos no nome e economize 5 horas depois.

**E mais:** se você não consegue nomear algo claramente, você não entende o que esse código faz.

---

## Princípio 5 — Funcionar Localmente Não É Funcionar em Produção

Fiz deploy uma vez. Funcionou perfeitamente na minha máquina. Quebrou instantaneamente em produção.

Por quê?

| Ambiente | Local | Produção |
|---|---|---|
| Usuários | 1 (você) | 1.000 simultâneos |
| Dados | 10 linhas de teste | Milhões de rows |
| Latência | localhost | Rede real |
| Sistema Operacional | Seu SO | SO diferente |
| Recursos | Seu laptop potente | Servidor limitado |

Seu laptop é um mentiroso. É rápido, confiável, perfeito. Produção é lenta, instável, caótica.

O bug que só acontece em prod é o pior tipo — você não consegue reproduzir localmente. Você está debugando às cegas.

**Regra prática:**
- Use Docker para espelhar o ambiente de produção localmente
- Use um ambiente de staging antes de ir pra prod
- Faça deploy cedo e com frequência — quanto mais cedo descobrir, mais barato corrigir

*"Funciona na minha máquina"* não é aceitável num ambiente profissional.

---

## O Padrão

Todos esses princípios são sobre **realidade, não teoria**.

A escola ensina algoritmos. Não ensina que:
- Logs salvam carreiras
- Usuários são agentes do caos
- Tech debt às vezes é a decisão certa
- Naming é metade do trabalho
- Seu laptop mente

Ninguém me ensinou isso. Aprendi na dor.
