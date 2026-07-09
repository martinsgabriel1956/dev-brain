# Sistemas de Arquivos Explicados

O sistema de arquivos é um método que o sistema operacional usa para organizar e armazenar arquivos em um dispositivo de armazenamento como um HD, um SSD, um pendrive. Ele rastreia onde cada arquivo está localizado e como os dados estão organizados para que o computador possa ler, escrever e gerenciar informações rapidamente.

Em apenas 9 minutos, este vídeo explica todos os sistemas de arquivos, dos mais antigos como o FAT12 (lançado em 1980) até os mais recentes, utilizados em data centers e sistemas de armazenamento corporativos onde a confiabilidade dos dados é extremamente importante.

## FAT (File Allocation Table)

Um dos sistemas de arquivos mais antigos utilizados no Windows é chamado FAT — Tabela de Alocação de Arquivos.

A primeira versão foi o **FAT12**, lançado em 1980. Ele só podia armazenar arquivos menores que 32 MB de tamanho — qualquer coisa maior do que isso resultava em erro. Isso era suficiente na época, mas os dispositivos de armazenamento rapidamente começaram a ficar maiores e mais eficientes.

Então uma nova versão, o **FAT16**, foi introduzida. Essa versão aumentou os limites de forma massiva: pela primeira vez os computadores podiam utilizar HDs de GB e armazenar arquivos individuais maiores que 2 GB.

Depois veio o **FAT32**, que ainda é usado até hoje. Ele suporta volumes maiores que 32 GB no Windows e até 2 TB em alguns outros sistemas operacionais. O FAT32 suporta tamanho máximo de arquivo de até 4 GB.

Em sistemas modernos, esse limite de 4 GB por arquivo pode se tornar um problema. Por exemplo, se você tentar copiar um arquivo de vídeo maior que 4 GB para um pendrive formatado em FAT32, o sistema mostrará um erro mesmo que o dispositivo ainda tenha bastante espaço livre.

Além disso, o FAT32 não pode criar partições maiores que 2 TB. Se alguém tentar formatar um HD de 4 TB usando FAT32, o sistema pode dividir em duas partições de 2 TB em vez de criar uma única partição grande.

Apesar dessas limitações, o FAT32 ainda é amplamente utilizado em pendrives, cartões de memória e alguns dispositivos externos. O principal motivo é a compatibilidade — como o FAT existe há muito tempo, funciona com praticamente qualquer sistema operacional e dispositivo.

## NTFS (New Technology File System)

NTFS significa Sistema de Arquivos de Nova Tecnologia. Ele pode suportar arquivos e volumes extremamente grandes — um único arquivo pode ter até 16 exabytes. (Para contexto: 1 exabyte equivale a 1 milhão de TB.) Em outras palavras, o tamanho de arquivo e de volume são praticamente ilimitados, o que remove a maior limitação do FAT32.

O NTFS também é um sistema de arquivos com **journaling**: ele mantém o registro das mudanças sendo feitas no disco. Se o computador travar de repente ou perder energia, o sistema pode utilizar esse registro para recuperar o sistema de arquivos e reduzir as chances de corrupção de dados.

O NTFS permite que o sistema operacional controle quem pode acessar certos arquivos ou pastas — por exemplo, um arquivo pode ser marcado como somente leitura, ou o acesso pode ser restrito a usuários específicos. Ele também suporta recursos como criptografia de arquivos, compressão e cotas de disco, tornando-o muito mais adequado para sistemas operacionais modernos. É por isso que versões modernas do Windows devem ser instaladas em disco formatado em NTFS.

A única desvantagem real do NTFS é a compatibilidade limitada com sistemas que não são Windows.

## exFAT (Extended File Allocation Table)

exFAT foi introduzido pela Microsoft em 2006 e é basicamente o FAT32 turbinado. Com o exFAT, um único arquivo pode ter até 16 exabytes — praticamente ilimitado para o uso do dia a dia. Isso torna o exFAT útil para armazenar arquivos de vídeo grandes, imagens de disco e gravações em alta resolução.

Comparado ao NTFS, o exFAT não inclui recursos avançados como journaling, permissões de arquivos, criptografia ou cotas de disco — mas essa simplicidade também o torna mais rápido e mais adequado para dispositivos de armazenamento portáteis.

