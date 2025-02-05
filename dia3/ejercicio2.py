def calcular_interes(capital, tasa, tiempo, capitalizacion_anual=1):
    
# Convertir la tasa de interés a decimal
    tasa_decimal = tasa / 100

    # Calcular el interés simple
    interes_simple = capital * tasa_decimal * tiempo

    # Calcular el interés compuesto
    interes_compuesto = capital * (1 + tasa_decimal / capitalizacion_anual) ** (capitalizacion_anual * tiempo) - capital

    return interes_simple, interes_compuesto


##1097100310
##Santiago Quiñonez