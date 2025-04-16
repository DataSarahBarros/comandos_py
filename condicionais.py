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

# def

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2)/2
print('A sua média foi {:.1f}'.format(media))
if media >=6.0:
    print('Você está acima da média, parabéns!')
else:
    print('Você está abaixo da média, estude mais!')


#desafio jogo

from random import randint
from time import sleep
computador = randint(0,5) #computador vai percorrer essa lista
print("-=-" * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
print('processando...')
sleep(2)
if jogador == computador:
    print('Parabéns você conseguiu me vencer')
else:
    print('eu pensei no número {} e não no {}'.format(computador, jogador))