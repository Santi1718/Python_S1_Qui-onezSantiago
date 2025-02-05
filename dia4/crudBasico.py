#Recorrer una lista
estudiantes = [
    "Adrián Quintero Pinzón",
    "Alejandra Pinzón Alvarez",
    "Ámbar Isabella Plata López",
    "Andrés David Reyes Espinel",
    "Aura Camila Pico Araque",
    "Camilo Andrés Suárez Fuentes",
    "Daniel Esteban Guerrero Quintero",
    "David Santiago Vera Mendez",
    "Edgar Leonardo Acevedo Arteaga",
    "Gerson Steven Chaparro Martínez",
    "Harley Yefrey Cabrales Vargas",
    "John Stiven Negron Regalado",
    "Juan David Saavedra Jaimez",
    "Juan David Santoyo Jaimes",
    "Juan David Vargas Soto",
    "Juan Eduardo Pinilla Guzmán",
    "Juan Fernando Umaña Barragan",
    "Juan Jose Abril Roman",
    "Maria Juliana Saavedra Mejia",
    "Mateo Roman Camargo",
    "Naya Zarela Lizcano Jaimes",
    "Nicolas Chedraui Mantilla",
    "Omar Fernando Granados Parra",
    "Santiago Aguilar Vesga",
    "Santiago Andrés Quiñonez Sosa",
    "Santiago Jaimes Perez",
    "Sara Sofía Díaz Rodríguez",
    "Sayara Yurley Aparicio Arciniegas",
    "Sergio Andrés Rueda Hernández",
    "Simón Dante Salamanca Galvis",
    "Thomas Sebastián Bastos Garcia",
    "Vladimir Diaz Contreras"
]

booleanito= True
while (booleanito==True):
    print("\nBienvenido al programa de lista de estudiantes")
    print("Que te gustaría hacer?")
    print("1.Agregar estudiante")
    print("2. Ver estudiantes")
    print("3.Editar estudiante")
    print("4.Eliminar estudiante")
    print("5.Salir del programa")
    opcionUsuario= int(input(":"))
    if(opcionUsuario==2):
        print("Lista estudiantes:")
        for i in range(len(estudiantes)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",estudiantes[i])
    elif(opcionUsuario==5):
        booleanito== False
        break
    elif(opcionUsuario==1):
        nombreEstudiante=input("Que nombre te gustaría agregarle al estudiante:")
        estudiantes.append(nombreEstudiante)
        print("Lista nueva de estudiantes:")
        for i in range(len(estudiantes)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",estudiantes[i])
    elif(opcionUsuario==3):
        print("Lista de estudiantes:")
        for i in range(len(estudiantes)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",estudiantes[i])
        numeroEstudiante=int(input("Cual estudiante quieres editar?:"))
        nombreEstudianteNuevo=input("Cual será el nombre nuevo del estudiante?:")
        estudiantes[numeroEstudiante-1]=nombreEstudianteNuevo
    elif(opcionUsuario==4):
        print("Lista de estudiantes:")
        for i in range(len(estudiantes)):##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
            print("Estudiante #",i+1,": ",estudiantes[i])
        numeroEstudiante=int(input("Cual estudiante quieres eliminar?:"))
        estudiantes.pop(numeroEstudiante-1)