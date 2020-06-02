class TablaVariables(object):
    def __init__(self):
        self.diccionario = {}

    def agregarVariable(self, name, varType, value):
        self.diccionario[name] = {
            "type": varType,
            "dir": value
        }

    def varExiste(self, name):
        if name in self.diccionario:
            return True
        else:
            return False

    def printVariables(self):
        for vars in self.diccionario:
            print("NombreVar:", vars, "Tipo:", self.diccionario[vars]["type"], "Dir:", self.diccionario[vars]["dir"])

    def buscarVariable(self, name):
        if self.varExiste(name):
            return self.diccionario[name]
        else:
            return "ERROR"
        