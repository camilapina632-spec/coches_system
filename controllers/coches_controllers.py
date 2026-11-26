from models import coches_model
from tkinter import messagebox

class CochesController: 
    def mostrar_coches(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in coches_model.CochesModel.consultar():
            self.tree.insert("", "end", values=row)

    def insertar_controller(self):
        coche1 = coches_model.CochesModel(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1

    def eliminar_controller(self):
        id=self.id.get()
        resp=self.confirmacion_eliminar("eliminar")
        if resp:
            respuesta=coches_model.CochesModel.eliminar(id)
        else:
            respuesta=False
        self.respuesta_sql(respuesta)

    def consultar_controller(self):
        registros=coches_model.CochesModel.consultar()
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
        coche1 = coches_model.CochesModel(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1        

    def buscar_controller(self,tipo_accion):
        id=self.id.get()
        coche1=coches_model.CochesModel.buscar(id)
        if len(coche1)>0:
            self.encontrado_view(coche1,tipo_accion )
                

#balsamiq