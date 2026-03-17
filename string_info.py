def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"

    print (palabra)
    print (len(palabra))
    print (palabra [0])
    print (palabra [-1])
    print (palabra * 3)
    print ("***" + palabra + "***")
