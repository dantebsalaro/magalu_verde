# Listas para as categorias que receberão desconto de x


computador = [
    "notebook", "macbook", "desktop", "computador", "pc gamer",
    "all-in-one", "chromebook", "netbook", "workstation",
    "mac mini", "mac pro", "thin client"
]

smartphone = [
    "celular", "smartphone", "iphone", "samsung", "motorola",
    "xiaomi", "oneplus", "realme", "asus zenfone", "nokia",
    "lg", "huawei"
]

tablet = [
    "tablet", "ipad", "ipad pro", "ipad mini", "galaxy tab",
    "kindle", "e-reader", "kobo", "wacom", "surface go",
    "lenovo tab", "fire hd"
]

bateria = [
    "bateria", "powerbank", "bateria li-ion", "bateria litio",
    "pilha recarregavel", "bateria de notebook", "bateria de tablet",
    "ups", "nobreak", "bateria automotiva", "power station",
    "bateria de drone"
]

periferico = [
    "mouse", "teclado", "webcam", "monitor", "impressora", "scanner",
    "hub usb", "leitor de cartao", "controle xbox", "controle ps",
    "joystick", "volante", "mesa digitalizadora", "pen drive",
    "hd externo", "ssd externo", "projetor", "periferico"
]

acessorio = [
    "fone de ouvido", "headset", "airpods", "caixa de som", "soundbar",
    "carregador", "cabo usb", "cabo hdmi", "adaptador", "fonte",
    "roteador", "modem", "switch de rede", "smartwatch",
    "camera de seguranca", "smart tv", "chromecast", "fire stick",
    "apple tv", "drone", "camera digital", "acessorio", "relogio", "relogio digital",
    "tv", "televisao"
]

#Variáveis usadas no código
valor_total = 0
np = 1 # Numeração do produto (Ex: total de produtos 3 -> np 1 = primeiro produto)
desc_total = 0

print('♻️  Bem-vindo ao Magalu Verde! 🌿')
print('💚 Troque seu eletrônico usado por desconto real.\n')

while True:
    produto = input('🛒 Digite a quantidade de produtos da compra: ')

    if produto.isdigit() and int(produto) > 0: #Validar entrada de número inteiro e maior que zero
        produto = int(produto)
        break
    else:
        print('\n❌ Valor inválido! Use apenas números inteiros e maiores que 0 (ex: 1; 2; 3).\n')


for i in range(produto): #Verificar se há entrada de ',' invés de '.'
    while True:
        valor = input(f'💰 Digite o valor do produto {np}: ').strip().replace(',', '.')
        validar = float(valor)
        np += 1

        if validar <= 0:
            print('❌ O valor deve ser maior que zero')
            continue
        try:
            vp = float(validar)
            break  #Sai do while quando for válido

        except ValueError:
            print("\n❌ Digite um número válido (ex: 10 ; 10.5 ; 10,5)\n")

    valor_total += vp

print('\n')

desc_max = valor_total * 0.25  # Teto de 25%

#Saber se o cliente tem algum eletrônico para descarte e, então, ganhar desconto + Validação
while True:
    tv = input('♻️ O cliente trouxe algum item? [S/N] ').upper().strip()
    if tv in ['S', 'N']:
        break
    print("❌ Digite apenas S ou N")

