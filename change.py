def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    gasto = float(input("ingresar gasto\n"))
    dinero = int(input("ingresar dinero\n"))

    vuelto = dinero - gasto

    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print(pesos)
    print (centavos)
