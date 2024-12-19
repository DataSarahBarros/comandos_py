import os
mensagens = []
nome = input('nome:')

while True:
    os.system('clear')

    if len(mensagens) > 0:
        for n in mensagens:
            print(n['nome'], "-", n['texto'])

print('________________')

# obtendo texto
texto = input('mensagem:')
if texto == 'fim':
    breakpoint

# adicionando mensagem na lista
mensagens.append({
    'nome': nome,
    'texto': texto
})