#Condição para verificar se o cliente possui algum eletrônico
if tv == "S":
    #Se o cliente tiver mais de um eletrônico, o código se repetirá até que se diga que não
    while True:
        cat = str(input('\n⚠️ ATENÇÃO! Se não encontrar o produto ou categoria, digite AJUDA.'
        '\n📦 Digite o produto ou sua categoria (SEM ACENTOS): ')).lower().strip()

        #Se o usuário não encontrar o produto ou categoria, ele pode pedir a lista do TrocaVerde
        if "ajuda" in cat:
            print('\ncomputador:'
'\n- notebook'
'\n- macbook'
'\n- desktop'
'\n- computador'
'\n- pc gamer'
'\n- all-in-one'
'\n- chromebook'
'\n- netbook'
'\n- workstation'
'\n- mac mini'
'\n- mac pro'
'\n- thin client\n\n'

'smartphone:'
'\n- celular'
'\n- smartphone'
'\n- iphone'
'\n- samsung'
'\n- motorola'
'\n- xiaomi'
'\n- oneplus'
'\n- realme'
'\n- asus zenfone'
'\n- nokia'
'\n- lg'
'\n- huawei\n\n'

'tablet:'
'\n- tablet'
'\n- ipad'
'\n- ipad pro'
'\n- ipad mini'
'\n- galaxy tab'
'\n- kindle'
'\n- e-reader'
'\n- kobo'
'\n- wacom'
'\n- surface go'
'\n- lenovo tab'
'\n- fire hd\n\n'

'bateria:'
'\n- bateria'
'\n- powerbank'
'\n- bateria li-ion'
'\n- bateria litio'
'\n- pilha recarregavel'
'\n- bateria de notebook'
'\n- bateria de tablet'
'\n- ups'
'\n- nobreak'
'\n- bateria automotiva'
'\n- power station'
'\n- bateria de drone\n\n'

'periferico:'
'\n- mouse'
'\n- teclado'
'\n- webcam'
'\n- monitor'
'\n- impressora'
'\n- scanner'
'\n- hub usb'
'\n- leitor de cartao'
'\n- controle xbox'
'\n- controle ps'
'\n- joystick'
'\n- volante'
'\n- mesa digitalizadora'
'\n- pen drive'
'\n- hd externo'
'\n- ssd externo'
'\n- projetor'
'\n- periferico\n\n'

'acessorio:'
'\n- fone de ouvido'
'\n- headset'
'\n- airpods'
'\n- caixa de som'
'\n- soundbar'
'\n- carregador'
'\n- cabo usb'
'\n- cabo hdmi'
'\n- adaptador'
'\n- fonte'
'\n- roteador'
'\n- modem'
'\n- switch de rede'
'\n- smartwatch'
'\n- camera de seguranca'
'\n- smart tv'
'\n- chromecast'
'\n- fire stick'
'\n- apple tv'
'\n- drone'
'\n- camera digital'
'\n- acessorio'
'\n- relogio'
'\n- relogio digital'
'\n- tv'
'\n- televisao\n\n')
            continue

        #Verificar de que categoria é o produto
        if cat in computador:
            desc = valor_total * 0.15
            print(f'💻 Categoria: Computador — 15% de desconto aplicado!')

        elif cat in smartphone:
            desc = valor_total * 0.10
            print(f'📱 Categoria: Smartphone — 10% de desconto aplicado!')

        elif cat in tablet:
            desc = valor_total * 0.12
            print(f'📟 Categoria: Tablet — 12% de desconto aplicado!')

        elif cat in bateria:
            desc = valor_total * 0.08
            print(f'🔋 Categoria: Bateria — 8% de desconto aplicado!')

        elif cat in periferico:
            desc = valor_total * 0.05
            print(f'🖱️  Categoria: Periférico — 5% de desconto aplicado!')

        elif cat in acessorio:
            desc = valor_total * 0.03
            print(f'🔌 Categoria: Acessório — 3% de desconto aplicado!')

        else:
            #Se o usuário digitar uma categoria ou produto que não existe, o código volta para o começo do loop
            print(f'\n❌ Produto ou categoria "{cat}" não encontrado. Verifique se foi escrito corretamente'
                  f'e tente novamente.')
            continue

        #O desconto será acumulado a cada vez que o loop se repetir
        desc_total += desc

        #Verifica se o desconto máximo já foi atingido, se já, o loop se quebra
        if desc_total >= desc_max:
            desc_total = desc_max
            print('\n')
            print('🏆 Desconto máximo de 25% atingido!')
            break

        print('\n')

        while True:
            mais = str(input('♻️ Mais algum produto TrocaVerde? [S/N] ')).upper().strip()
            if mais in ["S", "N"]:
                break
            else:
                print('\n❌ Valor Inválido! Os únicos valores válidos são "S" ou "N"! Tente novamente.\n')

        if mais == "N":
            print(f'\nO desconto será de R${desc_total:.2f}')
            break

elif tv == "N":
    print('\n')

print(f'✅ Valor total: R${valor_total - desc_total:.2f}')
print(f'\n💚 Obrigado por cuidar do planeta! #MagaluVerde ♻️')