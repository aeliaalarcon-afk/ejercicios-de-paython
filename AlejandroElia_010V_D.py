def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Asientos por ciudad de origen")
    print("2. Búsqueda de recorridos por rango de precio")
    print("3. Actualizar precio de recorrido")
    print("4. Agregar recorrido")
    print("5. Eliminar recorrido")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    """Lee y valida una opción entera entre 1 y 6."""
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def buscar_codigo(diccionario, codigo):
    """Retorna True si el código existe, sin distinguir mayúsculas/minúsculas."""
    codigo_buscado = codigo.strip().lower()
    for codigo_guardado in diccionario:
        if codigo_guardado.lower() == codigo_buscado:
            return True
    return False


def obtener_codigo_real(diccionario, codigo):
    """Retorna la clave real almacenada o None si no existe."""
    codigo_buscado = codigo.strip().lower()
    for codigo_guardado in diccionario:
        if codigo_guardado.lower() == codigo_buscado:
            return codigo_guardado
    return None


def asientos_origen(recorridos, venta, origen):
    """Muestra el total de asientos disponibles desde una ciudad de origen."""
    total_asientos = 0
    origen_buscado = origen.strip().lower()

    for codigo, datos_recorrido in recorridos.items():
        ciudad_origen = datos_recorrido[0]
        if ciudad_origen.lower() == origen_buscado:
            total_asientos += venta[codigo][1]

    print(f"El total de asientos disponibles es: {total_asientos}")


def busqueda_precio(recorridos, venta, p_min, p_max):
    """Muestra recorridos con precio en rango y al menos un asiento disponible."""
    encontrados = []

    for codigo, datos_venta in venta.items():
        precio = datos_venta[0]
        asientos = datos_venta[1]

        if p_min <= precio <= p_max and asientos > 0:
            origen = recorridos[codigo][0]
            destino = recorridos[codigo][1]
            encontrados.append(f"{origen}-{destino}--{codigo}")

    encontrados.sort()

    if len(encontrados) == 0:
        print("No hay recorridos en ese rango de precios.")
    else:
        print(f"Los recorridos encontrados son: {encontrados}")


def actualizar_precio(venta, codigo, nuevo_precio):
    """Actualiza el precio y retorna True; retorna False si el código no existe."""
    if not buscar_codigo(venta, codigo):
        return False

    codigo_real = obtener_codigo_real(venta, codigo)
    venta[codigo_real][0] = nuevo_precio
    return True


def validar_codigo(codigo, recorridos, venta):
    return (
        codigo.strip() != ""
        and not buscar_codigo(recorridos, codigo)
        and not buscar_codigo(venta, codigo)
    )


def validar_origen(origen):
    return origen.strip() != ""


def validar_destino(destino):
    return destino.strip() != ""


def validar_distancia(distancia):
    return isinstance(distancia, int) and not isinstance(distancia, bool) and distancia > 0


def validar_tipo_bus(tipo_bus):
    return tipo_bus in ("normal", "semi-cama", "cama")


def validar_servicio(servicio):
    return servicio in ("dia", "noche")


def validar_wifi(respuesta_wifi):
    return respuesta_wifi in ("s", "n")


def validar_precio(precio):
    return isinstance(precio, int) and not isinstance(precio, bool) and precio > 0


def validar_asientos(asientos):
    return isinstance(asientos, int) and not isinstance(asientos, bool) and asientos >= 0


def agregar_recorrido(
    recorridos,
    venta,
    codigo,
    origen,
    destino,
    distancia,
    tipo_bus,
    servicio,
    tiene_wifi,
    precio,
    asientos,
):
    """Agrega un recorrido en ambos diccionarios y retorna el resultado."""
    if not validar_codigo(codigo, recorridos, venta):
        return False

    codigo_normalizado = codigo.strip().upper()
    recorridos[codigo_normalizado] = [
        origen.strip(),
        destino.strip(),
        distancia,
        tipo_bus,
        servicio,
        tiene_wifi,
    ]
    venta[codigo_normalizado] = [precio, asientos]
    return True


def eliminar_recorrido(recorridos, venta, codigo):
    """Elimina el recorrido de ambos diccionarios y retorna el resultado."""
    if not buscar_codigo(venta, codigo):
        return False

    codigo_real = obtener_codigo_real(venta, codigo)
    del venta[codigo_real]

    if codigo_real in recorridos:
        del recorridos[codigo_real]

    return True


