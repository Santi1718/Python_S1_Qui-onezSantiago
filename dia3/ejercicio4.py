import random
import string

def generar_contrasena(longitud, exclusiones=None, minimos=None):
   

    # Definir los conjuntos de caracteres
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Aplicar exclusiones
    if exclusiones:
        letras_mayusculas = "".join([c for c in letras_mayusculas if c not in exclusiones])
        letras_minusculas = "".join([c for c in letras_minusculas if c not in exclusiones])
        numeros = "".join([c for c in numeros if c not in exclusiones])
        simbolos = "".join([c for c in simbolos if c not in exclusiones])

    # Definir la contraseña para usuario
    contrasena = []

    # Aplicar requisitos mn
    if minimos:
        for tipo, minimo in minimos.items():
            if tipo == "letras_mayusculas":
                contrasena.extend(random.choices(letras_mayusculas, k=minimo))
            elif tipo == "letras_minusculas":
                contrasena.extend(random.choices(letras_minusculas, k=minimo))
            elif tipo == "numeros":
                contrasena.extend(random.choices(numeros, k=minimo))
            elif tipo == "simbolos":
                contrasena.extend(random.choices(simbolos, k=minimo))

    # autocompletar contraseña con caracteres aleatorioss
    while len(contrasena) < longitud:
        tipo = random.choice(["letras_mayusculas", "letras_minusculas", "numeros", "simbolos"])
        if tipo == "letras_mayusculas":
            contrasena.append(random.choice(letras_mayusculas))
        elif tipo == "letras_minusculas":
            contrasena.append(random.choice(letras_minusculas))
        elif tipo == "numeros":
            contrasena.append(random.choice(numeros))
        elif tipo == "simbolos":
            contrasena.append(random.choice(simbolos))

    # Mezclar contraseña
    random.shuffle(contrasena)

    # Devolver contraseña
    return "".join(contrasena)

    ## Santiago Quiñonez
    ##1097100310
    