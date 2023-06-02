"""
numero = int(input("ingresa un numero: "))

if(numero >= 0):
    print("el valor absoluto de ", numero," es", numero)
else:
    numero = numero - numero - numero
    print(numero)

print("A por el partido rojo")
print("B por el partido verde")
print("C por el partido azul")
eleccion = str(input("has tu eleccion: "))

if eleccion.upper == "A":
    print("usted a votado por el partido rojo")
elif eleccion.upper == "B":
    print("usted a votado por el partido verde")
elif eleccion.upper == "C":
    print("usted a votado por el partido azul")
else:
    print("opcion erronea")


letra = str(input("ingresa una letra: "))


if letra == letra[0] and letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("es vocal")
else:
    print("no se puede processar este dato")


anio = int(input("año: "))

if anio % 4 != 0:
    print("no es bisiesto")
else:
    if anio % 100 != 0 or anio % 400 == 0:
        print("es bisiesto")
    else:
        print("no es bisiesto")
"""

dia = str(input("introduce el dia de la semana: "))
DD = int(input("introduce DD: "))
MM = int(input("introduce MM: "))



if dia.lower == "lunes" or dia.lower == "martes" or dia.lower == "miercoles" or dia.lower == "jueves" or dia.lower == "viernes" and DD > 31 and MM > 12:
    print("se produjo un error ")
else:
    if dia == "lunes" or dia == "martes" or dia == "miercoles":
        aprovados = int(input("cuantos aprovaron en el examen? "))
        reprovados = int(input("cuantos reprovaron en el examen? "))
        porcentaje_aprovados = aprovados / reprovados * 100
        print("aprovo el ",porcentaje_aprovados,"%")
    elif dia == "viernes" and DD == 1 and MM == 1 or MM == 7:
        print("comienzo de nuevo ciclo")
        nuevos_alumnos = int(input("cuantos nuevos alumnos ingresaran? "))
        cobro_alumno = float(input("cobro por cada alumno? "))
        print("total: ",nuevos_alumnos * cobro_alumno)
    else:
        alumnos_presentes = int(input("que porcentaje de alumnos asistio este dia? "))
        if alumnos_presentes < 50 :
            print("no asistio la mayoria")
        else:
            print("asistio la mayoria")


