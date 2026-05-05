# Facade — Padrão de Projeto Estrutural

**Fonte:** https://refactoring.guru/pt-br/design-patterns/facade
**Também conhecido como:** Fachada
**Categoria:** Padrão Estrutural
**Data de adição:** 2026-05-05

---

## Propósito

O **Facade** é um padrão de projeto estrutural que fornece uma interface simplificada para uma biblioteca, um framework, ou qualquer conjunto complexo de classes.

---

## Problema

Imagine que você precisa fazer seu código funcionar com um amplo conjunto de objetos que pertencem a uma sofisticada biblioteca ou framework. Normalmente, você precisaria:

- Inicializar todos aqueles objetos
- Rastrear as dependências
- Executar métodos na ordem correta

Como resultado, a lógica de negócio de suas classes fica firmemente acoplada aos detalhes de implementação das classes de terceiros, tornando difícil compreendê-lo e mantê-lo.

---

## Solução

Uma fachada é uma classe que fornece uma **interface simples** para um subsistema complexo que contém muitas partes que se movem. Uma fachada pode fornecer funcionalidades limitadas em comparação com trabalhar com os subsistemas diretamente. Contudo, ela inclui apenas aquelas funcionalidades que o cliente se importa.

Ter uma fachada é útil quando você precisa integrar sua aplicação com uma biblioteca sofisticada que tem dúzias de funcionalidades, mas você precisa de apenas um pouquinho delas.

**Exemplo:** Uma aplicação que carrega vídeos curtos de gatos para redes sociais poderia usar uma biblioteca de conversão de vídeo profissional. Contudo, tudo que ela realmente precisa é uma classe com um único método `codificar(nomeDoArquivo, formato)`. Após criar tal classe e conectá-la com a biblioteca, você terá sua primeira fachada.

---

## Analogia com o Mundo Real

Quando você liga para uma loja para fazer um pedido, um **operador** é sua fachada para todos os serviços e departamentos da loja. O operador fornece a você uma simples interface de voz para o sistema de pedido, pagamentos, e vários sistemas de entrega.

---

## Estrutura

```
Cliente
   │
   ▼
┌─────────────┐
│   Facade    │  ← Interface simples para o cliente
└─────────────┘
   │    │    │
   ▼    ▼    ▼
[Sub1][Sub2][Sub3]  ← Subsistema complexo (o cliente não conhece)
```

**Participantes:**

1. **Fachada** — fornece acesso conveniente a uma parte da funcionalidade do subsistema. Sabe onde direcionar o pedido do cliente e como operar todas as partes móveis.

2. **Fachada Adicional** — pode ser criada para prevenir a poluição de uma única fachada com funcionalidades não relevantes. Fachadas adicionais podem ser usadas tanto por clientes como por outras fachadas.

3. **Subsistema Complexo** — consiste em dúzias de objetos variados. As classes do subsistema **não estão cientes da existência da fachada**. Elas operam dentro do sistema e trabalham entre si diretamente.

4. **Cliente** — usa a fachada ao invés de chamar os objetos do subsistema diretamente.

---

## Pseudocódigo

O padrão Facade simplifica a interação com um framework complexo de conversão de vídeo.

```
// Classes de um framework complexo de terceiros — não controlamos esse código
class VideoFile
class OggCompressionCodec
class MPEG4CompressionCodec
class CodecFactory
class BitrateReader
class AudioMixer

// A fachada esconde a complexidade do framework atrás de uma interface simples
class VideoConverter
    method convert(filename, format): File
        file = new VideoFile(filename)
        sourceCodec = (new CodecFactory).extract(file)

        if (format == "mp4")
            destinationCodec = new MPEG4CompressionCodec()
        else
            destinationCodec = new OggCompressionCodec()

        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = (new AudioMixer()).fix(result)
        return new File(result)

// Código da aplicação não depende de uma dúzia de classes do framework
class Application
    method main()
        conversor = new VideoConverter()
        mp4 = conversor.convert("funny-cats-video.ogg", "mp4")
        mp4.save()
```

---

## Como Implementar

1. **Verifique** se é possível providenciar uma interface mais simples que a que o subsistema já fornece. Você está no caminho certo se essa interface torna o código cliente independente de muitas classes do subsistema.

2. **Declare e implemente** essa interface em uma nova classe fachada. A fachada deve redirecionar as chamadas do código cliente para os objetos apropriados do subsistema. A fachada deve ser responsável por inicializar o subsistema e gerenciar seu ciclo de vida, a menos que o código cliente já faça isso.

3. **Faça todo o código cliente** se comunicar com o subsistema apenas através da fachada. Agora o código cliente fica protegido de qualquer mudança no código do subsistema. Por exemplo, quando um subsistema recebe um upgrade para uma nova versão, você só precisa modificar o código na fachada.

4. **Se a fachada ficar grande demais**, considere extrair parte de seu comportamento para uma nova e refinada classe fachada.

---

## Aplicabilidade

**Use o Facade quando:**

- Você precisa ter uma interface limitada mas simples para um subsistema complexo. Com o passar do tempo, subsistemas ficam mais complexos — o Facade fornece um atalho para as funcionalidades mais usadas que correspondem aos requerimentos do cliente.

- Você quer estruturar um subsistema em camadas. Crie fachadas para definir pontos de entrada para cada nível de um subsistema. Você pode reduzir o acoplamento entre múltiplos subsistemas fazendo com que eles se comuniquem apenas através de fachadas. Essa abordagem se parece muito com o padrão Mediator.

---

## Prós e Contras

| ✅ Prós | ❌ Contras |
|---|---|
| Isola o código cliente da complexidade do subsistema | Pode se tornar um **God Object** acoplado a todas as classes da aplicação |
| Ponto único de mudança quando o subsistema é atualizado | Pode esconder complexidade que o cliente precisaria conhecer |
| Reduz dependências entre o cliente e o subsistema | |
| Facilita o uso de bibliotecas complexas | |

---

## Relações com Outros Padrões

- **Facade vs Adapter:** O Facade define uma *nova* interface para objetos existentes. O Adapter tenta fazer uma *interface existente* ser utilizável. O Adapter geralmente envolve apenas um objeto; o Facade trabalha com um inteiro subsistema.

- **Facade vs Abstract Factory:** Abstract Factory pode servir como alternativa quando você precisa apenas esconder do cliente *como* os objetos do subsistema são criados.

- **Facade vs Flyweight:** Flyweight mostra como fazer vários pequenos objetos; Facade mostra como fazer um único objeto que represente um subsistema inteiro.

- **Facade vs Mediator:** Ambos tentam organizar colaboração entre classes acopladas, mas:
  - O **Facade** define uma interface simplificada e não introduz nova funcionalidade. O subsistema não está ciente da fachada; seus objetos podem se comunicar diretamente entre si.
  - O **Mediator** centraliza a comunicação entre componentes. Os componentes só sabem do mediador e não se comunicam diretamente.

- **Facade vs Singleton:** Uma classe fachada pode frequentemente ser transformada em um Singleton, já que um único objeto fachada é suficiente na maioria dos casos.

- **Facade vs Proxy:** Ambos armazenam em buffer uma entidade complexa e inicializam ela por conta própria, mas o Proxy tem a mesma interface de seu objeto de serviço, o que os torna intercambiáveis.

---

## Referência

- **URL:** https://refactoring.guru/pt-br/design-patterns/facade
- **Site:** Refactoring Guru
- **Série:** Padrões de Projeto — Padrões Estruturais
