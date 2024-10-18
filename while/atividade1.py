contIntervalo = 0
somaForaIntervalo = 0

num = int(input("Informe um número. Para sair informe 0 (zero): "))

while num != 0:
    if 10 <= num <= 50: 
        contIntervalo += 1 
    else:
        somaForaIntervalo += num 
    
    num = int(input("Informe um número. Para sair informe 0 (zero): "))

print(f"Quantidade de números entre 10 e 50: {contIntervalo}")
print(f"Soma dos números fora do intervalo: {somaForaIntervalo}")
