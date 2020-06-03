class TablaVariables(object):
    def __init__(self):
        self.diccionario = {}

    def agregarVariable(self, name, varType, value):
        self.diccionario[name] = {
            "type": varType,
            "dir": value,
            "isArray": False,
            "arraySize": 0
        }

    def varExiste(self, name):
        if name in self.diccionario:
            return True
        else:
            return False

    def printVariables(self):
        for vars in self.diccionario:
            print("NombreVar:", vars, "Tipo:", self.diccionario[vars]["type"], "Dir:", self.diccionario[vars]["dir"], "isArray:", self.diccionario[vars]["isArray"], "TamArray:", self.diccionario[vars]["arraySize"])

    def buscarVariable(self, name):
        if self.varExiste(name):
            return self.diccionario[name]
        else:
            return "ERROR"
        
    def agregarArray(self, name, tamArray):
        self.diccionario[name]["isArray"] = True
        self.diccionario[name]["arraySize"] = tamArray

    def buscarVariableDir(self, dir):
        for vars in self.diccionario:
            if self.diccionario[vars]["dir"] == dir:
                return self.diccionario[vars]
        return "ERROR"

    def regresarDicTipos(self):
        dicTipos = {"int" : 0, "float": 0, "char":0}
        for vars in self.diccionario:
            if self.diccionario[vars]["type"] == "int":
                if self.diccionario[vars]["isArray"] == True:
                    dicTipos["int"] += self.diccionario[vars]["arraySize"]
                else:
                    dicTipos["int"] += 1
            elif self.diccionario[vars]["type"] == "float":
                if self.diccionario[vars]["isArray"] == True:
                    dicTipos["float"] += self.diccionario[vars]["arraySize"]
                else:
                    dicTipos["float"] += 1
            elif self.diccionario[vars]["type"] == "char":
                if self.diccionario[vars]["isArray"] == True:
                    dicTipos["char"] += self.diccionario[vars]["arraySize"]
                else:
                    dicTipos["char"] += 1
        return dicTipos