n=int(input("Ingrese el numero de empleados"))
horamayor=0
horamenor=0
tsueldobruto=0
teps=0
tpension=0
tsueldoneto=0
for i in range(1,n+1):
    nom=input("Ingrese el nombre del empleado ")
    hr=float(input("Ingrese las horas trabajadas para el empleado "))
    sueldobruto=hr*20000
    eps=sueldobruto*0.04
    pension=eps
    tsueldobruto=tsueldobruto+sueldobruto
    teps=teps+eps
    tpension=teps
    sueldoneto=sueldobruto-eps-pension
    tsueldoneto=tsueldoneto+sueldoneto
    print("El sueldo bruto del empleado ", i, " es de: ", sueldobruto)
    print("El descuento de pension es de: ", pension)
    print("El descuento de eps es de: ", eps)
    print("El sueldo neto del empleado es de: ", sueldoneto)
    if hr>horamayor:
        sueldobmayor=sueldobruto
        sueldonmayor=sueldoneto
        horamenor=horamayor
        horamayor=hr
    elif hr<=horamenor:
        sueldobmenor=sueldobruto
        sueldonmenor=sueldoneto
        horamenor=hr
print("el total del sueldo bruto es de: ", tsueldobruto)
print("el total de sueldo bruto es de: ", tsueldoneto)
print("el total del sueldo bruto es de: ", teps)
print("el total del sueldo bruto es de: ", tpension)

## Santiago Quiñonez 
## 1097100310