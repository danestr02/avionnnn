import funcionessss as fun

asientos=[
    ['x','','','','',''],
    ['','','','','',''],
    ['','','','','',''],
    ['','','','','','']
]

opcion=0
opc=0
while opcion<5:
    fun.menuuu()
    opcion=fun.correcion("Ingrese una opción entre 1 y 4",opc,1,5)
    if opcion==1:
        lugar=1
        for fila in range(4):
            print('*', end=' ')
            for columna in range(6):
                if len(asientos[fila][columna])==0:
                    print(str(lugar).ljust(3), end='')
                else:
                    print(str(asientos[fila][columna]).ljust(3), end='')
                lugar+=1
            print()
    if opcion==2:
        compra=int(input("Ingrese el N° de asiento que quiere comprar:"))
        cont=0
        libre=False
        for fila in range(4):
            for columna in range(6):
                cont+=1
                if compra==cont:
                    if len(asientos[fila][columna])==0:
                        libre=True
                    break
            if libre:
                break
        if libre:
            print("Asiento Libre!")
        else:
            print("Asiento Ocupado :(")
        

    if opcion==5:
        print("Saliendo del sistema...")