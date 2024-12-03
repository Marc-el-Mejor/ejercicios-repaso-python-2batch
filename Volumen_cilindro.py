from math import*
radio=  float(input("Dime el radio: "))
altura= float(input("Dime la altura: "))
volumen= str(round(pi*(radio**2)*altura, 2))
print("El volumen del cilindro es: "+volumen)