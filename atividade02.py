contagem_intervalo = 0
soma_fora_intervalo = 0

for i in range(10):
    numero = float(input(f"Informe o {i + 1}º número: "))
    
    if 10 <= numero <= 50:
        contagem_intervalo += 1  
    else:
        soma_fora_intervalo += numero  

print(f"Quantidade de números entre 10 e 50: {contagem_intervalo}")
print(f"Soma dos números fora do intervalo: {soma_fora_intervalo}")
