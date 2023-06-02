def capicua(num):
    numero_str = str(num)
    numero_invertido = numero_str[::-1]
    return numero_str == numero_invertido

num1 = str(input("ingresa un numero: "))
if capicua(num1):
    print(f"{num1} es capicúa")
else:
    print(f"{num1} no es capicúa")