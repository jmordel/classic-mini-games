#  Classic Mini-Games en Python

Colección de juegos clásicos desarrollados de forma modular en **Python** para practicar lógica de programación, estructuras de datos, pruebas unitarias e interfaces gráficas de escritorio con **Tkinter**.

---

##  Catálogo de juegos

| Proyecto | Descripción | Modos disponibles |
| :--- | :--- | :--- |
|  [**Piedra, Papel o Tijeras**](./LAB-Piedra-Papel-Tijeras) | Clásico juego de azar y estrategia con partida rápida y modo torneo al mejor de 3 puntos. | Consola (`CLI`) |
|  [**El Ahorcado**](./LAB-Ahorcado) | Adivina la palabra secreta antes de agotar los intentos. Incluye diccionario de más de 500 palabras y soporte para tildes. | Consola (`CLI`) + Interfaz (`Tkinter`) |
|  [**Mastermind**](./LAB-Mastermind) | Juego de deducción lógica para descifrar un código oculto de 4 colores mediante pistas de plenos y parciales. | Consola (`CLI`) + Interfaz (`Tkinter`) |
|  [**Tres en Raya**](./LAB-Tres-en-raya) | Tablero $3 \times 3$ con matrices bidimensionales y rival controlado por una IA básica que ataca y bloquea jugadas. | Consola (`CLI`) + Interfaz (`Tkinter`) |
|  [**Wordle**](./LAB-Wordle) | Adivina la palabra oculta de 5 letras en 6 intentos con pistas por color, filtrado de diccionario y teclado interactivo. | Consola (`CLI`) + Interfaz (`Tkinter`) |

---

##  Tecnologías y arquitectura

* **Lenguaje:** Python 3.8 o superior.
* **Librerías estándar:** `random`, `os` y `tkinter` (no requiere instalar dependencias externas).
* **Diseño modular:** Cada proyecto separa la lógica del juego (`src/*.py`), la batería de pruebas unitarias (`src/*_test.py`) y la interfaz gráfica (`src/*GUI.py`), acompañados de su propia documentación.

---

##  Estructura general del repositorio

```text
classic-mini-games/
├── LAB-Piedra-Papel-Tijeras/
├── LAB-Ahorcado/
├── LAB-Mastermind/
├── LAB-Tres-en-raya/
├── LAB-Wordle/
└── README.md
