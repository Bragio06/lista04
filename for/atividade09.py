N = int(input("Informe um número inteiro e positivo (N): "))

if N <= 0:
    print("Erro: O número deve ser maior que 0.")
else:
    S = 0
    
    for n in range(1, N + 1):
        S += 1 / n  

    print(f"O valor de S é: {S}")
