from TablaVariables import TablaVariables

class DirFunciones(object):
    def __init__(self):
        self.diccionario = {}

    def agregarFuncion(self, name, returnType):
        
        if not self.funcionExiste(name):
            self.diccionario[name] = {
                "returnType": returnType,
                "varTable": TablaVariables()
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
            print("NombreFunc:", funciones, "Tipo", self.diccionario[funciones]["returnType"])
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
