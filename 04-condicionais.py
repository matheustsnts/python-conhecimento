# Simples, Composto, Encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

#Calcular a média aritmética das notas
media = (n1 + n2) / 2

if (media >= 7):
    print(f"Resultado Aprovado!")
    print(f"Parabéns!")
elif(media >= 5):
    print(f"Você está de recuperação!")
else:
    print(f"Aluno reprovado...")

print(f"Sua média é {media}")