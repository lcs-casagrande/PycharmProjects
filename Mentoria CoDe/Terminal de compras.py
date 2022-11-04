from time import sleep

compras = []
valor = []
quantidade = []
cont = total = val = quant = itotal = 0
print('Bem-vindo ao mercado Casagrande')
sleep(.5)
while True:
    pro = str(input('Digite o produto ou [fim] para encerrar: '))
    if 'fim' in pro:
        break
    compras.append(pro)
    sleep(.2)
    quant = float(input('Quantos itens?'))
    itotal += quant
    quantidade.append((quant))
    pre = float(input('Digite o valor do produto: '))
    total += (quant * pre)
    valor.append(pre)
    sleep(.2)
print('Lista da compra:')
for c in compras:
    coptot=quantidade[cont]*valor[cont]
    print(f'{quantidade[cont]} {c} de R${valor[cont]:.2f} total R${coptot:.2f} ')
    cont += 1
    sleep(0.5)
print(f'Itens totais {itotal}.')
print(f'Valor total de R${total:.2f}.')
while True:
    pg = str(input('Qual a forma de pagamento:'
                   'Dinheiro, Pix:'
                   'Cartão :')).upper()

    if 'PIX' in pg:
        total = total * 0.9
        print(f'pagamento pix, com 10% de desconto, total R${total:.2f}.')
        break
    elif 'DINHEIRO' in pg:
        total = total * 0.9
        print(f'pagamento dinheiro, com 10% de desconto, total R${total:.2f}.')
        break
    elif 'CART' in pg:
        print(f'pagamento cartão total R${total:.2f}.')
        break
    else:
        print('Metodo de pagamento invalido')
