
tidade=cont=sexo=0
lista = []
lidade = []
mulheres = []
while True:
    nome = input('Qual seu nome?')
    while True:
        sexo = input('Qual seu sexo [M/F]?').upper()[0]
        if sexo in 'MF':
            break
    while True:
        idade = float(input('Qual sua idade?'))
        break
    tidade +=idade
    while True:
        novo = input('Novo cadastro[S/N]?').upper()[0]
        if novo in 'NS':
            break
    dict={'Nome': nome,'sexo': sexo,'Idade': idade}
    lista.append(dict)
    cont+=1
    if sexo == "F":
        mulheres.append(nome)

    if 'N' in novo:
        break
medidade=(tidade/cont)
print((f'Foram cadastrados {len(lista)} pessoas.'))
print(f'A media de idade é de {medidade}.')
print((f'As mulheres são:'))
for x in mulheres:
    print(x)
print(f'Pessoas acima da idade média:')
for p in lista:
    if p['Idade'] >= medidade:
        print(p["Nome"],end = ' - ')
