contDiv10 = 0
contDiv5 = 0
contDiv2 = 0

num = int(input("Informe um número positivo. Para sair, informe um número negativo: "))

while num >= 0:
    if num % 10 == 0:
        contDiv10 += 1  
    if num % 5 == 0:
        contDiv5 += 1  
    if num % 2 == 0:
        contDiv2 += 1   
    
    num = int(input("Informe um número positivo. Para sair, informe um número negativo: "))

print(f"Números divisíveis por 10: {contDiv10}")
print(f"Números divisíveis por 5: {contDiv5}")
print(f"Números divisíveis por 2: {contDiv2}")

if contDiv10 == 0 and contDiv5 == 0 and contDiv2 == 0:
    print("Nenhum número é divisível por 10, 5 ou 2.")
