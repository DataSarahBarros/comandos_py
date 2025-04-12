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


# exercícios
distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    print('Você irá pagar {} na passsagem.'.format(distancia * 0.50))
else:
    print('Você irá pagar {} em sua passagem.'.format(distancia * 0.45))


# exercícios
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')

# exercícios
a = float(input('Primeiro valor:'))
b = float(input('Segundo valor:'))
c = float(input('Terceiro valor:'))
# verificando os menores
if (a<b) and (a<c):
    menor = a
if (b<a) and (b<c):
    menor = b
if (c<b) and (c<a):
    menor = c
# verificando os maiores
if (a>b) and (a>c):
    maior = a
if (b>c) and (b>a):
    maior = b
if (c>a) and (c>b):
    maior = c
print('O menor valor foi {}'.format(menor))
print('O maior valor foi {}'.format(maior))


# exercícios
salario = float(input('Qual o sálario do funcionário?'))
if salario <=1.250:
    novo = salario * 0.15
else:
    novo = salario * 0.10
print('Quem ganhava R${:;2f} passa a ganhar R${.:2f} agora'.format(salario, novo))