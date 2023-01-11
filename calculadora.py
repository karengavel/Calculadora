import sys
print("Bienvenido a la calucladora! podrás realizar las siguientes operaciones:")

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
        [ 6] - Exponente
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
        print("Raiz...")
    elif opcion == 6:
        print("Exponente...")
    elif opcion == 7:
        print("Coseno...")
    elif opcion == 8:
        print("Tangente...")  
    elif opcion == 9:
        print("Seno...") 
    elif opcion == 10:
        print("Adiós")
        sys.exit()
        finalizar_programa = True
    else:
        print("No tenemos esa opción vuelve a intentar.")

