# indice de uma lista sempre começa por 0 e dentro de cochetes []

lista_numeros = [1,2,3]

lista_numeros[0] = 5

# listas podem ter diferentes dado
# numeros = [1, 2, 3]
# strings = ['João', 'Sarah', 'Samuel']
# decimais = [10.8, 15.2, 33.3]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

lista_vazia = []
lista_vazia.append('Sarah')
lista_vazia.append('Barros')
print(lista_vazia)


# analisando valores (variavel numeros) 

numeros = (10, 9, 8, 7, 6)
print('total:', len(numeros))
print('menor valor', min(numeros))
print('maior valor', max(numeros))


# para interroper o loop, vamos usar a função range, onde 'X' é uma variavel que servirá como contador dentro do loop, ela percorre a função range. A função range gera uma sequência de números com indice iguais a lista.

for x in range(5):
    print(x)