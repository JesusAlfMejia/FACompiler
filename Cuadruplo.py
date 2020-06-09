class Cuadruplo:
    def __init__(self):
        self.quad = []
        self.contador = 0

    def generarCuad(self, operador, op1, op2, res):
        self.quad.append([operador, op1, op2, res])
        self.contador += 1

    def printCuads(self):
        x = 0
        for cuad in self.quad:
            print(x, ")","Cuadruplo:", cuad[0], cuad[1], cuad[2], cuad[3])
            x += 1

    def rellenar(self, cont, res):
        self.quad[cont][3] = res

    def exportarCuad(self, filename):
        f= open(filename,"w+")
        f.write("Cuadruplos:\n")
        for i in self.quad:
            quadString = str(i[0]) + "~" + str(i[1]) + "~" + str(i[2]) + "~" + str(i[3]) + "\n"
            f.write(quadString)
        f.close() 