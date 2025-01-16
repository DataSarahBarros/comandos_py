def minha_funcao(valor1, valor2):
    return valor1 + valor2

resposta = minha_funcao(10,10)

print('resposta', resposta)

#exemplo com repeticoes

def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input('Valor1:'))
    valor2 = int(input('Valor2:'))
    
    resposta = minha_funcao(valor1, valor2)
    print(valor1, '+', valor2, '=', resposta)

# funcoes e condicoes juntos sem input

    def concesionaria (valor):

        if valor >= 1000:
            print('carro barato')
        else:
            print('carro caro')

    resultado = concesionaria(000)

    print(resultado)

#exemplo sem repeticoes

    valor1 = int(input('Digite um valor:'))
    valor2 = int(input('Digite outro valor:'))
    resposta = valor1 + valor2
# print('a soma entre', valor1, 'e', valor2, 'vale', resposta)
    print('A soma entre {} e {} vale {}'.format(valor1, valor2, resposta))


# ver o tipo (type) do valor que for inserido (input)
    valor = (input('Digite algo:'))
    print(type(valor))

# métodos de teste de tipo
    valor = (input('Digite algo:'))
    print('O tipo primitivo desse valor é', type(valor))
    print('Só tem espacos?', valor.isspace())
    print('É um número?', valor.isnumeric())
    print('É alabétivo?', valor.isalpha())
    print('É alfanumérico?', valor.isalnum())
    print('Está em maiúscula?', valor.isupper())
    print('Está em minúscula?', valor.islower())

# operadores aritméticos
    valor1 = int(input('Inserir valor:'))
    valor2 = int(input('Inserir outro valor:'))
    s= valor1 + valor2
    m = valor1 * valor2
    d = valor1 / valor2
    di = valor1 // valor2
    e = valor1 ** valor2
    print('A soma {}, o produto é {} e a divisão é {}'.format(s,m,d))
    print('Divisão inteora {} e a potência {}'.format(di,e))