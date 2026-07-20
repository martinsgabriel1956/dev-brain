---
title: "AI Jail: como blindar seu agente de IA (Claude Code, Codex, etc.) contra ataques de supply chain"
source_type: video-transcript
language: pt-BR
translated: false
---

## Introdução — o problema dos ataques de supply chain

A gente sabe que o npm está cada dia mais "envenenado" — confiar numa lib do npm virou quase uma aposta, por causa da quantidade de ataques de supply chain. E não é só o npm: o Composer (PHP) já tomou a mesma facada, e o ecossistema Python também está sofrendo com o mesmo tipo de problema.

Qual é a forma mais segura de instalar pacotes, rodar ferramentas de CLI e até o próprio Claude Code? A abordagem mais popular é criar uma espécie de **cela** (sandbox/jail) para o seu agente de IA — conceito que Fábio Akita já trouxe no canal dele e repetiu no Flow Podcast, chamado de **AI Jail**.

### Por que isso importa

Um agente de IA precisa ter acesso ao sistema para ser útil: ele roda `grep`, `npm`, compilador, linter — tudo que precisa para ler e trabalhar dentro do projeto. Só que, junto com esse acesso, vem o poder de:

- ler suas credenciais da AWS
- exportar suas chaves SSH
- rodar um `rm -rf` fora do projeto

E não adianta pensar "na minha máquina está tudo certo" — ataque de supply chain é real e sério. Em março (2026), a biblioteca **Axios** — famosa, usada para fazer fetch de dados, com milhões de downloads — foi comprometida e virou um Trojan que roda a cada `post install`. Não era preciso aceitar nada ou fazer nada: só ter o Axios na máquina e rodar um `post install` já disparava o ataque.

**Regra de ouro:** partir do princípio de que tudo é inseguro até que se prove o contrário — não dá mais para confiar nem em pacotes open source famosos. A única coisa entre o atacante e suas credenciais é a barreira de defesa que você constrói antes.

> **Nota lateral (patrocínio):** o vídeo inclui uma recomendação do PostHog (analytics/observabilidade — error tracking, session replay, SDKs para Python/Node/Go, plano gratuito) como ferramenta para monitorar o que acontece em produção depois que o produto está no ar. Tratado aqui como conteúdo patrocinado, não como parte da tese técnica central do vídeo.

## O que é o AI Jail

O artigo do Akita foi publicado em janeiro de 2026. O projeto está no GitHub dele: um shell script de ~170 linhas. O conceito por baixo é o **Bubblewrap** (`bwrap`) — o mesmo componente usado pelo Flatpak para isolar aplicativos de desktop no Linux. É um binário pequeno (menos de 1 MB), mantido pelo time do GNOME, que roda sem precisar de root.

A instalação é simples — está no repositório para Linux, Windows (via WSL2) etc. Depois é só chamar `ai-jail` e o projeto inteiro já roda dentro da cela.

### O que o AI Jail faz na prática

Ele monta a sua pasta `home` como se fosse um diretório temporário vazio (uma "home" totalmente em branco), e traz para dentro do projeto apenas o que você escolhe — você controla exatamente o que o agente precisa acessar.

**Demonstração:**

1. Na home normal: `cat ~/.aws/credentials` mostra as chaves (`aws_secret_access_key` etc.) — tudo visível.
2. Ao rodar `ai-jail bash` dentro de um projeto e tentar `cat ~/.aws/credentials`: "operação não permitida". Abrindo o arquivo num editor dentro da cela, ele aparece em branco — sem acesso.
3. Dentro do projeto atual, `ls` e `cat` funcionam normalmente (ex.: ler o `CLAUDE.md` do projeto) — tudo que está dentro do projeto é visível; tudo que está fora, não.
4. É possível definir granularmente quais pastas o agente pode escrever — por exemplo, `.claude` pode entrar como somente leitura, e o resto do projeto como leitura+escrita.
5. Rodando `ai-jail claude` dentro do projeto: o Claude Code inicia dentro da cela e não tem acesso a nada fora dela — nem ao login/credenciais salvas do usuário.

Na primeira instalação do AI Jail existe uma etapa de configuração onde você define comandos, regras, o que o agente vê e o que não vê. O arquivo `.aijail` gerado é **comitável**: qualquer dev que clonar o projeto e rodar `ai-jail` dentro dele herda exatamente as mesmas políticas de isolamento. A segurança vira parte do projeto, não algo que cada dev configura na mão.

