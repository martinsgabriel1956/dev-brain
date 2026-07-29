---
type: concept
title: "Comentários Como Ferramenta de Design"
aliases: ["write the comments first", "escrever comentários primeiro", "comments as design tool", "interface comment", "implementation comment"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [comentarios, documentacao, design, ousterhout, clean-code, abstracao]
skill: tech-mentor-backend
status: draft
---

# Comentários Como Ferramenta de Design

## TL;DR

Para [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, Caps. 12, 13 e 15), comentários não são um "mal necessário" — são a única forma de capturar a parte **informal** de uma abstração (o que não pode ser expresso em código: unidades, pré-condições, efeitos colaterais, motivo de uma decisão). Escrever o comentário de interface **antes** do corpo do método, não depois, transforma a documentação em ferramenta de design: se o comentário fica longo e precisa descrever implementação para ficar completo, isso expõe cedo que a abstração tem um problema.

## Discordância explícita com Clean Code

Robert Martin, em *Clean Code*: *"comments are, at best, a necessary evil... comments are always failures."* A alternativa proposta por Martin é extrair blocos de código em métodos com nomes longos e descritivos (ex.: `isLeastRelevantMultipleOfNextLargerPrimeFactor`) no lugar de um comentário.

Ousterhout rebate: código não consegue expressar tudo que importa (por que uma decisão foi tomada, que unidade uma variável usa, se um argumento nulo é permitido), então a ausência de comentários não é sinal de bom design — é ausência de informação. Além disso, nomes de método muito longos ainda são "crípticos" e fornecem menos informação que um comentário bem escrito; e cada vez que o método é invocado, o leitor precisa "retipar" mentalmente a documentação, porque ela não existe em lugar nenhum fora do nome.

## Quatro desculpas para não escrever comentários (Cap. 12) — e por que não seguram

1. **"Código bom se autodocumenta"** — falso para a parte informal da interface (nem tudo que importa é dedutível lendo o corpo do método).
2. **"Não tenho tempo"** — comentários raramente passam de ~5% do tempo total de desenvolvimento, mesmo assumindo metade das linhas sendo comentário.
3. **"Comentários ficam desatualizados"** — mitigável com disciplina (ver seção de manutenção abaixo), não motivo para não escrever.
4. **"Todo comentário que já vi é ruim"** — a única desculpa com algum mérito real, segundo o autor; solução é aprender a escrever bem, não desistir.

## Duas categorias que não devem se misturar

- **Comentário de interface** — descreve o que quem usa o módulo/método precisa saber: comportamento, argumentos, retorno, efeitos colaterais, exceções, pré-condições. Não deve conter detalhes de implementação.
- **Comentário de implementação** — descreve como o código funciona por dentro, para quem for mexer ali. Se um comentário de interface precisa descrever implementação para ficar completo, isso é o red flag **Implementation Documentation Contaminates Interface** — sinal de que o módulo é raso (ver [[wiki/concepts/modulo-profundo]]).

Regra de ouro para não repetir o código: depois de escrever um comentário, pergunte "alguém que nunca viu esse código conseguiria escrever esse comentário só olhando para o código ao lado?" Se sim, o comentário não ajuda em nada.

## Escrever os comentários primeiro (Cap. 15)

Processo descrito pelo autor: comentário de interface da classe → assinaturas e comentários dos métodos públicos mais importantes (corpo vazio) → variáveis de instância com comentário → só então os corpos dos métodos, com comentários de implementação conforme necessário. Três benefícios: (1) o contexto de design está fresco na cabeça, produzindo comentários melhores; (2) a escrita do comentário funciona como teste de design — comentário difícil de deixar curto e completo é sinal de abstração ruim (red flag **Hard to Describe**); (3) o processo fica mais agradável, porque achar a descrição mais simples e completa possível é uma fonte de satisfação, não drudge work adiado para o fim do projeto.

## Manutenção — como não deixar comentários ficarem obsoletos

- Manter o comentário perto do código que descreve (não em header file distante).
- Documentar no código, não na mensagem de commit.
- Evitar duplicação — se não há um lugar óbvio para uma decisão que atravessa módulos, usar um arquivo central (`designNotes`) com referências curtas a partir de cada ponto afetado.
- Revisar o diff antes de commitar, checando se a documentação ainda bate com o código.
- Comentários mais abstratos (de nível mais alto que o código) envelhecem melhor, porque só mudanças de comportamento geral os invalidam — não qualquer edição de detalhe.

## Relação com outros conceitos

- [[wiki/concepts/modulo-profundo]] — a qualidade do comentário de interface é o teste prático de quão profundo um módulo realmente é.
- [[wiki/concepts/red-flags-de-design]] — Comment Repeats Code, Implementation Documentation Contaminates Interface e Hard to Describe são os três red flags de comentários catalogados no livro.
- [[wiki/concepts/naming]] — nomes e comentários são as duas ferramentas do livro para reduzir obscuridade; Ousterhout defende as duas contra a posição de Martin de eliminar comentários em favor de nomes de método extremamente longos.
- [[wiki/concepts/refatoracao]] — regras de manutenção de comentários (Cap. 16) aplicadas especificamente ao contexto de modificar código já existente.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — Caps. 12, 13 e 15 (as quatro desculpas, interface vs. implementação, escrever comentários primeiro, discordância com Clean Code)
