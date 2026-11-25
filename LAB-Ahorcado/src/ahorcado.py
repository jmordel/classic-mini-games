import random


def _quitar_tilde(caracter: str) -> str:
    '''
    Convierte una vocal con tilde a su equivalente sin tilde en minúscula.
    '''
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    c = caracter.lower()
    return reemplazos.get(c, c)


def cargar_palabras(ruta: str) -> list[str]:
    '''
    Lee un fichero de texto con una palabra por línea y devuelve una lista.
    '''
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip())
        return res


def elegir_palabra(palabras: list[str]) -> str:
    '''
    Selecciona y devuelve una palabra aleatoria de la lista.
    '''
    return random.choice(palabras)


def enmascarar_palabra(palabra: str, letras_probadas: set[str]) -> str:
    '''
    Devuelve la palabra enmascarada con '_' en las letras no adivinadas,
    separando cada carácter con un espacio. Soporta palabras con tilde.
    '''
    letras_normalizadas = {_quitar_tilde(l) for l in letras_probadas}
    resultado = []
    for letra in palabra:
        if _quitar_tilde(letra) in letras_normalizadas:
            resultado.append(letra)
        else:
            resultado.append('_')
    return ' '.join(resultado)


def letra_valida(letras_probadas: set[str], letra: str) -> bool:
    '''
    Comprueba que la letra tenga longitud 1, sea alfabética y no se haya probado antes.
    '''
    letra = letra.lower()
    if len(letra) != 1:
        return False
    if not letra.isalpha():
        return False
    letras_normalizadas = {_quitar_tilde(l) for l in letras_probadas}
    if _quitar_tilde(letra) in letras_normalizadas:
        return False
    return True


def mensaje_error(letras_probadas: set[str], letra: str) -> str:
    '''
    Devuelve el motivo por el que una letra no es válida.
    '''
    letra = letra.lower()
    letras_normalizadas = {_quitar_tilde(l) for l in letras_probadas}
    if len(letra) != 1:
        return "Solo puedes introducir una letra."
    elif not letra.isalpha():
        return "Debes introducir un carácter alfabético."
    elif _quitar_tilde(letra) in letras_normalizadas:
        return "Ya has introducido esa letra antes."
    return ""


def pedir_letra(letras_probadas: set[str]) -> str:
    '''
    Solicita una letra por teclado hasta que el usuario introduzca una válida.
    '''
    letra = input("Adivina una letra: ").strip().lower()
    while not letra_valida(letras_probadas, letra):
        print(mensaje_error(letras_probadas, letra))
        letra = input("Intenta con otra letra: ").strip().lower()
    return letra


def comprobar_letra(palabra_secreta: str, letra: str) -> bool:
    '''
    Devuelve True si la letra está en la palabra secreta (ignorando tildes).
    '''
    letra_norm = _quitar_tilde(letra)
    for caracter in palabra_secreta:
        if _quitar_tilde(caracter) == letra_norm:
            return True
    return False


def mostrar_mensaje(acierto: bool) -> None:
    '''
    Muestra por consola si la letra propuesta estaba o no en la palabra.
    '''
    if acierto:
        print("¡Bien hecho! Esa letra está en la palabra.")
    else:
        print("Lo siento, esa letra no está en la palabra.")


def comprobar_palabra_completa(palabra_secreta: str, letras_probadas: set[str]) -> bool:
    '''
    Devuelve True si todas las letras de la palabra secreta han sido adivinadas.
    '''
    letras_normalizadas = {_quitar_tilde(l) for l in letras_probadas}
    for letra in palabra_secreta:
        if _quitar_tilde(letra) not in letras_normalizadas:
            return False
    return True


def ejecutar_turno(palabra_secreta: str, letras_probadas: set[str]) -> bool:
    '''
    Ejecuta un turno completo: muestra la palabra, pide letra, actualiza el conjunto,
    comprueba el acierto y muestra el mensaje correspondiente.
    '''
    print(f"Palabra: {enmascarar_palabra(palabra_secreta, letras_probadas)}")
    nueva_letra = pedir_letra(letras_probadas)
    letras_probadas.add(nueva_letra)
    acierto = comprobar_letra(palabra_secreta, nueva_letra)
    mostrar_mensaje(acierto)
    return acierto


def jugar(max_intentos: int, palabras: list[str]) -> None:
    '''
    Gestiona una partida completa del Ahorcado hasta que el jugador gane o agote intentos.
    '''
    print("¡Bienvenido al juego del Ahorcado!")
    palabra_secreta = elegir_palabra(palabras)
    letras_probadas = set()
    intentos_fallidos = 0

    while not comprobar_palabra_completa(palabra_secreta, letras_probadas) and intentos_fallidos < max_intentos:
        print(f"\nIntentos restantes: {max_intentos - intentos_fallidos}")
        acierto = ejecutar_turno(palabra_secreta, letras_probadas)
        if not acierto:
            intentos_fallidos += 1

    print()
    if comprobar_palabra_completa(palabra_secreta, letras_probadas):
        print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
    else:
        print(f"Has perdido la partida. La palabra secreta era: {palabra_secreta}")


if __name__ == "__main__":
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    jugar(6, palabras)