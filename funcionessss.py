def correcion(texto,ingreso,numMin,numMax):
    while ingreso<numMin or ingreso>numMax:
        try:
            print(texto)
            ingreso=int(input("----> "))
            if ingreso<numMin or ingreso>numMax:
                print("Numero fuera de rango, reintente...")
        except:
            print("Debe ingresar un valor numerico, reintente...")
    return ingreso

def menuuu():
    print("*"*30)
    print("Bienvenido a la tienda!")
    print("*"*30)
    print('''Seleccione una opción:
        1.- Mostrar asientos
        2.- Comprar asientos
        3.- Cambiar asientos
        4.- Eliminar asientos
        5.- SALIR''')


'''def asientos(matriz):
    asiento=1
    for i in range(4):
        for e in range(6):
            
    return matriz'''

