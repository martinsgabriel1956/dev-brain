---
type: source
title: "Onde foi parar a programação orientada a objetos?"
aliases: ["poo desceu um degrau", "onde foi parar a poo"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/onde-foi-parar-programacao-orientada-a-objetos-bernardo-lobato.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-11-03
source_count: 1
tags: [poo, oop, historia-do-software, paradigma, arquitetura, microsservicos, sistemas-distribuidos, agil]
skill: tech-mentor-backend
status: stable
---

## TL;DR

[[wiki/entities/bernardo-lobato|Bernardo Lobato]] percorre a história do software para defender que a [[wiki/concepts/programacao-orientada-a-objetos|POO]] não morreu, mas **desceu um degrau**: deixou de ser a forma obrigatória de organizar o sistema inteiro e passou a viver dentro de cada serviço, como uma ferramenta entre outras. O próprio autor avisa que são percepções pessoais, não um trabalho formal. A origem histórica confere com fontes primárias; a perda de relevância se apoia em anedotas.

## Key Claims

**Claim:** A POO desceu um degrau: continua útil dentro de cada serviço, mas o sistema completo se organiza em torno de serviços, contratos, eventos, filas e contêineres.
**Evidence:** em [[wiki/concepts/microsservicos|microsserviços]], cada serviço tem processo, dados e responsabilidades próprios, e a comunicação passa por APIs, eventos e mensageria.
**Confidence:** média. O argumento é coerente, mas sem dados.

**Claim:** A história repete um padrão: de `goto` para programação estruturada, daí para objetos, e de objetos para serviços. Cada passo sobe um nível de abstração em resposta à escala.
**Evidence:** o percurso histórico do vídeo.
**Confidence:** média-baixa. A sequência é uma simplificação, já que o próprio autor diz que os paradigmas funcional e lógico corriam em paralelo. Inferência da wiki: o último passo muda de categoria, de paradigma de programação para estilo arquitetural.

**Claim:** Os conceitos de classe, objeto e herança vieram da Simula, no fim dos anos 60; o termo *object oriented programming* foi cunhado por [[wiki/entities/alan-kay|Alan Kay]] antes do Smalltalk, criado na Xerox nos anos 70.
**Evidence:** relato do autor.
**Confidence:** alta. [external] A [página da Simula na Wikipedia](https://en.wikipedia.org/wiki/Simula) confirma a origem dos conceitos, com autoria de Dahl e Nygaard no Norwegian Computing Center. O [e-mail de Kay de 2003](https://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en) confirma o termo, que ele situa por volta de 1967.

**Claim:** A POO original era uma visão de partes independentes que guardam estado próprio e se comunicam por mensagens, hoje conhecidas popularmente como métodos.
**Evidence:** exemplo da interface gráfica: janela, botões e menus, cada um com estado próprio, respondendo a eventos.
**Confidence:** alta para a visão original. Ressalva [external]: no mesmo e-mail, Kay define POO por mensagens, retenção e ocultação local de estado e *late binding* extremo, e diz ter deixado herança de fora como recurso embutido. O vídeo lista herança entre os mecanismos da POO sem marcar essa divergência.

**Claim:** A POO ganhou força como resposta a software corporativo cada vez maior, com regras mais complexas e mais gente no mesmo código. Encapsulamento, abstração, polimorfismo, composição e herança serviam para controlar o acoplamento.
**Evidence:** argumento histórico do autor, sem dados.
**Confidence:** média.

**Claim:** Nas décadas de 1990 e 2000, saber POO era quase requisito obrigatório, e o resto do repertório valia pouco profissionalmente. O autor acha que o período ficou burocrático demais: processo e documentação acima do software em produção.
**Evidence:** C++, Java e C#; UML, RUP, JBoss, WebLogic e WebSphere. A burocracia é marcada como visão pessoal.
**Confidence:** média para o quadro de época; a burocracia é opinião.

**Claim:** O movimento ágil não foi uma crítica à POO, mas uma reação a processos rígidos.
**Evidence:** Manifesto Ágil, de 2001, valorizando software funcionando e capacidade de mudança.
**Confidence:** média-alta. [external] A [história oficial do manifesto](https://agilemanifesto.org/history.html) situa o encontro em fevereiro de 2001, em Snowbird, e não trata de orientação a objetos. Isso é compatível com a tese, mas não a prova.

**Claim:** A web levou problemas distribuídos à aplicação comum (latência, falhas de rede, concorrência, consistência eventual), e a modelagem por objetos não dá conta deles sozinha. Ao mesmo tempo, outros estilos cresceram.
**Evidence:** funções em JavaScript, multiparadigma em Python, lambdas e streams em Java, e a documentação do TypeScript.
**Confidence:** alta para TypeScript: [external] a [documentação](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-oop.html) diz que funções livres tendem a ser o modelo preferido em JavaScript, mas também aceita classes e hierarquias quando o problema pede. Média para o restante.

**Claim:** Parte do repertório amadureceu e sumiu de vista: injeção de dependência virou recurso de frameworks (Spring, NestJS), e herança perdeu espaço para composição, como já recomendava a [[wiki/entities/gang-of-four|Gang of Four]].
**Evidence:** exemplos do autor. A recomendação do livro não foi conferida no original nesta ingestão.
**Confidence:** média-alta.

**Claim:** O processo formal e o ensino mudaram: numa palestra, ninguém conhecia o RUP, e as grades universitárias consultadas não traziam POO como disciplina explícita.
**Evidence:** relato pessoal; não diz quais grades nem quantas, e admite que o tema deve estar embutido em outras cadeiras.
**Confidence:** baixa. É anedota e o próprio autor a situa na "minha bolha".

**Claim:** A POO continua excelente para representar estado, comportamento, invariantes, relações e responsabilidades dentro de um domínio, e o DDD a leva a nível estratégico.
**Evidence:** posição final do autor.
**Confidence:** média. Compatível com [[wiki/concepts/modelagem-orientada-a-objetos]] e [[wiki/concepts/encapsulamento]].

## Entities

[[wiki/entities/bernardo-lobato]], [[wiki/entities/alan-kay]], [[wiki/entities/edsger-dijkstra]], [[wiki/entities/gang-of-four]], [[wiki/entities/bertrand-meyer]].

## Concepts

[[wiki/concepts/programacao-orientada-a-objetos]], [[wiki/concepts/programacao-procedural]], [[wiki/concepts/programacao-funcional]], [[wiki/concepts/code-espaguete]], [[wiki/concepts/modelagem-orientada-a-objetos]], [[wiki/concepts/heranca-vs-composicao]], [[wiki/concepts/polimorfismo]], [[wiki/concepts/encapsulamento]], [[wiki/concepts/cqs]], [[wiki/concepts/microsservicos]].

## Open Questions

- **Desceu ou subiu?** Objetos independentes que só trocam mensagens lembram serviços. Inferência da wiki, não da fonte: a tese do degrau descreve a POO de classes, enquanto a visão de Kay talvez tenha reaparecido na arquitetura.
- **Perda de vocabulário ou de uso?** O autor pergunta quando o time discutiu polimorfismo pela última vez. Mas interface mais injeção de dependência, recomendada em [[wiki/concepts/heranca-vs-composicao]], é polimorfismo em uso diário. Inferência da wiki: o que sumiu pode ser a discussão, não a prática.
- **CQS está mesmo em baixa?** O vídeo põe [[wiki/concepts/cqs]] entre os conceitos menos discutidos, mas ele é a base do CQRS, que o mesmo autor trata em [[wiki/sources/cqrs-quando-faz-sentido-cqs-bernardo-lobato]].
- **"Obrigatória" para quem?** A fonte diz que a POO deve deixar de ser forma obrigatória de organizar o software; [[wiki/concepts/modelagem-orientada-a-objetos]] a chama de pré-requisito obrigatório para design patterns e arquitetura OO. Não se contradizem, porque o escopo é outro, mas isso muda o que um iniciante deve priorizar.
- Nenhum dado mede a relevância da POO no tempo: nem vagas, nem pesquisas, nem currículos identificados.

## Quotes

> "Minha tese é que ela mudou de lugar."

> "A POO desceu um degrau, ficou dentro do serviço."

> "Cada passo sobe um nivelzinho de abstração em resposta à escala."
