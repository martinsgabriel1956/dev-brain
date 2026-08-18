# CQRS

**Por Martin Fowler**
Publicado em: 14 de julho de 2011
Fonte original: https://martinfowler.com/bliki/CQRS.html

---

## Visão Geral

CQRS significa **Command Query Responsibility Segregation** (Segregação de Responsabilidade entre Comando e Consulta). Segundo Fowler, esse padrão permite usar modelos diferentes para atualizar e para ler informação. Embora potencialmente valioso em certos contextos, ele enfatiza que o CQRS introduz complexidade substancial, inadequada para a maioria dos sistemas.

## A Abordagem CRUD Tradicional

O método convencional trata sistemas de informação como datastores CRUD, suportando operações de criar, ler, atualizar e deletar sobre estruturas de registro. Conforme os requisitos ficam mais sofisticados, os sistemas tipicamente divergem desse modelo simples por meio de várias representações de informação e camadas de apresentação.

## O Modelo CQRS

Em vez de manter um único modelo conceitual, o CQRS divide a representação em modelos separados de comando e de consulta. Como Fowler explica: "A justificativa é que, para muitos problemas, particularmente em domínios mais complicados, ter o mesmo modelo conceitual para comandos e consultas leva a um modelo mais complexo que não faz bem nenhuma das duas coisas."

Esses modelos podem rodar como implementações de objetos distintas, em processos lógicos ou hardware diferentes. A comunicação entre o lado de comando e o de consulta pode ocorrer por meio de bancos de dados compartilhados ou de armazenamentos de dados separados, sendo que a segunda opção efetivamente cria um banco de dados de relatórios em tempo real.

## Padrões Relacionados

CQRS combina naturalmente com:
- Interfaces de usuário baseadas em tarefas (task-based UI)
- Programação orientada a eventos e Event Sourcing
- Abordagens de consistência eventual
- Princípios de Domain-Driven Design

## Quando Usar CQRS

Fowler identifica dois cenários principais em que o CQRS se mostra benéfico:

1. **Domínios complexos**, onde separar as responsabilidades genuinamente simplifica a modelagem (um caso minoritário)
2. **Aplicações de alta performance**, com cargas de leitura/escrita muito diferentes que exigem escalabilidade independente

Porém, ele alerta fortemente: o CQRS deve se aplicar apenas a bounded contexts específicos, nunca a sistemas inteiros. Implementações mal aplicadas aumentam substancialmente a complexidade e o risco do projeto, sem os benefícios correspondentes.

## Cautela

Fowler enfatiza cautela, observando que a maioria das implementações que ele encontrou se provou problemática em vez de bem-sucedida. Abordagens alternativas, como bancos de dados de relatórios (reporting databases), podem alcançar benefícios semelhantes sem a sobrecarga de complexidade do CQRS.
