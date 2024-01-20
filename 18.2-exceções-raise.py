from math import sqrt

class NumeroNegativoError(Exception):
   def __init__(self):
      pass

if __name__ == '__main__':
   try:
      num = int(input("Digite um número positivo: "))
      if num < 0:
         raise NumeroNegativoError
   except NumeroNegativoError:
      print(f"Foi fornecido um número negativo!")
   else:
      print(f"A raiz quadrada de {num} é {round(sqrt(num),2)}")
   finally:
     print(f"Fim do Cálculo!")
