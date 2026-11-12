from tkinter import Button, Entry, Label, Tk, messagebox
from estudiantes import estudiantes

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Estudiantes")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0, 0)
        self.main()

    # ------Vistas Estudiantes-------

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_acciones(self):
        tipo = "Estudiantes"
        self.borrarPantalla()
        Label(self.ventana, text=f"...::: Menu de {tipo} :::...").pack(pady=10)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_view).pack(pady=5)
        Button(self.ventana, text="2.- Borrar", command=self.borrar_view).pack(pady=5)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_view).pack(pady=5)
        Button(self.ventana, text="4.- Mostrar", command=self.consultar_view).pack(pady=5)
        Button(self.ventana, text="5.- Salir", command=self.main).pack(pady=5)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text = "\n...::: M E N U  P R I N C I P A L :::...").pack(pady = 10)
        Button(self.ventana, text = "1.- Estudiantes", command=self.menu_acciones).pack(pady = 5)
        Button(self.ventana, text = "2.- Salir", command = self.ventana.quit).pack(pady = 5)

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...", message="...¡Accion Realizada con Exito!...")
        else:
            messagebox.showerror(title="...Verifica por favor!", message="... ¡Esta accion no pudo realizarse en este momento!...")

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "... Ingresar los datos del estudiante ...").pack(pady= 10)
        Label(self.ventana, text = "Nombre: ").pack()
        self.nombre = Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)

        Label(self.ventana, text = "Nota: ").pack()
        self.nota = Entry(self.ventana)
        self.nota.focus()
        self.nota.pack(pady=5)

        Button(self.ventana, text="Guardar", command= self.insertar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command= self.menu_acciones).pack(pady=10)

    def borrar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "... Ingresa el ID del estudiante a eliminar ...").pack(pady= 10)
        Label(self.ventana, text = "ID: ").pack()
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Button(self.ventana, text="Eliminar", command= self.eliminar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command= self.menu_acciones).pack(pady=10)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "... Ingresa el ID del estudiante a modificar ...").pack(pady= 10)
        Label(self.ventana, text = "ID: ").pack()
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana, text = "Nombre: ").pack()
        self.nombre = Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)

        Label(self.ventana, text = "Nota: ").pack()
        self.nota = Entry(self.ventana)
        self.nota.focus()
        self.nota.pack(pady=5)

        Button(self.ventana, text="Modificar", command= self.modificar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command= self.menu_acciones).pack(pady=10)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="::: Consultar los estudiantes:::" ).pack(pady=10)
        filas = ""
        filas=self.consultar_controller(filas)
        Label(self.ventana, text=f"{'NO':<20}{'ID':<20}{'NOMBRE':<20}{'NOTA':<20}").pack(pady=5)
        Label(self.ventana, text="-"*200).pack(pady=5)
        Label(self.ventana, text=f"{filas}").pack(pady=5)
        Label(self.ventana, text="-"*200).pack(pady=5)
        Button(self.ventana, text="regresar", command=self.menu_acciones).pack(pady=5)
    

# ------ Controladores -------

    def insertar_controller(self):
        estudiante = estudiantes.Estudiantes(self.nombre.get(), self.nota.get())
        respuesta = estudiante.insertar()
        self.respuesta_sql(respuesta)
        self.insertar_controller()

    def eliminar_controller(self):
        respuesta = estudiantes.Estudiantes.eliminar(self.id.get())
        self.respuesta_sql(respuesta)
        

    def modificar_controller(self):
        self.id.get()
        estudiante = estudiantes.Estudiantes(self.nombre.get(), self.nota.get())
        respuesta = estudiante.actualizar(self.id.get())
        self.respuesta_sql(respuesta)
        del estudiante

    def consultar_controller(self, filas):
        registros = estudiantes.Estudiantes.consultar()
        if len(registros) > 0:
            num_estudiantes = 1
            for fila in registros:
                filas = filas + f"\n#{num_estudiantes:<20}{fila[0]:<20}{fila[1]:<20}{fila[2]:<20}"
                num_estudiantes += 1
        else:
            filas = "¡No existen datos que mostrar por el momento!"
        return filas     

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()