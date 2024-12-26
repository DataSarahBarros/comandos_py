#boolean retorna true or false
is_python = True
is_java = False

#boolean armazena condição

ingressos = 50
compradores = 250
tem_ingresso_suficiente = (ingressos >= compradores)
print(tem_ingresso_suficiente)

nome = 'sarah'
idade = 20
peso = 55.5

print(nome, idade, peso)

# 1 exemplo
usuário = input('Qual é o seu nome?')
print ('Olá usuário', usuário, 'Bem-vindo(a)!')

# 2 exemplo
usuário = input('Qual seu nome?')
print('Bem-Vindo(a) {}!'.format(usuário))

# 3 exemplo
dia = input ('Dia:')
mes = input ('Mês:')
ano = input ('Ano:')
print ('Você nasceu no dia',dia,'do',mes,'de',ano)