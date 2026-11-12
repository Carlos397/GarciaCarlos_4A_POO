from tkinter import Label, Entry, Button, Tk, messagebox
from coches import coches

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0, 0)
        self.main()
        
    ##. ...Vistas Coches
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy();
    
    def menu_acciones(self):
        tipo = "Coches"
        self.borrarPantalla()
        Label(self.ventana, text=f"...::: Menu de {tipo} :::...").pack(pady=10)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_view).pack(pady=5)
        Button(self.ventana, text="2.- Borrar", command=self.eliminar_view).pack(pady=5)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_view).pack(pady=5)
        Button(self.ventana, text="4.- Mostrar", command=self.consultar_view).pack(pady=5)
        Button(self.ventana, text="5.- Salir", command=self.main).pack(pady=5)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text = "\n...::: M E N U  P R I N C I P A L :::...").pack(pady = 10)
        Button(self.ventana, text = "1.- Coches", command=self.menu_acciones).pack(pady = 5)
        Button(self.ventana, text = "2.- Salir", command = self.ventana.quit).pack(pady = 5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "... Ingresar los datos del coche").pack(pady= 10)
        Label(self.ventana, text = "Marca: ").pack()
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana, text = "Color: ").pack()
        self.color = Entry(self.ventana)
        self.color.focus()
        self.color.pack(pady=5)

        Label(self.ventana, text = "Modelo: ").pack()
        self.modelo = Entry(self.ventana)
        self.modelo.focus()
        self.modelo.pack(pady=5)

        Label(self.ventana, text = "Velocidad: ").pack()
        self.velocidad = Entry(self.ventana)
        self.velocidad.focus()
        self.velocidad.pack(pady=5)

        Label(self.ventana, text = "Potencia: ").pack()
        self.potencia = Entry(self.ventana)
        self.potencia.focus()
        self.potencia.pack(pady=5)

        Label(self.ventana, text = "Asientos: ").pack()
        self.asientos = Entry(self.ventana)
        self.asientos.focus()
        self.asientos.pack(pady=5)

        Button(self.ventana, text="Guardad", command= self.insertar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command= self.menu_acciones).pack(pady=10)
    
    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "... Ingresar los datos del coche").pack(pady= 10)
        Label(self.ventana, text = "Id: ").pack()
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Button(self.ventana, text="Borrar", command= self.eliminar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command= self.menu_acciones).pack(pady=10)
    
    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text = "... Ingresar los datos del coche").pack(pady= 10)
        Label(self.ventana, text = "Marca: ").pack()
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana, text = "Color: ").pack()
        self.color = Entry(self.ventana)
        self.color.focus()
        self.color.pack(pady=5)

        Label(self.ventana, text = "Modelo: ").pack()
        self.modelo = Entry(self.ventana)
        self.modelo.focus()
        self.modelo.pack(pady=5)

        Label(self.ventana, text = "Velocidad: ").pack()
        self.velocidad = Entry(self.ventana)
        self.velocidad.focus()
        self.velocidad.pack(pady=5)

        Label(self.ventana, text = "Potencia: ").pack()
        self.potencia = Entry(self.ventana)
        self.potencia.focus()
        self.potencia.pack(pady=5)

        Label(self.ventana, text = "Asientos: ").pack()
        self.asientos = Entry(self.ventana)
        self.asientos.focus()
        self.asientos.pack(pady=5)

        Button(self.ventana, text="Guardad", command= self.modificar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command= self.menu_acciones).pack(pady=10)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="::: Consultar los coches:::" ).pack(pady=10)
        filas = ""
        filas=self.consultar_controller(filas)
        Label(self.ventana, text=f"{'NO':<20}{'ID':<20}{'Marca':<20}{'Color':<20}{'Modelo':<20}{'Velocidad':<20}{'Potencia':<20}{'Asientos':<20}").pack(pady=5)
        Label(self.ventana, text="-"*200).pack(pady=5)
        Label(self.ventana, text=f"{filas}").pack(pady=5)
        Label(self.ventana, text="-"*200).pack(pady=5)
        Button(self.ventana, text="regresar", command=self.menu_acciones).pack(pady=5)

    ## . ... Controladores de coches

    def insertar_controller(self):
        coche = coches.Coches(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get, self.potencia.get(), self.asientos.get())
        repuesta = coche.insertar()
        self.respuesta_sql(repuesta)
        del coche

    def eliminar_controller(self):
        id = self.id.get()
        respuesta = coches.Coches.eliminar(id)
        self.respuesta_sql(respuesta)

    def consultar_controller(self,filas):
        registros = coches.Coches.consultar()
        if len(registros) > 0:
            num_coches = 1
            for fila in registros:
                filas = filas + f"\n#{num_coches:<20}{fila[0]:<20}{fila[1]:<20}{fila[2]:<20}{fila[3]:<20}{fila[4]:<20}{fila[5]:<20}{fila[6]:<20}"
                num_coches += 1
        else:
            filas = "¡No existen datos que mostrar por el momento!"
        return filas    

    def modificar_controller(self):
        self.id.get()
        vehiculos = self.datos_coche("Coches")
        coche = coches.Coches(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get, self.potencia.get(), self.asientos.get())
        respuesta = coche.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...", message="...¡Accion Realizada con Exito!...")
        else:
            messagebox.showerror(title="...Verifica por favor!", message="... ¡Esta accion no pudo realizarse en este momento!...")

    def menuCoche(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Coches")
            match opcion:
                case "1":
                    #Crear objetos de la clase coches
                    #Utilizar la clase coches para crear un objeto, los valores del objeto se tienen que solicitar 
                    vehiculos = self.datos_coche("Coches")
                    coche = coches.Coches(vehiculos['marca'], vehiculos['color'], vehiculos['modelo'], vehiculos['velocidad'], vehiculos['potencia'], vehiculos['asientos'])
                    repuesta = coche.insertar()
                    self.respuesta_sql(repuesta)
                    del coche
                    
                case "2":
                    self.borrarPantalla()
                    id = int(input("Ingresa el ID del coche a eliminar: ").strip())
                    respuesta = coches.Coches.eliminar(id)
                    self.respuesta_sql(respuesta)

                case "3":
                    self.borrarPantalla()
                    id = int(input("Ingresa el ID del coche a actualizar: ").strip())
                    vehiculos = self.datos_coche("Coches")
                    coche = coches.Coches(vehiculos['marca'], vehiculos['color'], vehiculos['modelo'], vehiculos['velocidad'], vehiculos['potencia'], vehiculos['asientos'])
                    respuesta = coche.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del coche
                    
                case "4":
                    self.borrarPantalla()
                    registros = coches.Coches.consultar()
                    if len(registros) > 0:
                        num_coches = 1
                        for fila in registros:
                            print(f"Coche # {num_coches}\n\t ID: {fila[0]}\n\t Marca: {fila[1]}\n\t Color: {fila[2]}\n\t Modelo: {fila[3]}\n\t Velocidad: {fila[4]}\n\t Potencia: {fila[5]}\n\t Asientos: {fila[6]}")
                            num_coches += 1
                            self.esperarTecla()
                    else:
                        print("\n\n\t ¡No existen datos que mostrar por el momento!")
                        self.esperarTecla()

                case "5":
                    opcion = False
                case _:
                    self.borrarPantalla()
                    print("Opcion invalida, vuelve a intentarlo porfavor...")
                    self.esperarTecla()                       

    # def main(self):
    #     opcion = True
    #     while opcion:
    #         self.borrarPantalla()
    #         opcion=input("\n\t 1.- Coches \n\t 2.- Salir\n \t\tElige una Opcion: ").strip().lower()
    #         match opcion:
    #             case "1":
    #                 self.borrarPantalla()
    #                 self.menuCoche()
    #                 self.esperarTecla()

    #             case "2":
    #                 self.borrarPantalla()
    #                 print("Salir del sistema...")
    #                 opcion = False

    #             case _:
    #                 self.borrarPantalla()
    #                 print("Opcion invalida, vuelve a intentarlo porfavor...")
    #                 self.esperarTecla()

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()