class Memoria:
    def __init__(self, nInt, nFloat, nChar, nBool):
        self.ints = {}
        for x in range(nInt):
            self.ints[x] = 0
        self.floats = {}
        for x in range(nFloat):
            self.floats[x] = 0
        self.chars = {}
        for x in range(nChar):
            self.chars[x] = ''
        self.bools = {}
        for x in range(nBool):
            self.bools[x] = True

    def printMem(self):
        print("ints:", self.ints, "floats:", self.floats, "chars:", self.chars, "bools:", self.bools)