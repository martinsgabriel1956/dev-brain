---
type: concept
title: "Wireframe"
aliases: ["wireframes", "rascunho de tela", "protótipo de baixa fidelidade", "design barato e rápido"]
date_created: 2026-11-13
date_updated: 2026-11-15
source_count: 6
tags: [ui, ux, ui-design, prototipagem, wireframe, figma]
skill: ux-ui-mentor
status: draft
---

# Wireframe

"Literalmente um pequeno protótipo de uma tela", que pode ser de alta ou média fidelidade ([[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]). Na aula, [[wiki/entities/nasser|Násser]] rascunha no [[wiki/entities/figma]] um menu (logo, links Home/Sobre/Contato, CTA) e depois título, descrição e CTA para mostrar o [[wiki/concepts/espaco-em-branco|espaçamento]] e o [[wiki/concepts/grid-de-8-pontos]] em uso.

`[skill: ux-ui-mentor]` A skill põe o wireframe no lado de baixa fidelidade: sketch → wireframe → mockup → protótipo → MVP. Wireframe é estrutura sem cor, tipografia final ou imagens reais e responde "qual a estrutura?": hierarquia, layout e fluxo. Regra: use a menor fidelidade que ainda responda a pergunta. Armadilha comum: pular do wireframe para o mockup de alta fidelidade sem testar a estrutura. O wireframe da aula já tem cor de marca e tamanhos de fonte, então está mais perto de um wireframe de média fidelidade.

## Definição: design barato e rápido

Na aula dedicada ao tema ([[wiki/sources/wireframes-parte-1-o-que-e-uso-foco-page-map-papel-e-caneta]]), wireframe é "a maneira de desenhar interfaces ou qualquer outro produto digital com a maior simplicidade possível", um "processo de criação e exploração inicial": "telinhas [...] em preto e branco", web ou app.

- **Uso:** layout de conteúdo e funcionalidade e levantamento de requisitos com o cliente, "no início do desenvolvimento", antes do design completo. Exemplo: página de vendas de curso online (vídeo, diferencial, depoimentos, estrutura do produto, instrutor, bônus, chamada para cadastro).
- **Por quê:** corrigir na prototipagem (papel, [[wiki/entities/figma]]) e não "direto no software", onde as "mil alterações" custam tempo, orçamento e flow. O limite de alterações entra no contrato desde o primeiro momento.
- **Foco:** "não é focado em detalhe visual"; é proporção, jornada, conteúdo e posição dos elementos. Visual cedo demais gera "muito, muito mais alterações".
- **Troca:** o cliente conhece o produto; quem desenvolve escuta. Ver [[wiki/concepts/ux-design]].
- **Começo:** papel e caneta, sem pensar em espaçamento, tamanho ou quantidade de conteúdo; os "passos de fidelidade" vêm depois. Antes ou junto vem o [[wiki/concepts/page-map]], a ordem das dobras.

Isso bate com a skill (estrutura antes do visual, menor fidelidade que responda a pergunta). A diferença: a skill entrega o wireframe ao time interno e o mockup ao cliente; Násser leva o wireframe direto ao cliente. Os wireframes coloridos das aulas anteriores ficam, por esta definição, nas fidelidades mais altas.

## Relação com outros conceitos

- [[wiki/concepts/hierarquia-visual]] — o wireframe valida a hierarquia antes do visual.
- [[wiki/concepts/ui-design]] — artefato de trabalho do designer de interface.
- [[wiki/concepts/page-map]] — ordem das dobras que o wireframe desenha.
- [[wiki/concepts/simplicidade-visual]] — simplicidade como método, não só como resultado.

## Hero

Na aula de ilustrações, "o wireframe hero" é "aquela primeira seção do seu site", lugar indicado para texto de um lado e ilustração do outro ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]). Ver [[wiki/concepts/ilustracoes-em-interfaces]].

## Realinhar um wireframe

Em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]], um wireframe da futura seção de interface web é desalinhado de propósito e refeito no grid de 12 colunas com a escala 16/32/128.

## Baixa fidelidade, depois do pagemap

Na abertura do módulo de interfaces web, wireframes são "protótipos de baixa fidelidade que nos permitem melhorar muitas coisas e projetar de maneira simples", a segunda etapa do [[wiki/concepts/workflow-de-interface-web]] ([[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]]). Vêm depois do [[wiki/concepts/pagemap]]: primeiro o flow de dobras, depois o wireframe que cabe em cada uma. Uma biblioteca de wireframes no Notion, para copiar para o [[wiki/entities/figma]], vai crescer para ampliar o [[wiki/concepts/repertorio]] dos alunos. A aula contrasta com a definição anterior ("alta ou média fidelidade"): os wireframes do case [[wiki/entities/nubank]] "partiram" de versões de baixa fidelidade.

## Antes do style guide

Na aula de [[wiki/concepts/style-guide]], wireframe é uma das três etapas (pesquisa, wireframe, grids) que levam ao protótipo final, onde entram o style guide e as cores. O arquivo de wireframes foi compartilhado por link com os alunos: exemplo de documento que evolui sem esperar ficar perfeito ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).

## Antes do wireframe: briefing e page map

Em [[wiki/sources/wireframes-parte-2-briefing-objetivo-page-map-leitura-f-z]], o wireframe é a última etapa de uma sequência: [[wiki/concepts/briefing]] (marca, diferencial, carro-chefe, objetivo), depois flow, site map e [[wiki/concepts/page-map]], e só então os "wireframes que condizem com esse page map". O page map de portfólio começa pelo hero: headline "objetiva e direta" e um parágrafo mais detalhado abaixo. Os padrões de leitura em F e em Z entram como boa prática ao projetar ([[wiki/concepts/hierarquia-visual]]).

