#  Juego del Ahorcado

Implementación modular en **Python** del clásico juego del **Ahorcado**, desarrollado como práctica de laboratorio de programación. Incluye modo consola, batería de pruebas unitarias, soporte para palabras con tilde e interfaz gráfica con **Tkinter**.

---

##  Tecnologías y requisitos

* **Lenguaje:** Python 3.8 o superior.
* **Librerías utilizadas:** Módulos estándar `random` y `tkinter` (no requiere instalar dependencias externas).

---

##  Reglas del juego

1. El programa selecciona una palabra secreta al azar desde un diccionario de texto.
2. En cada turno se muestra la palabra oculta mediante guiones bajos (`_`) y el número de intentos disponibles.
3. El jugador propone una letra:
   * Si la letra está en la palabra (con o sin tilde), se revelan todas sus posiciones.
   * Si no está, se descuenta un intento.
4. La partida termina al descubrir la palabra completa (**victoria**) o al agotar los **6 intentos** (**derrota**).

---

##  Estructura del repositorio

```text
├── data/
│   ├── palabras_ahorcado.txt            # Diccionario principal (505 palabras)
│   └── palabras_ahorcado_conTildes.txt  # Diccionario con palabras acentuadas
├── img/
│   └── Diagrama.png                     # Diagrama de descomposición funcional
├── src/
│   ├── ahorcado.py                      # Lógica principal y modo consola
│   ├── ahorcadoGUI.py                   # Interfaz gráfica con Tkinter
│   └── ahorcado_test.py                 # Pruebas unitarias de las funciones
└── README.md
