#1text

valor1 = 10
valor2 = 50

# if / se
if valor1 > valor2:
    print(valor1, 'é maior que', valor2)
# else / se não
else:
    print(valor2, 'é maior que', valor1)
# elif / ou então

#2test

idade = int( input('informe a sua idade:'))

if idade >= 18:
    print('entrada liberada')
else:
    print('entrada bloqueada')

#3test

salario = float(input("informe o salário:"))
if salario <= 3000:
    print('dev junior')
elif salario > 3000 and salario <= 6000:
    print('dev pleno')
elif salario > 6000 and salario <= 15000:
    print('dev senior')
else:
    print('project manager')


# funcoes e condicoes juntos sem input

    def concesionaria (valor):

        if valor >= 1000:
            print('carro barato')
        else:
            print('carro caro')

    resultado = concesionaria(000)

    print(resultado)


from random import randint #biblioteca random gera números pseudoaleatórios e o metodo randint gera números inteiros aleatórios
from time import sleep #biblioteca time fornce funções relacionadas ao tempo e o método sleep pausa a excuçãoo do programa por um determinado número de segundos
computador = randint(0,5) #computador vai percorrer essa lista
print("-=-" * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...') #vai sortear um número
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) #jogador vai adivinhar
print('Pensando...')
sleep(3)
if jogador == computador:
    print('Parabéns você conseguiu me vencer')
else:
    print('eu pensei no número {} e não no {}'.format(computador, jogador))


# condição simples

velocidade = float(input('Qual a velocidade?'))
if velocidade > 80:
    print('Multado você excedeu o limite de velocidade')
    multa = (velocidade - 80) * 7
    print('Você deve pagar um multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')


# exercícios

n = int(input('Digite um número qualquer:'))
resultado = n % 2
if resultado == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))