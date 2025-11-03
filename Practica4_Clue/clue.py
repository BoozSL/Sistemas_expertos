import random

# ===============================
# DATOS DEL JUEGO
# ===============================

personajes = [
    "Lady Sol Worthington – Filántropa y coleccionista de arte.",
    "Profesor Percy Blackwood – Historiador y experto en arte antiguo.",
    "Señorita Trey Carmichael – Estilista de celebridades y experta en moda.",
    "Coronel Fours Thorne – Militar retirado y apasionado por las armas antiguas.",
    "Sacerdote Vance Hawthorne – St."
]

habitaciones = [
    "El Comedor",
    "La Sala de Música",
    "Biblioteca",
    "El Invernadero",
    "El Estudio Privado"
]

habitaciones_descripcion = {
    "Biblioteca": "Al entrar en la biblioteca, notaste como las paredes estaban cubiertas por estanterías repletas de libros antiguos, cuyos lomos gastados contaban siglos de conocimiento. En el centro, un escritorio de caoba robusto reflejaba la luz tenue de una lámpara de araña, evocando la atmósfera de antiguos estudios y sabias lecturas.",
    "La Sala de Música": "Llegaste a la sala de música. Allí brillaba un piano de cola negro, cuyas teclas parecían haber cantado melodías olvidadas. En las paredes, violines colgados y partituras dispersas indicaban que el arte siempre había llenado este espacio con armonías y creatividad, y en la esquina había una colección de vinilos y su tocadiscos que parecía recién usado.",
    "El Invernadero": "Al abrir las puertas del invernadero, fuiste recibido por un aire fresco y fragante. Plantas exóticas con hojas brillantes y flores extrañas crecían por doquier, mientras un pequeño estanque con peces multicolores añadía movimiento y vida al ambiente. Todo parecía un refugio secreto de naturaleza dentro de la mansión.",
    "El Comedor": "En el comedor, una larga mesa esperaba ceremonias y reuniones con su vajilla de porcelana fina cuidadosamente colocada. Candelabros dorados iluminaban las copas y platos, aun con los elegantes alimentos dispuestos a ser consumidos.",
    "El Estudio Privado": "Entraste al estudio privado, un lugar de concentración y misterio. Sobre el escritorio desordenado se amontonaban papeles y documentos, mientras mapas antiguos decoraban las paredes. Un reloj antiguo marcaba el paso del tiempo, recordando que en aquel espacio se habían tomado decisiones cruciales para la familia."
}

armas = [
    "Candelabro de bronce",
    "Sable antiguo",
    "Cuerda de piano",
    "Revolver de colección",
    "Palo de Polo"
]

# ===============================
# CONFIGURACIÓN DEL TABLERO
# ===============================

tablero = []
for i, hab in enumerate(habitaciones):
    tablero.append(hab)
    if i < len(habitaciones) - 1:
        tablero.append("pasillo")

# ===============================
# FUNCIONES DE CONFIGURACIÓN
# ===============================

def barajar_cartas():
    random.shuffle(personajes)
    random.shuffle(habitaciones)
    random.shuffle(armas)

    # Seleccionamos la combinación secreta
    respuesta = {
        "personaje": personajes.pop(),
        "arma": armas.pop(),
        "lugar": habitaciones.pop()
    }

    # Asignamos armas a habitaciones (una por cada una)
    habitaciones_con_armas = {}
    armas_disponibles = armas.copy()
    habitaciones_con_armas[respuesta["lugar"]] = respuesta["arma"]
    restantes = [h for h in habitaciones if h != respuesta["lugar"]]
    random.shuffle(restantes)
    random.shuffle(armas_disponibles)

    for hab, arma in zip(restantes, armas_disponibles):
        habitaciones_con_armas[hab] = arma

    # Mezclamos las cartas restantes para repartir
    cartas_restantes = personajes + armas + habitaciones
    random.shuffle(cartas_restantes)

    npcs = {
        "Lady 1": [],
        "Profesor 2": [],
        "Miss 3": [],
        "Coronel 4": [],
        "St. 5": []
    }

    i = 0
    for carta in cartas_restantes:
        npc_nombre = list(npcs.keys())[i % len(npcs)]
        npcs[npc_nombre].append(carta)
        i += 1

    npc_ubicaciones = {}
    for npc in npcs:
        npc_ubicaciones[npc] = random.choice(habitaciones)

    return respuesta, npcs, npc_ubicaciones, habitaciones_con_armas

