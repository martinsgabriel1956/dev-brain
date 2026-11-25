---
type: concept
title: "Otimização de Currículo para ATS"
aliases: ["ATS", "applicant tracking system", "robô que lê currículo", "keyword matching currículo"]
date_created: 2026-07-15
date_updated: 2026-11-25
source_count: 8
tags: [carreira, contratação, ats, currículo]
skill: tech-mentor-leadership
status: draft
---

# Otimização de Currículo para ATS

Antes de qualquer humano ler um currículo, a maioria das empresas passa o documento por um **ATS** (Applicant Tracking System) — um filtro automático que busca a presença e a recorrência de termos-chave da vaga (linguagem, framework, ferramenta) no texto do currículo.

## Como o filtro funciona na prática

- O ATS procura quantas vezes a tecnologia-base da vaga aparece no corpo do currículo (ex.: ".NET", "Python", "React")
- Uma única menção isolada é um sinal fraco — pode ser só um curso feito uma vez
- Repetir a tecnologia em **múltiplas seções** (resumo/"sobre mim", experiência, habilidades técnicas) sinaliza uso recorrente e real, não pontual
- Recomendação prática: pelo menos duas a três repetições da stack-alvo ao longo do documento

## PDF Pesquisável como Pré-Requisito Mecânico

[[wiki/sources/analise-curriculo-vaga-junior-desenvolvedor]] acrescenta um requisito mecânico anterior à contagem de repetições: o PDF do currículo precisa permitir Ctrl+F e retornar a palavra-chave — se o texto não é selecionável/pesquisável (por exemplo, currículo exportado como imagem), o ATS não encontra a keyword mesmo que ela apareça visualmente no documento. Um currículo com "TypeScript" citado três a quatro vezes ao longo do texto é dado como exemplo de repetição adequada.

## Habilidade Listada sem Evidência no Corpo do Currículo

A mesma fonte documenta um padrão recorrente nos três currículos analisados: uma tecnologia (no caso, Java) aparece na seção "habilidades técnicas" mas não é citada em nenhuma experiência, projeto ou curso do restante do documento. Isso não derruba o ATS (que só conta menções), mas compromete a etapa seguinte — a leitura humana — porque levanta a pergunta óbvia em entrevista: "onde você usou isso?". Reforça a distinção desta página entre repetição pontual (fraca) e repetição distribuída em múltiplas seções (forte): a keyword precisa aparecer também onde há contexto (experiência, projeto), não só na lista solta de habilidades.

## Relação com [[wiki/concepts/curriculo-vs-portfolio]]

Passar no ATS é só a primeira barreira — é sobre o currículo (a "promessa") ser lido por um humano. O link de GitHub/portfólio ativo é o que sustenta a promessa depois que o filtro automático deixa passar.

## O mesmo mecanismo fora do currículo: perfil de plataforma como metadado de busca

[[wiki/sources/duas-perguntas-linkedin-cursos-online-lei-de-sturgeon]] descreve o mesmo raciocínio aplicado a um lugar diferente: o perfil do [[wiki/entities/linkedin]]. Lá não é um ATS que filtra, é a recrutadora buscando diretamente por palavra-chave (tecnologia, senioridade, tempo de casa, região) numa ferramenta paga. O princípio é idêntico ao do ATS de currículo — título e competências não são vaidade, são metadados de busca — mas com uma inversão de custo: a busca da empresa é cara (licença de recrutamento pode custar dezenas de milhares de dólares/ano), enquanto preencher o próprio perfil de forma buscável tem custo zero para o candidato. Ver [[wiki/concepts/assimetria-de-custo-plataforma-de-contratacao]].

## Ver também

- [[wiki/concepts/curriculo-vs-portfolio]] — a etapa seguinte, depois de passar no ATS
- [[wiki/concepts/portfolio-backend-junior]] — o que compõe a prova técnica depois da triagem
- [[wiki/concepts/assimetria-de-custo-plataforma-de-contratacao]] — o mesmo mecanismo de metadados de busca aplicado ao perfil de uma plataforma de rede profissional em vez de a um documento de currículo

## Palavras-Chave Devem Vir das Vagas-Alvo, Não de uma Lista Genérica

[[wiki/sources/6-conselhos-carreira-programador-10-anos-experiencia]] conecta o mecanismo do ATS a um erro anterior: se o desenvolvedor não olhou primeiro o que as vagas-alvo pedem, corre o risco de otimizar o currículo para palavras-chave que não são as que os empregadores de fato buscam. Ver [[wiki/concepts/curriculo-vs-portfolio]] para a mesma tese aplicada ao processo de desenvolvimento de habilidades, não só ao texto do documento.

## Vagas como fonte de lacunas

[[wiki/sources/introducao-mapeando-vagas]] propõe ler os requisitos das vagas para achar lacunas do currículo ([[wiki/concepts/mapeamento-de-requisitos-de-vagas]]); a mesma leitura dá as palavras-chave para o ATS.

## CV sem cores nem gráficos

Na [[wiki/sources/frontpush-monetizacao-freelancer-como-construir-um-portfolio|aula 05 do módulo Monetização e Freelancer]], [[wiki/entities/nasser|Násser]] pede CV "preto no branco", sem cores, gráficos nem "eu sei 80% de tal tecnologia". O motivo dele é a imaturidade que isso revela, não o ATS, mas o resultado serve aos dois. Ver [[wiki/concepts/estrutura-de-curriculo]].

## O que destacar

A contagem de [[wiki/sources/mapear-requisitos-de-multiplas-vagas-galego]] diz o que "deixar mais em evidência no seu currículo": os itens que mais aparecem nas vagas-alvo ([[wiki/concepts/mapeamento-de-requisitos-de-vagas]]).

## Currículos por empresa no board

Em [[wiki/sources/acompanhando-as-applications-galego]], a aplicação seletiva é "customizada, bem desenhada pra aquela empresa", e o board no Notion guarda "alguns currículos diferentes" ao lado de cada candidatura ([[wiki/concepts/acompanhamento-de-candidaturas]]).

## Key sources

- [[wiki/sources/analise-curriculos-programador-junior-dicas-ats]]
- [[wiki/sources/6-conselhos-carreira-programador-10-anos-experiencia]] — palavras-chave do currículo devem vir do que as vagas-alvo pedem, não de uma lista genérica de habilidades já estudadas
- [[wiki/sources/duas-perguntas-linkedin-cursos-online-lei-de-sturgeon]] — mesmo mecanismo de metadados de busca, aplicado ao perfil do LinkedIn em vez de ao currículo
- [[wiki/sources/analise-curriculo-vaga-junior-desenvolvedor]] — PDF pesquisável como pré-requisito mecânico, e o padrão de habilidade listada (Java) sem nenhuma evidência de uso no corpo do currículo
- [[wiki/sources/introducao-mapeando-vagas]] — mapear requisitos das vagas
- [[wiki/sources/frontpush-monetizacao-freelancer-como-construir-um-portfolio]]: CV preto no branco
- [[wiki/sources/mapear-requisitos-de-multiplas-vagas-galego]] — contagem de requisitos define o que destacar
- [[wiki/sources/acompanhando-as-applications-galego]] — currículo customizado por empresa, guardado no board
