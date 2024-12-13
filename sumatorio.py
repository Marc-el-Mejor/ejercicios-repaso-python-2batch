numero=int(input("Dime un numero para el sumatorio: "))
i=1
sumatorio=0
cadena=""
while i<numero:
    sumatorio+=i
    cadena= cadena + str(i) + "+"
    i+=2
cadena= cadena.rstrip("+")
print("Sumatorio: " + cadena+"="+str(sumatorio))