---
type: source
title: "Test Discovery (xUnitPatterns.com — Gerard Meszaros)"
aliases: ["test discovery", "testcase class discovery", "test method discovery"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/test-discovery-xunitpatterns.md
source_url: "http://xunitpatterns.com/Test%20Discovery.html"
author: "Gerard Meszaros"
date_published: 2003-01-01
date_ingested: 2026-09-21
source_count: 0
tags: [testes, testcase-class, test-runner, xunit, fonte-primaria, terminologia]
skill: tech-mentor-testing
status: stable
---

# Test Discovery (xUnitPatterns.com — Gerard Meszaros)

## TL;DR

Verbete da categoria **XUnit Basics** do xUnitPatterns.com dedicado ao próprio termo **Test Discovery** — fecha, com fonte primária dedicada, a lacuna citada de passagem em três páginas já ingeridas ([[wiki/concepts/test-suite-object]], [[wiki/concepts/testcase-object]], [[wiki/sources/testcase-class-xunitpatterns]]) sobre como o [[wiki/concepts/test-runner|Test Runner]] efetivamente encontra os testes a executar. Resolve o problema "como o Test Runner sabe quais testes rodar?" respondendo: o **Test Automation Framework** usa **[[wiki/concepts/reflection|reflection]]** em tempo de execução (ou conhecimento em tempo de compilação) para descobrir automaticamente os **Test Methods** e/ou **Test Suite Objects** que compõem a suíte, eliminando o trabalho manual da alternativa — **Test Enumeration** — que esta fonte nomeia extensivamente por contraste, mas não define. Desdobra o mecanismo em duas variações complementares — **Testcase Class Discovery** (achar as classes) e **Test Method Discovery** (achar os métodos dentro delas) — cada uma com quatro a cinco exemplos de código concretos em C++/CppUnit, Java/JUnit e C#/NUnit, mais um exemplo em Ruby de Testcase Class Discovery via convenção de localização de arquivo.

---

## Afirmações Centrais

| Afirmação | Evidência | Fonte | Confiança |
|---|---|---|---|
| Test Discovery é o mecanismo pelo qual o Test Automation Framework descobre automaticamente todos os testes da suíte | "The Test Automation Framework discovers all the tests that belong to the test suite automatically" | fonte primária (Meszaros) | alta |
| O mecanismo usa reflection em tempo de execução, ou conhecimento em tempo de compilação | "uses runtime reflection (or compile time knowledge) to discover all the Test Methods [...] and/or all the Test Suite Objects" | fonte primária | alta |
| Test Discovery deve ser usado sempre que o framework der suporte a ele; Test Enumeration só quando o framework não suporta Discovery, ou para montar uma Named Test Suite com subconjunto de testes de várias suítes | "We should use Test Discovery whenever our Test Automation Framework supports it. [...] The only time to consider using Test Enumeration is when our framework does not support Test Discovery or when we wish to define a Named Test Suite" | fonte primária | alta |
| Existem duas variações: Testcase Class Discovery (achar as classes) e Test Method Discovery (achar os métodos) | "Building the Suite of Suites [...] involves two things. First, we must find all the Test Methods [...] and second, we must find all the Test Suite Objects" | fonte primária | alta |
| Test Method Discovery tem duas formas básicas: convenção de nomenclatura (prefixo "test") ou method attribute/annotation | "The more traditional way is the use of a Test Method naming convention such as 'starts with test'. [...] The other alternative [...] is to use a method attribute [...] or annotation" | fonte primária | alta |
| Testcase Class Discovery tem quatro soluções: subclassificar uma Testcase Superclass, Marker Interface, class attribute/annotation, diretório comum, ou convenção de nomenclatura de arquivo | "One solution involves tagging each Testcase Class by subclassing [...] or implementing a Marker Interface [...] Another alternative [...] is to use a class attribute [...] or annotation [...] Another solution is to put all the test case classes into a common directory [...] A fourth solution is to use a Testcase Class naming convention" | fonte primária | alta |
| Não usar Test Discovery força o desenvolvedor a escrever manualmente a Test Method Enumeration (registro explícito de cada teste) | Exemplo de código `CppUnit::Test *suite()` que adiciona cada `TestCaller` manualmente | fonte primária | alta |

---

## Key Claims

### 1. Test Discovery é o padrão default; Test Enumeration é o fallback com dois gatilhos específicos
A fonte não trata as duas técnicas como equivalentes intercambiáveis — estabelece uma hierarquia de preferência explícita: use Test Discovery sempre que o framework suportar. Os únicos dois motivos legítimos para recorrer à **Test Enumeration** (ainda sem fonte primária dedicada na wiki, apenas nomeada de passagem em [[wiki/concepts/test-suite-object]] e [[wiki/concepts/testcase-object]]) são (a) o framework simplesmente não suporta Discovery, ou (b) o time quer montar uma **Named Test Suite** — um subconjunto de testes escolhidos a dedo de outras suítes, como uma suíte de **Smoke Test** [SCM] — quando o framework também não suporta **Test Selection**. A fonte nota ainda que é comum combinar Test Suite Enumeration (manual) com Test Method Discovery (automático); o inverso — Test Method Enumeration manual dentro de uma suíte descoberta automaticamente — é raro.

### 2. Duas descobertas distintas e sequenciais: classe primeiro, método depois
Construir a **Suite of Suites** que o Test Runner executa exige resolver dois problemas em cascata (não necessariamente nessa ordem): primeiro achar todas as **Testcase Classes** relevantes (**Testcase Class Discovery**), depois achar todos os **Test Methods** dentro de cada uma (**Test Method Discovery**). Esta fonte é a primeira, na wiki, a nomear e detalhar essas duas sub-etapas separadamente — antes, [[wiki/sources/testcase-class-xunitpatterns]] e [[wiki/sources/testcase-object-xunitpatterns]] apenas citavam "Test Discovery" e "Test Enumeration" en passant, sem diferenciar descoberta de classe vs. descoberta de método.

### 3. Quatro mecanismos concretos de Testcase Class Discovery, com trade-off de acoplamento
A fonte lista quatro soluções concretas, cada uma com um trade-off implícito de acoplamento entre o código de teste e o framework: (a) subclassificar uma **Testcase Superclass** (ainda sem página própria na wiki) ou implementar uma **Marker Interface** [PJV1] — acopla via herança/tipo; (b) **class attribute**/**annotation** — acopla via metadado declarativo, sem herança forçada (mecanismo já detalhado com fonte primária em [[wiki/sources/annotation-xunitpatterns]] e [[wiki/sources/attribute-xunitpatterns]]); (c) diretório comum apontado ao Test Runner — acoplamento zero ao código, acoplamento total à convenção de organização de arquivos; (d) convenção de nomenclatura de arquivo, resolvida por um programa externo — o exemplo Ruby (`Dir['tests/*.rb'].each { |f| require f }`) implementa exatamente essa quarta variante, delegando a Test Method Discovery em si ao interpretador Ruby e ao Test::Unit depois do `require`.

### 4. Test Method Discovery: mesma dualidade nomenclatura vs. metadado já vista em Testcase Class Discovery
A simetria é direta: assim como a Testcase Class pode ser marcada por convenção de nome ou por metadado, o Test Method também — prefixo `"test"` (convenção clássica de JUnit 3/xUnit legado) vs. **method attribute** (`[Test]`, NUnit/.NET) ou **annotation** (`@Test`, JUnit 4+). O exemplo de C# desta fonte (`[Test]` + `[ExpectedException(...)]`) é o primeiro exemplo de código concreto na wiki mostrando dois **method attributes** do NUnit compostos no mesmo Test Method — até agora [[wiki/sources/attribute-xunitpatterns]] e [[wiki/sources/annotation-xunitpatterns]] discutiam o mecanismo em abstrato, sem exemplo multi-atributo.

### 5. Refatoração de migração: Rename Method quando o framework usa convenção de nomenclatura
Ao adotar um framework xUnit existente, a fonte recomenda literalmente seguir a convenção de descoberta que ele já implementa — se for por nome, pode ser necessário um **[[wiki/sources/rename-method-xunitpatterns|Rename Method]]** [Fowler] para que os Test Methods existentes passem a ser descobertos; se for por atributo, basta adicionar o atributo. É a primeira vez que a wiki registra essa refatoração especificamente ligada ao contexto de descoberta de testes, e não a refatoração genérica de nomes. [[wiki/sources/rename-method-xunitpatterns]], ingerida em 2026-09-21, dá fonte primária isolada ao termo genérico.

### 6. CppUnit como exemplo do estado "pré-Discovery" e "Discovery via macro de compilação"
A fonte usa o mesmo framework (CppUnit) em dois momentos opostos: primeiro, um exemplo de código legado mostrando o trabalho manual que Test Discovery elimina (função `suite()` construindo a Suite explicitamente, um `addTest`/`TestCaller` por Test Method); depois, uma versão mais recente do mesmo framework usando a macro `CPPUNIT_TEST_SUITE_REGISTRATION`, que gera esse mesmo código em tempo de compilação a partir de convenção de nomenclatura de método — uma forma de Test Method Discovery resolvida estaticamente, sem reflection em tempo de execução, contrariando a formulação inicial do "How It Works" que cita apenas reflection como mecanismo. É a primeira menção de **CppUnit** na wiki com detalhe técnico próprio — até agora só era citado de passagem em [[wiki/entities/junit]] como o provável primeiro port de JUnit, criado por Michael Feathers.

---

## Entidades Mencionadas

- [[wiki/entities/gerard-meszaros]] — autor do verbete; mesma fonte primária do catálogo já usada para [[wiki/sources/testcase-object-xunitpatterns]], [[wiki/sources/testcase-class-xunitpatterns]] e demais entradas do cluster XUnit Basics
- [[wiki/entities/junit]] — exemplo de Test Method Discovery via convenção de nomenclatura (prefixo "test", estilo JUnit 3) e via annotation (JUnit 4+, mecanismo já detalhado em [[wiki/sources/annotation-xunitpatterns]])
- [[wiki/entities/nunit]] — exemplo de Test Method Discovery e Testcase Class Discovery via method/class attribute (`[Test]`, `[TestFixture]`)
- [[wiki/entities/martin-fowler]] — citado como autor da refatoração **Rename Method**, recomendada ao migrar Test Methods para um framework que descobre por convenção de nomenclatura
- [[wiki/entities/cppunit]] *(novo stub criado nesta ingestão)* — framework C++ da família xUnit; exemplo central tanto do estado "pré-Discovery" (função `suite()` manual) quanto de Test Method Discovery via macro de compilação (`CPPUNIT_TEST_SUITE_REGISTRATION`)

## Conceitos Tocados

- [[wiki/concepts/test-discovery]] *(novo, criado nesta ingestão)* — página central do próprio termo, fecha a lacuna já sinalizada em três fontes anteriores
- [[wiki/concepts/test-enumeration]] *(novo stub criado nesta ingestão)* — a alternativa manual, nomeada extensivamente por contraste nesta fonte mas ainda sem verbete de glossário próprio ingerido
- [[wiki/concepts/marker-interface]] *(novo stub criado nesta ingestão)* — uma das quatro soluções de Testcase Class Discovery, citada com a sigla externa [PJV1]
- [[wiki/concepts/rename-method]] *(novo stub criado nesta ingestão)* — refatoração de Fowler recomendada na migração para descoberta por convenção de nomenclatura
- [[wiki/concepts/test-runner]] — o consumidor final da Suite of Suites montada via Test Discovery; página atualizada com o mecanismo completo de como ele "sabe" quais testes rodar
- [[wiki/concepts/testcase-object]] — Test Discovery/Test Method Discovery é finalmente detalhado como um dos dois mecanismos de criação, gap já sinalizado nesta página
- [[wiki/concepts/test-suite-object]] — mesma lacuna fechada do lado da montagem da Suite of Suites
- [[wiki/concepts/test-method]] — Test Method Discovery detalhado como o mecanismo pelo qual um Test Method é reconhecido pelo framework
- [[wiki/concepts/reflection]] — mecanismo citado como base de Test Discovery em runtime, com a ressalva (não formalizada pela própria fonte) de que a variação via macro de compilação do CppUnit não usa reflection, e sim geração de código em compile time

## Questões Abertas

- **Test Enumeration segue sem fonte primária isolada** — nomeada extensivamente nesta fonte por contraste (inclusive com sub-variações "Test Method Enumeration" e "Test Suite Enumeration"), mas o verbete dedicado (`Test Enumeration.html`) ainda não foi ingerido. Candidato natural para a próxima ingestão do mesmo cluster — resolveria também a definição de **Test Suite Factory**, cujo link no site aponta justamente para `Test Enumeration.html#Test Suite Factory` (lacuna já registrada em [[wiki/sources/test-case-xunitpatterns]]).
- ~~**Testcase Superclass, Marker Interface e Rename Method** são citados nesta fonte sem página/fonte primária dedicada própria~~ — Marker Interface e Rename Method resolvidos: [[wiki/sources/marker-interface-xunitpatterns]] e [[wiki/sources/rename-method-xunitpatterns]] (esta última ingerida em 2026-09-21) já têm fonte primária dedicada. Testcase Superclass já era uma lacuna aberta desde [[wiki/sources/testcase-class-xunitpatterns]] e segue sem página.
- **Named Test Suite, Test Selection e Production Bugs/Lost Test** são citados de passagem (contexto de "quando NÃO usar Test Discovery") sem elaboração — nenhuma página própria criada para eles nesta ingestão; ficam como candidatos de baixa prioridade, já que a fonte não os desenvolve além de nomeá-los.
- **Contradição aparente não resolvida pela própria fonte**: a seção "How It Works" define Test Discovery como baseado em "runtime reflection (or compile time knowledge)", mas só detalha reflection nos exemplos de Test Method Discovery via nomenclatura; o exemplo da macro `CPPUNIT_TEST_SUITE_REGISTRATION` é claramente "compile time knowledge" (geração de código estático), não reflection — a fonte não nomeia essa segunda categoria com o mesmo detalhe, tratando-a como nota lateral ("this macro finds all the Test Methods at compile time"). Registrado aqui como observação da wiki, não como fato citado explicitamente pela fonte.
- Sem contradição com o resto da wiki além do ponto acima — a fonte fecha, de forma consistente, lacunas já sinalizadas em [[wiki/concepts/test-suite-object]], [[wiki/concepts/testcase-object]] e [[wiki/sources/testcase-class-xunitpatterns]].

---

## Citações Relevantes

> "How does the Test Runner know what tests to run? The Test Automation Framework discovers all the tests that belong to the test suite automatically."

> "The Test Automation Framework uses runtime reflection (or compile time knowledge) to discover all the Test Methods that belong to the test suite and/or all the Test Suite Objects that belong to a Suite of Suites."

> "We should use Test Discovery whenever our Test Automation Framework supports it. [...] The only time to consider using Test Enumeration is when our framework does not support Test Discovery or when we wish to define a Named Test Suite that consists of a subset of tests [...] chosen from other test suites and the Test Automation Framework does not support Test Selection."

> "One solution involves tagging each Testcase Class by subclassing an Testcase Superclass or implementing a Marker Interface[PJV1]. [...] A fourth solution is to use a Testcase Class naming convention and use an external program to find all the files matching the naming pattern."

> "The more traditional way is the use of a Test Method naming convention such as 'starts with test'. [...] The other alternative [...] is to use a method attribute [...] or annotation [...] to identify each Test Method."

*(Tradução completa em `raw/test-discovery-xunitpatterns.md`.)*