## Na prática: catálogo de seções e o Frankenstein

A primeira aula prática de wireframes do [[wiki/entities/frontpush|FrontPUSH]] mostra um catálogo de modelos de seção, quase todos de [[wiki/concepts/secao-hero|hero]]: app, headline + ilustração, perspectiva, texto em tópicos, desktop, depoimentos e cadastro. A tese é montar a página como um "Frankenstein" desses modelos, guiado pelo [[wiki/concepts/page-map]] e por uma [[wiki/concepts/biblioteca-de-wireframes]] ([[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]]). Os modelos já usam perspectiva e ilustração, e ele anuncia os wireframes "de baixa fidelidade" do [[wiki/entities/nubank]] e a passagem do protótipo do FrontPUSH "para o protótipo de alta fidelidade".

## Page map por referências

Em [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]], [[wiki/entities/nasser|Násser]] explica de onde veio o [[wiki/concepts/page-map]] do wireframe do portfólio dele: hero (headline objetiva e direta, parágrafo, ilustrações e branding, botões com call to action), processo, workflow, cases, CTA final e quem sou eu, tirados de sites de referência ([[wiki/entities/jonas-miller]], [[wiki/entities/fabio-freire]]). Ele mostra também os protótipos de baixa e de alta fidelidade do próprio site e do [[wiki/entities/frontpush]]: "sempre começa assim".

## No processo: média fidelidade em escala de cinza

Em [[wiki/sources/wireframes-parte-3-passo-a-passo-fidelidade-escala-de-cinza-segredo]], o wireframe é o quinto de seis passos (requisitos → [[wiki/concepts/page-map]] → referências → esboço no papel → wireframe → protótipo final com o [[wiki/concepts/style-guide]]). São "telas semi-prontas em escala de cinza", de **média fidelidade** ([[wiki/concepts/fidelidade-de-prototipo]]): já consideram espaçamentos, funcionalidades, conteúdo, jornada e proporções, mas continuam fáceis de modificar, "por isso que é tudo cinza". Cor, contraste e branding ficam para o protótipo final. Os wireframes com cor das aulas anteriores eram demonstrações, não esse passo.

O segredo para saber desenhá-los: "fazer mil vezes e ter uma biblioteca na sua mente". Um wireframe novo é a montagem de estruturas já conhecidas. Násser admite ter pulado o wireframe cinza no [[wiki/entities/frontpush]].

## Wireframe no grid

Em [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]]: "muito do que eu falei em wireframes também se encaixa" nos grids. No wireframe mostrado, o conteúdo pega seis colunas centrais (três sobram de cada lado). A ilustração fica de fora, de propósito, pelo estilo dela. Ver [[wiki/concepts/grid-de-colunas]].

## Grid como base do wireframe

Em [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]], o grid é o que dá alinhamento, consistência e organização aos "protótipos de média fidelidade ou até baixa fidelidade" feitos com wireframes. Os plugins de grid são prometidos para as próximas aulas.

## Revisar os wireframes do autor

Em [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]] o autor convida: "venham aqui nos meus wireframes, vejam se tem alguma coisa errada, pergunta para mim".

## Wireframes no grid

Em [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]], os wireframes do curso (features, menu) estão todos no grid de 12 colunas de 72. Basta clicar no olhinho do grid para conferir. O bloco de features ocupa seis colunas, com título, parágrafo e lista alinhados à esquerda. Ele admite "alguns wireframes que eu pequei em determinado alinhamento" e corrige ao vivo uma ilustração torta. O exercício é abrir os wireframes do arquivo e conferir o alinhamento.

## Cor de base só no hero

Em [[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]]: o site pode ser todo branco, com blocos em cinza, e só o banner principal ("no wireframe hero") na cor de base. Ver [[wiki/concepts/paleta-de-cores]].

## Key Sources

- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — hero como primeira seção, com ilustração
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — wireframe desalinhado e refeito no grid de 12 colunas
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — blobs (plugin Blobs) como bolhas na composição de wireframes
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — wireframes isométricos com gradiente linear embaixo e sombra
- [[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]] — abertura do módulo de interfaces web: baixa fidelidade, depois do pagemap; biblioteca no Notion
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — pesquisa, wireframe e grids antes do style guide; arquivo compartilhado por link
- [[wiki/sources/wireframes-parte-1-o-que-e-uso-foco-page-map-papel-e-caneta]] — aula dedicada: definição, uso com cliente, foco, page map, papel e caneta
- [[wiki/sources/wireframes-parte-2-briefing-objetivo-page-map-leitura-f-z]] — pt.2 da série: briefing, objetivo, page map, leitura em F e em Z
- [[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]] — catálogo de wireframes de seção (Hero), PageMap e o Frankenstein
- [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]] — page map do portfólio tirado de referências; baixa e alta fidelidade do FrontPUSH
- [[wiki/sources/wireframes-parte-3-passo-a-passo-fidelidade-escala-de-cinza-segredo]] — papel → wireframe cinza (média fidelidade) → protótipo final; o segredo é fazer mil vezes
- [[wiki/sources/grids-parte-1-colunas-bootstrap-8pt-fixo-fluido-adaptativo-responsivo]] — wireframe com conteúdo nas seis colunas centrais
- [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] — grids para alinhar wireframes de baixa e média fidelidade
- [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]] — convite para revisar os wireframes do curso
- [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]] — wireframes de features e de menu conferidos no grid; exercício de verificar o alinhamento
- [[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]] — hero em roxo, resto branco e cinza
