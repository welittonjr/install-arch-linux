# Instalação do Arch Linux

+ [Início]()
+ [Configurações iniciais]()
    + [Definição de teclado](#setkeyboard)
    + [Conexão com a internet](#checknetwork)
    + [Verificar disco](#checkdisk)
+ [Preparar instalação]()
    + [Particionar o disco](#partdisk)
    + [Formatar partições](#partformt)
    + [Criar pastas para montagem](#createdir)
    + [Realizar montagem de partições](#mount)
+ [Alterar mirror](#updatemirror)
+ [Instalação de base](#install)
+ [Gerar fstab](#gfstab)
+ [Configurando ambiente arch]()
    + [Usando arch-chroot](#arch-chroot)
    + [Definindo fuso horario](#sethours)
    + [Atualizar o relogio](#updateclock)
    + [Adicionando tradução](#translate)
    + [Definir variavel de ambiente com tradução](#setenvtranslate)
    + [Definir teclado no sistema](#setkeybordsystem)
    + [Definir hostname](#sethostname)
    + [Definir o ip da maquina interna](#sethosts)
    + [Definir senha usuario root](#password)
    + [Criando usuario comum](#createuser)
+ [Instalação de pacotes](#install-apps)
+ [Adicionando usuario ao grupo sudo](#usersudo)
+ [Install Grub](#grub)
+ [Finalizar Instalação]()
    + [Sair do chroot](#exitchroot)
    + [Desmontando estrutura archlinux](#umount)
    + [Reiniciar o arch](#shutdown)
    

## <a name="setkeyboard"></a> Definição de teclado
Lista de layout de teclado
```bash
$ ls /usr/share/kbd/keymaps/**/*.map.gz | grep br
```
Definir teclado
```bash
$ loadkeys br-abnt2
```

## <a name="checknetwork"></a> Conexão com a internet
ver as interfaces de reder
```bash
ip addr show
```
com wifi
```bash
wifi-menu
```

## <a name="checkdisk"></a> verificando os dicos
```bash
lsblk
```
```bash
fdisk -l
```

## <a name="partdisk"></a> Particionar o disco
```bash
cfdisk /dev/sda
```

|Sevice   |Size |Type            |
|---------|-----|----------------|
|/dev/sda1|500M |BIOS boot       |
|/dev/sda2|     |Linux Filesystem|
|/dev/sda3|     |Linux Filesystem|
|/dev/sda4|     |Linux Swap      |

*Write and Quit*

```bash
fdisk -l /dev/sda
```

## <a name="partformt"></a> Formatar partições
```bash
mkfs.fat -F32 /dev/sda1
```
```bash
mkfs.ext4 /dev/sda2
```
```bash
mkfs.ext4 /dev/sda3
```
```bash
mkfswap /dev/sda4
```

## <a name="createdir"></a> Criar pastas para montagem
```bash
mkdir /mnt/{boot,home}
```

## <a name="mount"></a> Montar a partição raiz
```bash
mount /dev/sda1 /mnt/boot/efi
mount /dev/sda2 /mnt
mount /dev/sda3 /mnt/home
swapon /dev/sda4
```

## <a name="updatemirror"></a> Alterar mirror
```bash
cat /etc/pacman.d/mirrorlist
```

## <a name="install"></a> Instalação do archlinux e bases
```bash
pacstrap /mnt base base-devel linux linux-firmware
```

## <a name="gfstab"></a> Gerar fstab
```bash
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab
```

## <a name="arch-chroot"></a> Usando arch-chroot
```bash
arch-chroot /mnt /bin/bash
```
## <a name="sethours"></a> Definindo fuso horario
```bash
ln -sf /usr/share/zoneinfo/America/Belem /etc/localtime
ls -l /etc/localtime
```

## <a name="updateclock"></a> Atualizar o relogio
```bash
hwclock --systohc
```

## <a name="translate"></a> Adicionando tradução
definir **pt_BR.UTF-8 UTF-8**
```bash
nano /etc/locale.gen
```

## <a name="setenvtranslate"></a> Definir variavel de ambiente com tradução 
```bash
nano /etc/locale.conf
```
definir esse variavel no arquivo locale.conf
```bash
export LANG="pt_BR.UTF-8"
```
carregar a tradução do sistema
```bash
locale-gen
```

## <a name="setkeybordsystem"></a> Definir teclado no sistema
```bash
nano /etc/vconsole.conf
```
```bash
export KEYMAP="br-abnt2"
```

## <a name="sethostname"></a> Definir o nome da máquina
```bash
nano /etc/hostname
```
ex:
```bash
arch
```

## <a name="sethosts"></a> Definir o ip da maquina interna
```bash
nano /etc/hosts

127.0.0.1 localhost.localdomain localhost
::1	localhost.localdomain localhost
127.0.0.1 arch.localdomain arch
```

## <a name="password"></a> Definir password do usuário root
```bash
passwd
```

## <a name="createuser"></a> Criand usuário comum
```bash
useradd -m -g users -G wheel wellington
```

## <a name="install-apps"></a> instalando Apps
```bash
pacman -S dosfstools os-prober mtools nano network-manager-applet networkmanager grub
wpa_supplicant wireless_tools sudo dialog
```

## <a name="usersudo"></a> Adicionar usuario no grupo sudo
```bash
nano /etc/sudoers
```
definir nome do usuário
wellington ALL=(ALL)ALL
## <a name="grub"></a> Instalar o GRUB
```bash
grub-install /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg 
```

## <a name="exitchroot"></a> Sair do chroot
```bash
exit 0
```

## <a name="umount"></a> Desmontando estrutura archlinux
```bash
umount -R /mnt
```

## <a name="shutdown"></a> Reiniciar o arch
```bash
shutdown -h now
```
