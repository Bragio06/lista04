import math

N = int(input("Informe um número inteiro e positivo (N): "))
M = int(input("Informe um número inteiro e positivo (M): "))

if N < 0 or M < 0:
    print("Erro: Ambos os números devem ser positivos.")
else:
    fatorial_N = math.factorial(N)
    fatorial_M = math.factorial(M)

    soma_fatoriais = fatorial_N + fatorial_M

    print(f"A soma do fatorial de N e M é: {soma_fatoriais}")
