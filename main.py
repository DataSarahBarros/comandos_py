# criar uma variável que vai armazenar três frutas, criar um loop de forma que ele vai mover o último item da lista para o primeiro

# primeiro exemplo:
# lista_frutas = ['banana', 'uva']

# lista_frutas.append('kiwi') #método = append / parâmetro = item 'kiwi': acrescenta um novo item no final da lista


# while True:
#     ultima_fruta = lista_frutas.pop() #método = pop / parâmetro = nenhum: remove e retorna o último item
#     lista_frutas.insert(0, ultima_fruta)

#     print(lista_frutas)

# para interroper o loop, vamos usar a função range, onde f é uma variavel que servira como contador dentro do loop, ela percorre a função range. A função range gera uma sequência de números com indice iguais a lista

# segundo exemplo:
# lista_frutas = ['banana', 'uva', 'kiwi']

# for f in range(1):
#     ultima_fruta = lista_frutas.pop()
#     lista_frutas.insert(0, ultima_fruta)

#     print(lista_frutas)

# criar uma lista dentro do parametro da função, cinco str na lista. Desses cinco, validar um por um, quais desses é igual a determinada variável, quando printar essa função, trará o indice que esterminada str.

# def indice_fruta (lista_frutas, minhas_frutas): #definir minha função 'indice_frutas' o parametro da função é 'lista_frutas' (a lista a ser pesquisada) e 'minhas_frutas' (a str que quero encontrasr)

#     indice[] #criando uma lista vazia


     
#     return indice # retorna o valor da lista onde a função foi chamada

# minhas_frutas = lista_frutas() # a função 'lista_frutas' que armazena a lista de frutas na variável 'minhas_frutas'

# indice_fruta = minhas_frutas.index('banana') # método = index / parâmetros = item 'banana' : retorna o número de ocorrencias do item 
# print('A banana esta no indice: '.format(indice_fruta))