### Três flags importantes

- **`--dry-run`**: mostra tudo que o AI Jail vai fazer sem executar nada — permite auditar antes.
- **`--lockdown`** ("modo paranoico"): para rodar código de terceiros em que você não confia. Corta a rede, deixa o projeto somente leitura, zera tudo.
- **`--bootstrap`**: gera automaticamente um arquivo de permissões do sistema para o Claude Code (ver seção "Segunda camada" abaixo).

## AI Jail vs. o sandbox nativo do Claude Code

O Claude Code tem sandbox próprio desde outubro de 2025, e por baixo dos panos ele usa exatamente o mesmo stack: **Bubblewrap** no Linux e **Sandbox-exec** no Mac — o mesmo que o Akita usa no AI Jail. Ou seja, a própria Anthropic concorda que essa é a abordagem certa.

A diferença real está em outro lugar: quando um comando falha por uma restrição do sandbox do Claude Code, o próprio Claude pode tentar de novo usando a flag `--dangerously-skip-sandbox` (ou equivalente), caindo no fluxo normal sem restrição — e esse padrão de "voltar" já vem ativado por padrão na configuração de fábrica. Ou seja, o próprio agente pode decidir, sozinho, a hora de sair da cela.

No AI Jail não existe essa porta dos fundos: o processo roda dentro do `bwrap` e ponto final — não há flag mágica de escape. Além disso, o AI Jail é agnóstico de agente: funciona com Claude Code, Codex, OpenCode, Crush, etc. O sandbox do Claude Code, por comparação, protege apenas o Claude.

## As três camadas de segurança

A ideia central do artigo do Akita é empilhar três camadas independentes — como um cofre de banco: porta blindada, parede de concreto, alarme. Se uma falha, a próxima contém o dano. Nenhuma das três muda a forma como você trabalha no dia a dia.

### Camada 1 — Sessão (AI Jail)

A cela em si: home isolada e temporária que some ao fechar o terminal, dados sensíveis invisíveis, só o projeto tem permissão de escrita. Protege o que está acontecendo *nesse exato momento*, enquanto o agente roda.

### Camada 2 — Código (Git)

Para Akita, essa foi "a sacada mais braba". Pense no pior cenário: o agente surta e corrompe todos os arquivos do projeto. Segundo ele: "é irritante, é irritante — [mas não é] catástrofe", porque um `git checkout` volta tudo ao estado anterior. Se corromper até a pasta `.git`, no limite você apaga o projeto e clona de novo do GitHub — o repositório remoto continua íntegro.

Por isso o `git push` já vem configurado para **perguntar antes**: o AI Jail nunca permite um `git push --force` automático.

### Camada 3 — Sistema operacional imutável

O nível "hard paranoia", para quem leva a sério de verdade. No Linux normal, qualquer programa rodando como root pode escrever/mexer no sistema inteiro. Num sistema imutável (ex.: Fedora Silverblue/Atomic, NixOS), a raiz do sistema é somente leitura — um snapshot que nem root consegue modificar. As ferramentas de dev ficam em containers isolados, e o sistema por baixo fica intocável. Consequência: se algo escapar da cela, no próximo reboot o sistema volta ao estado original sozinho.

**Resumo das três camadas:** o SO cuida do sistema, o AI Jail cuida da sessão, o Git cuida do código. Para um ataque te derrubar de verdade, teria que furar as três camadas ao mesmo tempo: escapar da cela, sobreviver num sistema somente leitura e ainda corromper o repositório remoto no GitHub. Praticamente impossível.

Não é preciso implementar as três de uma vez — só o AI Jail, mais um Git sem push automático, já coloca você num nível de segurança bem acima da média.

## Suporte por sistema operacional

- **Linux:** suporte nativo via Bubblewrap.
- **Mac:** o AI Jail usa Sandbox-exec por baixo, com algumas limitações.
- **Windows:** sem suporte nativo direto, mas funciona normalmente via **WSL2**, onde o Bubblewrap roda sem problema.

## Fechamento

Resumo prático: instale o AI Jail, rode `ai-jail claude` (ao invés de chamar `claude` direto), comite o arquivo `.aijail` no repositório, deixe o Git configurado para perguntar antes de dar push. Cerca de 5 minutos de setup, e o agente perde acesso a tudo que é sensível na máquina.

Referências citadas no vídeo original: o repositório do AI Jail no GitHub e o artigo original de Fábio Akita (janeiro de 2026).
