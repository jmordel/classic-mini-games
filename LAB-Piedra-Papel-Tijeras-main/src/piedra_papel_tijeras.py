import random


def ordenador_decide_jugada():
    '''
    Elige aleatoriamente entre PIEDRA, PAPEL o TIJERAS y devuelve la elección.
    '''
    opciones = ["PIEDRA", "PAPEL", "TIJERAS"]
    res = random.choice(opciones)
    return res


def usuario_decide_jugada():
    '''
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección
    en mayúsculas. Valida que la opción introducida sea correcta.
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ").upper()
    while eleccion_usuario not in ["PIEDRA", "PAPEL", "TIJERAS"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ").upper()
    return eleccion_usuario


def determina_ganador(jugada_usuario, jugada_ordenador):
    '''
    Determina el resultado de una ronda comparando la jugada del usuario
    y la del ordenador (sin importar mayúsculas o minúsculas).
    '''
    jugada_usuario = jugada_usuario.upper()
    jugada_ordenador = jugada_ordenador.upper()

    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "PIEDRA" and jugada_ordenador == "TIJERAS":
        return "Ganaste"
    elif jugada_usuario == "TIJERAS" and jugada_ordenador == "PAPEL":
        return "Ganaste"
    elif jugada_usuario == "PAPEL" and jugada_ordenador == "PIEDRA":
        return "Ganaste"
    else:
        return "Perdiste"


def jugar():
    '''
    Lleva a cabo una única ronda del juego Piedra, Papel o Tijeras.
    '''
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    jugada_ordenador = ordenador_decide_jugada()
    jugada_usuario = usuario_decide_jugada()
    print(f"El ordenador eligió: {jugada_ordenador}")
    resultado = determina_ganador(jugada_usuario, jugada_ordenador)
    print(f"Resultado de la ronda: {resultado}")


def jugar_torneo():
    '''
    Lleva a cabo un torneo al mejor de 3 puntos. El primero en llegar a 3 gana.
    '''
    print("¡Bienvenido al torneo de Piedra, Papel o Tijeras (a 3 puntos)!")
    puntos_usuario = 0
    puntos_ordenador = 0

    while puntos_usuario < 3 and puntos_ordenador < 3:
        print(f"\n--- Marcador: Usuario {puntos_usuario} - {puntos_ordenador} Ordenador ---")
        jugada_ordenador = ordenador_decide_jugada()
        jugada_usuario = usuario_decide_jugada()
        print(f"El ordenador eligió: {jugada_ordenador}")

        resultado = determina_ganador(jugada_usuario, jugada_ordenador)
        print(f"Resultado de la ronda: {resultado}")

        if resultado == "Ganaste":
            puntos_usuario += 1
        elif resultado == "Perdiste":
            puntos_ordenador += 1

    print(f"\n=== Marcador final: Usuario {puntos_usuario} - {puntos_ordenador} Ordenador ===")
    if puntos_usuario == 3:
        print("¡Enhorabuena! Has ganado el torneo.")
    else:
        print("El ordenador ha ganado el torneo. ¡Suerte la próxima vez!")
