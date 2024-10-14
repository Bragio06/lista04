maior_altura = 0
menor_altura = float('inf')  
nome_menor_altura = ""
contador_feminino = 0

for i in range(20):
    nome = input(f"Informe o nome da {i + 1}ª pessoa: ")
    sexo = input("Informe o sexo (M/F): ").strip().upper()
    altura = float(input("Informe a altura (em metros): "))

    if altura > maior_altura:
        maior_altura = altura

    if sexo == 'F':
        contador_feminino += 1

    if altura < menor_altura:
        menor_altura = altura
        nome_menor_altura = nome

print("A maior altura é:", maior_altura)
print("Quantidade de pessoas do sexo feminino:", contador_feminino)
print("Nome da pessoa de menor altura:", nome_menor_altura)
