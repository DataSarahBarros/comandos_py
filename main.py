# criar uma variável que vai armazenar três frutas, criar um loop de forma que ele vai mover o último item da lista para o primeiro

# primeiro exemplo:
# lista_frutas = ['banana', 'uva']

# lista_frutas.append('kiwi') #método = append / parâmetro = item 'kiwi': acrescenta um novo item no final da lista


# while True:
#     ultima_fruta = lista_frutas.pop() #método = pop / parâmetro = nenhum: remove e retorna o último item
#     lista_frutas.insert(0, ultima_fruta) #método = insert / parâmetro = item ou posição, ou os dois que é o caso vai colocar o item 'ultima fruta' na posição 0. O métod insert insere um novo intem na posição dada.
#     print(lista_frutas)

# para interroper o loop, vamos usar a função range, onde f é uma variavel que servira como contador dentro do loop, ela percorre a função range. A função range gera uma sequência de números com indice iguais a lista

# segundo exemplo:
# lista_frutas = ['banana', 'uva', 'kiwi']

# for f in range(1): 
#     ultima_fruta = lista_frutas.pop()
#     lista_frutas.insert(0, ultima_fruta)

#     print(lista_frutas)

# criar uma lista dentro do parametro da função, contendo cinco str na lista. Desses cinco, validar um por um, quais desses é igual a determinada variável, quando printar essa função, trará o indice dessa variavel desterminada.

# aprendendo a usar enumerate: é uma função que itera sobre uma sequência (lista) enquanto acompanha o índice de cada elemento

# lista_frutas = ['banana', 'uva', 'kiwi']

# for indice_fruta, fruta in enumerate(lista_frutas):
#     print('a fruta {} esta no indice {}'.format(fruta, indice_fruta))

#resolvendo o problema usando a função enumerate:

def encontrar_indice (indice_frutas, indice_minhas_frutas): #definir minha função 'indice_frutas' o parametro da função é 'lista_frutas' (a lista a ser pesquisada) e 'minhas_frutas' (a str que quero encontrasr)

    for i, str in enumerate(indice_frutas): #Utiliza um loop for com enumerate para percorrer a lista, obtendo o índice (i) e o valor da string (string) em cada iteração.
        if str == indice_minhas_frutas:
            return i # retorna o valor da lista onde a função foi chamada
        return -1 #se o valor da veriavel for diferete de -1

lista_frutas = ['banana', 'maçã', 'laranja', 'uva', 'abacaxi']
minhas_frutas = 'laranja'

indice = encontrar_indice(lista_frutas, minhas_frutas)

if indice != -1: #o elemento foi encontrado
  print(f"A fruta '{minhas_frutas}' foi encontrada no indice {indice}.")
else:
  print(f"A fruta '{minhas_frutas}' não foi encontrada na lista.")