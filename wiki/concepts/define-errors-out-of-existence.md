---
type: concept
title: "Define Errors Out of Existence"
aliases: ["definir erros para fora da existência", "eliminar erros por design", "redesenhar semântica para evitar exceção"]
date_created: 2026-09-08
date_updated: 2026-09-08
source_count: 2
tags: [error-handling, api-design, design, ousterhout, usabilidade]
skill: tech-mentor-backend
status: draft
---

# Define Errors Out of Existence

## TL;DR

Técnica de [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, Cap. 10): a forma mais eficaz de reduzir a complexidade desproporcional causada por exceções não é tratá-las melhor — é **redesenhar a semântica da operação para que a condição de erro deixe de existir**. Uma API também é uma interface de usuário (o dev que a chama é o usuário); em vez de lançar exceção sempre que a entrada não bate exatamente com o esperado, o design deveria tentar entregar o resultado mais próximo do que o usuário provavelmente queria.

## O argumento central

Exceções custam caro em complexidade desproporcional ao benefício: cada `throw` obriga todo chamador a decidir como reagir (capturar, propagar, ignorar), multiplicando os caminhos possíveis pelo código. Um estudo citado no livro (Yuan et al., USENIX OSDI 2014) encontrou que mais de 90% das falhas catastróficas em sistemas distribuídos vieram de tratamento de erro incorreto — não do erro em si. A resposta de Ousterhout não é "trate erros melhor": é eliminar a necessidade de tratá-los, mudando o design da operação.

## Exemplo canônico: substring além do limite

Pedir um substring de uma string de 10 caracteres do índice 5 ao 11 (fora do intervalo). Java lança `IndexOutOfBoundsException`. Python, em list slices, simplesmente trunca e retorna o que existe (índices 5 a 10). A segunda abordagem elimina a condição de erro: não existe uma forma sensata de o usuário "quebrar" a chamada, porque o comportamento para entradas fora do range já está definido de forma útil.

[[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] usa exatamente esse exemplo (Java vs. Python) para escolher este capítulo como o trecho mais importante do livro, na visão de [[wiki/entities/otavio-santana]] — reforçando que uma API é, do ponto de vista de usabilidade, uma interface de usuário como qualquer outra, e merece o mesmo cuidado que se dá a UI.

## Outros exemplos do livro

- `unset` do Tcl (o próprio Ousterhout admite ter sido um erro de design): lançava erro para variável inexistente, em vez de simplesmente garantir que a variável não existe mais no final.
- Deleção de arquivo aberto: Unix adia a deleção até o último handle fechar (sem erro); Windows recusa a deleção, obrigando o usuário a caçar e matar o processo que segura o handle.

## Duas estratégias, segundo a fonte do podcast

1. **Projetar para que o erro seja impossível de acontecer** — redesenhar a operação (como nos exemplos acima).
2. **Inferir a intenção do usuário e entregar o resultado mais próximo do esperado** — em vez de rejeitar a chamada. Maurício Linhares cita a experiência com Ruby como exemplo de API que raramente lança erro sem antes tentar entender o que o chamador está tentando fazer.

## Relação com outros conceitos

- [[wiki/concepts/red-flags-de-design]] — esta técnica é a resposta prática recomendada quando exceções aparecem espalhadas pela API sem necessidade real.
- [[wiki/concepts/error-handling-estruturado]] — conceito complementar, não concorrente: trata de como estruturar erros que *precisam* existir (classes de erro + HTTP codes); "define errors out of existence" trata de eliminar a necessidade da exceção antes de chegar nesse ponto.
- [[wiki/concepts/modulo-profundo]] — uma interface que lança exceções desnecessárias é, por definição, mais rasa: expõe mais casos que quem consome precisa conhecer e tratar.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — Cap. 10, exemplos completos de `unset` do Tcl, deleção de arquivo Unix vs. Windows, substring do Java, e o estudo Yuan et al. (USENIX OSDI 2014)
- [[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] — escolhido por Otávio Santana como o trecho mais importante do livro; reforça o enquadramento de API como interface de usuário
