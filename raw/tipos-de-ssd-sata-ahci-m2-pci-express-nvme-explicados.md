# Todos os tipos de SSD explicados: SATA, AHCI, M.2, PCI Express e NVMe (transcrição)

> Transcrição de vídeo (PT-BR), limpa de erros de ASR; sem tradução (já em português). Canal não identificado na transcrição (o vídeo cita outro seu, "todos os tipos de armazenamento em 8 minutos", provavelmente "Todos os principais tipos de armazenamento de dados"). ASR corrigido: "HCI" → AHCI, "NVMA/NVMES" → NVMe, "PC Express" → PCI Express, "Luri" → Lu (IA da Alura) `[?]`. Duração: 9 minutos.

Existem vários tipos de SSDs. Alguns são tão lentos que não têm diferença nenhuma comparados a um HD convencional; outros são tão rápidos que transferem terabytes de dados em poucos minutos. Das gerações do PCI Express ao padrão NVMe, este vídeo explica todos os tipos de SSD, dos primeiros modelos aos mais novos.

## SSD SATA

Ponto de partida clássico. Conectam-se às mesmas portas SATA que os antigos HDs usavam, por isso foram fáceis de adotar: se o computador aceitava um HD, aceitava um SSD SATA. Em desempenho foram um salto gigantesco sobre os discos mecânicos: o boot caiu de minutos para segundos, programas abrem instantaneamente e notebooks antigos pareciam novos.

O problema: ficam travados em algo em torno de **550 MB/s**. Parece rápido vindo de um HD, mas é lento perto dos SSDs modernos. Analogia: sair de andar a pé para andar de bicicleta impressiona, até passar uma moto. Hoje são usados em PCs de baixo custo ou como armazenamento extra em máquinas mais antigas (e até novas): baratos, confiáveis e fáceis de encontrar, mas fora da ponta da tecnologia.

## AHCI

Se o SATA é a conexão física, o AHCI (Advanced Host Controller Interface) é a **linguagem** que essa conexão fala. Foi criado muito antes dos SSDs, para discos rígidos, e depois reaproveitado para SSDs. Nunca foi feito para a velocidade da memória flash: gerencia **apenas uma fila de comandos com no máximo 32 tarefas** ao mesmo tempo. Isso bastava para um HD mecânico, mas um SSD capaz de lidar com milhares de solicitações simultâneas faz do AHCI o gargalo.

Analogia: supermercado lotado com um único caixa; mesmo com vários funcionários prontos, a fila anda devagar. Todo SSD SATA roda em AHCI "por baixo dos panos": estável, compatível, mas fora de época. Outra analogia: assistir Netflix em 4K numa internet de escada.

(Trecho patrocinado: Alura, "a maior escola de tecnologia do Brasil", cursos de iniciante a avançado em programação, IA, dados, segurança, front-end, back-end, DevOps; aprendizado com projetos reais; a partir do plano Pro, a Lu, IA da Alura, tira dúvidas, explica conceitos, corrige exercícios e indica cursos; Tech Guide mostra quais tecnologias o mercado mais demanda; comunidade com eventos, grupos de estudo e mentorias; desconto via link/QR code na descrição.)

## M.2 não é sinônimo de rápido nem de NVMe

Duas confusões comuns: "M.2 significa SSD rápido" e "M.2 sempre significa NVMe". Nenhuma é verdade. **M.2 é apenas o formato físico** (o formato e o conector): um cartão pequeno, parecido com um chiclete, que se conecta direto na placa-mãe, sem cabos, bom para notebooks e desktops mais limpos.

Nem todo SSD M.2 é rápido: alguns são **SSD SATA no formato M.2**, presos ao limite de 550 MB/s. O formato só diz que ele encaixa no M.2; é preciso conferir qual tecnologia usa por dentro, **SATA ou NVMe**. A maioria dos M.2 atuais é NVMe, mas há muitos SATA, e a diferença é enorme: SATA ~550 MB/s contra NVMe a mais de 7.000 MB/s (carro esportivo a 60 km/h contra um jato na pista).

## PCI Express

É a conexão que os SSDs mais rápidos usam para falar com o processador. Ao contrário do SATA (pista única), o PCIe oferece **múltiplas pistas (lanes)** em paralelo; mais pistas e geração mais nova = mais velocidade. Valores citados com **quatro pistas**:

| Geração | Velocidade aproximada |
|---|---|
| PCIe 3.0 x4 | ~3.500 MB/s |
| PCIe 4.0 x4 | ~7.500 MB/s |
| PCIe 5.0 x4 | ~14.000 MB/s |

Faz diferença em jogos, edição de vídeo, renderização 3D e transferência de arquivos grandes, mas vem com preço mais alto e às vezes maior consumo de energia. Há também o limite de **pistas PCIe disponíveis**: processador e placa-mãe têm número limitado, e ligar muitos dispositivos ao mesmo tempo pode dividir a largura de banda. Ainda assim virou o padrão para SSDs de alto desempenho. Analogia: estrada secundária de pista única (SATA) vs. via expressa de várias pistas (PCIe); o destino é o mesmo, o tempo de viagem muda.

## NVMe

Protocolo moderno criado **especificamente para SSDs**. Diferente do AHCI (era dos discos rígidos), foi desenhado do zero para aproveitar a memória flash. Em vez de uma fila com 32 comandos, o NVMe suporta até **64.000 filas, cada uma com 64.000 comandos**: milhões de solicitações em paralelo. A latência também cai: tarefas que levavam cerca de **30 µs no AHCI** podem cair para **10 µs** no NVMe.

Por isso os SSDs NVMe parecem rápidos não só em benchmarks, mas no uso geral: jogos carregam quase instantaneamente, arquivos enormes são transferidos em segundos e a multitarefa fica fluida. É o protocolo padrão dos SSDs modernos de alta velocidade e, combinado com PCIe, libera todo o potencial. Analogia: se o AHCI era um supermercado com um caixa, o NVMe abre mil caixas ao mesmo tempo.
