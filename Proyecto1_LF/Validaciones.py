
class Validaciones():

    # validacion de de Estados
    def validacion1(self,cadena, separador):
        for caracter in cadena:
            if caracter.isalnum() or caracter == separador or caracter.isdigit():
                next
            else:
                return False
        return True

    def separacion(self,cadena, separador):
        # separar Cadena
        if cadena != None:
            Lista = cadena.split(separador)

        return Lista

    # Validacion  de alfabetos
    def Validacion2(self,cadena, separador):
        ListaV2 = self.separacion(cadena, separador)
        for i in ListaV2:
            if cadena.count(i) > 1:
                return False
            else:
                next
        return True

    # Validacion de Existencia de estados
    def Existencia(self, cadena, Estados):
        for i in cadena:
            if i.isalpha():
                if Estados.count(i) == 1:
                    next
                else:
                    return False
            else:
                next
        return True

    def validacion3(self,cadena):
        lista1 = self.separacion(cadena, " ")
        for i in lista1:
            if i != '':
                if i[0].isalnum() and i[1] == "," and (i[2].isdigit() or i[2].isalpha()) and i[3] == ";" and i[4].isalnum():
                    next
                else:
                    return False
            else:
                break

        return True