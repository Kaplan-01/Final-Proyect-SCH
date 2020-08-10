''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 09-08-2020
DESCRIPTION: Update and delete objetive
'''
import web # IMPORTACCION DE WEB.

import mvc.models.model as model

model_alumnos = model.Alumnos()

render = web.template.render("mvc/views/alumnos/")

class Borrar():
    
    def GET(self, id_alumno):
        try:
            result = model_alumnos.view(id_alumno)[0]
            return render.borrar(result) # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            print(e)
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.

    def POST(self, id_alumno):
        try:
            form = web.input()
            id_alumno = form.id_alumno      # Hidden
            print(id_alumno)
            result = model_alumnos.borrar(id_alumno)
            web.seeother('/list/')
        except Exception as e:
            print(e)
            return "Error"