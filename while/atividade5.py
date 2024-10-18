soma_salarios = 0
cont_salarios = 0
maior_idade = 0
menor_idade = float('inf')
cont_mulheres = 0
menor_salario = float('inf')
menor_salario_idade = None
menor_salario_sexo = None

while True:
    idade = int(input("Informe a idade (digite um número negativo para encerrar): "))
    
    if idade < 0:
        break  
    
    sexo = input("Informe o sexo (M/F): ").strip().upper()
    
    salario = float(input("Informe o salário: "))
    
    
    soma_salarios += salario
    cont_salarios += 1
    
   
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    
    
    if sexo == 'F':
        cont_mulheres += 1
    
    
    if salario < menor_salario:
        menor_salario = salario
        menor_salario_idade = idade
        menor_salario_sexo = sexo


if cont_salarios > 0:
    media_salarios = soma_salarios / cont_salarios
    print(f"Média dos salários: {media_salarios:.2f}")
else:
    print("Nenhum salário foi informado.")

print(f"Maior idade do grupo: {maior_idade}")
print(f"Menor idade do grupo: {menor_idade}")
print(f"Quantidade de mulheres: {cont_mulheres}")

if menor_salario_idade is not None:
    print(f"Idade da pessoa com o menor salário: {menor_salario_idade}, Sexo: {menor_salario_sexo}")
else:
    print("Nenhuma pessoa foi cadastrada.")
