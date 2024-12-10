nota1=float(input("Dime la nota del primer examen: "))
nota2=float(input("Dime la nota del segundo examen: "))
nota3=float(input("Dime la nota del tercer examen: "))
nota_media= (nota1+nota2+nota3)/3
if nota1<0 or nota2<0 or nota3<0:
    print("Una de las notas es negativa")
if nota1<3 or nota2<3 or nota3<3:
    print("Ha suspendido")
elif nota_media>=5:
    print("Ha aprobado")
else:
    print("Ha suspendido")