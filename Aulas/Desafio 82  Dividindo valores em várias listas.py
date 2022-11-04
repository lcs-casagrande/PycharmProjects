par = []
impar = []
completa = []
while True:
    n = int(input('Digite um numero: '))
    completa.append(n)
    if n % 2==0:
        par.append(n)
    else:
        impar.append(n)
    c = input('Quer continuar? ').upper()
    if c in 'N':
        break
print('-='*30)
print(f'Lista completa {completa}.')
print(f'Lista par {par}.')
print(f'lista impar {impar}.')
