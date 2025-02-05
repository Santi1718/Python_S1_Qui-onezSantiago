def recomendar_comida(clima, hora):
    match clima.lower():
        case "soleado":
            comida_base = "pescadito"
        case "lluvioso":
            comida_base = "tinto"
        case "frío":
            comida_base = "chocolatico"
        case _:
            return "Clima no reconocido. Intente nuevamente."
    
    if hora.lower() == "mañana":
        comida = f"{comida_base} con jugo de sandia"
    elif hora.lower() == "tarde":
        comida = f"{comida_base} con galletas"
    elif hora.lower() == "noche":
        comida = f"{comida_base} con pancito"
    else:
        return "Hora no reconocida. Intente nuevamente."
    
    return f"Te recomiendo: {comida}."

## Santiago Quiñonez
## 1097100310