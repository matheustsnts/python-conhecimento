# nome = 'Curso de Python'
# instrutor = 'Fábio'
# print(f"{nome} com {instrutor}")

#frase = 'Vamos aprender Python hoje.'
# palavras = frase.split()
# print(palavras[1])
# for palavra in palavras:
#   print(palavra)

# for letra in frase:
#   print(letra)
# print(frase[0:5])

# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' not in produtos)

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)

# objeto_celeste = 'galáxia esPIRAL M31'
# print(objeto_celeste.title())

# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco')
# print(suplemento)
# print(n_suplemento)

# frase = '     Ômega 3 é bom para a saúde!     '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.ljust(20,"-"))
# print(fruta.center(20,"-"))

# p = 'Bóson Treinamentos'
# print(p.startswith('B'))
# print(p.endswith('o'))

# Docstrings
texto = """
Docstring é uma espécie de documentação
que podemos inserir dentro de um módulo, função
ou classe no Python, entre outros locais.
   Respeita deslocamento do texto e é    multilinhas
"""

print(texto)
