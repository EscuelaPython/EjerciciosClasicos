"""Ingresar 3 numeros enteros por teclado e imprimir
el mayor """

num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
num3=int(input("Ingrese otro numero: "))
mayor=0
if num1>num2:
    if num1>num3:
        mayor=num1

if num2>num1:
    if num2>num3:
        mayor=num2

if num3>num1:
    if num3>num2:
        mayor=num3

print("El mayor es: ",mayor)

