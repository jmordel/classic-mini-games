#  Tres en Raya (Tic-Tac-Toe)

Implementación modular en **Python** del clásico **Tres en Raya**, desarrollado como práctica de programación con listas bidimensionales (matrices $3 \times 3$). Incluye modo consola contra una IA básica, pruebas unitarias e interfaz gráfica interactiva con **Tkinter**.

---

## 🛠️ Tecnologías y requisitos

* **Lenguaje:** Python 3.8 o superior.
* **Librerías utilizadas:** Módulos estándar `random` y `tkinter` (no requiere instalar dependencias externas).

---

## 📋 Reglas del juego

1. El tablero es una cuadrícula de **$3 \times 3$** casillas inicialmente vacías.
2. El jugador utiliza la ficha **X** y el ordenador la ficha **O**.
3. Por turnos, cada participante coloca una ficha en una casilla libre.
4. Gana el primero que consiga alinear **3 fichas iguales** en horizontal, vertical o diagonal. Si se completan las 9 casillas sin ganador, la partida termina en **empate**.

---

## 📁 Estructura del repositorio

```text
├── src/
│   ├── tres_en_raya.py       # Lógica del tablero, validación, IA y modo consola
│   ├── tres_en_raya_test.py  # Pruebas unitarias de las funciones
│   └── tres_en_rayaGUI.py    # Interfaz gráfica con Tkinter
└── README.md
