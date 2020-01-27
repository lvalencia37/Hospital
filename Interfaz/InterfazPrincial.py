from tkinter import *
from tkinter import messagebox
from Usuario.InterfazUser import *

class InterfazPrincipal:
	##PAntalla de inicio
	def Inicio():
	
		global VentanaPricipal
		VentanaPricipal = Tk()
		VentanaPricipal.title("Pricipal")
		VentanaPricipal.iconbitmap("people.ico") 
		VentanaPricipal.geometry("480x270")
		imagen=PhotoImage(file="hospital.gif")
		lblImagen=Label(VentanaPricipal,image=imagen).place(x=1,y=1)
		InterfazPrincipal.menuPrincipal(VentanaPricipal)

		VentanaPricipal.mainloop() 

	## Menu de la interfaz principal
	def menuPrincipal(ventana):

			barraMenu=Menu(ventana)
			ventana.config(menu=barraMenu, width=300, height=300)

			crudUsuario=Menu(barraMenu, tearoff=0)
			crudUsuario.add_command(label="Crear Usuario", command=InterfazUser.CrearUser)
			crudUsuario.add_command(label="Consultar Usuario")
			crudUsuario.add_command(label="Modificar Usuario")
			crudUsuario.add_command(label="Eliminar Usuario")

			crudDoctor=Menu(barraMenu, tearoff=0)
			crudDoctor.add_command(label="Crear Doctor")
			crudDoctor.add_command(label="Consultar Doctor")
			crudDoctor.add_command(label="Modificar Doctor")
			crudDoctor.add_command(label="Eliminar Doctor")

			crudMedicamento=Menu(barraMenu, tearoff=0)
			crudMedicamento.add_command(label="Crear Medicamento")
			crudMedicamento.add_command(label="Consultar Medicamento")
			crudMedicamento.add_command(label="Modificar Medicamento")
			crudMedicamento.add_command(label="Eliminar Medicamento")

			crudReceta=Menu(barraMenu, tearoff=0)
			crudReceta.add_command(label="Crear Receta")
			crudReceta.add_command(label="Consultar Receta")
			crudReceta.add_command(label="Modificar Receta")
			crudReceta.add_command(label="Eliminar Receta")

			ayudaMenu=Menu(barraMenu, tearoff=0)
			ayudaMenu.add_command(label="Licencia")
			ayudaMenu.add_command(label="Ayuda de ")

			barraMenu.add_cascade(label="Usuario", menu=crudUsuario)
			barraMenu.add_cascade(label="Doctor", menu=crudDoctor)
			barraMenu.add_cascade(label="Medicamento", menu=crudMedicamento)
			barraMenu.add_cascade(label="Receta", menu=crudReceta)
			barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)




a=InterfazPrincipal
a.Inicio()