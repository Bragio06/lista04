N = int(input("Informe um número inteiro e positivo (N): "))

if N <= 0:
    print("Erro: O número deve ser maior que 0.")
else:
    print(f"Tabuada de {N}:")
    for i in range(11):
        resultado = N * i
        print(f"{N} x {i} = {resultado}")
