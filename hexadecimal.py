num=int(input("Dime un numero para convertirlo a sistema hexadecimal: "))
lista=[]
cociente=num
while cociente>0:
    resto= cociente%16
    cociente=cociente//16
    lista.append(resto)

for i in range(0,len(lista)):
    if lista[i]>=10:
        if lista[i]==10:
            lista[i]="A"
        elif lista[i]==11:
            lista[i]="B"
        elif lista[i]==12:
            lista[i]="C"
        elif lista[i]==13:
            lista[i]="D"
        elif lista[i]==14:
            lista[i]="E"
        elif lista[i]==15:
            lista[i]="F"


print(lista)