---
type: concept
title: "Mapeamento de requisitos de vagas"
aliases: ["mapear requisitos", "gap analysis de currículo", "lacunas do currículo"]
date_created: 2026-11-16
date_updated: 2026-11-25
source_count: 3
tags: [carreira, busca-de-vagas, curriculo, plano-de-estudo]
skill: tech-mentor-leadership
status: draft
---

# Mapeamento de requisitos de vagas

Ler várias vagas do cargo-alvo e anotar o que elas pedem, para ver "o que as vagas estão pedindo que falta pra você": as lacunas do currículo que podem ser estudadas ou melhoradas ([[wiki/sources/introducao-mapeando-vagas]]). O resultado vira plano de estudo e insumo para o currículo.

- O mesmo levantamento serve à [[wiki/concepts/otimizacao-ats-curriculo]] (palavras-chave das vagas).
- `[skill: tech-mentor-leadership]` A skill trata o "gap entre onde estou e onde preciso estar" como primeiro passo para crescer intencionalmente (`references/career-progression.md`); aqui o "onde preciso estar" vem das vagas, não de uma ladder interna.
- Ver também [[wiki/concepts/cacar-a-empresa-nao-a-vaga]] (a lista de empresas-alvo define quais vagas ler) e [[wiki/concepts/acompanhamento-de-candidaturas]].

## Método: contar requisitos numa tabela (Galego)

A aula [[wiki/sources/mapear-requisitos-de-multiplas-vagas-galego]] dá o passo a passo. A pergunta "o que devo aprender?" é "o caminho inverso": comece pelas vagas das empresas-alvo e conte, porque ler 10 vagas de cabeça "é muita informação".

| Coluna | O que vai nela | Exemplo da demo |
|---|---|---|
| Item | tecnologia ou técnica pedida | Java, Clojure, Kafka, AWS, Terraform, teste unitário |
| Categoria | linguagem, cloud/DevOps, banco, ferramenta, técnica, domain knowledge, soft skills | Java → Programming Language; AWS → Cloud/DevOps; Agile → Soft Skills |
| Prioridade | alta, média ou baixa, conforme o papel | Java e Kafka altas; Dynamo Database média; Prometheus baixa |
| Contagem | em quantas vagas apareceu | Java, AWS, Kafka e Dynamo Database: 2 depois de Nubank e Itaú |
| Proficiência | seu nível hoje | expert, aprendendo |
| Notas | evidência ou plano | "fiz projeto pessoal X com Java"; Kubernetes "necessário entender, mas não dominar 100%" |

Regras da aula:

- **Amostra de 10 a 15 vagas** de empresas de tamanho, nível e perfil parecidos (na demo, banco e fintech: [[wiki/entities/nubank]], Brex, [[wiki/entities/itau]]).
- **Prioridade pelo papel**, não pela vaga: numa vaga de dev, Kubernetes é "legal saber"; Java é "com certeza absoluta".
- **A contagem vira ação:** destacar no currículo o que mais aparece ([[wiki/concepts/otimizacao-ats-curriculo]]); estudar e fazer um projeto com a stack dominante ([[wiki/concepts/curriculo-vs-portfolio]]); ou levar a tecnologia para a empresa atual, se for a ferramenta certa, para ter experiência "validada" e contável em entrevista.
- O mapa **não ajuda na candidatura em si**; ajuda a decidir o que mostrar e o que estudar.

Limites: a contagem não separa requisito obrigatório de "bônus" (o Kotlin da Brex), e descartar vagas de pouco overlap, como a aula faz, esconde as lacunas de quem quer mudar de stack.

## Base do front júnior (FrontPUSH)

A [[wiki/sources/frontpush-monetizacao-freelancer-como-conseguir-a-primeira-vaga|aula 04 do módulo Monetização e Freelancer]] lista a base de um currículo de front júnior: HTML e CSS, JavaScript e lógica, um framework (React, Vue ou Angular), noções de banco de dados e soft skills; e as duas vertentes que a vaga cobra, "front do front" e "back do front".

## Key Sources

- [[wiki/sources/frontpush-monetizacao-freelancer-como-conseguir-a-primeira-vaga]]: base do currículo de front júnior
- [[wiki/sources/introducao-mapeando-vagas]]
- [[wiki/sources/mapear-requisitos-de-multiplas-vagas-galego]]: método da tabela (categoria, prioridade, contagem, proficiência, notas) com vagas de Nubank, Brex e Itaú
