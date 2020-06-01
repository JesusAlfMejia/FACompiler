class Cuadruplo:
    def __init__(self):
        self.quad = []
        self.contador = 0

    def generarCuad(self, operador, op1, op2, res):
        self.quad.append([operador, op1, op2, res])
        self.contador += 1

    def printCuads(self):
        for cuad in self.quad:
            print("Cuadruplo:", cuad[0], cuad[1], cuad[2], cuad[3])

    def rellenar(self, cont, res):
        self.quad[cont][3] = res