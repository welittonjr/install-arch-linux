# Instalação do Arch Linux

# [Início]()
+ [Configurações iniciais]()
    + [Definição de teclado](#setkeyboard)
    + [Conexão com a internet](#checknetwork)
    + [Verificar disco](#checkdisk)
+ [Preparar instalação]()
    + [Particionar o disco](#partdisk)
    + [Formatar partições](#partformt)

## <a hre="setkeyboard"></a> Definição de teclado
Lista de layout de teclado
```bash
$ ls /usr/share/kbd/keymaps/**/*.map.gz | grep br
```
Definir teclado
```bash
$ loadkeys br-abnt2
```

## <a hre="checknetwork"></a> Conexão com a internet
ver as interfaces de reder
```bash
ip addr show
```
com wifi
```bash
wifi-menu
```

## <a hre="checkdisk"></a> verificando os dicos
```bash
lsblk
```
```bash
fdisk -l
```

## <a hre="partdisk"></a> Particionar o disco
```bash
cfdisk /dev/sda
```

|Sevice   |Size |Type            |
|---------|-----|----------------|
|/dev/sda1|500M |BIOS boot       |
|/dev/sda2|     |linux filesystem|
|         |     |                |

*Write and Quit*

```bash
fdisk -l /dev/sda
```

## <a hre="partformt"></a> Formatar partições
```bash
# primeiro o BIOS boot
mkfs.fat -F32 /dev/sda1
# depois
mkfs.ext4 /dev/sda2
```

## montar a partição raiz
```bash
mount /dev/sda2 /mnt/
```

## instalação do archlinux e bases
```bash
pacstrap /mnt base base-devel linux linux-firmware
```

## fstab
```bash
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab
```

## chroot
```bash
arch-chroot /mnt /bin/bash
```

## instalando apps
```bash
pacman -S vim nano networkmanager
```

## definindo fuso horario
```bash
ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
ls -l /etc/localtime
```

## atualizar o relogio
```bash
hwclock --systohc
```

## adicionando tradução
```bash
nano /etc/locale.gen
```
definir **pt_BR.UTF-8 UTF-8**

## Definir variavel de ambiente
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
## Definir o nome da máquina
```bash
nano /etc/hostname
```
ex:
```bash
arch
```
## Definir o ip da maquina interna
```bash
nano /etc/hosts

127.0.0.1 localhost.localdomain localhost
::1	localhost.localdomain localhost
127.0.0.1 arch.localdomain arch
```

## Definir password do usuário root
```bash
passwd
```

## Instalar o GRUB
```bash
pacman -S grub
pacman -S os-prober
grub-install /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg 
```
## Adicionar usuario

## Sair do chroot
```bash
exit 0
```


## Desmontando estrutura archlinux
```bash
umount -R /mnt
```

## Reiniciar o arch
```bash
shutdown -h now
```
