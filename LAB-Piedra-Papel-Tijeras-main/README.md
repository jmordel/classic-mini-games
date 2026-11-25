# 🪨📄✂️ Piedra, Papel o Tijeras

Implementación modular en **Python** del clásico juego **Piedra, Papel o Tijeras**, desarrollado como práctica de laboratorio de programación. El proyecto separa la lógica del juego de su batería de pruebas e incorpora validación de entrada, partidas rápidas y un modo torneo al mejor de tres puntos.

---

## 🛠️ Tecnologías y requisitos

* **Lenguaje:** Python 3.8 o superior.
* **Librerías utilizadas:** Módulo estándar `random` (no requiere instalar dependencias externas).

---

## 📋 Reglas del juego

En cada ronda, el usuario y el ordenador eligen una jugada de forma simultánea:

| Jugada | Gana a | Pierde contra | Empata con |
| :--- | :--- | :--- | :--- |
| 🪨 **Piedra** | ✂️ Tijeras | 📄 Papel | 🪨 Piedra |
| 📄 **Papel** | 🪨 Piedra | ✂️ Tijeras | 📄 Papel |
| ✂️ **Tijeras** | 📄 Papel | 🪨 Piedra | ✂️ Tijeras |

---

## 📁 Estructura del repositorio

```text
├── src/
│   ├── piedra_papel_tijeras.py       # Lógica principal y modos de juego
│   └── piedra_papel_tijeras_test.py  # Pruebas unitarias de las funciones
└── README.md