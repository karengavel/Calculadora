import sys
print("Bienvenido a la calucladora! podrás realizar las siguientes operaciones:")

def menu(): 
 eleccion = 'x' 
 while not eleccion.isnumeric() or int(eleccion) not in range(1,9):
        print("Puedes elegir una de estas opciones:")
        print('''
        [1] - Sumar 
        [2] - Restar
        [3] - Multiplicar
        [4] - Dividir
        [5] - Coseno
        [6] - Tangente
        [7] - Seno
        [8] - Salir ''')
        eleccion = input()
 return int(eleccion)

 
finalizar_programa = False
while not finalizar_programa:
    opcion = menu()
    if opcion == 1:
        print("Sumando...")
    elif opcion == 2:
        print("Restando...")
    elif opcion == 3:
        print("Multiplicando...")
    elif opcion == 4:
        print("Dividiendo...")
    elif opcion == 5:
        print("Coseno...")
    elif opcion == 6:
        print("Tangente...")  
    elif opcion == 7:
        print("Seno...") 
    elif opcion == 8:
        print("Adiós")
        sys.exit()
        finalizar_programa = True
    else:
        print("No tenemos esa opción vuelve a intentar.")
