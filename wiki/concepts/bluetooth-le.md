---
type: concept
title: "Bluetooth Low Energy (BLE)"
aliases: ["BLE", "bluetooth low energy", "GATT", "bluetooth de baixo consumo"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [bluetooth, ble, mobile, hardware, gatt, protocolo]
skill: tech-mentor-mobile
status: stub
---

# Bluetooth Low Energy (BLE)

Protocolo de comunicação sem fio de curto alcance e baixo consumo de energia, usado para conectar apps a dispositivos periféricos (wearables, sensores, fones, equipamentos IoT). Frequentemente tratado como "só conectar o fone", mas envolve um ciclo de conexão com várias etapas explícitas que, se mal gerenciadas, geram conexão fantasma e dreno de bateria.

## O Ciclo de Conexão

1. **Advertising** — o dispositivo periférico fica anunciando sua existência continuamente.
2. **Scan** — o app escaneia o ambiente em busca de dispositivos anunciando.
3. **Pairing** — encontrado o dispositivo, o app pareia com ele.
4. **Connection** — só depois do pareamento a conexão de fato abre.

## Hierarquia de Serviços (GATT)

Dentro da conexão existe uma hierarquia de **serviços** — os canais por onde o dado de fato trafega. Cada serviço expõe **características**, e para cada característica o app decide se lê, escreve, ou se inscreve para receber notificações quando o valor muda.

## Restrições Práticas

- **Conexões simultâneas são limitadas** — o número de periféricos conectados ao mesmo tempo tem um teto.
- **MTU (tamanho do pacote) é negociado** — não é fixo, varia por conexão.
- **A conexão cai** — reconexão não é automática; precisa ser gerenciada manualmente pelo app.

## Por que importa

Quem não gerencia esse ciclo completo — abrir, manter, fechar — sofre com:
- Conexão fantasma (app acha que está conectado, mas não está)
- Dreno de bateria (scan ou advertising contínuo sem necessidade)
- Bugs que só acontecem no aparelho do cliente e nunca no ambiente de desenvolvimento

## Relação com outros conceitos

- [[wiki/concepts/protocolo-de-rede]] — BLE é outro exemplo de protocolo em camadas com handshake próprio (advertising → scan → pair → GATT), análogo ao DNS → TCP → TLS de redes IP

## Key Sources

- [[wiki/sources/operador-de-crud-vs-engenheiro-repertorio]] — ciclo de conexão BLE como exemplo do "mundo debaixo do CRUD" fora de redes IP tradicionais
