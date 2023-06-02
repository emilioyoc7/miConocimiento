"""
pares = 0
inpares = 0

num = int(input("ingresa un numero: "))

while num != 0 and num > 0:
    if num % 2 == 0:
        pares += 1
    else:
        inpares += 1 
    num = int(input("ingresa un numero: "))
print("numeros pares:", pares,"numeros inpares: ",inpares)

total = 0
num = float(input("precio de venta: "))

while num != 0:
    if num < 0:
        print("numero no valido!")
    else:
        total += num
    num = float(input("precio de venta: "))
if total > 1000:
    total -= total * 0.1
print("total a pagar:", total)


lineas_completas = 0
numero_cantidad = 0
libro = str(input("ingresa el nombre del libro: "))
while libro != "*":
    if libro == "/":
        lineas_completas += 1
        print(libro,"cantidas de numeros: ",numero_cantidad)
        numero_cantidad = 0
    else:
        for i in libro:
            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
                numero_cantidad += 1
     
    libro = str(input("ingresa el nombre del libro: "))
print("se leyeron ",lineas_completas)
""" 
        
        
"""
cantidad  = 0

n = int(input("numero: "))

while n != 0:
    primo = True
    for i in range(2,n):
        if n % 2 == 0:
            primo = False
            break
    if primo:
        cantidad += 1
    n = int(input("numero: "))
print("primos ", cantidad)
"""