# ===============================
# FUNCIONES DE APOYO
# ===============================

def obtener_habitacion(pos):
    if 0 <= pos < len(tablero):
        return tablero[pos]
    return None

def mostrar_en_cuarto(npc_ubicaciones, lugar):
    if lugar == "pasillo":
        print("Estás en un pasillo, no hay nadie más aquí.")
        return []

    presentes = [npc for npc, hab in npc_ubicaciones.items() if hab == lugar]
    if presentes:
        print(f"En {lugar} están: {', '.join(presentes)}")
    else:
        print(f"Estás solo en {lugar}.")
    return presentes

def mostrar_armas_en_habitacion(habitaciones_con_armas, lugar):
    if lugar in habitaciones_con_armas:
        arma = habitaciones_con_armas[lugar]
        print(f"En {lugar} puedes ver el arma: {arma}")
    else:
        print(f"No hay armas visibles en {lugar}.")

def mostrar_descripcion_habitacion(lugar):
    if lugar in habitaciones_descripcion:
        print("\n" + habitaciones_descripcion[lugar] + "\n")

def preguntar_a_npc(npcs, npc_nombre, carta):
    if carta in npcs[npc_nombre]:
        print(f"{npc_nombre} confirma que tiene la carta '{carta}'.")
    else:
        print(f"{npc_nombre} no tiene la carta '{carta}'.")

def menu_numerico(opciones, mensaje="Selecciona una opción: "):
    for i, op in enumerate(opciones, 1):
        print(f"{i}. {op}")
    while True:
        try:
            eleccion = int(input(mensaje))
            if 1 <= eleccion <= len(opciones):
                return eleccion
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Ingresa un número válido.")

def mostrar_mapa(tablero, posicion):
    print("\nMAPA DEL TABLERO:")
    mapa = ""
    for i, lugar in enumerate(tablero):
        if i == posicion:
            mapa += f"[->{lugar}<-] "
        else:
            mapa += f"[{lugar}] "
    print(mapa + "\n")

def mostrar_final(respuesta):
    personaje = respuesta["personaje"]
    if "Lady Sol" in personaje:
        print("\nFinalmente, Lady Sol fue confrontada. Ante las pruebas inevitables, su expresión cambió de arrogancia a resignación, y confesó que, temerosa de perderlo todo y alimentada por años de resentimiento, había envenenado al conde.")
    elif "Profesor Percy" in personaje:
        print("\nLa investigación reveló secretos ocultos y viejas rencillas. Al final, fue el Profesor Percy Blackwood quien confesó, agobiado por los celos y la ambición.")
    elif "Trey" in personaje:
        print("\nTras interrogar a todos, las pistas señalaron hacia Trey Carmichael. Su ambición escondía motivos ocultos y tomó la fatal decisión que terminó con la vida del conde.")
    elif "Coronel" in personaje:
        print("\nPronto, la verdad emergió: el Coronel Fours Thorne, marcado por un rencor antiguo y conflictos no resueltos, fue el culpable.")
    elif "Hawthorne" in personaje:
        print("\nPero pronto, el sacerdote Vance Hawthorne fue confrontado, presionado por la evidencia y la mirada justa de sus antiguos amigos, confesó haber asesinado al conde.")
    print("\nFin del juego.\n")

# ===============================
# JUEGO PRINCIPAL
# ===============================

