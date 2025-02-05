def Fahrenheit_Celsius(F):
    C=(F-32)* 5/9
    return C
def Celsius_Fahrenheit(C):
    F=(C* 9/5)+32
    return F

print("opcion1. Fahrenheit a Celsius")
print("opcion2. Celsius a Farenheit")
n=str(input("Que funcion quieres usar? "))

if n=="1":
    c=float(input("ingresa los Fahrenheit a convertir:"))
    print(Fahrenheit_Celsius(F))

    if n=="2":
        F=float(input("ingrese los Celius a converir:"))
        print(Celsius_Fahrenheit(C))

        ## Santiago Quiñonez 
        ## 1097100310
