import tkinter as tk
from tkinter import messagebox

try:
    from wordle import *
    from wordle import _normalizar
except ModuleNotFoundError:
    from src.wordle import *
    from src.wordle import _normalizar


COLORES_CELDA = {
    VERDE: "#538D4E",
    AMARILLO: "#B59F3B",
    GRIS: "#3A3A3C",
}


class WordleApp:
    def __init__(self, root, max_intentos=6):
        self.root = root
        self.root.title("Wordle")
        self.root.resizable(False, False)
        self.root.configure(bg="#121213")

        self.max_intentos = max_intentos
        self.palabras = cargar_palabras_5_letras("data/palabras_ahorcado.txt")
        self.secreta = elegir_palabra_secreta(self.palabras)
        self.fila_actual = 0
        self.intento_actual = ""

        # Cabecera
        self.label_titulo = tk.Label(
            root,
            text="🟩 WORDLE 🟨",
            font=("Helvetica", 20, "bold"),
            bg="#121213",
            fg="white"
        )
        self.label_titulo.pack(pady=(14, 4))

        self.label_info = tk.Label(
            root,
            text="Escribe una palabra de 5 letras y pulsa ENTER",
            font=("Helvetica", 10),
            bg="#121213",
            fg="#818384"
        )
        self.label_info.pack(pady=(0, 12))

        # Cuadrícula 6x5
        frame_grid = tk.Frame(root, bg="#121213")
        frame_grid.pack(padx=20, pady=5)

        self.celdas = []
        for f in range(self.max_intentos):
            fila_labels = []
            for c in range(5):
                lbl = tk.Label(
                    frame_grid,
                    text="",
                    font=("Helvetica", 22, "bold"),
                    width=3,
                    height=1,
                    bg="#121213",
                    fg="white",
                    relief="solid",
                    bd=2,
                    highlightbackground="#3A3A3C"
                )
                lbl.grid(row=f, column=c, padx=4, pady=4, ipady=6)
                fila_labels.append(lbl)
            self.celdas.append(fila_labels)

        # Teclado virtual en pantalla
        frame_teclado = tk.Frame(root, bg="#121213")
        frame_teclado.pack(pady=(14, 16), padx=10)

        self.botones_teclas = {}
        filas_teclado = [
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ"],
            ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "⌫"]
        ]

        for fila_letras in filas_teclado:
            f_row = tk.Frame(frame_teclado, bg="#121213")
            f_row.pack(pady=3)
            for tecla in fila_letras:
                ancho = 6 if tecla in ("ENTER", "⌫") else 3
                btn = tk.Button(
                    f_row,
                    text=tecla,
                    font=("Helvetica", 10, "bold"),
                    width=ancho,
                    height=2,
                    bg="#818384",
                    fg="white",
                    relief="flat",
                    command=lambda t=tecla: self.procesar_tecla(t)
                )
                btn.pack(side=tk.LEFT, padx=2)
                if len(tecla) == 1:
                    self.botones_teclas[tecla] = btn

        # Vincular teclado físico y forzar foco inicial
        self.root.bind("<Key>", self.evento_teclado_fisico)
        self.root.focus_force()

    def evento_teclado_fisico(self, event):
        if event.keysym in ("Return", "KP_Enter"):
            self.procesar_tecla("ENTER")
        elif event.keysym == "BackSpace":
            self.procesar_tecla("⌫")
        elif event.char and event.char.isalpha() and len(event.char) == 1:
            self.procesar_tecla(_normalizar(event.char))

    def procesar_tecla(self, tecla: str):
        if self.fila_actual >= self.max_intentos:
            return

        if tecla == "⌫":
            if self.intento_actual:
                self.intento_actual = self.intento_actual[:-1]
                col = len(self.intento_actual)
                self.celdas[self.fila_actual][col].config(text="", bg="#121213")
        elif tecla == "ENTER":
            self.enviar_palabra()
        elif len(self.intento_actual) < 5 and len(tecla) == 1:
            col = len(self.intento_actual)
            self.intento_actual += tecla
            self.celdas[self.fila_actual][col].config(text=tecla)

    def enviar_palabra(self):
        if len(self.intento_actual) != 5:
            self.label_info.config(text="Faltan letras: completa las 5 casillas", fg="#E74C3C")
            return

        self.label_info.config(text="Escribe una palabra de 5 letras y pulsa ENTER", fg="#818384")
        estados = evaluar_intento(self.secreta, self.intento_actual)

        # Colorear fila y teclado virtual
        prioridad = {GRIS: 1, AMARILLO: 2, VERDE: 3}
        for c in range(5):
            letra = self.intento_actual[c]
            estado = estados[c]
            color = COLORES_CELDA[estado]
            self.celdas[self.fila_actual][c].config(bg=color)

            if letra in self.botones_teclas:
                btn = self.botones_teclas[letra]
                color_actual = btn.cget("bg")
                estado_previo = next((k for k, v in COLORES_CELDA.items() if v == color_actual), None)
                if estado_previo is None or prioridad[estado] > prioridad[estado_previo]:
                    btn.config(bg=color)

        if all(e == VERDE for e in estados):
            messagebox.showinfo("¡Victoria!", f"¡Has adivinado '{self.secreta}' en {self.fila_actual + 1} intentos!")
            self.reiniciar_juego()
            return

        self.fila_actual += 1
        self.intento_actual = ""

        if self.fila_actual >= self.max_intentos:
            messagebox.showinfo("Fin de la partida", f"Se acabaron los intentos.\n\nLa palabra era: {self.secreta}")
            self.reiniciar_juego()

    def reiniciar_juego(self):
        self.secreta = elegir_palabra_secreta(self.palabras)
        self.fila_actual = 0
        self.intento_actual = ""
        for f in range(self.max_intentos):
            for c in range(5):
                self.celdas[f][c].config(text="", bg="#121213")
        for btn in self.botones_teclas.values():
            btn.config(bg="#818384")
        self.root.focus_force()


if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()