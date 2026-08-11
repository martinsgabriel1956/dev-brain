# Qual é o teu potencial como programador? Atitude e mindset acima da tech skill

> Transcrição limpa de vídeo (Lucas Montano) reagindo ao artigo *"How to recognize the potential in engineers"* de Gregor Ojstersek (newsletter Engineering Leadership / Substack). Pontuação e parágrafos ajustados para leitura; conteúdo preservado.

---

Cara, qual que é o teu potencial como programador? O que te faz um programador de alta performance? A gente vai ver um artigo aqui, mas eu queria validar o artigo escrevendo em forma de código.

Segundo o artigo, a performance de um software engineer vai ser basicamente definida em três parâmetros: a tua **tech skill**, a tua **atitude** e o teu **mindset**. É isso que te faz alguém com performance na programação.

E, de acordo com alguns autores, se a tua atitude for maior que a tua tech skill, e o teu mindset for maior que a tua tech skill — ou seja, tu tem atitude e tu tem um bom mindset — tu vai ser considerado um **great engineer**, um ótimo engenheiro. Vamos retornar essa string. E, do contrário, a gente vai retornar que tu é meramente **average**, tu vai estar na média.

Primeira versão do script (a ingênua):

```python
def avaliar_engenheiro(tech_skill, atitude, mindset):
    if atitude > tech_skill and mindset > tech_skill:
        return "great engineer"
    else:
        return "just an average engineer"  # (e ainda escrito "avarage" errado)
```

Olhando para esse código, o que tá errado? Sim, eu poderia ter um return só e fazer um lift disso; poderia simplificar mais ainda. Mas, tirando simplificar o código, o que tá de errado aqui? O "average" tá escrito errado — é "avarage". Mas o meu **maior** problema é outro, e vou mostrar rodando o script.

Digamos que a gente tenha um engenheiro com tech skill de **90**, atitude de **50** e mindset de **20** (tá muito desmotivado, precisa ver mais vídeos). Olhando para esse cara: tech skill de 90, ele vai ser um ótimo engenheiro, né? Não — pela regra, ele é "just an average engineer". Até faz sentido: o cara tem um mindset errado, não tá motivado; na prática ele tá rendendo por volta de 45% da tech skill dele.

Agora, se a gente aumentar a atitude para **80** e o mindset para **80** — tech skill 90, atitude 80, mindset 80 — quando rodar isso, a gente vai ver que, pela regra ingênua, ele ainda é só mais um engenheiro médio (porque a atitude não é *maior* que a tech skill). Ou seja, a regra `>` está furada.

## O artigo: como reconhecer o potencial de um engenheiro

Do Gregor, lá no Substack. Existe um equívoco comum na indústria: o de que as habilidades técnicas são o que diferencia os engenheiros entre si — seja conhecer mais linguagens, mais frameworks, ou ter experiência em vários projetos diferentes. As habilidades técnicas certamente são importantes, mas o que realmente faz a diferença é outra coisa.

> "Eu valorizo a atitude e a mentalidade acima das habilidades técnicas ao reconhecer o potencial dos engenheiros."

As principais características não têm nada a ver com habilidade técnica — têm tudo a ver com atitude e mentalidade. Por quê? Com a atitude e a mentalidade certas, você consegue aprender todas as habilidades técnicas necessárias. E não só isso: você é uma ótima pessoa para se trabalhar e está tornando os outros ao seu redor melhores por causa disso.

O gráfico do artigo cruza dois eixos (tempo/técnica vs. valor entregue): com grande atitude e mentalidade, o valor entregue cresce muito. (É interessante que esses eixos, tecnicamente, não fazem tanto sentido.)

> "Se você melhorar a sua codificação em 20%, você entrega 20% mais valor. Mas se você ajudar outras cinco pessoas a melhorarem 20%, você agrega 100% mais valor."

Eu concordo com isso — mas tem um outro problema. Imagina um Dev especialista (sênior) e, embaixo dele, cinco devs juniores: um ratio sênior-para-júnior de 1:5. O que o autor diz é: em vez desse sênior ir de 50% para 70% (crescer 20% — e nem sei o que isso significa de verdade, porque não dá pra medir "20% melhor" nem "sei 30% de Angular", "meu JavaScript é 4 de 5 estrelas"… ninguém sabe o que é 100% de uma linguagem), é muito melhor instigar as outras pessoas: cada uma dos cinco juniores subindo 20% dá 5 × 20% = **100%** de aumento agregado.

Na teoria parece bonito. A grande questão é: **quanto tempo isso demanda?** Esse papel costuma ser dos leads — muitas vezes o Tech Lead para de codar porque o trabalho dele é fazer quem está ao redor ficar 20% melhor. E existem várias estruturas (Tech Lead, Team Lead, Staff, Principal, seniores fazendo esse papel). No fim do dia, o que importa é o **resultado que o time inteiro entrega** — e, nesse resultado, sim, mindset e atitude fazem diferença.

## As três características principais

O autor acredita que, com essas três, você pode ser um grande engenheiro (e bom em qualquer coisa que quiser):

### 1. Senso de propriedade e responsabilidade (ownership)

