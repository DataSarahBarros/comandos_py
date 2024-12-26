# dicionarios usam chave e valor para armazenar informacoes

#1exemplo

varievel = {
    'chave': 'valor',
}

#2exemplo

pessoa = {
    'nome': 'programadora python',
    'idade': 20,
    'peso': 55.5
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])

#3exemplo

# informacoes do jogador
player = {
    'nome':'sarah',
    'level': 1,
    'hp': 100,
    'exp': 0,
    'dano': 5,
}

#lista de inimigos
npcs = {
    {'nome': 'monstro', 'dano': 2, 'hp': 50,'exp': 5},
    {'nome': 'monstrinho', 'dano': 5, 'hp': 150,'exp':15},
    {'nome': 'monstrao', 'dano': 7, 'hp': 20,'exp': 10},
}