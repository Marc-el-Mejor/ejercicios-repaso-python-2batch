i=5
lista=[]

while i>0:
    try:
        numero=int(input("Dime un numero entero: "))
        lista.append(numero)
        i-=1
    except:
        print("No es un numero Gilipollas")

numero_mayor=0
for x in lista:
    if numero_mayor>=x:
        numero_mayor=numero_mayor
    else:
        numero_mayor=x
print("El numero mayor es: "+str(numero_mayor))
