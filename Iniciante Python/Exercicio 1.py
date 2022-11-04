galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma +=pessoa['idade']

    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro. S ou N')
    if resp == 'N':
        break
print('+-'*20)
print(galera)
print(f'Temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A média de idade é {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end = ' ')
print()
print(f'Listas das pessoas que estão acima da média:' ,end=' ')
for p in galera :
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ' , end=' ')
        print()
print('<<ENCERRADO>>')
