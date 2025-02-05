cantidadTerminos = int(input ("Ingrese N numero"))
if cantidadTerminos <= 0:
    print(0)
sumatoria = 0
for i in range(1,cantidadTerminos+1):
    if i % 2 == 0:
        sumatoria -= 1/i
    else:
        sumatoria += 1/i

print ("La sumatoria dio: ",sumatoria)

## 1097100310
## Santiago Quiñonez