import tkinter as tk
from tkinter import messagebox

try:
    from tres_en_raya import *
except ModuleNotFoundError:
    from src.tres_en_raya import *


class TresEnRayaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E272E")

        self.tablero = crear_tablero()
        self.puntos_jugador = 0
        self.puntos_ordenador = 0
        self.empates = 0

        # Título y marcador
        self.label_titulo = tk.Label(
            root,
            text="❌ TRES EN RAYA ⭕",
            font=("Helvetica", 18, "bold"),
            bg="#1E272E",
            fg="white"
        )
        self.label_titulo.pack(pady=(15, 5))

        self.label_marcador = tk.Label(
            root,
            text=self._texto_marcador(),
            font=("Helvetica", 11, "bold"),
            bg="#1E272E",
            fg="#00D8D6"
        )
        self.label_marcador.pack(pady=(0, 12))

        # Cuadrícula 3x3 de botones
        frame_tablero = tk.Frame(root, bg="#485460", padx=4, pady=4)
        frame_tablero.pack(padx=20, pady=5)

        self.botones = [[None for _ in range(3)] for _ in range(3)]
        for f in range(3):
            for c in range(3):
                btn = tk.Button(
                    frame_tablero,
                    text="",
                    font=("Helvetica", 28, "bold"),
                    width=4,
                    height=2,
                    bg="#2F3640",
                    fg="white",
                    activebackground="#353B48",
                    relief="flat",
                    command=lambda fila=f, col=c: self.pulsar_casilla(fila, col)
                )
                btn.grid(row=f, column=c, padx=3, pady=3)
                self.botones[f][c] = btn

        # Botón de reinicio manual
        self.btn_reiniciar = tk.Button(
            root,
            text="🔄 Nueva ronda",
            font=("Helvetica", 10, "bold"),
            bg="#57606F",
            fg="white",
            relief="flat",
            padx=12,
            pady=6,
            command=self.reiniciar_ronda
        )
        self.btn_reiniciar.pack(pady=(12, 16))

    def _texto_marcador(self) -> str:
        return f"Tú (X): {self.puntos_jugador}   |   Empates: {self.empates}   |   PC (O): {self.puntos_ordenador}"

    def pulsar_casilla(self, fila: int, col: int):
        if not casilla_libre(self.tablero, fila, col):
            return

        # Turno del jugador
        colocar_ficha(self.tablero, fila, col, JUGADOR)
        self.botones[fila][col].config(text=JUGADOR, fg="#FF5E57")

        if hay_ganador(self.tablero, JUGADOR):
            self.puntos_jugador += 1
            self.label_marcador.config(text=self._texto_marcador())
            messagebox.showinfo("Fin de la ronda", "¡Has ganado la partida!")
            self.reiniciar_ronda()
            return

        if tablero_lleno(self.tablero):
            self.empates += 1
            self.label_marcador.config(text=self._texto_marcador())
            messagebox.showinfo("Fin de la ronda", "¡Empate!")
            self.reiniciar_ronda()
            return

        # Turno del ordenador
        f_pc, c_pc = jugada_ordenador(self.tablero)
        colocar_ficha(self.tablero, f_pc, c_pc, ORDENADOR)
        self.botones[f_pc][c_pc].config(text=ORDENADOR, fg="#0BE881")

        if hay_ganador(self.tablero, ORDENADOR):
            self.puntos_ordenador += 1
            self.label_marcador.config(text=self._texto_marcador())
            messagebox.showinfo("Fin de la ronda", "El ordenador ha ganado esta ronda.")
            self.reiniciar_ronda()
            return

        if tablero_lleno(self.tablero):
            self.empates += 1
            self.label_marcador.config(text=self._texto_marcador())
            messagebox.showinfo("Fin de la ronda", "¡Empate!")
            self.reiniciar_ronda()

    def reiniciar_ronda(self):
        self.tablero = crear_tablero()
        for f in range(3):
            for c in range(3):
                self.botones[f][c].config(text="", bg="#2F3640")


if __name__ == "__main__":
    root = tk.Tk()
    app = TresEnRayaApp(root)
    root.mainloop()