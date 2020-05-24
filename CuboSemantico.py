
class CuboSemantico:
    def __init__(self):
        self.cuboSem = {
            "int" : {
                "int" : {
                    "+" : "int",
                    "-" : "int",
                    "*" : "int",
                    "/" : "float",
                    "==" : "bool",
                    "!=" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    "||" : "error",
                    "&&" : "error"
                },
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "==" : "bool",
                    "!=" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    "||" : "error",
                    "&&" : "error"
                },
                "char" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" : "error",
                    "||" : "error",
                    "&&" : "error"
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error"
                }
            },
            "float" : {
                "int" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "==" : "bool",
                    "!=" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    "||" : "error",
                    "&&" : "error"
                },
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "==" : "bool",
                    "!=" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    "||" : "error",
                    "&&" : "error"
                },
                "char" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error" 
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error"
                }
            },
            "char" : {
                "int" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error" 
                },
                "float" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error"
                },
                "char" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "bool",
                    "!=" : "bool",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error"
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error"
                }
            },
            "bool" : {
                "int" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error" 
                },
                "float" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error"
                },
                "char" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "error",
                    "!=" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "error",
                    "&&" : "error"
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "==" : "bool",
                    "!=" : "bool",
                    ">=" : "error",
                    "<=" : "error",
                    ">" : "error",
                    "<" :"error",
                    "||" : "bool",
                    "&&" : "bool"
                }
            }
        }

    def obtenerSem(self, op1, op2, operacion):
        return self.cuboSem[op1][op2][operacion]

if __name__ == "__main__":
    cuboSem = CuboSemantico()
    print(cuboSem.obtenerSem("int","float","+"))