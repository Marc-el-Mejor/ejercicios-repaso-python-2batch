edad1=int(input("Dime la edad de persona 1 edad: "))
edad2=int(input("Dime la edad de persona 2 edad: "))
if edad2<0 or edad1<0:
    print("Una de las edades es negativa")
if edad1==edad2:
    print("Las dos personas tienen la misma edad")
elif edad1>edad2:
    print("La persona 1 tiene mas años que la persona 2")
else:
    print("La persona 2 tiene mas años que la persona 1")