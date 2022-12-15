import Validaciones


class ADF:
    def __int__(self, nombre, estado, alfabeto, estadoI, estadosA,tranciones ):
        self.Nombre= nombre
        self.Estado=estado
        self.Alfabeto=alfabeto
        self.EstadoI=estadoI
        self.EstadoA=estadosA
        self.Tranciones=tranciones
#lista enlazada simple
class ListaADF:
    def __int__(self):
        self.cabecera=None
        self.final=None
    #Insercion de automatas
    def insertar(self,Automata):

        if self.cabecera is None:
            self.cabecera = Automata
            return
        final= self.cabecera
        while final.siguiente is not None:
            final=final.siguiente
        final.siguiente = Automata