import tkinter
from tkinter import*
from functools import partial
from tkinter import Menu, filedialog, messagebox as MessageBox
import xml.etree.ElementTree as ET
import Validaciones
Validar= Validaciones.Validaciones()





fuente = 'Lucida Sans Typewriter'


class Ventana():
    def __init__(self):
        self.window= Tk()
        self.window.title("PROYECTO 1")
        self.window.geometry("375x300")
        self.window['bg']='#E9E9D3'
        self.Tamano = 20
        Titulo = Label(self.window, text="MENU PRINCIPAL", fg='black', bg = '#E9E9D3', font=(fuente, self.Tamano))
        Titulo.place(x=75, y=25)
        self.bgbotones="#C69684"
        self.x=100

        ADF = Button(self.window, text="ADF", font=(fuente, 10), bg=self.bgbotones, command=partial(Ventana.AGF_Ventana,self))
        ADF.place(x=self.x, y=75)
        ADF.config(width=20, height=2)
        GR = Button(self.window, text="GR", font=(fuente, 10), bg=self.bgbotones, command=self.GR_Ventana)
        GR.place(x=self.x, y=125)
        GR.config(width=20, height=2)
        Cargar = Button(self.window, text="Cargar Archivo", font=(fuente, 10), bg=self.bgbotones, command=self.Cargar_Ventana)
        Cargar.place(x=self.x, y=175)
        Cargar.config(width=20, height=2)
        Salir = Button(self.window, text="Salir", font=(fuente, 10), bg=self.bgbotones)
        Salir.place(x=self.x, y=225)
        Salir.config(width=20, height=2)
        self.window.mainloop()

    def AGF_Ventana(self):
        self.windowA = Toplevel()
        self.windowA.title("Automatas Finitos Deterministas")
        self.windowA.geometry("375x300")
        self.windowA['bg']='#E9E9D3'

        Titulo = Label(self.windowA, text="AUTOMATAS FINITOS DETERMINISTAS", fg='black', bg='#E9E9D3', font=(fuente, 12))
        Titulo.place(x=40, y=25)
        self.bgbotones = "#C69684"
        self.x = 100
        self.Tamano = 12
        crear = Button(self.windowA, text="Crear AFD", font=(fuente, 10), bg=self.bgbotones, command=partial(Ventana.Crear_AFD,self))
        crear.place(x=self.x, y=75)
        crear.config(width=20, height=2)
        evaluar = Button(self.windowA, text="Evaluar Cadena", font=(fuente, 10), bg=self.bgbotones)
        evaluar.place(x=self.x, y=125)
        evaluar.config(width=20, height=2)
        generar = Button(self.windowA, text="Generar reporte AFD", font=(fuente, 10), bg=self.bgbotones)
        generar.place(x=self.x, y=175)
        generar.config(width=20, height=2)
        Salir = Button(self.windowA, text="Salir", font=(fuente, 10), bg=self.bgbotones)
        Salir.place(x=self.x, y=225)
        Salir.config(width=20, height=2)

    def Crear_AFD(self):
        self.nombre = StringVar()
        self.estados = StringVar()
        self.alfabeto = StringVar()
        self.estadoI=  StringVar()
        self.estadosA= StringVar()
        self.transiciones=StringVar()

        self.windowAFD = Toplevel()
        self.windowAFD.title("EMPLEADOS")
        self.windowAFD.geometry('400x400')
        self.bgventana='#E9E9D3'
        self.windowAFD['bg']=self.bgventana

        Titulo = Label(self.windowAFD, text="CREAR AFD", fg='black', bg=self.bgventana, font=(fuente, self.Tamano))
        Titulo.place(x=100, y=5)

        Nombre = Label(self.windowAFD, text="Nombre", bg=self.bgventana, font=(fuente, 11))
        Nombre.place(x=35, y=40)

        txtNombre = tkinter.Entry(self.windowAFD, textvariable=self.nombre)
        txtNombre.place(x=200, y=40)


        Estados = Label(self.windowAFD, text="Estados", bg=self.bgventana, font=(fuente, 11))
        Estados.place(x=35, y=80)

        txtEstados = tkinter.Entry(self.windowAFD, textvariable=self.estados)
        txtEstados.place(x=200, y=80)





        Alfabeto = Label(self.windowAFD, text="Alfabeto", bg=self.bgventana, font=(fuente, 11))
        Alfabeto.place(x=35, y=120)

        txtAlfabeto = tkinter.Entry(self.windowAFD, textvariable=self.alfabeto)
        txtAlfabeto.place(x=200, y=120)


        EstadoInicial = Label(self.windowAFD, text="Estado Inicial", bg=self.bgventana, font=(fuente, 11))
        EstadoInicial.place(x=35, y=160)

        txtEstadoInicial = tkinter.Entry(self.windowAFD, textvariable=self.estadoI)
        txtEstadoInicial.place(x=200, y=160)

        EstadoAceptacion = Label(self.windowAFD, text="Estado Aceptacion", bg=self.bgventana, font=(fuente, 11))
        EstadoAceptacion.place(x=35, y=200)

        txtEstadoAceptacion = tkinter.Entry(self.windowAFD, textvariable=self.estadosA)
        txtEstadoAceptacion.place(x=200, y=200)

        Transiciones = Label(self.windowAFD, text="Transiciones", bg=self.bgventana, font=(fuente, 11))
        Transiciones.place(x=35, y=240)

        self.txtTransiciones = tkinter.Text(self.windowAFD,height=5,width=15)
        self.txtTransiciones.place(x=200, y=240)

        Aceptar = Button(self.windowAFD, text="Aceptar", font=(fuente, 10), bg=self.bgbotones, command=self.Verificar)
        Aceptar.place(x=175, y=350)



    def Verificar(self):
        self.transiciones.set(self.txtTransiciones.get("1.0",END))
        print(self.transiciones.get())
        if Validar.validacion1(self.estados.get(), ";"):
            next
        else:
            return MessageBox.showwarning("Alerta", "La cadena de Estados no es Valida")
        if Validar.Validacion2(self.alfabeto.get(),","):
            next
        else:
            return MessageBox.showwarning("Alerta", "La cadena de Alfabetos no es Valida")
        if Validar.Existencia(self.estadoI.get(),self.estados.get()):
            next
        else:
            return MessageBox.showwarning("Alerta", "El Estado Inicial no existe")
        if Validar.Existencia(self.estadosA.get(), self.estados.get()):
            next
        else:
            return MessageBox.showwarning("Alerta", "El uno de los Estados de Aceptacion no existe")


        MessageBox.showinfo("Guardado", "AFD ha sido guardado correctamente")

    def GR_Ventana(self):
            self.windowG = Toplevel()
            self.windowG.title("Automatas Finitos Deterministas")
            self.windowG.geometry("375x300")
            self.windowG['bg'] = '#E9E9D3'

            Titulo = Label(self.windowG, text="GRAMATICAS REGULARES", fg='black', bg='#E9E9D3',
                           font=(fuente, 12))
            Titulo.place(x=60, y=25)
            self.bgbotones = "#C69684"
            self.x = 100
            self.bgbotones = "#C69684"
            self.x = 100
            self.Tamano = 12
            crear = Button(self.windowG, text="Crear GR", font=(fuente, 10), bg=self.bgbotones)
            crear.place(x=self.x, y=75)
            crear.config(width=20, height=2)
            evaluar = Button(self.windowG, text="Evaluar Cadena", font=(fuente, 10), bg=self.bgbotones)
            evaluar.place(x=self.x, y=125)
            evaluar.config(width=20, height=2)
            generar = Button(self.windowG, text="Generar reporte GR", font=(fuente, 10), bg=self.bgbotones)
            generar.place(x=self.x, y=175)
            generar.config(width=20, height=2)
            ayuda = Button(self.windowG, text="Ayuda", font=(fuente, 10), bg=self.bgbotones)
            ayuda.place(x=self.x, y=225)
            ayuda.config(width=20, height=2)

    def Cargar_Ventana(self):
        self.windowC = Toplevel()
        self.windowC.title("CARGAR ARCHIVOS")
        self.windowC.geometry("300x200")
        self.windowC['bg'] = '#E9E9D3'
        Titulo = Label(self.windowC, text="CARGAR ARCHIVOS", fg='black', bg='#E9E9D3', font=(fuente, 12))
        Titulo.place(x=75, y=25)
        self.bgbotones = "#C69684"
        self.x = 75
        self.Tamano = 12
        crear = Button(self.windowC, text="Cargar AFD", font=(fuente, 10), bg=self.bgbotones)
        crear.place(x=self.x, y=75)
        crear.config(width=20, height=2)
        evaluar = Button(self.windowC, text="Cargar GR", font=(fuente, 10), bg=self.bgbotones)
        evaluar.place(x=self.x, y=125)
        evaluar.config(width=20, height=2)


def main():
    Ventana()
    return 0
if __name__ == '__main__':
    main()

