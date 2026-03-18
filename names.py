def names():
    """Lee nombre y apellido e imprime formatos específicos."""
    # Dejamos los input vacíos para que el test no lea los mensajes como errores
    nombre = input()
    apellido = input()


    nombre_completo = nombre + " " + apellido


    print(nombre_completo.lower())
    print(nombre_completo.title())
    print(nombre_completo.upper())


    print(f"\t{nombre_completo.lower()}")