def main():
    # Los dos diccionarios se crean en el programa principal.
    recorridos = {
        "R001": ["Santiago", "Valparaíso", 120, "normal", "dia", True],
        "R002": ["Santiago", "Concepción", 500, "cama", "noche", True],
        "R003": ["La Serena", "Coquimbo", 15, "normal", "dia", False],
        "R004": ["Temuco", "Valdivia", 165, "semi-cama", "dia", True],
        "R005": ["Iquique", "Arica", 310, "cama", "noche", False],
        "R006": ["Santiago", "Rancagua", 90, "normal", "dia", True],
    }

    venta = {
        "R001": [7990, 20],
        "R002": [25990, 0],
        "R003": [1990, 35],
        "R004": [12990, 8],
        "R005": [18990, 3],
        "R006": [4990, 12],
    }

    ejecutando = True

    while ejecutando:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            origen = input("Ingrese ciudad de origen a consultar: ")
            if validar_origen(origen):
                asientos_origen(recorridos, venta, origen)
            else:
                print("La ciudad de origen no puede estar vacía")

        elif opcion == 2:
            datos_validos = False

            while not datos_validos:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))

                    if p_min < 0 or p_max < 0:
                        print("Los precios deben ser mayores o iguales a cero")
                    elif p_min > p_max:
                        print("El precio mínimo no puede ser mayor al precio máximo")
                    else:
                        datos_validos = True
                except ValueError:
                    print("Debe ingresar valores enteros")

            busqueda_precio(recorridos, venta, p_min, p_max)

        elif opcion == 3:
            continuar = "s"

            while continuar == "s":
                codigo = input("Ingrese código del recorrido: ")

                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))

                    if not validar_precio(nuevo_precio):
                        print("El nuevo precio debe ser un entero positivo")
                    else:
                        actualizado = actualizar_precio(venta, codigo, nuevo_precio)
                        if actualizado:
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                except ValueError:
                    print("El nuevo precio debe ser un entero positivo")

                continuar = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                while continuar not in ("s", "n"):
                    print("Debe responder s o n")
                    continuar = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()

        elif opcion == 4:
            codigo = input("Ingrese código del recorrido: ")
            origen = input("Ingrese origen: ")
            destino = input("Ingrese destino: ")
            distancia_texto = input("Ingrese distancia (km): ")
            tipo_bus = input("Ingrese tipo de bus (normal/semi-cama/cama): ").strip().lower()
            servicio = input("Ingrese servicio (dia/noche): ").strip().lower()
            respuesta_wifi = input("¿Tiene WiFi? (s/n): ").strip().lower()
            precio_texto = input("Ingrese precio: ")
            asientos_texto = input("Ingrese asientos: ")

            try:
                distancia = int(distancia_texto)
            except ValueError:
                distancia = None

            try:
                precio = int(precio_texto)
            except ValueError:
                precio = None

            try:
                asientos = int(asientos_texto)
            except ValueError:
                asientos = None

            errores = []

            if not validar_codigo(codigo, recorridos, venta):
                errores.append("Código inválido o ya existente")
            if not validar_origen(origen):
                errores.append("El origen no puede estar vacío")
            if not validar_destino(destino):
                errores.append("El destino no puede estar vacío")
            if not validar_distancia(distancia):
                errores.append("La distancia debe ser un entero mayor que cero")
            if not validar_tipo_bus(tipo_bus):
                errores.append("El tipo de bus debe ser normal, semi-cama o cama")
            if not validar_servicio(servicio):
                errores.append("El servicio debe ser dia o noche")
            if not validar_wifi(respuesta_wifi):
                errores.append("La respuesta de WiFi debe ser s o n")
            if not validar_precio(precio):
                errores.append("El precio debe ser un entero mayor que cero")
            if not validar_asientos(asientos):
                errores.append("Los asientos deben ser un entero mayor o igual a cero")

            if len(errores) > 0:
                for error in errores:
                    print(error)
                print("No se registró el recorrido")
            else:
                tiene_wifi = respuesta_wifi == "s"
                agregado = agregar_recorrido(
                    recorridos,
                    venta,
                    codigo,
                    origen,
                    destino,
                    distancia,
                    tipo_bus,
                    servicio,
                    tiene_wifi,
                    precio,
                    asientos,
                )

                if agregado:
                    print("Recorrido agregado")
                else:
                    print("El código ya existe")

        elif opcion == 5:
            codigo = input("Ingrese código del recorrido a eliminar: ")
            eliminado = eliminar_recorrido(recorridos, venta, codigo)

            if eliminado:
                print("Recorrido eliminado")
            else:
                print("El código no existe")

        elif opcion == 6:
            ejecutando = False
            print("Programa finalizado.")


if __name__ == "__main__":
    main()