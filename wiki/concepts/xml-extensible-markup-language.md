---
type: concept
title: "XML (Extensible Markup Language)"
aliases: ["Extensible Markup Language", "XML data format"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: [xml, formato-de-dados, interoperabilidade, legado, serializacao]
skill: tech-mentor-backend
status: stub
---

# XML (Extensible Markup Language)

Formato de dados estruturado, validável e independente de plataforma, tornado recomendação oficial do [[wiki/entities/w3c]] em 1998, coordenado por Jon Bosak (Sun). Nasceu como alternativa mais simples ao SGML, preservando a capacidade de representar documentos estruturados sem toda a complexidade do padrão original. Resolvia o mesmo problema de fundo que motivou o [[wiki/concepts/soap|SOAP]]: sistemas de fornecedores diferentes precisavam trocar dados de forma padronizada e validável.

> Nota de desambiguação: esta página trata do formato de dados XML. Para a técnica de usar tags XML para estruturar prompts de IA, ver [[wiki/concepts/xml-markdown-prompts]] — mesma sintaxe, domínio de aplicação completamente diferente.

## Auge (fim dos anos 1990 – anos 2000)

XML virou a espinha dorsal de praticamente toda a tecnologia corporativa do período: formato de mensagem do [[wiki/concepts/soap]], `pom.xml` no Maven, `build.xml` no Ant, além de um ecossistema de manipulação e validação (JAXB, DOM, SAX, XSD, XSLT) e de padrões industriais de troca de dados.

## Declínio nas APIs web

Com o crescimento das aplicações web (Ajax) e mobile, JSON passou a dominar por ser mais compacto, mais fácil de manipular em JavaScript e mais barato de serializar/deserializar. Esse deslocamento afetou principalmente APIs públicas voltadas a aplicações web — não o uso corporativo/documental do formato.

## Onde continua essencial

Documentos do Microsoft Office, projetos Java, arquivos de configuração, nota fiscal eletrônica e diversos padrões internacionais de troca de dados. Continua sendo a escolha natural sempre que padronização, validação de schema e interoperabilidade entre sistemas heterogêneos são requisitos centrais — não apenas um detalhe de serialização.

## Key Sources

- [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]]
