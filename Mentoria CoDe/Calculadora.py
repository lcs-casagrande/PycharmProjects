# etrada de numeros
import math
res = n1=float(input('Digite um numero: '))
while True:
    op=input(str('Operação:[+],[-],[*],[/],[^],: '))
    if op in '-/=+*^':
        break
while True:

    n2=float(input('Digite segundo numero: '))
    if '*' in op:
        res= n1 * n2
    elif '+' in op:
         res= n1+n2
    elif '-' in op:
        res = n1 - n2
    elif '/' in op:
        res = n1 / n2
    elif '^' in op:
        res = math.pow(n1,n2)
    else:
        print('Operação invalida')
    while True:
        op2 = str(input('Digite proxima operação ou [=] para concluir!'))
        if op2 in '=^/+-*' :
            break
    if op2=='=':
        break
    n1=res
    op=op2

print(f'O resultado é {res}')