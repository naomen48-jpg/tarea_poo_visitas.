import tkinter as tk
from tkinter import ttk, messagebox

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("600x400")

        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Cédula").grid(row=0, column=0)
        self.entry_cedula = tk.Entry(frame_form)
        self.entry_cedula.grid(row=0, column=1)

        tk.Label(frame_form, text="Nombre").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(frame_form, text="Motivo").grid(row=2, column=0)
        self.entry_motivo = tk.Entry(frame_form)
        self.entry_motivo.grid(row=2, column=1)

        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Registrar", command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=2, padx=5)

        self.tree = ttk.Treeview(root, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")
        self.tree.pack(fill="both", expand=True)

    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        exito = self.servicio.registrar_visitante(cedula, nombre, motivo)

        if exito:
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def eliminar(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        item = self.tree.item(seleccionado)
        cedula = item["values"][0]

        eliminado = self.servicio.eliminar_visitante(cedula)

        if eliminado:
            messagebox.showinfo("Éxito", "Visitante eliminado")
            self.actualizar_tabla()

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for v in self.servicio.obtener_visitantes():
            self.tree.insert("", "end", values=(v.cedula, v.nombre, v.motivo))

    def limpiar_campos(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)
