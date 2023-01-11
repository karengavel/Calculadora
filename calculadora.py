import sys
import math  
import numpy

print("Bienvenido a la calculadora! podrás realizar las siguientes operaciones:")

def menu(): 
 eleccion = 'x' 
 while not eleccion.isnumeric() or int(eleccion) not in range(1,11):
        print("Puedes elegir una de estas opciones:")
        print('''
        [ 1] - Sumar 
        [ 2] - Restar
        [ 3] - Multiplicar
        [ 4] - Dividir
        [ 5] - Raiz
        [ 6] - Potencia
        [ 7] - Coseno
        [ 8] - Tangente
        [ 9] - Seno
        [10] - Salir ''')
        eleccion = input()
 return int(eleccion)

def suma():
    print ("Haz elegido sumar! ")
    x = float(input("Ingresa el primer número a sumar: "))
    y = float(input("Ingresa el segundo número a sumar: "))
    print(F"La suma de los números es: {x+y} ")

def resta():
    print ("Haz elegido restar! ")
    x = float(input("Ingresa el primer número a restar: "))
    y = float(input("Ingresa el segundo número a restar: "))
    print(F"La suma de los números es: {x-y} ")

def multiplicacion():
    print ("Haz elegido multiplicar! ")
    x = float(input("Ingresa el primer número a multiplicar: "))
    y = float(input("Ingresa el segundo número a multiplicar: "))
    print(F"La suma de los números es: {x*y} ")

def division():
    print ("Haz elegido dividir! ")
    x = float(input("Ingresa el dividendo: "))
    y = float(input("Ingresa el divisor: "))
    print(F"La suma de los números es: {x/y} ")

def raiz():
    print ("Haz elegido raiz cuadrada! ")
    x = float(input("Ingresa el número a sacar raiz: "))
    print(F"La suma de los números es: {numpy.sqrt(x)} ")

def potencia():
    print ("Haz elegido Potencia! ")
    x = float(input("Ingresa el número a potenciar: "))
    y = float(input("Número a que potencia lo requieres: "))
    print(F"La potencia de {x} elevado a la {y} es: {numpy.power(x,y)} ")

def coseno():
    print ("Haz elegido coseno! ")
    x = float(input("Ingresa número: "))
    print(F"El coseno es: {math.cos(x)} ")

def tangente():
    print ("Haz elegido tangente! ")
    x = float(input("Ingresa número: "))
    print(F"La tangente es: {math.tan(x)}")

def seno():
    print ("Haz elegido seno! ")
    x = float(input("Ingresa número: "))
    print(F"La seno es: {math.sin(x)} ")

def funcionPrincipal():
 finalizar_programa = False
 while not finalizar_programa:
    opcion = menu()
    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    elif opcion == 5:
        raiz()
    elif opcion == 6:
        potencia()
    elif opcion == 7:
        coseno()
    elif opcion == 8:
        tangente() 
    elif opcion == 9:
        seno()
    elif opcion == 10:
        print("Adiós")
        sys.exit()
        finalizar_programa = True
    else:
        print("No tenemos esa opción vuelve a intentar.")

funcionPrincipal()

