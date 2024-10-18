N = int(input("Informe o valor de N: "))
M = int(input("Informe o valor de M: "))

if N >= M or N < 0 or M < 0:
    print("Erro: N deve ser menor que M e ambos devem ser não negativos.")
else:
    soma = 0  
    print(f"Números no intervalo entre, {N}, e, {M},que não são múltiplos de 3 nem de 7:")
    
    for numero in range(N, M + 1):
        if numero % 3 != 0 and numero % 7 != 0:
            print(numero)  
            soma += numero 
    print("Soma dos números:", soma)
