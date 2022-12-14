import tkinter
from tkinter import*
from functools import partial
from tkinter import Menu, filedialog, messagebox as MessageBox
import xml.etree.ElementTree as ET


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

        ADF = Button(self.window, text="ADF", font=(fuente, 10), bg=self.bgbotones, command=self.AGF_Ventana)
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
        self.bgbotones = "#C69684"
        self.x = 100
        self.Tamano = 12
        crear = Button(self.windowA, text="Crear AFD", font=(fuente, 10), bg=self.bgbotones)
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

        Titulo = Label(self.windowC, text="CARGAR ARCHIVOS", fg='black', bg='#E9E9D3',
                       font=(fuente, 12))
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

