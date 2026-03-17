def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input("escriba su nombre")
    apellido = input("escriba su apellido")
    nombre_completo = nombre + apellido
    print (nombre_completo.lower())
    print (nombre_completo.upper())
    print (nombre_completo.title())
