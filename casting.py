def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = int(input("ingrese el precio:"))
    descuento = float(input("ingrese el descuento:"))
    cantidad = int(input("ingrese la cantidad:"))

    print (f"Precio: {precio}")
    print(f"Descuento: {descuento}")

    precio_con_descuento = precio - descuento
    print(f"Precio con descuento: {precio_con_descuento}")
    precio_total = precio_con_descuento * cantidad
    print (f"Total: {precio_total}")
