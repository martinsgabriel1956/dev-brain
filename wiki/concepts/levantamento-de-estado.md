---
type: concept
title: "Levantamento de estado (lifting state up)"
aliases: ["lifting state up", "levantar estado", "callback como prop", "comunicação filho → pai"]
date_created: 2026-11-16
date_updated: 2026-11-17
source_count: 3
tags: [react, estado, componentes, props]
skill: lang-dynamic
status: stub
---

# Levantamento de estado (lifting state up)

Quando dois componentes precisam do mesmo dado, ou o pai precisa de algo que acontece no filho, o estado sobe para o ancestral comum. O filho recebe o valor por props e avisa mudanças chamando uma função que também veio por props.

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]): o `Dropzone` sabe qual arquivo foi escolhido, mas quem envia o formulário é o `CreatePoint`. O pai guarda `const [selectedFile, setSelectedFile] = useState<File>()` e passa `<Dropzone onFileUploaded={setSelectedFile} />`. O filho declara `onFileUploaded: (file: File) => void` e o chama no `onDrop`. Para [[wiki/entities/diego-fernandes]], é "comunicação entre componentes em níveis diferentes, dentro da árvore".

**Quando não basta:** com muitos níveis de repasse (*prop drilling*), entram [[wiki/concepts/context-api]] ou um gerenciador de estado. Para o estado de servidor, bibliotecas próprias ([[wiki/concepts/server-state]]).

Relacionado: [[wiki/concepts/props-react]], [[wiki/concepts/useState]], [[wiki/concepts/estado-compartilhado]], [[wiki/concepts/callback-javascript]].

## Na NLW #2, dia 5 (Diego Fernandes)

O `TeacherItem` copia `favorited` para um estado próprio e perde a sincronia; manter os ids no `TeacherList` e passar `favorited` + `onToggle` seria a fonte de verdade única. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: Dropzone → CreatePoint
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: favorito: estado no pai
- [[wiki/sources/frontpush-spa-componentes-estrutura-app-js-componentizacao]]: FrontPUSH, React aula 05: o contraponto: sidebar e content da KaBuM dependem do mesmo produto
