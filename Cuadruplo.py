class Cuadruplo:
    def __init__(self):
        self.quad = []

    def generarCuad(self, operador, op1, op2, res):
        self.quad.append([operador, op1, op2, res])

    def printCuads(self):
        for cuad in self.quad:
            print("Cuadruplo:", cuad[0], cuad[1], cuad[2], cuad[3])