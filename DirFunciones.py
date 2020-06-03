from TablaVariables import TablaVariables

class DirFunciones(object):
    def __init__(self):
        self.diccionario = {}

    def agregarFuncion(self, name, returnType):
        
        if not self.funcionExiste(name):
            self.diccionario[name] = {
                "returnType": returnType,
                "varTable": TablaVariables(),
                "paramTable": [],
                "numberParams": 0,
                "numLocalInt": 0,
                "numLocalFloat": 0,
                "numLocalChar": 0,
                "numTempInt": 0,
                "numTempFloat": 0,
                "numTempChar": 0,
                "numTempBool": 0,
                "memoriaTam": 0,
                "actualCuad": 0,

            }
            return "OK"
        else:
            if name == "global":
                return "global"
            elif name == "main":
                return "main"
            else:
                return name

    def funcionExiste(self, name):
        if name in self.diccionario:
            return True
        else:
            return False

    def agregarVariables(self, nombreFuncion, listaVars):
        for variable in listaVars:
            if not self.diccionario[nombreFuncion]["varTable"].varExiste(variable[0]):
                self.diccionario[nombreFuncion]["varTable"].agregarVariable(variable[0], variable[1], variable[2])
            #print("Se le esta agregando las variables", variable[0], variable[1])
            else: 
                return variable[0]
        return "OK"

    def printFunciones(self):
        for funciones in self.diccionario:
            print(funciones)

    def printTodo(self):
        for funciones in self.diccionario:
            print("NombreFunc:", funciones, "Tipo", self.diccionario[funciones]["returnType"], "paramTable", self.diccionario[funciones]["paramTable"],
            "numberParams", self.diccionario[funciones]["numberParams"], "numLocalInt", self.diccionario[funciones]["numLocalInt"], 
            "numLocalFloat", self.diccionario[funciones]["numLocalFloat"], "numLocalChar", self.diccionario[funciones]["numLocalChar"],)
            self.diccionario[funciones]["varTable"].printVariables()

    def buscarVariable(self, name, nombreFuncion):
        resultado = self.diccionario[nombreFuncion]["varTable"].buscarVariable(name)
        if resultado == "ERROR":
            resultado = self.diccionario["global"]["varTable"].buscarVariable(name)
            if resultado == "ERROR":
                return "ERROR"
            else:
                return resultado
        else:
            return resultado

    def agregarArray(self, nombreFunc, nombreVar, tamArray):
        self.diccionario[nombreFunc]["varTable"].agregarArray(nombreVar, tamArray)

    def buscarVariableDir(self, dir, nombreFuncion):
        resultado = self.diccionario[nombreFuncion]["varTable"].buscarVariableDir(dir)
        if resultado == "ERROR":
            resultado = self.diccionario["global"]["varTable"].buscarVariableDir(dir)
            if resultado == "ERROR":
                return "ERROR"
            else:
                return resultado
        else:
            return resultado 

    def agregarParamTable(self, nombreFunc, listaVariables):
        for elem in listaVariables:
            self.diccionario[nombreFunc]["paramTable"].append(elem[1])
        self.diccionario[nombreFunc]["numberParams"] = len(self.diccionario[nombreFunc]["paramTable"])

    def calcularLocales(self, nombreFunc):
        dicTipos = self.diccionario[nombreFunc]["varTable"].regresarDicTipos()
        self.diccionario[nombreFunc]["numLocalInt"] = dicTipos["int"]
        self.diccionario[nombreFunc]["numLocalFloat"] = dicTipos["float"]
        self.diccionario[nombreFunc]["numLocalChar"] = dicTipos["char"]