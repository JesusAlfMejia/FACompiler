class TablaConstantes(object):
    def __init__(self):
        self.diccionario = {}

    def agregarConstante(self, elem, constType, value):
        if self.constExiste(elem):
            return "ERROR"
        else:
            self.diccionario[elem] = {
                "type": constType,
                "dir": value
            }
            return "OK"

    def constExiste(self, elem):
        if elem in self.diccionario:
            return True
        else:
            return False

    def printConstantes(self):
        for elem in self.diccionario:
            print("Elemento:", elem, "Tipo:", self.diccionario[elem]["type"], "Dir:", self.diccionario[elem]["dir"])

    def buscarElemento(self, elem):
        if self.constExiste(elem):
            return self.diccionario[elem]["dir"]
        else:
            return "ERROR"