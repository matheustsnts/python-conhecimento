def mensagem():
    return "Programa funcional!!!"


def fibonacci(n):
    ultimo=1
    penultimo=1
    if (n == 0):
        return n
    elif (n==1) or (n==2):
        return 1
    else:
        count=3
        while count <= n:
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
        return termo

def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat *= i
        i += 1
    return fat
            
