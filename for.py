"""
total = 0

for x in range(0,101,3):
    total = total + x
print(total)

factorial = int(input("ingresa un numero: "))

f = 1

if factorial != 0:
    for i in range(1,factorial+1):
        f = f * i
print(f)

n1 = 0
n2 = 1
print(n1)
print(n2)

for i in range(8):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3


mensaje = str(input("msj oficial: "))
encriptacion = int(input("incriptacion: "))
abc = "abcdefghijklmnñopqrstuvwxyz"
encriptado = ""
for caracter in mensaje:
    if caracter.lower() in abc:
        indice = abc.find(caracter.lower())
        indice = (indice + encriptacion)% 27
        encriptado = encriptado + abc[indice]
    else:
        encriptado = encriptado + caracter
print("mensaje encriptado: ",encriptado)
"""
  