N = int(input("Informe o valor de N: "))
M = int(input("Informe o valor de M: "))

if N > M:
    print("Erro: N deve ser menor ou igual a M.")
else:
    print(f"Números pares entre, {N}, e, {M} :")
    for numero in range(N, M + 1):
        if numero % 2 == 0:
            print(numero) 