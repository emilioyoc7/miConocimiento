"""
dni = int(input("DNI: "))

def check_dni(dnii):
    dnii = str(dnii)
    dnii = len(dnii)
    if dnii == 7 or dnii == 9:
        return True
    else:
        return False

if check_dni(dni) == True:
    print("es correcto")
else:
    print("incorrecto")


def palabra(cadena):
    longitud = len(cadena)
    if longitud == 0:
        return 0
    cantidad = 0
    for i in range(longitud):
        if cadena[i] != " ":
            cantidad += 1
        else:
            if cadena[i] == " " and i < (longitud-1) and candena[i] != " ":
                cantidad = 0
    return cantidad

frase = str(input("frase: "))

print(palabra(frase))
"""

nombre = str(input("ingresa tu nombre completo: "))

apellido = str(input("ingresa solo un apellido: "))

cantidad = 0
nombre1 = ""
def validar_nombre(n,n2):
    for i in n:
        if i != " ":
           n2 = n2 + i
        else:
            break
    return n2

primer_nombre = validar_nombre(nombre,nombre1)

def validar_apellido(a):
    for i in a:
        if i == " ":
            return False
            break
    return True
    
if validar_apellido(apellido) == False:
    print("error al ingresar el apellido")

def cantidad_apellido(apellido):
    apellido = len(apellido)
    return apellido

apellido_cantidad = cantidad_apellido(apellido)


dni = int(input("ingresa tu dni: "))

def validar_dni(d):
    d = str(d)
    dnii = len(d)
    if dnii == 7 or dnii == 8:
        return True
    else:
        return False

def tres_d_dni(d2):
    dnii2 = d2 // 10000
    return dnii2

digitos = tres_d_dni(dni)
    
def union(nombre,apellido,digitos):
    digitos = str(digitos)
    apellido = str(apellido)
    unidos = nombre + apellido + digitos
    return unidos




if validar_apellido(apellido) == True:
    print(nombre,apellido)
if validar_dni(dni) == True:
    print(dni)
print(union(primer_nombre,apellido_cantidad,digitos))
