# 🟩🟨 Wordle

Implementación modular en **Python** del popular juego de palabras **Wordle**. El proyecto reutiliza y filtra el diccionario de palabras de 5 letras, gestiona correctamente las letras repetidas mediante evaluación en dos pasadas e incluye tanto modo consola como interfaz gráfica con teclado interactivo en **Tkinter**.

---

## 🛠️ Tecnologías y requisitos

* **Lenguaje:** Python 3.8 o superior.
* **Librerías utilizadas:** Módulos estándar `os`, `random` y `tkinter` (sin dependencias externas).

---

## 📋 Reglas del juego

1. El objetivo es adivinar una palabra secreta de **5 letras** en un máximo de **6 intentos**.
2. Tras cada palabra introducida, las casillas cambian de color según su coincidencia:
   * 🟩 **Verde:** La letra está en la palabra y en la **posición exacta**.
   * 🟨 **Amarillo:** La letra forma parte de la palabra, pero en **otra posición**.
   * ⬛ **Gris:** La letra **no** aparece en la palabra (o ya se han cubierto todas sus apariciones).

---

## 📁 Estructura del repositorio

```text
├── data/
│   └── palabras_ahorcado.txt  # Diccionario fuente (se filtran las de 5 letras)
├── src/
│   ├── wordle.py              # Lógica principal, filtrado y modo consola
│   ├── wordle_test.py         # Pruebas unitarias de evaluación y validación
│   └── wordleGUI.py           # Interfaz gráfica 6x5 con Tkinter
└── README.md