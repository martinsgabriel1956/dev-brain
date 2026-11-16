---
type: source
title: "NLW #1 com Diego Fernandes, dia 5: upload de imagens, validação, GitHub e deploy do Ecoleta"
aliases: ["NLW 1 Diego dia 5", "Ecoleta upload multer", "Ecoleta celebrate Joi", "NLW 1 trilha Node React dia 5"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [nodejs, express, multer, upload, multipart-form-data, crypto, react, react-dropzone, formdata, celebrate, joi, yup, validacao, git, github, gitignore, deploy, heroku, digitalocean, netlify, vercel, s3, backend, frontend, rocketseat, ecoleta, iniciante]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1 com Diego Fernandes, dia 5: upload de imagens, validação, GitHub e deploy do Ecoleta

## TL;DR

Última aula de código (cerca de 1h02) da trilha de [[wiki/entities/diego-fernandes]] na [[wiki/entities/next-level-week|NLW #1]]. "Eu não preparei essa aula, então eu vou fazer tudo na raça." São cinco partes:

1. **Upload no back-end com [[wiki/entities/multer]].** `diskStorage` grava em `uploads/` com nome `${hash}-${originalname}` (hash de `crypto.randomBytes(6)`), e a rota `POST /points` ganha `upload.single('image')`. O Insomnia passa a mandar [[wiki/concepts/multipart-form-data]], porque "o JSON não suporta arquivos", e `items` vira texto separado por vírgula. O `image_url` é montado na listagem e no detalhe, e o app mobile passa a usá-lo.
2. **Dropzone no React** (`react-dropzone`), com `accept: 'image/*'` e preview por `URL.createObjectURL`. O arquivo sobe para o `CreatePoint` por uma função passada como prop (`onFileUploaded`), o [[wiki/concepts/levantamento-de-estado]]. O envio passa a ser `new FormData()` com `data.append(...)`.
3. **Validação no servidor** com celebrate + [[wiki/entities/joi]]: `Joi.object().keys({...})` no `body`, `abortEarly: false` e `app.use(errors())`. Yup fica indicado para o front-end. Ver [[wiki/concepts/validacao-de-entrada]].
4. **GitHub:** repositório `nlw-01`, remoção do `.git` de web e mobile, [[wiki/concepts/gitignore]] (`node_modules`, `uploads/*` com `!uploads/.gitkeep`, `*.sqlite`), `git push origin master` e a sugestão de um README com imagens.
5. **Deploy (só falado):**
   - Mobile nas lojas.
   - Back-end no [[wiki/entities/heroku]] para teste, na DigitalOcean para apps pequenos e na AWS, GCP ou Azure quando crescer, "com uma pessoa [...] de SRE".
   - Front-end no [[wiki/entities/netlify]] ou na [[wiki/entities/vercel]], depois S3 ou Cloud Storage.

## Key Claims

### Upload de imagens no back-end com Multer

- **Ponto de partida:** a pessoa "consegue inserir um registro" sem nome, porque "a gente não fez nenhuma validação". O dia promete upload, dropzone, validação, GitHub ("uma das coisas mais importantes dessa Next Level Week é colocar sempre o projeto no seu portfólio") e deploy.
- **`npm install multer` e `@types/multer -D`.** Em `src/config/multer.ts`, o `multer.diskStorage({ destination, filename })`:
  - `destination: path.resolve(__dirname, '..', '..', 'uploads')`, a mesma pasta dos SVGs do seed.
  - `filename(request, file, callback)` recebe o request, os dados do arquivo e um callback.
- **Por que renomear:** usar o nome da máquina do usuário traz a chance de "um arquivo com o mesmo nome de um arquivo de uma outra pessoa". Timestamp também falha, porque duas pessoas podem fazer upload "exatamente no mesmo milissegundo".
- **O nome:** `crypto.randomBytes(6).toString('hex')`, "a forma mais nativa possível", mais um hífen e `file.originalname`, então `teste.jpg` vira `hash-teste.jpg` e "ainda dá para identificar". O `callback(null, fileName)` leva erro nulo, porque "praticamente é impossível dar erro nessas duas linhas". Ver [[wiki/concepts/callback-javascript]] e [[wiki/concepts/criptografia]].
- **`file` traz** `fieldname`, `originalname`, `encoding`, `mimetype` ("image/jpeg, image/png"), `size` e `filename`.
- **Rota:** `const upload = multer(multerConfig)` e `routes.post('/points', upload.single('image'), pointsController.create)`. Para várias fotos ("umas 10 fotos" do Seu Zé), seria `upload.array('fotos')`. Ver [[wiki/concepts/middleware]].
- **[[wiki/concepts/multipart-form-data]]:** "infelizmente o JSON não suporta arquivos". No Insomnia, o body muda de JSON para *Multipart*, campo por campo, com `image` do tipo *File*. A foto do mercado vem do [[wiki/entities/unsplash]].
- **`items` em texto:** "eu não consigo enviar ele como um array aqui". O controller passa a fazer `items.split(',').map((item: string) => Number(item.trim()))`. Diego prefere `Number(...)` a `+item` porque "fica mais descritivo".
- **`image: request.file.filename`** substitui a imagem fixa do Unsplash. A latitude volta como string na resposta do POST, mas o banco guarda número.
- **`fileFilter`** existe para limitar tipo e tamanho ("não quero upload de arquivos que não sejam JPG, PNG [...] mais do que 2 MB"), mas "não vai dar tempo da gente implementar". Ver as tensões.

### Serialização da image_url

- **O campo `image` agora é só o nome do arquivo,** e o mobile usava a URL completa. A listagem e o detalhe ganham `image_url: \`http://192.168.1.12:3333/uploads/${point.image}\``. "Será que o meu endereço é o mesmo ainda? [...] não, tá vendo que mudou agora até o 12." Ver [[wiki/concepts/endereco-ip]].
- **Repetição aceita:** "poderia separar em uma função útil". Para Node, há bibliotecas de serialização ("API Response Transform").
- **O mobile** troca `point.image` por `point.image_url` no marcador e no detalhe ([[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta|dia 4]]). Os arquivos de `uploads/` são servidos pelo `express.static` do [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta|dia 2]].

### Dropzone no React

- **`react-dropzone`,** "bem famoso". Diego parte do exemplo básico da documentação e cria o componente `components/Dropzone/index.tsx` com `useDropzone({ onDrop, accept: 'image/*' })` e `<input {...getInputProps()} accept="image/*" />`. O `accept` no `input` acinzenta os arquivos que não são imagem no seletor; o da biblioteca barra quem burla isso pelo inspetor.
- **Preview:** `URL.createObjectURL(file)` vai para `selectedFileUrl`. Com URL, aparece `<img src={selectedFileUrl} alt="Point thumbnail" />`; sem, a mensagem "Imagem do estabelecimento" com `FiUpload`. O CSS veio pronto ([[wiki/entities/feather-icons]]).
- **[[wiki/concepts/levantamento-de-estado]]:**
  - O `CreatePoint` guarda `const [selectedFile, setSelectedFile] = useState<File>()` e passa `<Dropzone onFileUploaded={setSelectedFile} />`.
  - No filho, `interface Props { onFileUploaded: (file: File) => void }`, com `void` "porque ele não tem retorno".
  - "A gente pode passar funções pra componentes filhos [...] para conseguir fazer uma comunicação entre componentes em níveis diferentes." Ver [[wiki/concepts/props-react]].
- **`useCallback`** com `[onFileUploaded]` nas dependências. Explicação de Diego: sem ele, "essa função é recriada na memória do zero", o que "para casos mais complexos" gera "perda de performance". Ver [[wiki/concepts/useCallback]] e as tensões.

### FormData no envio do formulário

- **`const data = new FormData()`** com `data.append('name', name)` e os demais campos. Latitude e longitude vão com `String(...)`, os itens com `items.join(',')`, e o arquivo só se existir: `if (selectedFile) data.append('image', selectedFile)`. "Como a gente não criou validação aqui, o TypeScript reclama."
- **Atalhos do VS Code** para montar os `append`: Ctrl+D (próxima ocorrência), *Add Cursors to Line Ends* (Shift+Alt+I) e Shift+Ctrl+→ para selecionar até o fim da palavra. "A gente aprendeu umas 46 hotkeys." Ver [[wiki/entities/vs-code]].
- **Conferência:** na aba Network, o POST leva todos os campos e a imagem "que é um binário". O `GET /points/9` devolve o `image_url`.

### Validação com celebrate e Joi

- **Front-end:** Yup, "validação baseada em esquema". **Back-end:** celebrate, que "integra muito bem com Express" e usa o [[wiki/entities/joi]] "por baixo dos panos"; o celebrate "não se preocupa com as regras de validação".
- **Na rota,** entre `upload.single('image')` e o controller:
  - `celebrate({ body: Joi.object().keys({ name: Joi.string().required(), email: Joi.string().required().email(), whatsapp: Joi.number().required(), latitude, longitude, city, uf: Joi.string().required().max(2), items: Joi.string().required() }) }, { abortEarly: false })`.
  - Também dá para validar `query`, `params`, headers e cookies.
- **WhatsApp:** "eu não vou fazer uma validação de tamanho [...] porque [...] cada país tem a sua formatação". A transcrição oscila entre string e número ("Por que string aqui? Porque... Não sei. Botar número"). O `items` com regex fica como desafio.
- **A imagem fica fora do Joi:** "eu validaria a imagem utilizando aquele file filter" do Multer.
- **Tipos:** `@types/hapi__joi -D`. O nome de pacote com escopo `@hapi/joi` vira `hapi__joi` no DefinitelyTyped ("eu não posso ter dois arrobas"). Ver [[wiki/concepts/arquivo-de-declaracao-de-tipos]].
- **`app.use(errors())` antes do `listen`:** sem `name`, a resposta é "Status code 400, message: Name is required", com o segmento (`body`) e a chave. Com `abortEarly: false`, vêm todos os erros de uma vez. Dá para personalizar mensagens e fazer i18n. Ver [[wiki/concepts/http-status-code]].

### Projeto no GitHub

- **Repositório** `nlw-01`, "Projeto construído durante o Next Level Week 01", privado só até a aula sair: "eu gosto de deixar todos os projetos públicos". Ver [[wiki/entities/github]].
- **Autenticação:** com *two-factor authentication* é preciso SSH, senão "você consegue fazer o envio via HTTPS". Ver as tensões.
- **Um repositório para três projetos:** o CRA e o Expo criam `.git` próprios em `web/` e `mobile/`. Saem com `rm -rf .git` (Mac/Linux) ou mostrando pastas ocultas no Windows.
- **[[wiki/concepts/gitignore]] no server:**
  - `node_modules` ("não é legal a gente subir essa pasta").
  - `uploads/*` com `!uploads/.gitkeep`, para manter a pasta vazia.
  - `*.sqlite`, para "que a pessoa crie o banco do zero".
- **Envio:** `git init`, `git add .`, `git commit -m "app"`, `git remote add origin` e `git push origin master`. O ideal seria "um git commit para cada projeto, para cada feature". "O Git [...] chega a ser mais importante ou tão importante quanto a linguagem de programação." Ver [[wiki/concepts/git]].
- **README com imagens do Figma e tecnologias,** que "chama a atenção de quem tá olhando teu GitHub". Ver [[wiki/concepts/portfolio-backend-junior]] e [[wiki/concepts/curriculo-vs-portfolio]].

### Deploy

- **Mobile:** a hospedagem "são as próprias lojas". Google Play custaria "30 dólares, alguma coisa assim", uma vez; Apple, "99 dólares por ano" para pessoa física.
- **Back-end:**
  - **[[wiki/entities/heroku]]** para teste. O plano gratuito "desliga sozinho se ninguém estiver utilizando", então não serve para produção. Pago, "a partir de 7 dólares", com infraestrutura gerenciada.
  - **DigitalOcean** acima disso: preço "previsível", "o servidor fica rodando para sempre". A Rocketseat a usa para serviços com poucos usuários.
  - **Escala:** AWS, Google Cloud e Azure, com "uma pessoa na sua equipe especializada [...] SRE". Ver [[wiki/entities/aws]].
- **Front-end:**
  - **[[wiki/entities/netlify]]**, "como se fosse um Heroku, porém para front-end": aponta o repositório, e ele builda e publica. Plano gratuito com "até 100GB".
  - **[[wiki/entities/vercel]]** ("a antiga ZEIT"), parecido. Netlify "um pouquinho mais fácil".
  - **Ao crescer,** Amazon S3 ou Google Cloud Storage, porque "o projeto React é só arquivo estático". Ver [[wiki/concepts/amazon-s3]] e [[wiki/concepts/object-storage]].
- **Fechamento da trilha:** "nossa quinta e última aula focada em código".

## Tensões e precisões

- **Os uploads somem no deploy recomendado.** O Multer grava em disco local, e o Heroku, citado como primeira opção, tem sistema de arquivos efêmero: tudo que não veio no deploy se apaga a cada reinício ou deploy `[external]` (https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem). O mesmo vale para o `database.sqlite`. Upload em produção vai para object storage, como o S3 que a própria aula cita só para o front-end, de preferência com URL assinada para o cliente enviar direto `[skill: lang-dynamic]`. Ver [[wiki/concepts/sistema-de-arquivos-efemero]], [[wiki/concepts/object-storage]] e [[wiki/concepts/media-upload-pattern]].
- **Sem `fileFilter` nem `limits`, o upload aceita qualquer coisa.**
  - Um `.html` ou `.svg` com script, servido pelo `express.static` no mesmo domínio da API, vira **XSS armazenado** para quem abrir o `image_url`.
  - Arquivos gigantes enchem o disco.
  - O `mimetype` vem do cliente e é falsificável. O certo é checar os bytes iniciais (*magic bytes*, como a biblioteca `file-type` faz), definir `limits.fileSize` e servir uploads com `Content-Disposition` ou de outro domínio.
  - Ver [[wiki/concepts/xss]] e [[wiki/concepts/upload-arbitrario-rce]].
- **O nome do arquivo usa o `originalname`.** O Multer já tira os diretórios do nome por padrão (`preservePath: false`), o que barra o `../` `[external]` (https://github.com/expressjs/multer#multeropts). Ainda assim, espaços, acentos e caracteres de URL quebram o `image_url`. A skill recomenda sanitizar ou gerar o nome só com o hash e uma extensão derivada do tipo validado `[skill: lang-dynamic]`. Para a unicidade, `crypto.randomUUID()` é a opção nativa e direta.
- **O arquivo chega ao disco antes da validação.** A ordem `upload.single` → `celebrate` → controller grava a imagem e só depois recusa o body. Cada POST inválido (ou que falhe na transação) deixa um órfão em `uploads/`. É preciso apagar no erro ou validar antes de persistir.
- **`request.file` pode não existir.** O front só anexa a imagem `if (selectedFile)`, e o Joi não valida arquivo. Sem imagem, `request.file.filename` lança `TypeError` e a resposta é 500, não 400.
- **Regras do Joi frouxas:** `uf: Joi.string().max(2)` aceita "S" ou "sc". O certo é `.length(2).uppercase()` ou uma lista das 27 UFs. Ver [[wiki/concepts/validacao-de-entrada]].
- **Pacotes de validação:** `@hapi/joi` voltou a ser `joi`, que traz os próprios tipos, então o `@types/hapi__joi` ficou obsoleto `[external]` (https://github.com/hapijs/joi). `[skill: lang-dynamic]` Hoje Zod ou Valibot permitem um único schema no front e no back (Standard Schema), em vez de Yup aqui e Joi ali. Ver [[wiki/entities/joi]].
- **O `.gitignore` apaga os ícones dos itens.** Os SVGs do seed foram postos em `uploads/` no dia 2. Com `uploads/*` ignorado, quem clona o repositório fica sem as imagens dos itens. Assets do projeto e arquivos de usuário devem morar em pastas separadas (`assets/` versionado, `uploads/` ignorado). Ver [[wiki/concepts/gitignore]].
- **Git e GitHub mudaram.**
  - O GitHub passou a criar repositórios com o branch padrão `main` em outubro de 2020 `[external]` (https://github.blog/changelog/2020-10-01-the-default-branch-for-newly-created-repositories-is-now-main/).
  - Desde agosto de 2021, operações Git por HTTPS não aceitam senha, com ou sem 2FA: é token (PAT) ou SSH `[external]` (https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/).
  - O "com 2FA usa SSH, senão HTTPS" já não descreve o cenário.
- **O mapa de deploy envelheceu.**
  - O Heroku acabou com o plano gratuito em novembro de 2022 `[external]` (https://blog.heroku.com/next-chapter); hoje há os planos Eco e Basic.
  - A taxa do Google Play é de US$ 25, única, não 30 `[external]` (https://support.google.com/googleplay/android-developer/answer/6112435); a Apple continua US$ 99/ano.
  - Os "100 GB" do Netlify eram de banda mensal, não de "bundles", e o plano gratuito mudou de modelo depois `[external, não verificado]`.
  - Ver [[wiki/concepts/deploy-strategies]].
- **`useCallback` não é sobre "recriar função na memória".** Criar uma função a cada render é barato. O `useCallback` preserva a *identidade* da função entre renders, o que importa quando ela vai para um filho com `memo` ou para dependências de efeitos. Ver [[wiki/concepts/useCallback]].
- **`URL.createObjectURL` sem `revokeObjectURL`.** Cada troca de imagem deixa a URL anterior viva até a página fechar `[external]` (https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL_static).
- **O IP mudou no meio da semana** (de .13 para .12), e foi preciso editar o código. É o problema da URL fixa, já apontado nos dias 2 e 4. Ver [[wiki/concepts/variaveis-de-ambiente]].
- **"Um repositório para tudo" é uma escolha.** Monorepo com `server/`, `web/` e `mobile/` funciona para portfólio. O commit único "app" no fim da semana é o que a própria aula desaconselha ("era bom [...] ter dado um git commit para cada [...] feature").

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/multer]]: upload multipart no Express
- [[wiki/entities/joi]]: validação de schema, via celebrate
- [[wiki/entities/express]], [[wiki/entities/nodejs]], [[wiki/entities/typescript]]
- [[wiki/entities/react]]: Dropzone, FormData, callback como prop
- [[wiki/entities/insomnia]]: body multipart
- [[wiki/entities/github]]: repositório e portfólio
- [[wiki/entities/heroku]], [[wiki/entities/netlify]], [[wiki/entities/vercel]], [[wiki/entities/aws]]: hospedagem
- [[wiki/entities/unsplash]], [[wiki/entities/feather-icons]], [[wiki/entities/vs-code]]
- [[wiki/entities/next-level-week]], [[wiki/entities/rocketseat]]

Citados sem página: react-dropzone, celebrate, Yup, DigitalOcean, Google Cloud, Microsoft Azure, Google Cloud Storage, Google Play, App Store, Discord.

## Conceitos

[[wiki/concepts/multipart-form-data]] · [[wiki/concepts/levantamento-de-estado]] · [[wiki/concepts/gitignore]] · [[wiki/concepts/sistema-de-arquivos-efemero]] · [[wiki/concepts/validacao-de-entrada]] · [[wiki/concepts/http-status-code]] · [[wiki/concepts/middleware]] · [[wiki/concepts/callback-javascript]] · [[wiki/concepts/criptografia]] · [[wiki/concepts/props-react]] · [[wiki/concepts/useCallback]] · [[wiki/concepts/arquivo-de-declaracao-de-tipos]] · [[wiki/concepts/xss]] · [[wiki/concepts/upload-arbitrario-rce]] · [[wiki/concepts/object-storage]] · [[wiki/concepts/amazon-s3]] · [[wiki/concepts/media-upload-pattern]] · [[wiki/concepts/git]] · [[wiki/concepts/deploy-strategies]] · [[wiki/concepts/portfolio-backend-junior]] · [[wiki/concepts/curriculo-vs-portfolio]] · [[wiki/concepts/endereco-ip]] · [[wiki/concepts/variaveis-de-ambiente]]

## Open Questions

- Com este dia, a trilha de Diego fica completa na wiki (dias 1–5). A comparação das duas trilhas está em [[wiki/questions/nlw-1-duas-trilhas-ecoleta-comparacao]].
- Seguem sem resposta na aula: o filtro de itens (dia 4), o select com o IBGE no mobile (desafio), a tela de sucesso na web (desafio) e o `items` com regex (desafio).
- Data provável: 5 de junho de 2020 `[external, não verificado]`.
