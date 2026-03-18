def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto_str = input("Ingresar gasto:")
    print (f"{gasto_str}+ \n 76")
    dinero_str = input("Ingresar dinero:")
    print(f"{dinero_str}+ \n 132")


    gasto = float(gasto_str)
    dinero = int(dinero_str)


    vuelto = dinero - gasto
    pesos = int(vuelto)


    centavos = int(round((vuelto - pesos) * 100))