def jugar():
    print("La fiesta del Conde Sexton de Borbón\n")
    print("Era una noche especial en la imponente mansión del conde Sexton de Borbón. Celebraba sus 50 años, un hito que no siempre se tiene el lujo de alcanzar. En su residencia, un laberinto de estancias elegantes, invitó solo a sus más allegados: figuras destacadas tanto de la alta sociedad como de su círculo íntimo.")
    print("Lady Sol Worthington, refinada y aventurera; el Profesor Percy Blackwood, viejo amigo y rival silencioso; la joven diseñadora Trey Carmichael; el Coronel Fours Thorne, camarada marcado por un pasado de silencios incómodos; y el Sacerdote Vance Hawthorne, influyente en la fortuna del conde.")
    print("La fiesta comenzó en la biblioteca, donde libros antiguos cubrían las paredes. El piano de cola llamaba en la sala de música y las flores exóticas del invernadero llenaban la casa de un aroma peculiar. Sin embargo, bajo el brillo de los candelabros y la porcelana fina del comedor, una tensión creciente se palpaba en el aire.")
    print("Pero la noche tomó un giro inesperado cuando el conde fue encontrado sin vida en los pasillos.\n")

    respuesta, npcs, npc_ubicaciones, habitaciones_con_armas = barajar_cartas()
    posicion = 0  # Comienza en el comedor
    turnos = 30  # Aumentado a 30

    lugar_actual = tablero[posicion]
    print(f"Comienzas en: {lugar_actual}")
    mostrar_mapa(tablero, posicion)
    mostrar_descripcion_habitacion(lugar_actual)
    mostrar_en_cuarto(npc_ubicaciones, lugar_actual)
    mostrar_armas_en_habitacion(habitaciones_con_armas, lugar_actual)

    while turnos > 0:
        print(f"\nTurno {31 - turnos}/30")
        print(f"Estás en: {lugar_actual}")

        print("\nElige una acción:")
        accion = menu_numerico(["Moverte", "Preguntar", "Declarar", "Salir"])

        # ----------------------------
        # MOVER
        # ----------------------------
        if accion == 1:
            print("\nPuedes moverte un espacio por turno (izquierda o derecha).")
            direccion = menu_numerico(["Izquierda", "Derecha"], "¿A dónde quieres ir?: ")

            if direccion == 1:
                nueva_pos = max(0, posicion - 1)
            else:
                nueva_pos = min(len(tablero) - 1, posicion + 1)

            posicion = nueva_pos
            lugar_actual = obtener_habitacion(posicion)

            mostrar_mapa(tablero, posicion)

            if lugar_actual == "pasillo":
                print("Estás en un pasillo.")
            else:
                print(f"Has llegado a {lugar_actual}.")
                mostrar_descripcion_habitacion(lugar_actual)
                mostrar_en_cuarto(npc_ubicaciones, lugar_actual)
                mostrar_armas_en_habitacion(habitaciones_con_armas, lugar_actual)

            turnos -= 1

        # ----------------------------
        # PREGUNTAR
        # ----------------------------
        elif accion == 2:
            if lugar_actual == "pasillo":
                print("No puedes preguntar en un pasillo.")
                continue

            presentes = [npc for npc, hab in npc_ubicaciones.items() if hab == lugar_actual]
            if not presentes:
                print("No hay nadie a quien preguntar aquí.")
                continue

            preguntas_hechas = 0
            print("\nModo de interrogatorio (máximo 4 preguntas por turno).")

            while preguntas_hechas < 4:
                print(f"\nPregunta #{preguntas_hechas + 1}")
                opciones_npc = presentes + ["Terminar preguntas"]
                eleccion = menu_numerico(opciones_npc, "¿A quién preguntas?: ")

                if eleccion == len(opciones_npc):  # Terminar preguntas
                    print("Terminas tus preguntas por este turno.")
                    break

                npc = presentes[eleccion - 1]
                carta = input("¿Qué carta preguntas?: ")
                preguntar_a_npc(npcs, npc, carta)
                preguntas_hechas += 1

                if preguntas_hechas == 4:
                    print("Has usado tus 4 preguntas de este turno.")

            turnos -= 1

        # ----------------------------
        # DECLARAR
        # ----------------------------
        elif accion == 3:
            if lugar_actual == "pasillo":
                print("No puedes declarar en un pasillo. Debes estar en una habitación.")
                continue

            print("\nEstás haciendo una acusación final.")
            p = input("Personaje sospechoso: ")
            a = input("Arma: ")
            l = input("Lugar: ")

            if (p == respuesta["personaje"] and
                a == respuesta["arma"] and
                l == respuesta["lugar"]):
                print("\n¡Has resuelto el misterio! Ganaste el juego.")
                mostrar_final(respuesta)
                break
            else:
                print("\nAcusación incorrecta. Has perdido.")
                mostrar_final(respuesta)
                break

            turnos -= 1

        # ----------------------------
        # SALIR
        # ----------------------------
        elif accion == 4:
            print("Saliendo del juego...")
            break

    if turnos == 0:
        print("\nSe acabaron los turnos.")
        mostrar_final(respuesta)

# ===============================
# INICIAR JUEGO
# ===============================
if __name__ == "__main__":
    jugar()
