# Como IA Generativa e Agêntica Desloca a Preocupação de Dívida Técnica para Dívida Cognitiva

**Autora:** Margaret-Anne Storey
**Publicado:** 09 fev. 2026
**Fonte:** https://margaretstorey.com/blog/2026/02/09/cognitive-debt/

> Tradução integral do original em inglês, extraído via fetch da URL acima.

---

O termo *dívida técnica* costuma ser usado para se referir ao acúmulo de escolhas de design ou implementação que, mais tarde, tornam o software mais difícil e mais custoso de entender, modificar ou estender ao longo do tempo. A dívida técnica capta bem a ideia de que a "compreensão humana" também importa, mas as palavras "dívida técnica" evocam a noção de que a dívida acumulada é uma propriedade do código, e que o esforço para removê-la deve ser aplicado sobre o código.

*Dívida cognitiva*, um termo que vem ganhando [tração](https://www.media.mit.edu/publications/your-brain-on-chatgpt/) recentemente, comunica em vez disso a noção de que a dívida acumulada por "ir rápido demais" vive na cabeça dos desenvolvedores e afeta suas experiências vividas e sua capacidade de "ir rápido" ou de fazer mudanças. Mesmo que agentes de IA produzam código que poderia ser fácil de entender, os humanos envolvidos podem simplesmente ter perdido o fio da meada e não entender mais o que o programa deveria fazer, como suas intenções foram implementadas, ou como possivelmente alterá-lo.

*Legenda da imagem do post original: "A dívida técnica vive no código; a dívida cognitiva vive na mente dos desenvolvedores".*

## Dívida cognitiva como ameaça maior

A dívida cognitiva é provavelmente uma ameaça muito maior do que a dívida técnica à medida que IA e agentes são adotados. Peter Naur nos lembrou, décadas atrás, que um programa é mais do que seu código-fonte. Ao contrário, [um programa é uma teoria](https://pages.cs.wisc.edu/~remzi/Naur.pdf) que vive na mente do(s) desenvolvedor(es), capturando o que o programa faz, como as intenções dos desenvolvedores foram implementadas, e como o programa pode ser alterado ao longo do tempo. Normalmente essa teoria não está apenas na mente de um único desenvolvedor — fragmentos dela estão distribuídos pelas mentes de muitos, às vezes milhares, de outros desenvolvedores.

## Exemplo: o curso de empreendedorismo

A autora viu essa dinâmica se manifestar vividamente em um curso de empreendedorismo que lecionou recentemente. Equipes de estudantes estavam construindo produtos de software ao longo do semestre, avançando rapidamente para lançar funcionalidades e cumprir marcos. Mas, por volta das semanas 7 ou 8, uma equipe bateu numa parede: não conseguiam mais fazer nem mudanças simples sem quebrar algo inesperado. Ao se reunir com a equipe, inicialmente eles culparam a dívida técnica: código bagunçado, arquitetura pobre, implementações apressadas. Mas, ao investigar mais a fundo, o problema real emergiu: ninguém na equipe conseguia explicar *por que* certas decisões de design haviam sido tomadas ou *como* diferentes partes do sistema deveriam funcionar juntas. O código podia estar bagunçado, mas o problema maior era que a teoria do sistema — a compreensão compartilhada da equipe — havia se fragmentado ou desaparecido por completo. Eles haviam acumulado dívida cognitiva mais rápido do que dívida técnica, e isso os paralisou.

## Coordenação e Fred Brooks

Essa dinâmica ecoa uma lição clássica do *Mythical Man-Month*, de Fred Brooks. Adicionar mais agentes a um projeto pode adicionar mais sobrecarga de coordenação, decisões invisíveis e, portanto, carga cognitiva. Claro, agentes também podem ser usados para gerenciar carga cognitiva, resumindo quais mudanças foram feitas e como — mas as restrições fundamentais da memória e da capacidade de trabalho humanas serão esticadas pela pressão por velocidade a qualquer custo. A relutância em desacelerar e fazer o trabalho que Kent Beck chama de "tornar a [mudança difícil, fácil](https://tidyfirst.substack.com/p/tidy-first-example)" é o que levará à dívida cognitiva e à sobrecarga no futuro.

Em uma [sessão](https://martinfowler.com/fragments/2026-02-09.html) do recente *Future of Software Engineering Retreat* (organizado por Martin Fowler e a Thoughtworks), discutiu-se como desenvolvedores precisam desacelerar e usar práticas como pair programming, refatoração e desenvolvimento orientado a testes para lidar com a dívida técnica E a dívida cognitiva. Ao desacelerar e seguir essas práticas, a dívida cognitiva também pode ser reduzida e a compreensão compartilhada entre desenvolvedores e equipes, reconstruída.

## O que times podem fazer

Mas o que as equipes podem fazer concretamente à medida que IA e agentes se tornam mais prevalentes?

Primeiro, precisam reconhecer que velocidade sem compreensão não é sustentável. Equipes devem estabelecer estratégias de mitigação de dívida cognitiva. Por exemplo, podem exigir que ao menos um humano na equipe compreenda totalmente cada mudança gerada por IA antes de ela ir para produção, documentar não apenas *o que* mudou, mas *por quê*, e criar checkpoints regulares em que a equipe reconstrói a compreensão compartilhada por meio de code reviews, retrospectivas ou sessões de compartilhamento de conhecimento.

Segundo, precisamos de formas melhores de detectar dívida cognitiva antes que ela se torne paralisante. Sinais de alerta incluem: membros da equipe hesitando em fazer mudanças por medo de consequências não intencionais, dependência crescente de "conhecimento tribal" concentrado em apenas uma ou duas pessoas, ou uma sensação crescente de que o sistema está se tornando uma caixa-preta. Esses podem ser sinais de que a teoria compartilhada está se corroendo.

Por fim, esse fenômeno demanda atenção séria de pesquisa. Como medimos a dívida cognitiva? Quais práticas são mais eficazes para preveni-la ou reduzi-la em ambientes de desenvolvimento aumentados por IA? Como a dívida cognitiva escala em equipes distribuídas ou projetos open-source, onde a "teoria" precisa ser reconstruída por recém-chegados? À medida que IA generativa e agêntica remodelam a forma como o software é construído, entender e gerenciar a dívida cognitiva pode ser um dos desafios mais importantes que nosso campo enfrenta.

## Fechamento

A autora explorará essas questões em uma palestra (keynote) na [ICSE Technical Debt Conference](https://conf.researchr.org/attending/TechDebt-2026/keynotes#dr-margaret-anne-storey) e em um [painel](https://conf.researchr.org/info/icse-2026/panels). A dívida cognitiva tende a não se anunciar por meio de builds quebrados ou bugs sutis pós-deploy, mas sim através de uma perda silenciosa da teoria compartilhada. À medida que IA generativa e agêntica aceleram o desenvolvimento, proteger essa teoria compartilhada sobre o que o software faz e como ele pode mudar pode importar mais para a saúde do software no longo prazo do que qualquer métrica isolada de velocidade ou produção.

---

**Sobre a autora:** Professora de Ciência da Computação, University of Victoria (Canadá). Canada Research Chair em Aspectos Humanos e Sociais de Engenharia de Software.
