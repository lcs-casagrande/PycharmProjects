#recebendo os dados
cadastro = input('Deseja cadastrar?')
c = cadastro.lower()
contador = 0
if c == 's' or 'sim':
    while c == 's' or 'sim':
        nome = input('Nome: ')
        sexo = input('Sexo: ')
        idade = input('Idade: ')
        contador = contador + 1
        cad = input('Novo cadastro?')
        c = cad.lower()
        if c != 's' or 'sim':
            break
banco = {'nome': nome, 'sexo': sexo, 'idade': idade}
print(contador)
print(cad)
print(c)
