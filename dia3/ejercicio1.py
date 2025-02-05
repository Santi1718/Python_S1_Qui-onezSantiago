def Celsius_Fahrenheit(C):
    F=(C* 9/5)+32
    return F
def Fahrenheit_Celsius(F):
    C=(F-32)* 5/9
    return C

print("opcion1. Celsius a Fahrenheit")
print("opcion2. Fahrenheit a Celsius")
n=str(input("Que funcion quieres usar? "))

if n=="1":
    C=float(input("Igresa los celsius que quieres convertir:"))
    print (Celsius_Fahrenheit(C))

if n=="2":
    F=float(input("Igrese Los Fahrenheit que quieres convertir: "))
    print(Fahrenheit_Celsius(F)) 