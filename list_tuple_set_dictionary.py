# listas são coleções de elementos. Uma lista pode ser alterada, recebendo ou perdendo elementos. Utilizase os colchetes
# para iniciar uma lista.
frutas = ['maçã', 'banana', 'morango']
print(f'listas'
      f'\n{frutas}')

# Posição na lista: para indicar uma posição na lista, utiliza-se a sintaxe lista[posição]
print(frutas[0])

# Inserção e remoção de elementos
frutas.append('limão')
print(frutas)

frutas.pop(0)
print(frutas)

# Ordenação
frutas.sort()
print(frutas)

frutas.reverse()
print(f'{frutas}\n\n\n'
      f'tuplas')


# tuplas: são listas imutáveis. São iniciadas por parenteses
dias_da_semana = ('Dom','Seg','Ter','Qua','Qui','Sex','Sáb')
print(dias_da_semana)

#tupla para lista e vice-versa
dias_da_semana_list = list(dias_da_semana)
dias_da_semana_list.append('Nona-Feira')
print(dias_da_semana_list)
dias_da_semana_list.pop(0)
print(dias_da_semana_list[0])
tuple(dias_da_semana_list)
print(f'dias_da_semana_list\n\n\n'
      f'set')



# set: é uma sequência de elementos únicos. É indicado pelas chaves.
vogais = {'a','e','i','o','u'}
print(vogais)

# para adicionar um elemento novo a um set, utiliza-se a função add
vogais.add('b')
print(f'vogais\n\n\n'
      f'listas feitas de tuplas ')
# print(vogais[0]) não funciona pq um set não é ordenado.


# lista feita de tuplas
p1 = ('Marcio', 23)
p2 = ('Pedro', 24)
p3 = ('Sarah', 21)
pessoas = [p1,p2,p3]
print(pessoas)
# posição na lista, posição na tupla
idade_p1 = pessoas[0][1]
print(idade_p1)

# dicionários: é um set com pares. Também é iniciado por chaves, mas a diferença fica na sintaxe dos elementos.
print('\n\n\ndicionario')
pessoas_dicionario = {'Marcio':23, 'Pedro':24, 'Sarah':21}
print(pessoas_dicionario['Marcio'])

