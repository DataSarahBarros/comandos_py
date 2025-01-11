soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print('soma', soma)
print('multiplicacao', multiplicacao)
print('divisao', divisao)
print('potencia', potencia)


# importando biblioteca e módulos

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
                                                # math.ceil(raiz) arredonda para cima
                                                # math.floor(raiz) arredonda para baixo
                                                # math.trunc(raiz) truncar a parte inteira
                                                
# sem importar todos os módulos da biblioteca

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)


import random
#num random.random
# método radom da classe random gera um número aleatório float entre 0 e 1
# num random.randint(1, 10) aqui ele vai da um número aleatório de um até 10 
print(num)

# funções trigonométricas usando math

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# funções trigonométricas usando math

import math
an = float(input('Digite um ângulo:'))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o seno {:.2f}'.format(an, seno))
print('O ângulo de {} tem o consseno {:.2f}'.format(an, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tangente))