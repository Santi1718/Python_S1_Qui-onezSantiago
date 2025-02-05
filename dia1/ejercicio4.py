## Santiago Quiñonez


##colocar varibales 
mayorNum = 0
menorNum = 0
##se cra un ciclo para que repita 10 veces
for i in range(1,11):
    print("Ingrese el termino #", i)
    n = int(input())
    print(n)
    if (mayorNum == 0) or (menorNum == 0):
        mayorNum = n
        menorNum = n
    else:
        if (n>mayorNum):
            mayorNum = n
        else:
            if (n<menorNum):
                menorNum = n
print("El numero mayor es: ", mayorNum)
print("El numero menor es: ", menorNum)

## 1097100310
## Santiago Quiñonez