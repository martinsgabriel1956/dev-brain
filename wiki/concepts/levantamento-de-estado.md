---
type: concept
title: "Levantamento de estado (lifting state up)"
aliases: ["lifting state up", "levantar estado", "callback como prop", "comunicação filho → pai"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [react, estado, componentes, props]
skill: lang-dynamic
status: stub
---

# Levantamento de estado (lifting state up)

Quando dois componentes precisam do mesmo dado, ou o pai precisa de algo que acontece no filho, o estado sobe para o ancestral comum. O filho recebe o valor por props e avisa mudanças chamando uma função que também veio por props.

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]): o `Dropzone` sabe qual arquivo foi escolhido, mas quem envia o formulário é o `CreatePoint`. O pai guarda `const [selectedFile, setSelectedFile] = useState<File>()` e passa `<Dropzone onFileUploaded={setSelectedFile} />`. O filho declara `onFileUploaded: (file: File) => void` e o chama no `onDrop`. Para [[wiki/entities/diego-fernandes]], é "comunicação entre componentes em níveis diferentes, dentro da árvore".

**Quando não basta:** com muitos níveis de repasse (*prop drilling*), entram [[wiki/concepts/context-api]] ou um gerenciador de estado. Para o estado de servidor, bibliotecas próprias ([[wiki/concepts/server-state]]).

Relacionado: [[wiki/concepts/props-react]], [[wiki/concepts/useState]], [[wiki/concepts/estado-compartilhado]], [[wiki/concepts/callback-javascript]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: Dropzone → CreatePoint
