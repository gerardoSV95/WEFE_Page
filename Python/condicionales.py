#Ejercicio 1
""" n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))


if n1%2==0 and n2%2==0:
    print(n1, "y", n2, "son numeros pares")
elif n1%2!=0 and n2%2!=0:
    print(n1, "y", n2, "no son numeros pares")
elif  n1%2==0 and n2%2!=0:
    print(n1, "es par.")
else:
    print(n2, "es par")
 """
#Ejercicio 2
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

if num1>num2 and num1>num3:
    print(f"{num1} es mayor que {num2} y {num3}")
if num2>num1 and num2>num3:
    print(f"{num2} es mayor que {num1} y {num3}")
if num3>num1 and num3>num2:    
    print(f"{num3} es mayor que {num1} y {num2}")
