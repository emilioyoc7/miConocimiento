"""precio = float(input("precio: "))
total = precio + (precio * 0.10)
print(total)

edad = int(input("edad: "))
print("tu edad es: ", edad)

edad2 = int(input("edad: "))
print("veamos si tu edad es 18..", edad2 == 18)


N = input("ingresa tu nombre: ")
print("ahora estas en la matrix", N)


cena = float(input("cuanto costo la cena? "))
servicio = cena * 0.062 
propina = cena * 0.10
print("total:", cena + servicio + propina)

k = float(input("cuantos kilometros recorres con 1 litro?"))
l = float(input("que capacidad tiene el tanque?"))
kr = float(input("cuantos kilometros recorreran?"))

kl = k * l
tn = kl % kr

print(tn)


capacidadm2 = 4
porcentajegradas = 0.2
porcentajesespeciales = 0.3
porcentajescomunes = 0.7

dimenciones = float(input("dimenciones del estadio (m2): "))
personasgradas = int(input("personas en las graadas: "))
porcentajesescenario = int(input("porcentaje escenario: "))

m2gradas = dimenciones * porcentajegradas
m2escenario = dimenciones * (porcentajesescenario / 100)
m2disponibles = dimenciones - m2gradas - m2escenario
personastotales = (m2disponibles * 4) + personasgradas

print("caben ", personastotales," personas")
"""





