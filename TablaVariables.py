class TablaVariables(object):
    def __init__(self):
        self.diccionario = {}

    def agregarVariable(self, name, type, value):
        if not self.varExiste(name):
            self.diccionario[name] = {
                "type": type,
                "value": value
            }
        else:
            print("Ya existe una variable con el nombre", name)

    def varExiste(self, name):
        if name in self.diccionario:
            return True
        else:
            return False

    def printVariables(self):
        for vars in self.diccionario:
            print("NombreVar:", vars, "Tipo:", self.diccionario[vars]["type"])