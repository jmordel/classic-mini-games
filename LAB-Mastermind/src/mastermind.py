import random

COLORES_VALIDOS = ["R", "A", "V", "M", "N", "B"]
NOMBRES_COLORES = {
    "R": "Rojo",
    "A": "Azul",
    "V": "Verde",
    "M": "Morado",
    "N": "Naranja",
    "B": "Blanco"
}


def generar_codigo(longitud: int = 4, permitir_repetidos: bool = False) -> list[str]:
    '''
    Genera el código secreto aleatorio a partir de los colores disponibles.
    '''
    if permitir_repetidos:
        return [random.choice(COLORES_VALIDOS) for _ in range(longitud)]
    return random.sample(COLORES_VALIDOS, longitud)


def es_intento_valido(intento: str, longitud: int = 4) -> bool:
    '''
    Comprueba que la cadena tenga la longitud exacta y solo use letras de colores válidos.
    '''
    intento = intento.strip().upper()
    if len(intento) != longitud:
        return False
    for letra in intento:
        if letra not in COLORES_VALIDOS:
            return False
    return True


def pedir_intento(longitud: int = 4) -> list[str]:
    '''
    Solicita una combinación por teclado hasta que el usuario introduzca una válida.
    '''
    colores_str = ", ".join(COLORES_VALIDOS)
    entrada = input(f"Introduce {longitud} colores ({colores_str}): ").strip().upper()
    while not es_intento_valido(entrada, longitud):
        print(f"Combinación no válida. Usa exactamente {longitud} letras entre: {colores_str}.")
        entrada = input(f"Inténtalo de nuevo: ").strip().upper()
    return list(entrada)


def calcular_pistas(codigo_secreto: list[str], intento: list[str]) -> tuple[int, int]:
    '''
    Compara el intento con el código secreto y devuelve una tupla (plenos, parciales):
    - plenos: colores acertados en su posición exacta.
    - parciales: colores que están en el código pero en distinta posición.
    '''
    plenos = 0
    sobrantes_codigo = []
    sobrantes_intento = []

    for c_secreto, c_intento in zip(codigo_secreto, intento):
        if c_secreto == c_intento:
            plenos += 1
        else:
            sobrantes_codigo.append(c_secreto)
            sobrantes_intento.append(c_intento)

    parciales = 0
    for color in set(sobrantes_intento):
        parciales += min(sobrantes_codigo.count(color), sobrantes_intento.count(color))

    return plenos, parciales


def mostrar_historial(historial: list[tuple[list[str], int, int]]) -> None:
    '''
    Muestra por consola todos los intentos realizados hasta el momento y sus pistas.
    '''
    print("\n--- TABLERO DE INTENTOS ---")
    for num, (intento, plenos, parciales) in enumerate(historial, start=1):
        combinacion = " ".join(intento)
        print(f"Intento {num:2d}: [ {combinacion} ]  ->  Plenos: {plenos} | Parciales: {parciales}")
    print("---------------------------\n")


def jugar(max_intentos: int = 10, longitud: int = 4) -> None:
    '''
    Gestiona una partida completa de Mastermind en consola.
    '''
    print("¡Bienvenido a MASTERMIND!")
    leyenda = ", ".join(f"{k}={v}" for k, v in NOMBRES_COLORES.items())
    print(f"Colores disponibles: {leyenda}")
    print(f"Adivina el código secreto de {longitud} colores en un máximo de {max_intentos} intentos.\n")

    codigo_secreto = generar_codigo(longitud=longitud, permitir_repetidos=False)
    historial = []

    while len(historial) < max_intentos:
        print(f"Intentos restantes: {max_intentos - len(historial)}")
        intento = pedir_intento(longitud)
        plenos, parciales = calcular_pistas(codigo_secreto, intento)
        historial.append((intento, plenos, parciales))
        mostrar_historial(historial)

        if plenos == longitud:
            print(f"¡Enhorabuena! Has descifrado el código {' '.join(codigo_secreto)} en {len(historial)} intentos.")
            return

    print(f"Has agotado tus {max_intentos} intentos. El código secreto era: {' '.join(codigo_secreto)}")


if __name__ == "__main__":
    jugar()