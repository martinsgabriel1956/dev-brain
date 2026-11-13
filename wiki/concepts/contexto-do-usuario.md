---
type: concept
title: "Contexto do Usuário no Design"
aliases: ["perfil do usuário", "preferências e comportamento do usuário", "cultura no design", "design para idosos", "público-alvo da interface"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 5
tags: [ui, ux, ui-design, usuario, cultura, acessibilidade, idosos, design-inclusivo]
skill: ux-ui-mentor
status: stub
---

# Contexto do Usuário no Design

Quem é o usuário, o que prefere, como se comporta e de que cultura vem. Junto com o [[wiki/concepts/objetivo-da-interface|objetivo]], são os fatores que o designer precisa responder antes de decidir a interação; por isso a melhor forma "depende" ([[wiki/sources/elementos-da-interface-introducao-ui-design]]). O slide da aula lista seis: objetivos, preferências, comportamento, usuário, cultura e posicionamento.

## Usuário: o exemplo dos idosos

Saber que a maioria dos usuários é idosa já muda o projeto ([[wiki/sources/elementos-da-interface-introducao-ui-design]]):

- **Tipografia maior.** 14 px e 16 px seriam pequenos; a escala começaria em 18 px, a depender da fonte.
- **Mais [[wiki/concepts/contraste]].** Cuidado com cinzas próximos do fundo; oferecer botão de alto contraste.

`[skill: ux-ui-mentor]` Idosos não são grupo homogêneo, mas os padrões se repetem: texto base de 16 a 18 px com zoom até 200% sem quebra, alvos de toque de 44 a 48 px, rótulos visíveis (não só placeholder), menos gestos escondidos, sem timeouts curtos, confirmação clara de sucesso ([[wiki/concepts/feedback-do-sistema]]) e um canal humano visível.

## Comportamento: padrões aprendidos

O usuário traz hábitos de outras interfaces. Num website, o menu fica à esquerda ou no topo, e pô-lo embaixo "fere um pattern" ([[wiki/sources/elementos-da-interface-introducao-ui-design]]). Ver [[wiki/concepts/padroes-de-interface]] e [[wiki/concepts/lei-de-jakob]].

## Cultura

- **Direção de leitura.** A esquerda é o primeiro ponto de atenção porque leitores ocidentais leem da esquerda para a direita. Em idiomas da direita para a esquerda a lógica se inverte (inferência do agente, não dita na aula).
- **Cor.** A mesma cor pode ter outra leitura no Brasil, nos EUA, no Japão ou na Europa. Uma solução pensada para o Brasil não necessariamente funciona fora ([[wiki/sources/elementos-da-interface-introducao-ui-design]]).

## Relação com outros conceitos

- [[wiki/concepts/usuarios-como-agentes-do-caos]] — projetar para o usuário real, não para o ideal.
- [[wiki/concepts/ux-design]] — conhecer o usuário é trabalho de pesquisa de UX.
- [[wiki/concepts/hierarquia-visual]] — a posição (topo, esquerda) depende da direção de leitura.

## Comportamento: o olhar vai para o que está isolado

Em [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]], o autor liga o macro espaço ao fator comportamento: numa tela toda preta com uma bolinha de destaque no centro, o usuário olha para a bolinha "automaticamente". Ver [[wiki/concepts/espaco-em-branco]].

## Público-alvo e forma

Na loja de produtos para bebês, quem compra são os pais, que querem algo seguro para os filhos; uma fonte pontiaguda fica "desconexa com o público-alvo". Formas arredondadas, cores pastéis e ilustrações à mão conversam com esse público ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]; ver [[wiki/concepts/formas-geometricas-e-organicas]]).

## Proposta do produto e nicho

O [[wiki/entities/creatorpush]], de proposta "mais baixo nível", ganha formas mais redondas para ficar mais perto do usuário; um site de arquitetura, ao contrário, pede formas retas para passar confiança. "Depende daquilo que a gente está tratando" ([[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]]).

## Imagem quando o texto não ajuda

Num app em japonês ou chinês, "uma boa ilustração ou uma boa imagem" dá ao usuário ocidental a ideia mínima do que fazer; na biometria, uma animação antes da foto do rosto explica a etapa ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]).

## Key Sources

- [[wiki/sources/elementos-da-interface-introducao-ui-design]]
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — comportamento: o olhar vai ao elemento isolado por espaço
- [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]] — loja de bebês: pais querem algo seguro
- [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] — Creator Push mais redondo; arquitetura mais reta
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — imagem como guia em app de idioma desconhecido e na biometria
