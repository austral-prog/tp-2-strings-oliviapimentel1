def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = float(input("ingrese el precio:"))
    descuento = int(input("ingrese el descuento:"))
    cantidad = float(input("ingrese la cantidad:"))

    precio_con_descuento = ((precio - descuento) * cantidad)
    print (precio_con_descuento)
