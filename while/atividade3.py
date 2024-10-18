num = int(input("Informe um número positivo. Para sair informe 0 (zero): "))

while num != 0:
    
    if num > 0:
        
        if num % 13 == 2:
            print(num)  
    else:
        print("Por favor, informe apenas números positivos.")
    
    num = int(input("Informe um número positivo. Para sair informe 0 (zero): "))
