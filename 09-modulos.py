import funcoes.md_funcional as mf

if __name__ == '__main__':
    print(mf.mensagem())
    num = int(input("Digite um valor inteiro positivo: "))
   
    print(f"\nCalcular fatorial do número: ")
    fat = mf.fatorial(num)
    print(f"O fatorial é {fat}")
    
    print(f"\nCalcular a sequência de Fibonacci: ")
    fib = mf.fibonacci(num)
    print(f"O fibonacci de {num} é {fib}")
