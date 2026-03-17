def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    gasto = float(input("ingrese su gasto\n"))
    print (gasto)

    dinero = int(input("ingrese su dinero\n"))
    print (dinero)

    vuelto = dinero - gasto

    pesos = int(vuelto)
    print (pesos)
    centavos = round(vuelto - pesos) * 100
    print (centavos)
