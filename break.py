
anio1 = int(input("primer fecha: "))
anio2 = int(input("segunda fecha: "))

for i in range(anio1,anio2+1):
    if not i % 10 == 0:
        continue
    if not i % 4 == 0:
        continue
    if i % 100 != 0 or i % 400 == 0:
        print(i)
      
            







 
        



   