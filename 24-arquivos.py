# Manipulação de arquivos de texto

# print(f"\Método read():\n")
# print(manipulador.readline())
# print(manipulador.readline())

# print(f"\nMétodo readlines():\n")
# print(manipulador.readlines())

# try:
#   manipulador = open('24-arquivo.txt', 'r', encoding='utf-8')
#   for linha in manipulador:
#      linha = linha.rstrip()
#      if texto in linha:
#         print(f"A string foi encontrada")
#         print(linha)
#      else:
#         print(f"String não encontrada!!!")
# except IOError:
#   print(f"Não foi possível abrir o arquivo.")
# else:
#   manipulador.close()

# Escrever arquivos de texto
# try:
#   manipulador = open('24-arquivos3.txt', 'w', encoding='utf-8')
#   manipulador.write("Boson Treinamentos\n")
#   manipulador.write("Como criar um arquivo de Texto com Python.")
# except IOError:
#   print(f"Não foi possível abrir o arquivo.")
# else:
#   manipulador.close()

# texto = '\nPython é usado em Ciência de Dados extensivamente'

# try:
#   manipulador = open('24-arquivo3.txt', 'a', encoding='utf-8')
   # manipulador.write("\nPython é muito empregado em IA.")
   # manipulador.write("\nInteligência artificial veio para ficar.")
#   manipulador.write(texto)
# except IOError:
#   print(f"Não foi possível abrir o arquivo.")
# else:
#   manipulador.close()

frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola' ]
try:
   manipulador = open('24-frutas.dat', 'w', encoding='utf-8')
   manipulador.writelines(frutas)
except IOError:
   print(f'Não foi possível abrir o arquivo.')
else:
   manipulador.close()

# Ler o arquivo criado
try:
   manipulador = open('frutas.dat','r', encoding='utf-8')
   print(manipulador.read())
except IOError:
   print(f'Não foi possível abrir o arquivo.')
else:
   manipulador.close()
