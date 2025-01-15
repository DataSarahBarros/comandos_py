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


# sem input 

#     def concesionaria (valor):

#     if valor >= 1000:
#         print('carro barato')
#     else:
#         print('carro caro')

# resultado = concesionaria(000)

# print(resultado)