---
type: concept
title: "Teste Unitário sem I/O"
aliases: ["unit test sem rede e disco", "premissa do teste unitário"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_count: 1
tags: [testes, teste-unitario, io, ci, isolamento]
skill: tech-mentor-testing
status: draft
---

# Teste Unitário sem I/O

Premissa defendida em [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]]: o teste unitário **não acessa rede nem disco**, para rodar em qualquer lugar — só depende da máquina onde executa. Quando acessa:

- no **servidor de build** (GitHub etc.) pode não haver rota para o banco de desenvolvimento;
- na **máquina do colega** a configuração (`localhost`, caminhos) não bate;
- o teste fica lento e frágil, e mistura o assunto testado (regra de validação) com outros (driver do banco, DNS).

Sintomas vistos na demo: erro de collection nula (banco nunca configurado) e "host não é conhecido" (`HttpClient` tentando sair para a rede). A saída é substituir o acesso externo por um [[wiki/concepts/test-doubles|test double]] atrás de uma interface ([[wiki/concepts/dependency-injection]]). Testar o acesso real é papel de teste de integração ([[wiki/concepts/testes-integracao-banco-real]], [[wiki/concepts/piramide-de-testes]]).

Ver [[wiki/concepts/acoplamento-que-impede-teste-unitario]]. Observação **[skill]**: a literatura também classifica como "unitário" testes sociáveis que usam objetos reais em memória ([[wiki/concepts/unit-test-solitario-vs-sociavel]]); a regra vale para I/O, não para colaboradores puros.

## Key sources

- [[wiki/sources/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti]]
