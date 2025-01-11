# módulo random usando choice pra trazer um resultado aleatório da lista

from random import choice
Aluno1 = str(input('Primeiro aluno: '))
Aluno2 = str(input('Segundo aluno: '))
Aluno3 = str(input('Terceiro aluno: '))
Aluno4 = str(input('Quarto aluno: '))
lista = [Aluno1, Aluno2, Aluno3, Aluno4]
escolhido = choice(lista) #Choice: Elemento aleatório único de uma sequência
print('O aluno  escolhido foi {}'.format(escolhido))

# módulo random sando shuffle para embaralhar a lista e printar resultados diferentes

from random import shuffle
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4]
shuffle(lista) # Baralhar uma lista
print('A ordem de apresentação será ')
print(lista)