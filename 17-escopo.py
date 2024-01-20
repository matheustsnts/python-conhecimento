# Escopo Global e Local

var_global = "Curso Completo de Python"

def escreve_texto():
   global var_global
   var_global = "Banco de Dados com SQL"
   var_local = "Fábio dos Reis"
   print(f'Variável Global {var_global}')
   
if __name__ == '__main__':
   print(f"Execução a função escreve_texto()")
   escreve_texto()

   print('Tentar acessar as variáveis diretamente')
   print(f"Variável Global: {var_global}")
#   print(f"Variável Local: {var_local}")
