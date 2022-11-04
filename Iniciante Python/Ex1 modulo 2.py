banco = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma +=pessoa['idade']
    banco.append(pessoa.copy())
    resp = str(input('Quer continuar? ')).upper()[0]
    if resp == 'N':
        break
print('+-'*20)
#print(banco)
print(f'Temos {len(banco)} pessoas cadastradas')
media = soma / len(banco)
print(f'A média de idade é {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in banco:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end = ' ')
print()
print(f'Listas das pessoas que estão acima da média:' ,end=' ')
for p in banco :
    if p['idade'] >= media:
        print(f'{p["nome"]}',end = ' ')
print()
print('<<Fim da operação>>')
