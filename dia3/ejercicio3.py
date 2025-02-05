import math
def clasificar_numero(n):
    if n < 0:
        return "El numero debe ser no negativo"
    
    par_impar="par"if n % 2 == 0 else "impar"

    if n < 2:
        tipo="No es primo ni compuesto"
    else:
        for i in range(2,int(math.sqrt(n))):
            if n % i == 0:
                tipo = "Compuestoo"
                break
        else:
            tipo = "Primo"
    raiz = int(math.sqrt(n))
    cuadrado_perfecto = "Es un cuadrado perfecto" if raiz * raiz == n else "no es un cuadrado perfecto"
    return f"El numero {n} es {par_impar},{tipo} y {cuadrado_perfecto}"     


numero=int(input("Escribe un numero"))
resultado= clasificar_numero(numero)
print(resultado)

##Santiago QUiñonez
##109710310
