# Funções
# Modularização, Reúso do Código, Legibilidade

# def mensagem():
#   print('Bóson Treinamentos em Tecnologia')
#   print('Curso Completo de Python.')

# mensagem()

# Função com argumentos
# def soma(a,b):
#   print(a+b)

# soma(12,7)

# def mult(x, y):
#  return x * y

# a = 5
# b = 8
# c = mult(a, b)
# print(f"O produto de {a} e {b} é {c}.")

# def div(k,j):
#   if j != 0:
#      return k / j
#   else:
#      return 'Impossível dividir por zero!'

# if __name__ == '__main__':
#   a = int(input("Digite um número: "))
#   b = int(input("Digite outro número: "))

#   if b != 0:
#      r = div(a, b)
#      print(f"{a} dividido por {b} é igual à {r}.")
#   else:
#      print(div(a,b))

# def quadrado(val):
#   quadrados = []
#   for x in val:
#      quadrados.append(x ** 2)
#   return quadrados

# if __name__ == '__main__':
#   valores = [2,5,7,9,12]
#   resultados = quadrado(valores)

#   for g in resultados:
#      print(g)

# def contar(num=11, caractere='+'):
#   for i in range(1, num):
#      print(caractere)

# if __name__ == '__main__':
#   contar(num=8, caractere='@')


x = 5
y = 6
z = 3

def soma_mult(a, b, c = 0):
   if c == 0:
      return a * b
   else:
      return a + b + c


if __name__ == '__main__':
   res = soma_mult(x,y,z)
   print(res)
