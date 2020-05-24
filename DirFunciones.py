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

    def funcionExiste(self, name):
        if name in self.diccionario:
            return True
        else:
            return False

    def agregarVariables(self, nombreFuncion, listaVars):
        for variable in listaVars:
            self.diccionario[nombreFuncion]["varTable"].agregarVariable(variable[0], variable[1], None)
            #print("Se le esta agregando las variables", variable[0], variable[1])

    def printFunciones(self):
        for funciones in self.diccionario:
            print(funciones)

    def printTodo(self):
        for funciones in self.diccionario:
            print("NombreFunc:", funciones, "Tipo", self.diccionario[funciones]["returnType"])
            self.diccionario[funciones]["varTable"].printVariables()