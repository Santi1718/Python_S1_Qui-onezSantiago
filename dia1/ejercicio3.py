## Santiago Quiñonez 
##1097100310

## colocar expresion que muestre enteros positivos comenxzando desde el cero 
input ("Los numeros que satisfacen la expresion dada son:")
for i in range(0,200):
    for q in range(0,200):
        expresionMatematica = i**3+ q**4 -2* i**2
        if expresionMatematica < 680:
            input ("p", i)
            input ("q" , q)
            input("Sumatoria: ",expresionMatematica)