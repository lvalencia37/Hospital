from tkinter import *
from tkinter import messagebox
import funciones
import menu

class InterFazPrincipal:
	loginRe=None
	PassRe=None

	def login(self):
		global VentanaLogin
		VentanaLogin = Tk()
		VentanaLogin.title("Login")
		VentanaLogin.iconbitmap("people.ico") 
		VentanaLogin.resizable(0, 0)
		VentanaLogin.geometry("480x270")

		imagen=PhotoImage(file="hospital.gif")
		lblImagen=Label(VentanaLogin,image=imagen).place(x=1,y=1)
		
		LoginId=StringVar()
		PasswordId=StringVar()
		global loginRe,PassRe
		loginRe=LoginId
		PassRe=PasswordId
		
		miFrame = Frame(VentanaLogin)
		miFrame.pack()

		login = Entry(miFrame, textvariable=LoginId)
		login.grid(row=0,column=1, padx=10, pady=10)

		password = Entry(miFrame, textvariable=PasswordId)
		password.grid(row=1, column=1, padx=10, pady=1)
		password.config(show="*")

		loginLabel=Label(miFrame, text="Correo: ")
		loginLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

		loginPassword=Label(miFrame, text="Password: ")
		loginPassword.grid(row=1, column=0, sticky="e", padx=10, pady=10)

		botonCrear = Button(miFrame, text="Entrar", command=Interfaz.VallidacionLogin)
		botonCrear.grid(row=3, column=0, sticky="e", padx=10, pady=10)

		VentanaLogin.mainloop() 

	def VallidacionLogin():
		try:
			Logeo=funciones.DataBase()
			res=Logeo.consultar_login(loginRe.get(),PassRe.get())		 
			if res == 1:
				VentanaLogin.destroy()
				Interfaz.otraVentana()
			elif res ==  2:
				messagebox.showwarning("Error usuario", "Se encontraron dos credenciales")
			elif  res == 0:
				messagebox.showwarning("Error usuario", "Las credenciales son incorrectas")
		except Exception as e:
			raise e







a=InterFazPrincipal
a.login("h")
