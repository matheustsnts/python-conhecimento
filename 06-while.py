nome = None

while True:
    nome = input("Digite seu nome, ou x para parar: ")
    
    if (nome == 'x') or (nome == 'X'):
        break
    
    print(f"Bem-vindo, {nome}")
print('Até logo!')