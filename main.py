from coches import coches
# from tkinter import Label,Entry,Button,Tk,messagebox,StringVar
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    def esperarTecla(self):
        input("...¡Oprima enter para continuar!...")

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    # def menu_acciones(self,tipo):
    #     print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
    #     opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n \t\tElige una Opcion: ").strip().lower()
    #     return opcion
    
    # ...VISTAS

    def barraMenu(self):
        menuBar= Menu(self.ventana)
        self.ventana.config(menu=menuBar)

        menuPrincipal = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Principal", menu=menuPrincipal)
        menuPrincipal.add_command(label="Menu Principal", command=self.main)
        menuPrincipal.add_command(label = "Menu Acciones", command=self.menu_acciones)
        menuPrincipal.add_separator()
        menuPrincipal.add_command(label = "Salir", command = self.ventana.quit)

        accionesMenu = Menu(menuBar, tearoff = False)
        menuBar.add_cascade(label = "Acciones", menu = accionesMenu)
        accionesMenu.add_command(label= "Agregar", command = self.insertar_view)
        accionesMenu.add_command(label= "Borrar", command = self.eliminar_view)
        accionesMenu.add_command(label= "Modificar", command = self.modificar_view)
        accionesMenu.add_command(label= "Mostrar", command = self.consultar_view)
        menuPrincipal.add_separator()
        accionesMenu.add_command(label= "Regresar", command = self.main)


    def menu_acciones(self):
        self.borrarPantalla()
        self.barraMenu()
        tipo="Coches"
        Label(self.ventana,text=f"\n\t\t\t...::: Menu de {tipo} :::... \n").pack(pady=10)
        Button(self.ventana,text="1.-Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.-Borrar",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.-Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.-Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=5)
                
    def main(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="\n\t M E N U  P R I N C I P A L ").pack(pady=10)
        Button(self.ventana,text="1.-Coches",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text="2.-Salir",command=self.ventana.quit).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        self.barraMenu()
        self.frame1= Frame(self.ventana)
        self.frame1.pack(pady=10)
        Label(self.frame1,text="... Ingresar datos del Coche...").grid(row=0, column=0,pady=5,padx=5,sticky="e")
        
        Label(self.frame1,text="Marca").grid(row=0, column=0,pady=5,padx=5,sticky="e")
        self.marca=Entry(self.frame1)
        self.marca.focus()
        self.marca.grid(row=0, column= 1, pady=5, padx=5, sticky="w")
        
        Label(self.frame1,text="Color").grid(row=1, column=0,pady=5,padx=5,sticky="e")
        self.color=Entry(self.frame1)
        self.color.grid(row=1, column= 1, pady=5, padx=5, sticky="w")
        
        Label(self.frame1,text="Modelo").grid(row=2, column=0,pady=5,padx=5,sticky="e")
        self.modelo=Entry(self.frame1)
        self.modelo.grid(row=2, column= 1, pady=5, padx=5, sticky="w")        
        
        Label(self.frame1,text="Velocidad").grid(row=3, column=0,pady=5,padx=5,sticky="e")
        self.velocidad=Entry(self.frame1)
        self.velocidad.grid(row=3, column= 1, pady=5, padx=5, sticky="w")
        
        Label(self.frame1,text="Potencia").grid(row=4, column=0,pady=5,padx=5,sticky="e")
        self.potencia=Entry(self.frame1)
        self.potencia.grid(row=4, column= 1, pady=5, padx=5, sticky="w")

        Label(self.frame1,text="Numero de asientos").grid(row=5, column=0,pady=5,padx=5,sticky="e")
        self.asientos=Entry(self.frame1)
        self.asientos.grid(row=5, column= 1, pady=5, padx=5, sticky="w")

        Button(self.frame1,text="Guardar",command=lambda:{self.insertar_controller(),self.insertar_view()}).grid(row=6, column=0, columnspan=2, pady=10, sticky="e")
        Button(self.frame1,text="Regresar",command=self.menu_acciones).grid(row=7, column=0, columnspan=2, pady=10, sticky="w")


    def eliminar_view(self):
        self.borrarPantalla()
        self.barraMenu()
        self.frame1= Frame(self.ventana)
        self.frame1.pack(pady=10)
        Label(self.frame1,text="... Ingresar el ID del Coche a Eliminar...").grid(row=0, column=0, pady=10)

        Label(self.frame1,text="ID").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.id=Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        self.btn_buscar=Button(self.frame1,text="Buscar",command=lambda:self.buscar_controller("eliminar"))
        self.btn_buscar.grid(row=2, column=0, columnspan=2, pady=5)

        self.btn_eliminar=Button(self.frame1,text="Eliminar", state="disabled", command=lambda:{self.eliminar_controller(),self.eliminar_view()})
        self.btn_eliminar.grid(row=3, column=0, columnspan=2, pady=5, sticky="e")
        Button(self.frame1,text="Regresar",command=self.menu_acciones).grid(row=4, column=0, columnspan=2, pady=10)


    def modificar_view(self):
        self.borrarPantalla()
        self.barraMenu()
        self.var_marca=StringVar()
        self.var_color=StringVar()
        self.var_modelo=StringVar()
        self.var_velocidad=StringVar()
        self.var_potencia=StringVar()
        self.var_asientos=StringVar()

        self.frame1= Frame(self.ventana)
        self.frame1.pack(pady=10)
        Label(self.frame1,text="... Modificar datos del Coche ...").grid(row=0, column=0, pady=10)

        Label(self.frame1,text="ID").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.id=Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        Button(self.frame1,text="Buscar",
            command=lambda:self.buscar_controller("modificar")).grid(row=2, column=0, columnspan=2, pady=5)

        Label(self.frame1,text="Nueva Marca").grid(row=3, column=0, pady=5, padx=5, sticky="e")
        self.marca=Entry(self.frame1,textvariable=self.var_marca)
        self.marca.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1,text="Nuevo Color").grid(row=4, column=0, pady=5, padx=5, sticky="e")
        self.color=Entry(self.frame1,textvariable=self.var_color)
        self.color.grid(row=4, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1,text="Nuevo Modelo").grid(row=5, column=0, pady=5, padx=5, sticky="e")
        self.modelo=Entry(self.frame1,textvariable=self.var_modelo)
        self.modelo.grid(row=5, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1,text="Nueva Velocidad").grid(row=6, column=0, pady=5, padx=5, sticky="e")
        self.velocidad=Entry(self.frame1,textvariable=self.var_velocidad)
        self.velocidad.grid(row=6, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1,text="Nueva Potencia").grid(row=7, column=0, pady=5, padx=5, sticky="e")
        self.potencia=Entry(self.frame1,textvariable=self.var_potencia)
        self.potencia.grid(row=7, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1,text="Nuevo Numero de asientos").grid(row=8, column=0, pady=5, padx=5, sticky="e")
        self.asientos=Entry(self.frame1,textvariable=self.var_asientos)
        self.asientos.grid(row=8, column=1, pady=5, padx=5, sticky="w")

        self.btn_modificar=Button(
            self.ventana,
            text="Guardar",
            state="disabled",
            command=lambda:(self.modificar_controller(),self.modificar_view())
        )
        self.btn_modificar.grid(row=9, column=0, columnspan=2, pady=10, sticky="w")

        Button(self.ventana,text="Regresar",command=self.menu_acciones).grid(row=9, column=0, columnspan=2, pady=10, sticky="e")


    def consultar_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="::: Consultar los Coches :::").pack(pady=10)

        filas=self.consultar_controller()

        Label(self.ventana,text=filas,justify=LEFT).pack(pady=5)

        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    def confirmacion_eliminar(self,tipo):
        resp=messagebox.askquestion(title="...¡Atencion¡...",message=f"...¿Desea {tipo} este registro?")
        if resp=="yes":
            return True
        else:
            return False

    def cambiar_estado_btn(self,estado,tipo_accion):
        if estado:
            if tipo_accion=="eliminar":
                self.btn_eliminar.config(state="normal")
            elif tipo_accion=="modificar":
                self.btn_modificar.config(state="normal")

        else:
            if tipo_accion=="eliminar":
                self.btn_eliminar.config(state="disabled")
            elif tipo_accion=="modificar":
                self.btn_modificar.config(state="disabled")

    def insertar_controller(self):
        coche1 = coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1

    def eliminar_controller(self):
        id=self.id.get()
        resp=self.confirmacion_eliminar("eliminar")
        if resp:
            respuesta=coches.Coches.eliminar(id)
        else:
            respuesta=False
        self.respuesta_sql(respuesta)

    def consultar_controller(self):
        registros=coches.Coches.consultar()
        filas=""

        if len(registros)>0:
            num_coches=1

            for fila in registros:
                filas+=f"Coche # {num_coches}\n"
                filas+=f"\tID: {fila[0]}\n"
                filas+=f"\tMarca: {fila[1]}\n"
                filas+=f"\tColor: {fila[2]}\n"
                filas+=f"\tModelo: {fila[3]}\n"
                filas+=f"\tVelocidad: {fila[4]}\n"
                filas+=f"\tPotencia: {fila[5]}\n"
                filas+=f"\tAsientos: {fila[6]}\n\n"

                num_coches+=1

        else:
            filas="No existen datos que mostrar por el momento..."

        return filas

    def modificar_controller(self):
        id=self.id.get()
        coche1 = coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1        

    def buscar_controller(self,tipo_accion):
        id=self.id.get()
        coche1=coches.Coches.buscar(id)
        if len(coche1)>0:
            messagebox.showinfo(title="...¡ Registro encontrado ¡...",message=f"...¡El registro fue encontrado con exito, puedes {tipo_accion} ¡...")
            self.cambiar_estado_btn(True,tipo_accion)         
            if tipo_accion=="modificar":
                self.var_marca.set(coche1[0][1])
                self.var_color.set(coche1[0][2])
                self.var_modelo.set(coche1[0][3])
                self.var_velocidad.set(coche1[0][4])
                self.var_potencia.set(coche1[0][5])
                self.var_asientos.set(coche1[0][6])
        else:
            messagebox.showerror(title="...¡ Verifique por favor ¡...",message=f"...¡El registro no fue encontrado, no es posible {tipo_accion} ¡...")
            self.cambiar_estado_btn(False,tipo_accion)            

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="Exitoso",message="accion realizada con exito")
        else:
            input("accion no exitosa")
            messagebox.showerror(title="Verifica por favor",message="accion no exitosa")
                
    
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()

#balsamiq