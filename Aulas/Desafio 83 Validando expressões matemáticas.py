parente=[]
espressao=input('Digite uma expressão:')
for c in espressao:
    if c == '(':
        parente.append(c)
    elif c == ')':
        if len(parente) > 0:
            parente.pop()
        elif len(parente) ==0:
            parente.append(c)
            break

if len(parente) == 0:
    print('Sua expressão esta valida.')
else:
    print('Sua expressão esta errada.')