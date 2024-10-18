print("Graus Fahrenheit\tGraus Celsius")
print("-----------------------------------")

for F in range(32, 213):  
    C = (5 / 9) * (F - 32)  
    print(f"{F}\t\t\t{C:.1f}")  
