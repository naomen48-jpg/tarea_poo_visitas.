import tkinter as tk
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter

if __name__ == "__main__":
    root = tk.Tk()

    servicio = VisitaServicio()
    app = AppTkinter(root, servicio)

    root.mainloop()
