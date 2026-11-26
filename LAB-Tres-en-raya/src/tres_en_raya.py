import random

VACIO = " "
JUGADOR = "X"
ORDENADOR = "O"


def crear_tablero() -> list[list[str]]:
    '''
    Crea y devuelve un tablero vacío de 3x3.
    '''
    return [[VACIO for _ in range(3)] for _ in range(3)]


def mostrar_tablero(tablero: list[list[str]]) -> None:
    '''
    Imprime el estado actual del tablero por consola con índices de fila y columna.
    '''
    print("\n    1   2   3")
    for i, fila in enumerate(tablero):
        print(f" {i + 1}  " + " | ".join(fila))
        if i < 2:
            print("   ---+---+---")
    print()


def casilla_libre(tablero: list[list[str]], fila: int, col: int) -> bool:
    '''
    Devuelve True si las coordenadas (0..2) están dentro del tablero y la casilla está vacía.
    '''
    if not (0 <= fila < 3 and 0 <= col < 3):
        return False
    return tablero[fila][col] == VACIO


def colocar_ficha(tablero: list[list[str]], fila: int, col: int, ficha: str) -> bool:
    '''
    Coloca la ficha en (fila, col) si la casilla está libre. Devuelve True si se realizó el movimiento.
    '''
    if casilla_libre(tablero, fila, col):
        tablero[fila][col] = ficha
        return True
    return False


def pedir_casilla(tablero: list[list[str]]) -> tuple[int, int]:
    '''
    Solicita al usuario una coordenada 'fila,columna' (del 1 al 3) hasta recibir una casilla libre.
    '''
    while True:
        entrada = input("Elige fila y columna (ej. 2,2): ").strip().replace(" ", "")
        partes = entrada.split(",")
        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            fila = int(partes[0]) - 1
            col = int(partes[1]) - 1
            if casilla_libre(tablero, fila, col):
                return fila, col
            else:
                print("Casilla ocupada o fuera de rango (usa números del 1 al 3).")
        else:
            print("Formato no válido. Escribe dos números separados por coma, por ejemplo: 1,3")


def _buscar_jugada_ganadora(tablero: list[list[str]], ficha: str) -> tuple[int, int] | None:
    '''
    Comprueba si 'ficha' puede completar tres en raya en el siguiente movimiento.
    '''
    for f in range(3):
        for c in range(3):
            if casilla_libre(tablero, f, c):
                tablero[f][c] = ficha
                gana = hay_ganador(tablero, ficha)
                tablero[f][c] = VACIO
                if gana:
                    return f, c
    return None


def jugada_ordenador(tablero: list[list[str]]) -> tuple[int, int]:
    '''
    Decide la jugada del ordenador:
    1. Si puede ganar en este turno, completa la línea.
    2. Si el jugador puede ganar en el siguiente turno, lo bloquea.
    3. Prioriza el centro o elige una casilla libre al azar.
    '''
    jugada = _buscar_jugada_ganadora(tablero, ORDENADOR)
    if jugada is not None:
        return jugada

    bloqueo = _buscar_jugada_ganadora(tablero, JUGADOR)
    if bloqueo is not None:
        return bloqueo

    if casilla_libre(tablero, 1, 1):
        return 1, 1

    libres = [(f, c) for f in range(3) for c in range(3) if casilla_libre(tablero, f, c)]
    return random.choice(libres)


def hay_ganador(tablero: list[list[str]], ficha: str) -> bool:
    '''
    Devuelve True si 'ficha' tiene 3 en raya en alguna fila, columna o diagonal.
    '''
    # Filas y columnas
    for i in range(3):
        if all(tablero[i][c] == ficha for c in range(3)):
            return True
        if all(tablero[f][i] == ficha for f in range(3)):
            return True

    # Diagonales
    if all(tablero[i][i] == ficha for i in range(3)):
        return True
    if all(tablero[i][2 - i] == ficha for i in range(3)):
        return True

    return False


def tablero_lleno(tablero: list[list[str]]) -> bool:
    '''
    Devuelve True si no quedan casillas libres en el tablero.
    '''
    for fila in tablero:
        if VACIO in fila:
            return False
    return True


def jugar() -> None:
    '''
    Gestiona una partida completa de Tres en Raya en consola contra el ordenador.
    '''
    print("¡Bienvenido al TRES EN RAYA!")
    print(f"Tú juegas con '{JUGADOR}' y el ordenador con '{ORDENADOR}'.")

    tablero = crear_tablero()
    turno_jugador = True

    while True:
        mostrar_tablero(tablero)

        if turno_jugador:
            fila, col = pedir_casilla(tablero)
            colocar_ficha(tablero, fila, col, JUGADOR)
            if hay_ganador(tablero, JUGADOR):
                mostrar_tablero(tablero)
                print("¡Enhorabuena! Has hecho tres en raya y has ganado la partida.")
                break
        else:
            fila, col = jugada_ordenador(tablero)
            colocar_ficha(tablero, fila, col, ORDENADOR)
            print(f"El ordenador coloca su ficha en ({fila + 1}, {col + 1}).")
            if hay_ganador(tablero, ORDENADOR):
                mostrar_tablero(tablero)
                print("El ordenador ha hecho tres en raya. ¡Suerte la próxima vez!")
                break

        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate! No quedan casillas libres.")
            break

        turno_jugador = not turno_jugador


if __name__ == "__main__":
    jugar()