---
type: concept
title: "Linda (Coordination Language)"
aliases: ["Linda", "linguagem de coordenação Linda"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 1
tags: [sistemas-distribuidos, coordenacao, linda, tuple-space]
skill: tech-mentor-backend
status: stub
---

# Linda (Coordination Language)

Linguagem de coordenação criada por [[wiki/entities/david-gelernter|David Gelernter]] e [[wiki/entities/nicholas-carriero|Nicholas Carriero]] na Universidade de Yale em 1986. Introduziu o [[wiki/concepts/tuple-space|tuple space]] como primitiva de coordenação global entre processos — não é uma linguagem de computação de propósito geral, mas um modelo de **comunicação generativa** (generative communication) para ser combinado com uma linguagem hospedeira.

Serviu de base teórica para implementações posteriores como [[wiki/concepts/javaspaces|JavaSpaces]] (Java) e portes para Lisp, Lua, Prolog, Python, Ruby, Smalltalk, Tcl e .NET.

## Key sources

- [[wiki/sources/tuple-space-wikipedia]] — origem e contexto histórico (Yale, 1986); cita o paper original "Generative communication in Linda" (Gelernter, ACM TOPLAS, 1985)
