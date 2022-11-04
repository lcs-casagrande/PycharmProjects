lanche = ('Hambúrguer','Suco','Pizza','Pudim','Batata frita')
# Tuplas são imutaveis
#lanche[1] = 'Refrigerante'
'''
print('Primeiro')
for comida in lanche:
      print(f'Eu vou comer {comida}.',end=' ')
print('Comi para caramba')
print('Segundo')
for cont in range (0, len(lanche)):
      print(f'Eu vou comer {lanche[cont]}', end=' ')
print('Terceiro')
for pos, comida in enumerate(lanche):
      print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))
print(lanche)
'''
a = (2,5,4,)
b = (5,8,1,2)
c = b + a
print(c)
print('count')
print(c.count(8))
print('index')
print(c.index(5,1))
pessoa = ('Gustavo',39, "m",99.88)
del(pessoa)3
print(pessoa)