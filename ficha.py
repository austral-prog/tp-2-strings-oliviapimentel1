def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass

    nombre = input("ingrese su nombre:")
    email = input("ingrese su email:")
    nota1 = int(input("ingrese nota 1:"))
    nota2 = int(input("ingrese nota 2:"))
    nota3 = int(input("ingrese nota 3:"))

    print("=" * 24)
    print("""    FICHA DEL ALUMNO""")
    print("=" * 24)

    nombre_limpio = nombre.strip().title()
    print (f"Nombre: {nombre_limpio}")

    email_limpio = email.lower()
    print (f"Email: {email_limpio}")

    caracteres_nombre = len(nombre_limpio)
    print (f"Caracteres en nombre: {caracteres_nombre}")

    espacio = nombre_limpio.find(" ")
    iniciales = nombre_limpio[0] + nombre_limpio[espacio + 1]
    print (f"Iniciales: {iniciales}")

    nombre_parte = nombre_limpio[0:espacio].lower()
    apellido_parte = nombre_limpio[espacio + 1:].lower()
    usuario = apellido_parte + "." + nombre_parte
    print (f"Usuario: {usuario}")

    tiene_arroba = "@" in email
    print (f"Email valido: {tiene_arroba}")

    despues_del_arroba = email_limpio.find("@")
    dominio = email_limpio [despues_del_arroba + 1:]
    print (f"Dominio: {dominio}")


    nombre_de_archivo = nombre_limpio.replace(" ", "_")
    print (f"Nombre para archivo: {nombre_de_archivo}")

    cantidad_a = nombre_limpio.lower().count("a")
    print (f"Cantidad de a: {cantidad_a}")

    codigo_secreto = nombre_limpio.upper()[::-1]
    print (f"Codigo secreto: {codigo_secreto}")

    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    suma = nota1 + nota2 + nota3
    print (f"Suma: {suma}")
    promedio = (nota1 + nota2 + nota3) / 3
    print (f"Promedio: {promedio}")
    promedio_entero = (nota1 + nota2 + nota3) // 3
    print (f"Promedio entero: {promedio_entero}")

    print ("=" * 24)
