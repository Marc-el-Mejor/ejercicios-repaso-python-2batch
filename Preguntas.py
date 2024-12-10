from math import*
nombre=  input("Dime un nombre: ")
nombre_completo=  input("Dime un nombre completo: ")
nombre_completo= nombre_completo.replace(" ","")
pregunta1=sqrt(20)>5
pregunta2=4<sqrt(20)<5
pregunta3= pi*2*5>30
pregunta4= pi*2*0==0
pregunta5= 5<len(nombre)<10
pregunta6= 25<(len(nombre_completo))<35

print("¿Es la raíz cuadrada de 20 mayor que 5? "+ str(pregunta1))
print("¿Es la raíz cuadrada de 20 mayor que 5? "+ str(pregunta2))
print("¿Es la longitud de la circunferencia de una esfera de radio 5 mayor que 30? "+ str(pregunta3))
print("¿Es la longitud de la circunferencia de una esfera de radio 0 igual a 0? "+ str(pregunta4))
print("¿Tiene mi nombre más de 5 caracteres y menos de 10? "+ str(pregunta5))
print("¿Tiene mi nombre completo más de 25 caracteres y menos de 35? "+ str(pregunta6))
