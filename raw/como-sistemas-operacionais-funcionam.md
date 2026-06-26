# Como Sistemas Operacionais Funcionam por Baixo dos Panos

> Transcrição de vídeo — tradução/adaptação do conteúdo original em português.

---

Você clica duas vezes num programa e ele abre. Mas entre esse clique e a primeira tela, o sistema operacional executou centenas de operações invisíveis. O que realmente acontece por baixo dos panos?

## O papel do sistema operacional

Imagine um prédio comercial com várias empresas funcionando ao mesmo tempo, cada uma usando salas, energia, elevador e banheiro. O sistema operacional é o administrador desse prédio: decide quem usa o quê, quando, e garante que ninguém invada o espaço do outro.

Sem ele, cada programa teria que saber falar diretamente com o hardware. Cada jogo, editor de texto e navegador precisaria de código para controlar o disco, a placa de vídeo e o teclado. O SO resolve isso criando uma **camada entre o hardware e os programas**.

---

## Processos

Toda vez que você abre um programa, o sistema operacional cria um **processo** — uma instância de um programa em execução. Ele tem:

- Um número de identificação: o **PID** (*Process ID*)
- Um estado atual
- Sua própria área de memória **isolada**

Um navegador não consegue acessar a memória do editor de texto, por exemplo. Isso é fundamental para segurança: se um processo travar, em geral ele não derruba os outros.

### Ciclo de vida de um processo

1. **Novo** — acabou de ser criado
2. **Pronto** — preparado para rodar, esperando o processador
3. **Executando** — o processador está dedicado a ele
4. **Esperando** — aguardando algum recurso (ex: leitura de disco)
5. **Finalizado**

---

## Threads

E se um processo precisar fazer várias coisas ao mesmo tempo? Um navegador precisa renderizar a página, dar play num vídeo e responder ao teclado — tudo simultaneamente.

Para isso existem as **threads**: fluxos de execução dentro de um mesmo processo. Cada thread tem sua própria pilha de execução, mas todas compartilham a mesma memória.

| | Processo | Thread |
|---|---|---|
| Memória | Isolada | Compartilhada |
| Criação | Cara (como abrir empresa nova) | Barata (usa recursos existentes) |
| Comunicação | Mais complexa | Mais rápida |

A comunicação entre threads é mais rápida justamente porque elas já compartilham memória — mas isso tem um preço.

### Deadlock

Se duas threads precisam de recursos que a outra está segurando, ambas ficam esperando indefinidamente. Isso é o **deadlock**.

> É como um cruzamento onde quatro carros chegam ao mesmo tempo e nenhum dá passagem.

Para evitar isso, usam-se mecanismos de sincronização. O mais comum é o **Mutex** (*Mutual Exclusion*): funciona como uma chave de porta — apenas uma thread pode segurar a chave por vez.

---

## Escalonador (Scheduler)

Com centenas de threads e processos competindo pelo processador, alguém precisa decidir quem roda em qual momento. Esse é o papel do **escalonador**.

### Round Robin

O algoritmo mais clássico: cada processo ganha uma fatia de tempo igual (ex: 10 ms) e depois cede lugar para o próximo. É justo, mas não diferencia urgências.

### Filas de prioridade

Sistemas reais usam filas de prioridade: processos mais urgentes são atendidos primeiro. O sistema pode aumentar a prioridade de processos que estão esperando há muito tempo, evitando que sejam ignorados para sempre (*starvation*).

### Context Switch

A troca de contexto entre processos tem um custo: o processador precisa salvar todo o estado do processo atual e carregar o do próximo. Isso acontece **milhares de vezes por segundo** — e você não percebe.

---

## Interrupções

Como o sistema operacional retoma o controle enquanto um processo está rodando?

Através de **interrupções**: sinais que param o que o processador está fazendo e transferem o controle de volta ao SO. Exemplos:

- **Timer de hardware**: avisa que a fatia de tempo do processo acabou
- **Teclado**: pressionar uma tecla gera uma interrupção
- **Disco**: quando termina de ler um arquivo, gera outra

Sem interrupções, um processo poderia monopolizar o processador para sempre.

---

## Gerenciamento de Memória

Cada processo precisa de memória para funcionar: variáveis, código, pilha de execução — tudo na RAM. Mas a RAM tem limite, e dois processos não podem escrever no mesmo endereço sem causar caos.

### Memória Virtual

A solução é a **memória virtual**: cada processo *acha* que tem toda a memória para ele. Ele vê endereços do zero até o limite, mas esses endereços são **virtuais**, não físicos.

O sistema operacional mantém uma tabela de tradução que converte endereço virtual → endereço físico real na RAM.

### Swap

Quando a RAM enche, o SO move para o disco os pedaços de memória que não estão sendo usados — isso é o **swap**. Funciona, mas o disco é muito mais lento que a RAM. Uso excessivo de swap = sistema travando.

---

## Sistema de Arquivos

Quando você salva um documento, ele não fica organizado linearmente no disco. O disco é um bloco gigante de zeros e uns.

Quem cria a abstração de pastas, nomes e hierarquia é o **sistema de arquivos**. Um arquivo de 12 MB pode estar dividido em vários blocos espalhados pelo disco (bloco 47, 193, 512...) e o sistema de arquivos mantém uma tabela que sabe onde cada pedaço está.

### Sistemas de arquivos por SO

| Sistema Operacional | Sistema de Arquivos |
|---|---|
| Linux | ext4 |
| Windows | NTFS |
| macOS | APFS |

Cada um tem seus trade-offs de performance, segurança e funcionalidades.

### Deleção de arquivos

Quando você "deleta" um arquivo, na maioria dos casos o sistema de arquivos **apenas remove a referência** da tabela — os dados continuam no disco até serem sobrescritos. Por isso programas de recuperação de dados funcionam.

---

## Chamadas de Sistema (Syscalls)

Se cada programa tivesse que implementar código para acessar o disco, a tela e a rede, seria um caos. Para isso existem as **chamadas de sistema**.

Quando um programa quer ler um arquivo, ele não acessa o disco diretamente — faz um pedido ao **kernel**.

### User Mode vs. Kernel Mode

| Modo | Quem roda | Acesso |
|---|---|---|
| User Mode | Programas | Limitado |
| Kernel Mode | Kernel | Total ao hardware |

Quando o programa chama `open()` para abrir um arquivo, o processador troca de modo: sai do user mode, entra no kernel mode, o kernel executa a operação e volta com o resultado.

Essa separação impede que um programa qualquer acesse a memória de outro ou formate discos sem permissão.

> É por isso que quando o kernel trava, **tudo** trava. A famosa tela azul do Windows é um exemplo: o kernel é a fundação — se ele cai, não tem nada embaixo para segurar.

---

## Resumo

Cada vez que você abre um programa, em milissegundos:

1. O SO cria um **processo** com PID e área de memória isolada
2. O **escalonador** decide quando ele vai rodar
3. **Interrupções** garantem que o SO retome o controle
4. A **memória virtual** isola o espaço de cada processo
5. O **sistema de arquivos** resolve onde os dados estão no disco
6. **Syscalls** fazem a ponte entre o programa e o hardware, com o kernel como guardião

O sistema operacional fez parecer tudo simples — mas agora você sabe o que está acontecendo por baixo dos panos.