Exemplo bem prático com code review: você faz uma modificação, sobe o pull request, e seus colegas têm que revisar. Normal. O que é ter senso de propriedade e responsabilidade? Quando alguém pergunta "Lucas, como está o teu PR / a tua tarefa?" e a resposta é: "cara, eu fiz há uns três dias, subi o PR, mas tô esperando mais uma aprovação; ninguém aprovou ainda". Aí a pergunta certa é: **por que você não foi atrás dessa aprovação?**

Ownership é: você é responsável pela sua entrega. Se você depende de alguém para te desbloquear, vai atrás — você tem que resolver. Quantas vezes a gente vira "passageiro" (sentado no banco do carona) em vez de pilotar a própria entrega? Toda hora que você está bloqueado, é sua responsabilidade se desbloquear.

Indicadores de bom ownership (do artigo):

- Se voluntariam para projetos quando ninguém quer tomar iniciativa (isso é mais ser proativo, na verdade).
- Enfrentam problemas recorrentes e difíceis que ninguém resolve. Ex.: um teste *flaky* que falha a cada 5 builds e "magicamente" passa ao rodar de novo — todo mundo sabe, ninguém investiga a causa. Ou um monte de passo manual de deploy que ninguém automatiza.
- São proativos: sugerem melhorias **e** tomam a iniciativa de implementá-las. Só sugerir melhoria, sem implementar, é pior do que não sugerir. Existe o perfil que critica tudo, comenta no seu PR que "tem uma forma melhor", mas não mostra qual é nem coloca a mão no código — você segue o caminho dele, prova que não funciona, ele continua argumentando sem codar, e no fim alguém desiste de cansaço e volta para a implementação original.
- Não esperam a tarefa ser atribuída: buscam proativamente o que é mais impactante. Não precisam de requisitos superdetalhados — resolvem o problema conversando com as pessoas certas. São eles que escrevem o plano quando o time está discutindo (muito importante em empresa grande, onde os requisitos nunca estão bem detalhados: mostra que a pessoa reuniu as opiniões e formulou um plano com o qual o time todo concordou).

### 2. Impulso e motivação para melhorar (drive)

- São apaixonados por novas tecnologias e conceitos — o que **não** significa pular de framework em framework, de biblioteca em biblioteca.
- Compartilham conhecimento regularmente. Ex.: um script que automatiza o mapeamento local de proxy (para mocar retornos de request sem dar 10 cliques na interface do Charles Proxy) — vale compartilhar com os colegas como foi implementado. Pode ser conhecimento técnico ou do próprio projeto.
- Gostam de ler e ouvir (ouvir devia vir antes) e muitas vezes de escrever. Um bom indicador é manter um blog pessoal, uma newsletter, ou postar no Twitter/X.

### 3. Ser um jogador de time e tornar os outros melhores

- Têm a **mentalidade de dar primeiro** (*give-first*): entendem que ótimos relacionamentos começam com a doação. Estão sempre procurando maneiras de ajudar e oferecem ajuda a quem precisa.
- Pensam no que é melhor para o time.
- Os outros gostam de trabalhar com eles — o "efeito magnético". Isso aparece fácil em empresas com ciclo de feedback para os leads. "Os outros gostam de trabalhar com você" diz muito sobre você.
- Se esforçam para construir bons relacionamentos com a equipe e a organização.

## Conclusão do autor

> "Na indústria de engenharia, as principais características que eu procuro não estão relacionadas à competência técnica. Isso porque construir software é uma atividade social — pessoas trabalhando em silos trazem mais problemas do que benefícios. Seja uma ótima pessoa para trabalhar e foque em ajudar os outros: isso aumenta drasticamente o seu valor."

Dica que dei há 5 anos no canal: **para de ser idiota.** É isso — essa é a soft skill que você precisa. Seja proativo, deixe de ser preguiçoso. São coisas básicas. Só que eu ainda acho que o **conhecimento técnico tem peso maior**: eu não preciso de um monte de coach no meu time; preciso de gente que entrega também.

## Corrigindo o script (versão com pesos e thresholds)

A regra `>` era simplista demais. Melhor dar pesos e usar thresholds:

```python
def avaliar_engenheiro(tech_skill, atitude, mindset):
    tech_score     = tech_skill * 0.5    # peso 0.5
    atitude_score  = atitude    * 0.25   # peso 0.25
    mindset_score  = mindset    * 0.25   # peso 0.25
    total = (tech_score + atitude_score + mindset_score) / 100  # normaliza 0..1

    GREAT   = 0.85
    AVERAGE = 0.65

    if total >= GREAT:
        return "great engineer"
    elif total >= AVERAGE:
        return "average engineer"
    else:
        return "suck"
```

Testando:

- Tech 90, atitude 80, mindset 80 → **great engineer**.
- Tech 100, atitude 20 ("o idiota"), mindset 30 ("meio preguiçoso") → ainda dá **great engineer**.

Ou seja: com a ponderação, o peso técnico ainda domina o resultado. Concordo com o autor que atitude e mindset importam — mas, na minha ponderação, a tech skill continua tendo o maior peso.
