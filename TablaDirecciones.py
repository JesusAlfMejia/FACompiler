class TablaDirecciones:
    def __init__(self, dir1, dir2):
        self.dirInicial = dir1
        self.dirFinal = dir2
        self.dirActual = self.dirInicial

    def obtenerDir(self):
        dirRegreso = self.dirActual
        self.dirActual += 1
        if(self.dirActual > self.dirFinal):
            return -1 
        return dirRegreso
        
    def aumentarDir(self, num):
        self.dirActual += num
        if(self.dirActual > self.dirFinal):
            return -1
        return self.dirActual 

    def calcularTam(self):
        tam = self.dirActual - self.dirInicial
        self.dirActual = self.dirInicial
        return tam