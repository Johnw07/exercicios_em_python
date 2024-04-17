x = float(input("Escreva o salario:"))
print("salario antes do reajuste:",x ) 

if x <= 280 :
    x + x * 0.2 
    print("o reajuste aplicado foi:",x * 0.2)
    print("salario depois do reajuste:",x + x * 0.2)
    
elif x > 280 and x <= 700 :
    x + x * 0.15 
    print("o reajuste aplicado foi:",x * 0.15)
    print("salario depois do reajuste:",x + x * 0.15)
    
elif x > 700 and x <= 1500 :
    x + x * 0.1 
    print("o reajuste aplicado foi:",x * 0.1)
    print("salario depois do reajuste:",x + x * 0.1)
    
else :
    x + x * 0.05
    print("o reajuste aplicado foi:",x * 0.05)
    print("salario depois do reajuste:",x + x * 0.05)


