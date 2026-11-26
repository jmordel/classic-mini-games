import tkinter as tk
from tkinter import messagebox

try:
    from mastermind import *
except ModuleNotFoundError:
    from src.mastermind import *


COLORES_HEX = {
    "R": "#E53935",  # Rojo
    "A": "#1E88E5",  # Azul
    "V": "#43A047",  # Verde
    "M": "#8E24AA",  # Morado
    "N": "#FB8C00",  # Naranja
    "B": "#F5F5F5",  # Blanco
}


class MastermindApp:
    def __init__(self, root, max_intentos=10, longitud=4):
        self.root = root
        self.root.title("Mastermind")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")

        self.max_intentos = max_intentos
        self.longitud = longitud
        self.codigo_secreto = generar_codigo(longitud=self.longitud, permitir_repetidos=False)
        self.intento_actual = []
        self.fila_actual = 0

        # Cabecera
        self.label_titulo = tk.Label(
            root,
            text="🧠 MASTERMIND",
            font=("Helvetica", 18, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        self.label_titulo.pack(pady=(12, 2))

        self.label_estado = tk.Label(
            root,
            text=f"Intento 1 de {self.max_intentos} — Elige {self.longitud} colores",
            font=("Helvetica", 11),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        self.label_estado.pack(pady=(0, 8))

        # Tablero principal (Canvas)
        self.ancho_canvas = 310
        self.alto_fila = 42
        self.alto_canvas = self.max_intentos * self.alto_fila + 10
        self.canvas = tk.Canvas(
            root,
            width=self.ancho_canvas,
            height=self.alto_canvas,
            bg="#34495E",
            highlightthickness=2,
            highlightbackground="#1A252F"
        )
        self.canvas.pack(padx=15, pady=5)

        self.celdas_colores = []
        self.celdas_pistas = []
        self.dibujar_tablero()

        # Panel de botones de colores
        frame_colores = tk.Frame(root, bg="#2C3E50")
        frame_colores.pack(pady=(10, 5))

        for codigo in COLORES_VALIDOS:
            fg_texto = "black" if codigo == "B" else "white"
            btn = tk.Button(
                frame_colores,
                text=NOMBRES_COLORES[codigo],
                bg=COLORES_HEX[codigo],
                fg=fg_texto,
                font=("Helvetica", 9, "bold"),
                width=7,
                relief="raised",
                command=lambda c=codigo: self.seleccionar_color(c)
            )
            btn.pack(side=tk.LEFT, padx=3)

        # Panel de acciones (Borrar / Comprobar)
        frame_acciones = tk.Frame(root, bg="#2C3E50")
        frame_acciones.pack(pady=(5, 15))

        self.btn_borrar = tk.Button(
            frame_acciones,
            text="⌫ Borrar",
            font=("Helvetica", 10, "bold"),
            bg="#7F8C8D",
            fg="white",
            width=12,
            command=self.borrar_ultimo
        )
        self.btn_borrar.pack(side=tk.LEFT, padx=8)

        self.btn_comprobar = tk.Button(
            frame_acciones,
            text="✔ Comprobar",
            font=("Helvetica", 10, "bold"),
            bg="#27AE60",
            fg="white",
            width=14,
            state=tk.DISABLED,
            command=self.comprobar_jugada
        )
        self.btn_comprobar.pack(side=tk.LEFT, padx=8)

    def dibujar_tablero(self):
        """Dibuja las 10 filas vacías con sus 4 huecos de color y 4 indicadores de pista."""
        self.canvas.delete("all")
        self.celdas_colores.clear()
        self.celdas_pistas.clear()

        for fila in range(self.max_intentos):
            y_centro = 25 + fila * self.alto_fila

            # Número de intento
            self.canvas.create_text(
                22, y_centro,
                text=f"{fila + 1}.",
                fill="#BDC3C7",
                font=("Helvetica", 10, "bold")
            )

            # 4 círculos grandes para la combinación
            fila_ovals = []
            for col in range(self.longitud):
                x = 58 + col * 42
                oval = self.canvas.create_oval(
                    x - 14, y_centro - 14,
                    x + 14, y_centro + 14,
                    fill="#2C3E50",
                    outline="#7F8C8D",
                    width=2
                )
                fila_ovals.append(oval)
            self.celdas_colores.append(fila_ovals)

            # Cuadrícula 2x2 de clavijas pequeñas para pistas (Plenos / Parciales)
            fila_pistas = []
            offsets = [(-7, -7), (7, -7), (-7, 7), (7, 7)]
            for dx, dy in offsets:
                px, py = 255 + dx, y_centro + dy
                pista = self.canvas.create_oval(
                    px - 5, py - 5,
                    px + 5, py + 5,
                    fill="#2C3E50",
                    outline="#7F8C8D",
                    width=1
                )
                fila_pistas.append(pista)
            self.celdas_pistas.append(fila_pistas)

    def seleccionar_color(self, codigo_color):
        """Añade un color al hueco disponible de la fila actual."""
        if len(self.intento_actual) >= self.longitud or self.fila_actual >= self.max_intentos:
            return

        col = len(self.intento_actual)
        self.intento_actual.append(codigo_color)
        oval_id = self.celdas_colores[self.fila_actual][col]
        self.canvas.itemconfig(oval_id, fill=COLORES_HEX[codigo_color], outline="white")

        if len(self.intento_actual) == self.longitud:
            self.btn_comprobar.config(state=tk.NORMAL)

    def borrar_ultimo(self):
        """Elimina el último color colocado en la fila actual."""
        if not self.intento_actual:
            return

        self.intento_actual.pop()
        col = len(self.intento_actual)
        oval_id = self.celdas_colores[self.fila_actual][col]
        self.canvas.itemconfig(oval_id, fill="#2C3E50", outline="#7F8C8D")
        self.btn_comprobar.config(state=tk.DISABLED)

    def comprobar_jugada(self):
        """Evalúa el intento usando calcular_pistas() de mastermind.py y pinta las pistas."""
        plenos, parciales = calcular_pistas(self.codigo_secreto, self.intento_actual)

        # Pintar clavijas: Verde brillante = Pleno, Amarillo = Parcial
        pistas_fila = self.celdas_pistas[self.fila_actual]
        idx = 0
        for _ in range(plenos):
            self.canvas.itemconfig(pistas_fila[idx], fill="#2ECC71", outline="#2ECC71")
            idx += 1
        for _ in range(parciales):
            self.canvas.itemconfig(pistas_fila[idx], fill="#F1C40F", outline="#F1C40F")
            idx += 1

        # Comprobar victoria
        if plenos == self.longitud:
            secreto_str = " - ".join(NOMBRES_COLORES[c] for c in self.codigo_secreto)
            messagebox.showinfo(
                "¡Victoria!",
                f"¡Has descifrado el código en {self.fila_actual + 1} intentos!\n\nCódigo: {secreto_str}"
            )
            self.reiniciar_juego()
            return

        # Avanzar a la siguiente fila
        self.fila_actual += 1
        self.intento_actual = []
        self.btn_comprobar.config(state=tk.DISABLED)

        # Comprobar derrota
        if self.fila_actual >= self.max_intentos:
            secreto_str = " - ".join(NOMBRES_COLORES[c] for c in self.codigo_secreto)
            messagebox.showinfo(
                "Fin de la partida",
                f"Has agotado los {self.max_intentos} intentos.\n\nEl código secreto era:\n{secreto_str}"
            )
            self.reiniciar_juego()
        else:
            self.label_estado.config(
                text=f"Intento {self.fila_actual + 1} de {self.max_intentos} — Elige {self.longitud} colores"
            )

    def reiniciar_juego(self):
        """Reinicia el tablero y genera un nuevo código secreto."""
        self.codigo_secreto = generar_codigo(longitud=self.longitud, permitir_repetidos=False)
        self.intento_actual = []
        self.fila_actual = 0
        self.btn_comprobar.config(state=tk.DISABLED)
        self.label_estado.config(
            text=f"Intento 1 de {self.max_intentos} — Elige {self.longitud} colores"
        )
        self.dibujar_tablero()


if __name__ == "__main__":
    root = tk.Tk()
    app = MastermindApp(root, max_intentos=10, longitud=4)
    root.mainloop()