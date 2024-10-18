a, b = 1, 1
soma = a + b  

for _ in range(18):  
    a, b = b, a + b  
    soma += b  

print("A soma dos 20 primeiros termos da série de Fibonacci é:", soma)
