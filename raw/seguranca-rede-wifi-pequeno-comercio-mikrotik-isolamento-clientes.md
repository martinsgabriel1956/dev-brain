# Segurança de rede Wi-Fi em pequeno comércio: isolando clientes da rede interna com MikroTik

> **Origem:** transcrição de vídeo em português (YouTube, canal com comunidade de membros; autor não identificado na transcrição) colada pelo usuário em 2026-10-02. Já estava em português (sem tradução). Texto limpo, pontuado e dividido em seções; o conteúdo foi preservado. Foram omitidos apenas os pedidos de like/comentário/dislike e a despedida.
>
> **Correções de reconhecimento de fala (por contexto):** "MicroTik" → *MikroTik*; "192.198.0.x" / "192.68.0.x" → *192.168.0.x*; "AP router" mantido como dito (roteador Wi-Fi/ponto de acesso); "a PoE, é a porta" → provavelmente "a ether1" (porta de entrada/WAN; no MikroTik de 5 portas a porta 1 é a de uplink), preservado como dito; "R$ 2,400,00" → *R$ 2.400,00*; "R$ 4,800,00" → *R$ 4.800,00*; "10.0.0 e 10.0.0.x" tratados como a mesma faixa 10.0.0.x. O material citado (PDF e checklist) fica na comunidade do autor e **não** foi fornecido. As "cinco linhas de regra" da proteção bidirecional aparecem só em slide, não na fala.

## Abertura

Você chega a um restaurante, comércio ou clínica, pede a senha do Wi-Fi e se conecta normalmente. Mas e se esse Wi-Fi for exatamente a mesma rede onde estão o computador do financeiro, o sistema de PDV, as impressoras ou até as câmeras? Nesse caso você não está só acessando a internet: está **dentro da rede da empresa**, colocando um dispositivo desconhecido na mesma rede dos equipamentos dela.

O vídeo é uma pincelada, bem básica, sobre **segurança de rede Wi-Fi em pequenos comércios ou pequenas redes** (e até em casa). Quem pediu o tema foi o Diogo, da comunidade, que queria segurança de sistemas web; o autor diz que esse vem depois, e antes dá uma passada por segurança de rede local.

## O problema: a rede plana padrão de mercado

O padrão: assinatura de internet, roteador da operadora com Wi-Fi, uma senha distribuída às máquinas da empresa. Quando chega um cliente e pede Wi-Fi, a senha é a mesma, e ele passa a trafegar **em paralelo com todos os equipamentos**. Imagine uma clínica numa terça às 8h com 200 pessoas, ou um restaurante num almoço de domingo com mais de 100: todo mundo dentro da mesma rede.

Agora o cenário "mais maldoso": uma pessoa chega com um notebook com uma ferramenta de varredura de rede (um Kali Linux ou qualquer outra), pede o acesso ao Wi-Fi e consegue **escanear toda a rede sem que ninguém perceba**, porque recebeu a senha.

Esta é uma **rede plana**: o cliente tem internet, mas também trafega pacotes dentro da rede local, junto do PDV, do computador financeiro, do DVR das câmeras e das impressoras.

## Alternativa 1 (segura, mas cara): duas internets de operadoras diferentes

Isolamento completo, com IPs de saída distintos. Mas um plano empresarial custa algo em torno de R$ 200/mês: **+R$ 2.400 em 12 meses, +R$ 4.800 em 24**. Pode haver limitação regional (só uma operadora na área). E pedir dois modems à mesma operadora não resolve: a saída continua no mesmo IP, o que mantém a vulnerabilidade.

## Alternativa 2: roteador da operadora com Wi-Fi desligado + MikroTik

A solução inicial: o roteador da operadora fica com o **Wi-Fi desligado** e se liga, por cabo, a um **MikroTik** (equipamento razoavelmente barato, normalmente com cinco portas Ethernet; a primeira recebe a internet e as outras quatro a derivam, mas qualquer porta pode ser configurada para qualquer função). O autor avisa que não é propaganda.

Ao MikroTik ligam-se **dois APs** (cada um um "AP router"): um configurado na faixa **10.0.0.x** e outro em **192.168.0.x**. As duas redes ficam isoladas por faixa de IP, mas ainda não é suficiente.

