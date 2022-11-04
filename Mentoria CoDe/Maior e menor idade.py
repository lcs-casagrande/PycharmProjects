maior = 0
menor = 0
for p in range (1,6):
    idade=int(input('Idade da {}ª pessoa:' .format(p)))
    if p == 1:
        maior = idade
        menor = idade
    if idade>maior:
        maior=idade
    if idade<menor:
        menor=idade
print(f'O mais velho tem {maior} anos')
print(f'O mais novo tem {menor} anos' )
