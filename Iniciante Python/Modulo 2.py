'''#dic = {}
tidade=cont=0
lista = []
lidade = []
while True:
    nome = input('Qual seu nome?')
    sexo = input('Qual seu sexo [M/F]?').upper()[0]
    idade = int(input('Qual sua idade?'))
    tidade +=idade
    novo = input('Novo dastro[S/N]?').upper()[0]
    dict={'Nome': f'{nome}','sexo': sexo,'Idade': idade}
    lista.append(dict)
    cont+=1
    if 'N' in novo:
        break
medidade=(tidade/cont)


print(len(lista))
print(medidade)


def rigth_justify():
    s=input('Digite uma palavra:')
    print(f'{s:>70}')
rigth_justify()

'''
cont=-1
lista = ['A',1,'E',5,'T',7,'W',8,'G']

for x in lista:
    print(x, end='')
print('>', end=' ')
for x in lista:
    cont+=1
    if cont %2 ==0:
        print(x , end='')
print('', end='')
for x in lista[::-1]:
    cont += 1
    if  x.isdigit()==True:
    #if cont % 2 ==0:
        print(x, end='')



