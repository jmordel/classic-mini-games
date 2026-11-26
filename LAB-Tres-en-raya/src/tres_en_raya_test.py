try:
    from tres_en_raya import *
except ModuleNotFoundError:
    from src.tres_en_raya import *


def test_crear_y_colocar():
    print("Testeando crear_tablero() y colocar_ficha()...")
    t = crear_tablero()
    assert casilla_libre(t, 0, 0) is True
    assert colocar_ficha(t, 0, 0, JUGADOR) is True
    assert casilla_libre(t, 0, 0) is False
    assert colocar_ficha(t, 0, 0, ORDENADOR) is False
    print("OK -> Tablero creado y validación de casilla ocupada correcta.\n")


def test_hay_ganador():
    print("Testeando hay_ganador()...")
    # Victoria en fila
    t_fila = [
        ["X", "X", "X"],
        [" ", "O", " "],
        ["O", " ", " "]
    ]
    # Victoria en diagonal
    t_diag = [
        ["O", "X", " "],
        ["X", "O", " "],
        [" ", " ", "O"]
    ]
    # Sin ganador
    t_nada = crear_tablero()

    print("Victoria horizontal X:", hay_ganador(t_fila, "X"))
    print("Victoria diagonal O:", hay_ganador(t_diag, "O"))
    print("Tablero vacío X:", hay_ganador(t_nada, "X"))
    print()


def test_jugada_ordenador():
    print("Testeando jugada_ordenador() (bloqueo)...")
    t = [
        ["X", "X", " "],
        [" ", "O", " "],
        [" ", " ", " "]
    ]
    jugada = jugada_ordenador(t)
    print(f"Ordenador elige bloquear en: {jugada} (esperado: (0, 2))")
    print()


if __name__ == "__main__":
    test_crear_y_colocar()
    test_hay_ganador()
    test_jugada_ordenador()