### Por que dois APs e não um AP multi-SSID

Dá para usar um AP multi-SSID e configurar duas redes separadas. O problema: esses equipamentos, **independentemente do preço**, funcionam bem até cerca de **50 conexões**; a partir daí a comunicação degrada (sinal que cai e volta, como em lugares cheios). Com um único AP, o sistema da empresa também sofreria essa variação num momento de fluxo grande, podendo gerar **prejuízo operacional**. Por isso, sempre que possível: **um AP para os clientes e outro para a empresa**.

### Firewall no MikroTik: proteção unidirecional

Como clientes e empresa saem para a internet **pelo MikroTik**, e ele tem firewall, dá para bloquear entre as faixas. A regra é simples:

```
/ip firewall filter add chain=forward src-address=10.0.0.0/24 dst-address=192.168.0.0/24 action=drop
```

(escrita no vídeo como "IP firewall filter, add chain=forward, origem 10.0.0.x, destino 192.168.0.x, drop"). Explicação do autor: `chain=forward` é o tráfego **através** do MikroTik; `src-address` é a origem; `dst-address` é o destino; `action=drop` é descartar o pacote.

Resultado: o cliente acessa qualquer coisa da internet, mas **não acessa a rede interna**; as máquinas da empresa seguem com internet normal. Isso é uma **proteção unidirecional**; a bidirecional vem no final.

### IP fixo na rede interna

"Tudo isso é um mínimo; há muito mais a fazer." O segundo ponto é tornar a rede interna de **IP fixo**, o que libera para trabalhar com regras de firewall dentro dela. Exemplo na faixa 192.168.0.x: PDV .10, computador financeiro .20, impressora .30, DVR .40, câmeras .50, .51, .52, .53. Assim, mesmo que alguém acesse a rede local com uma senha vazada, estará "conectado, mas não dentro da rede".

O AP de clientes continua com **DHCP**. Ele não lê nem acessa a rede local. Ainda resta uma vulnerabilidade: dentro da rede de clientes, **todo mundo enxerga todo mundo**.

### Client Isolation (AP Isolation)

A grande maioria dos APs do mercado tem a opção **Client Isolation / AP Isolation** de fábrica: marca-se a opção e ninguém enxerga ninguém. Serve no AP dos clientes (10 clientes conectados e nenhum vê o outro). **Não pode** ser usada no AP da rede interna: ninguém enxergaria a impressora e o financeiro não falaria com o PDV. Por isso é preciso dois roteadores: um com o serviço ativo, outro com ele desativado.

### Checklist de síntese

Não é só a faixa de IP que protege (já é melhor que nada), **o que realmente protege é o firewall**. A partir de dois APs, dois acessos à rede e o isolamento entre eles, "você realmente está seguro".

## Desafio: três APs e proteção bidirecional

Roteador da operadora (Wi-Fi sempre off) → MikroTik → três APs: **clientes** (10.0.0.x), **funcionários** (172.16.0.x) e **empresa** (192.168.0.x). Faixas totalmente isoladas. A proteção bidirecional usa "cinco linhazinhas de regra" de firewall (mostradas em slide). Ninguém enxerga ninguém entre redes:

- AP de **clientes**: Client Isolation ativo, nenhum cliente enxerga o outro.
- AP de **funcionários**: o mesmo.
- AP da **empresa**: **sem** isolamento, senão a rede local para de conversar.

Resultado gráfico: todos acessam a internet; a rede local conversa entre si; a rede de funcionários não conversa entre dispositivos; a rede de clientes também não.

## Quanto cobrar

Depois de ter experiência com AP router e MikroTik, a configuração leva cerca de **duas horas**. O autor sugere cobrar em torno de **R$ 600** só pela instalação, passando ao cliente a lista de equipamentos para ele comprar. É "só o básico de rede, o primeiro passo", mas já dá alguma proteção. Há um checklist de operação no material da comunidade. Se houver engajamento, o autor se aprofunda em rede e segurança, e a comunidade terá em breve um vídeo só sobre segurança de sistemas web.