Outra vantagem do exFAT é a compatibilidade: versões modernas do Windows e do macOS o suportam com leitura e escrita completas. Por causa desse equilíbrio entre suporte a arquivos grandes e ampla compatibilidade, o exFAT é comumente usado em pendrives grandes, dispositivos de armazenamento externos e cartões de memória SDXC usados em câmeras e dispositivos de gravação.

## HFS, HFS+ e APFS (linhagem Apple)

HFS significa Sistema de Arquivos Hierárquico e foi introduzido pela Apple em 1985. Foi usado nos primeiros computadores Macintosh. O HFS permitia arquivos de até 2 GB e suportava volumes de até 2 TB.

Depois, a Apple introduziu o **HFS+**, também conhecido como Mac OS Estendido. Essa versão aumentou significativamente o limite de armazenamento e também adicionou journaling. Por muitos anos, o HFS+ permaneceu como o principal sistema de arquivos usado em computadores Mac.

Em 2017, a Apple introduziu um sistema completamente novo chamado **APFS** (Apple File System). Ele foi projetado principalmente para SSDs modernos e armazenamento flash, e inclui recursos modernos como criptografia forte, snapshots e melhor gerenciamento de espaço. Hoje, o APFS é o sistema de arquivos padrão utilizado nas versões modernas do macOS.

Assim como os sistemas do Linux, os sistemas de arquivos da Apple não são suportados nativamente no Windows — um computador com Windows normalmente não consegue ler um disco APFS ou HFS+ sem software adicional.

## ext2, ext3 e ext4 (linhagem Linux)

ext significa Sistema de Arquivos Estendido e foi criado para o sistema operacional Linux. Diferente do Windows, que usa principalmente NTFS, a maioria dos sistemas Linux depende do ext.

**ext2** foi o sistema de arquivos mais antigo e eficiente da família, porém não era um sistema com journaling — o que significava que, se o sistema travasse ou perdesse energia, havia grande chance de corrupção de arquivos.

Para corrigir esse problema, o **ext3** foi introduzido, e a principal melhoria foi o journaling. Assim como o NTFS, o ext3 mantém o registro das mudanças sendo feitas no disco e pode recuperar dados utilizando esse registro.

Depois, o **ext4** foi lançado em 2008 e hoje é o sistema de arquivos mais utilizado no Linux. O ext4 suporta dispositivos de armazenamento muito maiores, permitindo arquivos de até cerca de 16 TB e volumes de até 1 exabyte.

Como esses sistemas de arquivos foram projetados especificamente para Linux, o Windows e o macOS não oferecem suporte nativo a eles — se você conectar um disco ext4 de Linux em um computador com Windows, normalmente ele não conseguirá ler sem software especial. Por esse motivo, esses sistemas são usados principalmente em discos de sistemas Linux e servidores Linux, em vez de dispositivos de armazenamento portáteis.

## ZFS (Zettabyte File System)

ZFS significa Sistema de Arquivos de Zettabyte. Foi originalmente desenvolvido pela Sun Microsystems e lançado pela primeira vez em 2006.

Uma das maiores vantagens do ZFS é a proteção de dados: ele verifica constantemente os dados armazenados usando checksums para detectar corrupção. Se dados danificados forem encontrados e existir uma cópia de backup, o ZFS pode repará-los automaticamente.

O ZFS também suporta sistemas de armazenamento muito grandes, permitindo volumes que podem atingir a escala de zettabytes — infinitamente além da necessidade de computadores pessoais comuns.

Por causa desses recursos, o ZFS é comumente usado em servidores, data centers e sistemas de armazenamento corporativos, onde a confiabilidade de dados é extremamente importante. Hoje, o ZFS está disponível no Linux, FreeBSD e outros sistemas baseados em Unix, e continua sendo desenvolvido pelo projeto OpenZFS.

## Fechamento

Os sistemas de arquivos são a base para o funcionamento do sistema operacional, mas são apenas um entre vários tipos diferentes de formatos de arquivos.

> Nota: o vídeo original contém, no meio do conteúdo, um bloco publicitário sobre um curso de investimentos ("AVP") usando a analogia de "sistema" (bom sistema de arquivos vs. bom sistema financeiro). Esse trecho foi omitido desta transcrição por não ser conteúdo técnico.
