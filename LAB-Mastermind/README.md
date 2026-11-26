#  Mastermind

Implementación modular en **Python** del clásico juego de deducción lógica **Mastermind**, desarrollado como práctica de programación. El proyecto separa la lógica del motor de pistas, la validación de entradas y el tablero de historial de su batería de pruebas unitarias.

---

## 🛠️ Tecnologías y requisitos

* **Lenguaje:** Python 3.8 o superior.
* **Librerías utilizadas:** Módulo estándar `random` (no requiere instalar dependencias externas).

---

## 📋 Reglas del juego

El ordenador genera en secreto una combinación oculta de **4 colores** elegidos entre 6 opciones posibles:

| Inicial | Color |
| :---: | :--- |
| **R** |  Rojo |
| **A** |  Azul |
| **V** |  Verde |
| **M** |  Morado |
| **N** |  Naranja |
| **B** |  Blanco |

En cada turno (hasta un máximo de **10 intentos**), el jugador propone una secuencia de 4 letras y recibe dos pistas:
* **Plenos:** número de colores acertados en su **posición exacta**.
* **Parciales:** número de colores presentes en el código secreto pero ubicados en **otra posición**.

---

## 📁 Estructura del repositorio

```text
├── src/
│   ├── mastermind.py       # Lógica principal, cálculo de pistas y modo consola
│   └── mastermind_test.py  # Pruebas unitarias de las funciones
└── README.md
