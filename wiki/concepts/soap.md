---
type: concept
title: "SOAP"
aliases: ["Simple Object Access Protocol", "web services SOAP", "WSDL"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 1
tags: [soap, wsdl, integracao, legado, xml, interoperabilidade, seguranca]
skill: tech-mentor-backend
status: stub
---

# SOAP

Protocolo de troca de mensagens estruturadas em [[wiki/concepts/xml-extensible-markup-language|XML]] para comunicação entre sistemas distribuídos, criado em 1998 com forte participação da [[wiki/entities/microsoft]] e padronizado depois pelo [[wiki/entities/w3c]] (Simple Object Access Protocol). Resolvia um problema concreto do fim dos anos 1990: empresas precisavam conectar aplicações escritas em Java, C++ e .NET sem depender de soluções proprietárias de cada fornecedor — o mesmo problema que soluções same-platform como Java RMI e CORBA não resolviam entre plataformas diferentes.

## Por que setores regulados adotaram em massa

Bancos e seguradoras precisavam, além de interoperabilidade, de recursos que o REST simples não oferecia nativamente: assinatura digital, criptografia, transações distribuídas e **contratos rígidos** entre cliente e servidor. O ecossistema de especificações WS-Security, WS-ReliableMessaging e WS-AtomicTransaction existe exatamente para atender essas exigências — ver [[wiki/concepts/contrato-de-api]] para a ideia geral de contrato, aqui levada ao extremo formal via **WSDL** (Web Services Description Language), que descreve operações, tipos e formatos de mensagem de forma máquina-legível e permite gerar clientes/servidores automaticamente.

## Auge e declínio

Entre ~2002 e 2008, SOAP foi praticamente o padrão para serviços corporativos, consolidado por frameworks como Apache Axis, JAX-WS (Java) e Windows Communication Foundation (Microsoft). A partir de 2010, a expansão de aplicações web e mobile aumentou a demanda por APIs mais leves — REST + JSON passou a atender a maior parte desses cenários com muito menos complexidade de infraestrutura, e novos projetos migraram para lá.

## Por que ainda roda em produção

SOAP não desapareceu — migrou para segundo plano em setores onde contratos rígidos, interoperabilidade entre plataformas heterogêneas e segurança avançada continuam sendo requisitos reais, não modismo: bancos, seguradoras, operadoras de saúde, órgãos governamentais. No Brasil, a integração de notas fiscais eletrônicas com a Receita Federal ainda roda sobre SOAP. Muitos serviços SOAP eram (e ainda são) publicados e orquestrados por um [[wiki/concepts/esb-enterprise-service-bus|ESB]].

## Key Sources

- [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]]
