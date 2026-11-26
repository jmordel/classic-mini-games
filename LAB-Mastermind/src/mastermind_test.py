try:
    from mastermind import *
except ModuleNotFoundError:
    from src.mastermind import *


def test_generar_codigo():
    print("Testeando generar_codigo()...")
    codigo_sin_rep = generar_codigo(4, permitir_repetidos=False)
    codigo_con_rep = generar_codigo(4, permitir_repetidos=True)
    print("Código sin repetición:", codigo_sin_rep)
    print("Código con repetición:", codigo_con_rep)
    print()


def test_es_intento_valido():
    print("Testeando es_intento_valido()...")
    pruebas = ["RAVM", "ravm", "R A V", "RAVMN", "RAVZ", "1234", ""]
    for p in pruebas:
        print(f"Entrada '{p}' -> ¿Válida?: {es_intento_valido(p)}")
    print()


def test_calcular_pistas(codigo, intento):
    print(f"Testeando calcular_pistas() | Secreto: {codigo} vs Intento: {intento}")
    plenos, parciales = calcular_pistas(codigo, intento)
    print(f"Resultado -> Plenos: {plenos}, Parciales: {parciales}")
    print()


def test_pedir_intento():
    print("Testeando pedir_intento()...")
    intento = pedir_intento(4)
    print("Intento válido recibido:", intento)
    print()


if __name__ == "__main__":
    test_generar_codigo()
    test_es_intento_valido()
    test_calcular_pistas(["R", "A", "V", "M"], ["R", "A", "V", "M"])  # 4 plenos, 0 parciales
    test_calcular_pistas(["R", "A", "V", "M"], ["M", "V", "A", "R"])  # 0 plenos, 4 parciales
    test_calcular_pistas(["R", "A", "V", "M"], ["R", "V", "N", "B"])  # 1 pleno, 1 parcial
    test_calcular_pistas(["R", "A", "V", "M"], ["N", "B", "N", "B"])  # 0 plenos, 0 parciales
    test_calcular_pistas(["R", "A", "V", "M"], ["R", "R", "R", "R"])  # 1 pleno, 0 parciales (repetidos)
    # test_pedir_intento()