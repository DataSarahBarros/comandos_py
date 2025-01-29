# Python comandos

‘mensagens em aspas simples’
todos os comandos, são funções e (funções ficam dentro de parênteses)

print(‘Olá Mundo!’) = Olá Mundo!
print(4 + 7) = 11
print (‘4’ + ’7’) = 47
print (4 / 4 )  = 1
print (‘olá’ , 5) = olá 5 -> aqui + não funciona 

# Comandos:
escreva / print
leia / input : armazena entrada de dados do usuário 
aspas simples (‘) e aspas duplas (“) é a mesma coisa
+ e , é a mesma coisa, mas situações  
type : pra saber o tipo da variável (float, string etc.)
for: loop que percorre sequencias, repetindo ações para cada elemento 
enquanto / while: loop que excuta ações enquanto a condição for verdadeira
def : definir uma função
true: verdadeiro 
append : anexar
for : para
in: em
while: enquanto 

# anotações

toda variável é um objeto
e toda variável recebe valor

nome (tipo string) = 'sarah'
idade (tipo n. inteiro) = 20
peso (tipo float n. decimal ) = 50.5

print ( nome, idade, peso )

input vem depois da variável:
nome = input(“Digite seu nome:”)

input sempre retorna tipo string (type str)

# tipos primitivos, quatro principais
*int - inteiro* = 7, -4, 0, 9875
*float -  real* = 7.0, 4.5, 0.076, -15.2
*bool - boleano/lógicos* = True, False
*str - carácteres/strings* = 'Hello', '7.0', ''
*f* - inserir valores de variáveis diretamente dentro de uma string. Indica que a string é uma f-string;. Exemplo:

varável = str (input('qualquer coisa:'))

# variáveis, objetos, atributos, métodos, funções, classes e instâncias

*varáveis* recebem valores.
*objetos* são entidade que possuem *atributos* (características) e *métodos* (ações).
*atributos* são definidos dentro de uma classe. A classe é como um molde para criar objetos.
*métodos* são *funções* associadas a *objetos* que definem o comportamento do *objeto*.
*funções* são blocos de códigos. Quebram um programa em partes menores e mais gerenciáveis, permitindo a reutilização de código.
*classe* são como molde para criar objetos.
*instância* é um objeto específico criado a partir de uma classe. É como se a classe fosse um molde e a instância fosse o objeto final produzido a partir desse molde.

# Relação entre os conceitos:

*Objetos* são instâncias de classes. Uma classe é como um molde para criar *objetos*.
*Métodos* são *funções* que pertencem a uma classe. Eles operam sobre os dados do *objeto*.
*Variáveis* podem armazenar referências a *objetos*.

# Manipulação de texto 

# Fatiar uma string
frase[9] = número do índice da str é 9
frase[9:13] = primeiro número do índice da str é 9 até o índice 12 *(A função range() gera uma sequência imutável de números inteiros. Por exemplo, range(5) gera os números 0, 1, 2, 3, 4.)*
frase[9:21] = primeiro número do índice da str é 9 até o índice 20 
frase[9:21:2] = primeiro número do índice da str é 9 até o índice 20 *'Vídeo Python'* pulando de dois em dois = **[v d o p t o]**
frase[:5] = começa do 0 e vai até 0 índice 4 = 5 caracteres = *Curso*
frase[15:] = começa do 15 e vai até o ultimo índice 20 = 6 caracteres = *Python*
frase[9::3] = primeiro número do índice da str é 9 até o ultimo índice que é 20 e vai pulando de três em três *vídeo python* = **[v o p h]**

# Análisar uma striing
len(frase) #len = comprimento: mostrar quantidade de caracteres = *21*
frase.count('o') #contar quantidades de 'o' na frase *'Curso em vídeo python'* resultado **[3]**
frase.count('o', 0, 13) # do indice 0 até o 12 contar quantidades de 'o' na frase *'Curso em víde'* resultado **[1]**
frase.find('deo') #find = encontrar : encontrou o 'deo' in frase. **[11]** deo começa no indice 11
frase.find('Android') encontrar 'Android' que é uma str false retorna: **[-1]**
'Curso' in frase = existe 'Curso' em frase **[True]**

# Transformação de str usando métodos
frase.replace('python','Android') #replace = trocar 'Python' por 'Android':
*'Curso em vídeo Python'* = **[Curso em vídeo Android]**
frase.upper() #upper = para cima ou seja, deixar tudo em maiúsculo:
*'Curso em vídeo python'* = **[CURSO EM VÍDEO PYTHON]**
frase.lower() #lower = inferior, deixar tudo minisculo:
*'Curso em vídeo python'* **[curso em vídeo python]**
frase.capitalize() #capitalize = capitar a primeira letra da primeira string em maiúsculo e o restante minúsculo:  
*'Curso em vídeo python'* **[Curso em vídeo python]**
frase.title(): title = título, faz toda palavra ter a primeira letra maiúscula: 
*'Curso Em vídeo python'* **[Curso Em Vídeo Python]**

frase.strip() = strip = tirar, tirar todos os espaços inúteis do início e fim
frase.rsatrip() = o *r* de right = direita, remover apenas os caracteres vazios da direita
frase.lsatrip() = o *l* de left = esquerda, remover apenas os caracteres vazios da esquerda

# Divisão 
frase.split() = split = dividir, dividir os espaços, cada palvra recebe indexação nova começando com 0 gerando uma lista de palavras *Curso [4 caracteres] em [1 caracter] vídeo [4 caracteres] python [5 caracteres]* sendo = **Curso [lista 1] em [lista 2] vídeo [lista 3] python [lista 4]**

# Junção

Quando se tem palavras separados em listas: **Curso [lista 1] em [lista 2] vídeo [lista 3] python [lista 4]** usa-se
'-'.join(frase) = juntar as listas com o caractere '-'  *Curso-Em-vídeo-python*

# Lógica de programação
*Ciclo de desenvolvimento:* Idealização, Especificação de requisitos, Validação de soluções, Desenvolvimentos e testes e Implementação e entrega.

*Algoritmos:* Algoritmo é uma série de instruções a serem seguidas, para resolver um problema.

*Método 50's para montar um algoritmo:*
Análise crítica do problema (tentar explicar o problema, pedindo mais informações e investigando, para compreender completamente o problema)

*Perguntas:* Quais são os dados de entrada necessários? O que devo fazer com estes dados? Quais são as restrições deste problema? Qual é o resultado esperado? Qual é a sequência de passos a ser feita para chegar ao resultado esperado?

*Conceitos obrigatórios para resolver problemas e criar algoritmos:*
    **variáveis, condicionais, repetições e listas:**
