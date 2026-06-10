# agents.md e CLAUDE.md Ainda Valem a Pena? O que o Paper de Zurique Realmente Diz

**Fonte:** Transcrição de vídeo (YouTube)  
**Autor:** Valdemar Neto (cofundador da Tech Leads Club)  
**Data de publicação:** desconhecida  
**Idioma original:** Português (Brasil)

---

## Introdução

Muita gente viu o paper circulando e concluiu: "agents.md e CLAUDE.md não servem para nada, custam mais e são ineficientes — vou deletar do repositório."

Não delete antes de assistir. O paper avalia **performance**, e é exatamente aí que está o aprendizado que todo mundo está deixando passar.

---

## O Paper

**Instituição:** Universidade de Zurique  
**Objeto:** Avaliação comparativa de repositórios com e sem arquivos de contexto para agentes de IA

### Metodologia

1. Selecionaram vários repositórios Python do GitHub (ex.: Ansible)
2. Pegaram pull requests existentes, converteram em issues
3. Geraram três ou quatro soluções para cada issue:
   - **Sem arquivo de contexto** (sem `agents.md`, sem `CLAUDE.md`)
   - **Com arquivo gerado por LLM**
   - **Com arquivo gerado por humano** *(assumiram que arquivos já presentes no repositório foram escritos por humanos — mas o paper reconhece que podem ter sido gerados por IA)*
4. Avaliaram:
   - Taxa de sucesso (testes passando)
   - Custo
   - Número de iterações até chegar na solução

---

## Resultados

| Condição | Taxa de sucesso (vs. sem arquivo) | Custo adicional |
|---|---|---|
| **Sem arquivo de contexto** | baseline | baseline |
| **Arquivo gerado por LLM** | **-3%** | **+20%** |
| **Arquivo gerado por humano** | **+4%** | **+19%** |

### Por que o custo aumenta com arquivo de contexto?

Porque ao fornecer um arquivo de contexto, o agente precisa:

- Seguir mais regras
- Interpretar o contexto
- Buscar mais arquivos
- Processar mais tokens

Isso é esperado — mais contexto implica mais processamento. **Não é um bug, é uma consequência direta de dar mais informação ao agente.**

---

## O que o Paper NÃO avaliou

Este é o ponto central que o autor destaca. A métrica do paper era **"os testes passaram?"** — não mais do que isso.

O paper **não avaliou:**

- ❌ Qualidade da implementação
- ❌ Segurança do código gerado
- ❌ Uso de design patterns adequados
- ❌ Se as instruções do arquivo de contexto foram bem seguidas
- ❌ Se o agente tomou decisões arquiteturais corretas

### O que o paper observou sobre adesão às instruções

> *"Quando tem um arquivo de contexto, tipicamente os agentes seguem as regras e guidelines que estão lá."*

Ou seja: **sem um arquivo de contexto, a chance de alucinação é muito maior.** O agente pode deletar testes para "fazer o código passar", implementar coisas completamente fora do padrão do projeto, ou ignorar convenções estabelecidas — e o paper não capturaria isso como falha, porque o único critério era: testes passaram?

---

## Aprendizados Práticos

### 1. agents.md / CLAUDE.md ainda são necessários

Eles fornecem contexto que o agente não tem por padrão e fazem ele seguir as regras do projeto. Removê-los vai resultar em decisões erradas que você vai corrigir em prompts subsequentes — o que custa mais tempo e dinheiro do que o custo do arquivo.

### 2. Mas o arquivo deve ser enxuto

Colocar coisas desnecessárias aumenta custo e latência sem agregar valor. A estratégia recomendada:

**No arquivo principal (`agents.md` / `CLAUDE.md`):**
- Apenas o contexto absolutamente necessário (base mínima)
- Links para outros arquivos específicos

**Em arquivos separados (carregados sob demanda):**
- `api-standards.md`
- `testing-conventions.md`
- `security-guidelines.md`
- Etc.

Dessa forma, o agente carrega apenas o que é relevante para o contexto atual — reduz custo sem perder as garantias de qualidade.

### 3. Adicionar tooling progressivamente

Se o agente alucinou e usou uma ferramenta errada ou um comando incorreto, adicione isso ao arquivo:

```
Use `pytest` para rodar testes (não `unittest` diretamente)
Use `ruff` para linting (não `flake8`)
```

Só adicione quando houver alucinação observada. Mantenha o arquivo no mínimo necessário e vá crescendo conforme os problemas aparecem.

---

## Resumo da Estratégia

```
agents.md / CLAUDE.md
        │
        ├── Base mínima (o absolutamente necessário)
        │
        ├── Links para arquivos específicos (sob demanda)
        │       ├── api-standards.md
        │       ├── testing-conventions.md
        │       └── ...
        │
        └── Correções de tooling (adicionadas quando o agente alucina)
```

**Não remover o arquivo** → agente alucina, custo real sobe em prompts corretivos  
**Arquivo inchado** → custo por token sobe sem necessidade  
**Arquivo mínimo com links** → equilíbrio entre controle e custo

---

## Furo Metodológico do Paper

O paper assume que arquivos de contexto já presentes nos repositórios foram escritos por humanos. Porém, esses arquivos podem ter sido gerados por LLMs. Isso compromete a distinção entre as categorias "humano" e "LLM" — e é reconhecido pelos próprios autores como uma limitação.
