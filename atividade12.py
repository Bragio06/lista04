jequitiba_altura = 1.50
jaqueira_altura = 1.10
jabuticabeira_altura = 2.98

jequitiba_crescimento = 1  
jaqueira_crescimento = 2    
jabuticabeira_crescimento = 0  

anos = 25

for ano in range(anos):
    jequitiba_altura += jequitiba_crescimento / 100  
    jaqueira_altura += jaqueira_crescimento / 100      
   


print(f"Altura do Jequitibá após {anos} anos: {jequitiba_altura:.2f} m")
print(f"Altura da Jaqueira após {anos} anos: {jaqueira_altura:.2f} m")
print(f"Altura da Jabuticabeira após {anos} anos: {jabuticabeira_altura:.2f} m")


if jequitiba_altura > jaqueira_altura and jequitiba_altura > jabuticabeira_altura:
    print("O Jequitibá terá a maior altura.")
elif jaqueira_altura > jequitiba_altura and jaqueira_altura > jabuticabeira_altura:
    print("A Jaqueira terá a maior altura.")
else:
    print("A Jabuticabeira terá a maior altura.")
