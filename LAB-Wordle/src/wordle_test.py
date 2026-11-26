try:
    from wordle import *
except ModuleNotFoundError:
    from src.wordle import *


def test_cargar_palabras():
    print("Testeando cargar_palabras_5_letras()...")
    palabras = cargar_palabras_5_letras("data/palabras_ahorcado.txt")
    print(f"Total palabras de 5 letras cargadas: {len(palabras)}")
    print("Muestra:", palabras[:8])
    assert all(len(p) == 5 for p in palabras)
    print()


def test_es_intento_valido():
    print("Testeando es_intento_valido()...")
    assert es_intento_valido("raton") is True
    assert es_intento_valido("RATÓN") is True
    assert es_intento_valido("casa") is False
    assert es_intento_valido("perros") is False
    assert es_intento_valido("12345") is False
    print("OK -> Validación de longitud y caracteres correcta.\n")


def test_evaluar_intento(secreta, intento):
    print(f"Testeando evaluar_intento() | Secreta: '{secreta}' vs Intento: '{intento}'")
    estados = evaluar_intento(secreta, intento)
    print(formatear_fila_consola(intento, estados))
    print()


if __name__ == "__main__":
    test_cargar_palabras()
    test_es_intento_valido()
    test_evaluar_intento("PIANO", "PIANO")  # Todo verde
    test_evaluar_intento("PIANO", "ONAPI")  # Todo amarillo
    test_evaluar_intento("PIANO", "SELVA")  # Solo la 'A' amarilla
    test_evaluar_intento("PERRO", "ARROZ")  # Doble R con una en sitio y otra desplazada