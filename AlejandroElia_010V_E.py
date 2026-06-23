# --- FUNCIONES DE VALIDACIÓN ---
def validar_descripcion(desc):
    # Retorna True si tiene contenido (quitando espacios), False si está vacía
    return len(desc.strip()) > 0

def validar_prioridad(prio):
    # Verifica que sea un número y esté entre 1 y 10
    try:
        p = int(prio)
        return 1 <= p <= 10
    except ValueError:
        return False

def validar_tiempo(tiempo):
    # Verifica que sea un decimal mayor a 0
    try:
        t = float(tiempo)
        return t > 0
    except ValueError:
        return False


# --- FUNCIONES DEL MENÚ ---
def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL ==========")
    print("1. Agregar tarea")
    print("2. Buscar tarea")
    print("3. Eliminar tarea")
    print("4. Actualizar estado")
    print("5. Mostrar tareas")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if 1 <= opc <= 6:
                return opc
            else:
                print("Opción inválida. Ingrese un número entre 1 y 6.")
        except ValueError:
            print("Por favor, ingrese un número entero.")


# --- FUNCIONES DE OPERACIÓN ---
def agregar_tarea(tareas):
    desc = input("Ingrese la descripción de la tarea: ")
    prio = input("Ingrese la prioridad (1-10): ")
    tiempo = input("Ingrese el tiempo estimado (en horas): ")

    datos_validos = True
    
    # Se evalúa cada campo y se muestran los errores aquí, no en las funciones de validación
    if not validar_descripcion(desc):
        print("Error: La descripción no puede estar vacía ni ser solo espacios.")
        datos_validos = False
    
    if not validar_prioridad(prio):
        print("Error: La prioridad debe ser un número entero entre 1 y 10.")
        datos_validos = False
        
    if not validar_tiempo(tiempo):
        print("Error: El tiempo estimado debe ser un número decimal mayor que cero.")
        datos_validos = False
        
    # Solo si todo es correcto se crea el diccionario y se agrega
    if datos_validos:
        nueva_tarea = {
            "descripcion": desc,
            "prioridad": int(prio),
            "tiempo_estimado": float(tiempo),
            "completada": False
        }
        tareas.append(nueva_tarea)
        print("Tarea agregada correctamente.")

def buscar_tarea(tareas, desc_buscada):
    # Recorre la lista buscando la descripción exacta
    for i in range(len(tareas)):
        if tareas[i]["descripcion"] == desc_buscada:
            return i
    return -1

def actualizar_estado(tareas):
    # Actualiza el campo completada de cada tarea según su prioridad
    for tarea in tareas:
        if tarea["prioridad"] >= 5:
            tarea["completada"] = True
        else:
            tarea["completada"] = False


# --- BLOQUE PRINCIPAL ---
lista_tareas = []

while True:
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        agregar_tarea(lista_tareas)
        
    elif opcion == 2:
        desc = input("Ingrese la descripción a buscar: ")
        pos = buscar_tarea(lista_tareas, desc)
        if pos != -1:
            t = lista_tareas[pos]
            print(f"\nTarea encontrada (Posición {pos}):")
            print(f"Descripción: {t['descripcion']}")
            print(f"Prioridad: {t['prioridad']}")
            print(f"Tiempo estimado: {t['tiempo_estimado']} horas")
            print(f"Completada: {t['completada']}")
        else:
            print("No existe ningún registro con esa descripción.")
            
    elif opcion == 3:
        desc = input("Ingrese la descripción de la tarea a eliminar: ")
        pos = buscar_tarea(lista_tareas, desc)
        if pos != -1:
            lista_tareas.pop(pos)
            print("Tarea eliminada correctamente.")
        else:
            print(f"La tarea '{desc}' no se encuentra registrada.")
            
    elif opcion == 4:
        actualizar_estado(lista_tareas)
        print("El estado de las tareas ha sido actualizado según su prioridad.")
        
    elif opcion == 5:
        actualizar_estado(lista_tareas)
        if len(lista_tareas) == 0:
            print("No hay tareas registradas aún.")
        else:
            print("\n=== LISTA DE TAREAS ===")
            for t in lista_tareas:
                print(f"Descripción: {t['descripcion']}")
                print(f"Prioridad: {t['prioridad']}")
                print(f"Tiempo estimado: {t['tiempo_estimado']}")
                if t['completada']:
                    print("Estado: COMPLETADA")
                else:
                    print("Estado: PENDIENTE")
                print("-" * 25)
                
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break