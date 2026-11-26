import os
import random

PALABRAS_RESPALDO = [
    "RATON", "BRAZO", "FUEGO", "NIEVE", "TIGRE", "PLUMA", "LIBRO", "SELVA",
    "MUNDO", "CIELO", "PLAYA", "NOCHE", "VERDE", "CLAVO", "SILLA", "RELOJ",
    "ARBOL", "PERRO", "LIMON", "QUESO", "BARCO", "LLAVE", "TRIGO", "PIANO"
]

VERDE = "VERDE"        # Letra correcta en posición correcta
AMARILLO = "AMARILLO"  # Letra presente en otra posición
GRIS = "GRIS"          # Letra no presente en la palabra


def _normalizar(texto: str) -> str:
    '''
    Convierte a mayúsculas y elimina tildes para comparar palabras limpiamente.
    '''
    reemplazos = str.maketrans("ÁÉÍÓÚÜ", "AEIOUU")
    return texto.strip().upper().translate(reemplazos)


def cargar_palabras_5_letras(ruta: str = "data/palabras_ahorcado.txt") -> list[str]:
    '''
    Carga un fichero de texto y filtra únicamente las palabras alfabéticas de 5 letras.
    Si el fichero no existe, devuelve una lista de respaldo integrada.
    '''
    palabras = set()
    if os.path.exists(ruta):
        with open(ruta, encoding="utf-8") as f:
            for linea in f:
                palabra = _normalizar(linea)
                if len(palabra) == 5 and palabra.isalpha():
                    palabras.add(palabra)

    if not palabras:
        return list(PALABRAS_RESPALDO)
    return sorted(palabras)


def elegir_palabra_secreta(palabras: list[str]) -> str:
    '''
    Selecciona y devuelve una palabra secreta de 5 letras al azar.
    '''
    return random.choice(palabras)


def es_intento_valido(intento: str) -> bool:
    '''
    Comprueba que el intento tenga exactamente 5 letras alfabéticas.
    '''
    palabra = _normalizar(intento)
    return len(palabra) == 5 and palabra.isalpha()


def pedir_intento() -> str:
    '''
    Solicita una palabra de 5 letras por teclado hasta recibir una entrada válida.
    '''
    entrada = input("Introduce una palabra de 5 letras: ")
    while not es_intento_valido(entrada):
        print("Entrada no válida. Debe ser una palabra de exactamente 5 letras.")
        entrada = input("Inténtalo de nuevo: ")
    return _normalizar(entrada)


def evaluar_intento(palabra_secreta: str, intento: str) -> list[str]:
    '''
    Evalúa cada letra del intento frente a la palabra secreta:
    - VERDE: letra y posición exactas.
    - AMARILLO: letra existente en otra posición disponible.
    - GRIS: letra ausente (o sin ocurrencias restantes).
    '''
    secreta = _normalizar(palabra_secreta)
    propuesta = _normalizar(intento)

    estados = [GRIS] * 5
    sobrantes = list(secreta)

    # 1. Primera pasada: coincidencias exactas (VERDE)
    for i in range(5):
        if propuesta[i] == secreta[i]:
            estados[i] = VERDE
            sobrantes[i] = None

    # 2. Segunda pasada: letras en distinta posición (AMARILLO)
    for i in range(5):
        if estados[i] == GRIS and propuesta[i] in sobrantes:
            estados[i] = AMARILLO
            sobrantes[sobrantes.index(propuesta[i])] = None

    return estados


def formatear_fila_consola(intento: str, estados: list[str]) -> str:
    '''
    Formatea una jugada para consola mostrando la palabra y sus pistas visuales.
    '''
    iconos = {VERDE: "🟩", AMARILLO: "🟨", GRIS: "⬛"}
    letras_str = " ".join(list(_normalizar(intento)))
    pistas_str = "".join(iconos[e] for e in estados)
    return f"  {letras_str}   ->   {pistas_str}"


def jugar(max_intentos: int = 6, ruta_diccionario: str = "data/palabras_ahorcado.txt") -> None:
    '''
    Gestiona una partida completa de Wordle en consola.
    '''
    palabras = cargar_palabras_5_letras(ruta_diccionario)
    secreta = elegir_palabra_secreta(palabras)
    historial = []

    print("¡Bienvenido a WORDLE!")
    print(f"Adivina la palabra oculta de 5 letras en un máximo de {max_intentos} intentos.")
    print("Leyenda: 🟩 Posición exacta | 🟨 Otra posición | ⬛ No está en la palabra\n")

    while len(historial) < max_intentos:
        print(f"Intento {len(historial) + 1} de {max_intentos}")
        intento = pedir_intento()
        estados = evaluar_intento(secreta, intento)
        historial.append((intento, estados))

        print("\n--- TABLERO ---")
        for pal, est in historial:
            print(formatear_fila_consola(pal, est))
        print("---------------\n")

        if all(e == VERDE for e in estados):
            print(f"¡Enhorabuena! Has acertado la palabra '{secreta}' en {len(historial)} intentos.")
            return

    print(f"Has agotado tus {max_intentos} intentos. La palabra secreta era: {secreta}")


if __name__ == "__main__":
    jugar()