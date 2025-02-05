import re

def es_palindromo(cadena):
    # Eliminar puntuación y caracteres especialess
    cadena = re.sub(r'[^\w\s]', '', cadena)
    
    # Convertir a minúsculas
    cadena = cadena.lower()
    
    # Eliminar los espacios
    cadena = cadena.replace(' ', '')
    
    # Comprobar si es palíndromo
    return cadena == cadena[::-1]

