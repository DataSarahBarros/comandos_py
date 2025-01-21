# for = loop sequencial, repetindo ações em cada elemento

nota = []

for x in range(5):
    codigo_aluno = input('RM:')
    nota = float(input('Nota:'))
    resultado = [codigo_aluno, nota]
    nota.append(resultado)

print('quantidade de notas', len(nota))

# o x é uma variavel temporaria, a cada repetição ele muda, igual o indice da lista, então a primeira execução o x = 0 e assim por diante. Range(5) é uma função que exucuta cinco vezes = [0,1,2,3,4] = 5 vezes

#faz a lista em notas, a varivel n que percorre a lista notas contem uma lista onde a posição 0 é o código e a posição 1 é a nota
#ums lista, dentro de uma lista 

for n in nota:
    codigo_aluno =  n[0]
    nota = n[1]
    print('O RM', codigo_aluno, 'tirou a nota', nota)

# while = loop que executa ações enquato a condição for verdadeira

while True:
    print('se eu rodar script meu pc morre')


# lista de repeticoes

    notas = []

    contador = 1

    while contador <=5:
        codigo_aluno = input('RM:')
        nota = float(input('Notas:'))
        resultado = (codigo_aluno, nota)
        notas.append(resultado)

    # alternativa: contador += 1
        contador = contador + 1

    print('quantidade de notas', len(notas))