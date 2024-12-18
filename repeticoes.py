# executar um bloco de instruções repetidamente
# for = loop sequencial, repetindo ações em cada elemento
# while = loop que executa ações enquato a condição for verdadeira

for x in range(10):
    print(x)

while True:
    print('se eu rodas o script meu pc morre')

# test loop
nota = []

for x in range(300):
    codigo_aluno = input('RM:')
    nota = float(input('Nota:'))
    resultado = [codigo_aluno, nota]
    nota.append(resultado)

# for x in range (5) 
# o x é uma variavel temporaria, a cada repetição ele muda, igual o indice da lista, então a primeira execução o x = 0 e assim por diante. Range(5) = [0,1,2,3,4] = 5 vezes
