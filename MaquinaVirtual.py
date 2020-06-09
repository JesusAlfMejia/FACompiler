from Memoria import Memoria
import fileinput
import sys
cuadruplos = []
tabConstantes = {}
dirFunciones = {}
memGlobal = ""
memLocal = ""
memTemp = ""
nuevaMemLocal = ""
nuevaMemTemp = ""
pilaMemLocal = []
pilaMemTemp = []
pilaInsPointer = []
insPointer = 0

def readObj(info):
    actualLectura = ""
    for x in info:
        if x == "Cuadruplos:":
            actualLectura = "Cuadruplos"
        elif x == "TablaConstantes:":
            actualLectura = "TablaConstantes"
        elif x == "DirFunciones:":
            actualLectura = "DirFunciones"
        elif actualLectura == "Cuadruplos":
            linea = x.split("~")
            readCuad(linea)
        elif actualLectura == "DirFunciones":
            if x:
                linea = x.split("~")
                readDirFunc(linea)
        elif actualLectura == "TablaConstantes":
            linea = x.split("~")
            if len(linea) > 3:
                print("Syntax error: Los strings no pueden llevar el caracter ~")
                sys.exit()
            readConstantes(linea)

            
def readCuad(info):
    global cuadruplos
    cuadruplos.append(info)

def readConstantes(info):
    global tabConstantes
    tabConstantes[info[2]] = {
        "type": info[1],
        "value": info[0]
    }


def readDirFunc(info):
    global dirFunciones
    dirFunciones[info[0]] = {
        "returnType": info[1],
        "cuad": int(info[2]),
        "numLocalInt": int(info[3]),
        "numLocalFloat": int(info[4]),
        "numLocalChar": int(info[5]),
        "numTempInt": int(info[6]),
        "numTempFloat": int(info[7]),
        "numTempChar": int(info[8]),
        "numTempBool": int(info[9]),
        "params": info[10]
    }
    stringParams = dirFunciones[info[0]]["params"]
    stringParams = stringParams[1:]
    stringParams = stringParams[:-1]
    paramsSplit = stringParams.split(',')
    params = {}
    index = 1
    for i in paramsSplit:
        if i != "":
            params[index] = i
        index += 1
    dirFunciones[info[0]]["params"] = params

def analizarCuadruplos():
    global cuadruplos
    global tabConstantes
    global dirFunciones
    global memGlobal
    global memLocal
    global memTemp
    global pilaMemLocal
    global pilaMemTemp
    global nuevaMemLocal
    global nuevaMemTemp
    global pilaInsPointer
    global insPointer
    memGlobal = Memoria(dirFunciones["global"]["numLocalInt"], dirFunciones["global"]["numLocalFloat"], dirFunciones["global"]["numLocalChar"], 0)
    memLocal = Memoria(0,0,0,0)
    memTemp = Memoria(dirFunciones["main"]["numTempInt"], dirFunciones["main"]["numTempFloat"], dirFunciones["main"]["numTempChar"], dirFunciones["main"]["numTempBool"])
    insPointer = dirFunciones["main"]["cuad"]
    while insPointer < len(cuadruplos):
        #print("insPointer", insPointer)
        #print("MemTemp")
        #memTemp.printMem()
        #print("MemGlobal")
        #memGlobal.printMem()
        codeOp = cuadruplos[insPointer][0]
        opIzq = cuadruplos[insPointer][1]
        if opIzq[0]  == "(":
            opIzq = removeString(opIzq)
            opIzq = regresarVal(opIzq)
        opDer = cuadruplos[insPointer][2]
        if opDer[0]  == "(":
            opDer = removeString(opDer)
            opDer = regresarVal(opDer)
        resDir = cuadruplos[insPointer][3]
        if resDir[0]  == "(":
            resDir = removeString(resDir)
            resDir = regresarVal(resDir)
        if codeOp == '+':
            res = regresarVal(opIzq) + regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '-':
            res = regresarVal(opIzq) - regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '*':
            res = regresarVal(opIzq) * regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '/':
            res = regresarVal(opIzq) / regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '==':
            res = regresarVal(opIzq) == regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '>=':
            res = regresarVal(opIzq) >= regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '<=':
            res = regresarVal(opIzq) <= regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '>':
            res = regresarVal(opIzq) > regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '<':
            res = regresarVal(opIzq) < regresarVal(opDer)
            #print(regresarVal(opIzq), regresarVal(opDer), res)
            asignarVal(resDir, res)
        elif codeOp == '!=':
            res = regresarVal(opIzq) != regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '&&':
            res = regresarVal(opIzq) and regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '||':
            res = regresarVal(opIzq) or regresarVal(opDer)
            asignarVal(resDir, res)
        elif codeOp == '=':
            res = regresarVal(opIzq)
            asignarVal(resDir, res)
        elif codeOp == '=':
            res = regresarVal(opIzq)
            asignarVal(resDir, res)
        elif codeOp == "gotof":
            if regresarVal(opIzq) == False:
                insPointer = int(resDir) - 1
        elif codeOp == "goto":
            insPointer = int(resDir) - 1
        elif codeOp == "print":
            print(regresarVal(resDir))
        elif codeOp == "read":
           inp = input()
           asignarVal(resDir, inp)
        elif codeOp == "addArray":
            nuevaDir = regresarVal(opIzq) + int(opDer)
            #res = regresarVal(nuevaDir)
            asignarVal(resDir, nuevaDir)
        elif codeOp == "verify": 
            if regresarVal(resDir) > int(opIzq):
                print("El indice del arreglo es mayor al declarado")
                sys.exit()
        elif codeOp == "return":
            res = regresarVal(opIzq)
            asignarVal(resDir, res)
        elif codeOp == "parameter":
            nuevaDir = dirFunciones[opDer]["params"][int(resDir)]
            res = regresarVal(opIzq)
            asignarParam(nuevaDir, res)
        elif codeOp == "era":
            directorio = dirFunciones[opIzq]
            nuevaMemLocal = Memoria(directorio["numLocalInt"], directorio["numLocalFloat"], directorio["numLocalChar"], 0)
            nuevaMemTemp = Memoria(directorio["numTempInt"], directorio["numTempFloat"], directorio["numTempChar"], directorio["numTempBool"])
        elif codeOp == "gosub":
            pilaMemLocal.append(memLocal)
            pilaMemTemp.append(memTemp)
            #tempDic = Memoria(dirFunciones["main"]["numTempInt"]
            memLocal = nuevaMemLocal
            memTemp = nuevaMemTemp
            pilaInsPointer.append(insPointer)
            insPointer = dirFunciones[opIzq]["cuad"] - 1
        elif codeOp == "Endfunc":
            memLocal = pilaMemLocal.pop()
            memTemp = pilaMemTemp.pop()
            insPointer = pilaInsPointer.pop()
        insPointer += 1
        
        

def regresarVal(dir):
    global memGlobal
    global memLocal
    global memTemp
    dir = int(dir)
    if dir >= 1000 and dir <= 3999:
        return memGlobal.ints[dir-1000]
    elif dir >= 4000 and dir <= 6999:
        return memGlobal.floats[dir-4000]
    elif dir >= 7000 and dir <= 9999:
        return memGlobal.chars[dir-7000]
    elif dir >= 10000 and dir <= 12999:
        return memLocal.ints[dir-10000]
    elif dir >= 13000 and dir <= 15999:
        return memLocal.floats[dir-13000]
    elif dir >= 16000 and dir <= 18999:
        return memLocal.chars[dir-16000]
    elif dir >= 19000 and dir <= 21999:
        return memTemp.ints[dir-19000]
    elif dir >= 22000 and dir <= 24999:
        return memTemp.floats[dir-22000]
    elif dir >= 25000 and dir <= 27999:
        return memTemp.chars[dir-25000]
    elif dir >= 28000 and dir <= 30999:
        return memTemp.bools[dir-28000]
    elif dir >= 31000:
        dir = str(dir)
        tipo = tabConstantes[dir]["type"]
        if tipo == "int":
            return int(tabConstantes[dir]["value"])
        elif tipo == "float":
            return float(tabConstantes[dir]["value"])  
        elif tipo == "char":
            return removeChar(tabConstantes[dir]["value"])
        elif tipo == "string":
            return removeString(tabConstantes[dir]["value"])

def asignarVal(dir, val):
    global memGlobal
    global memLocal
    global memTemp
    dir = int(dir)
    if dir >= 1000 and dir <= 3999:
        memGlobal.ints[dir-1000] = int(val)
    elif dir >= 4000 and dir <= 6999:
        memGlobal.floats[dir-4000] = float(val)
    elif dir >= 7000 and dir <= 9999:
        memGlobal.chars[dir-7000] = val
    elif dir >= 10000 and dir <= 12999:
        memLocal.ints[dir-10000] = int(val)
    elif dir >= 13000 and dir <= 15999:
        memLocal.floats[dir-13000] = float(val)
    elif dir >= 16000 and dir <= 18999:
        memLocal.chars[dir-16000] = val
    elif dir >= 19000 and dir <= 21999:
        memTemp.ints[dir-19000] = int(val)
    elif dir >= 22000 and dir <= 24999:
        memTemp.floats[dir-22000] = float(val)
    elif dir >= 25000 and dir <= 27999:
        memTemp.chars[dir-25000] = val
    elif dir >= 28000 and dir <= 30999:
        memTemp.bools[dir-28000] = val

def asignarParam(dir, val):
    global nuevaMemLocal
    global nuevaMemTemp
    dir = int(dir)
    if dir >= 10000 and dir <= 12999:
        nuevaMemLocal.ints[dir-10000] = int(val)
    elif dir >= 13000 and dir <= 15999:
        nuevaMemLocal.floats[dir-13000] = float(val)
    elif dir >= 16000 and dir <= 18999:
        nuevaMemLocal.chars[dir-16000] = val
    elif dir >= 19000 and dir <= 21999:
        nuevaMemTemp.ints[dir-19000] = int(val)
    elif dir >= 22000 and dir <= 24999:
        nuevaMemTemp.floats[dir-22000] = float(val)
    elif dir >= 25000 and dir <= 27999:
        nuevaMemTemp.chars[dir-25000] = val
    elif dir >= 28000 and dir <= 30999:
        nuevaMemTemp.bools[dir-28000] = val

def removeChar(char):
    char = char[1:]
    char = char[:-1]
    return char

def removeString(palabra):
    palabra = palabra[1:]
    palabra = palabra[:-1]
    return palabra

'''
"globalInt" : TablaDirecciones(1000, 3999),
    "globalFloat" : TablaDirecciones(4000, 6999),
    "globalChar" : TablaDirecciones(7000, 9999),
    "localInt": TablaDirecciones(10000, 12999),
    "localFloat": TablaDirecciones(13000, 15999),
    "localChar": TablaDirecciones(16000, 18999),
    "tempInt": TablaDirecciones(19000, 21999),
    "tempFloat": TablaDirecciones(22000, 24999),
    "tempChar": TablaDirecciones(25000, 27999),
    "tempBool": TablaDirecciones(28000, 30999),
    "constInt": TablaDirecciones(31000, 33999),
    "constFloat": TablaDirecciones(34000, 36999),
    "constChar": TablaDirecciones(37000, 39999),
    "constString": TablaDirecciones(40000, 42999)
'''

if __name__ == "__main__":
    f=open("codigo.obj", "r")
    fl = f.read()
    f.close()
    ovejota = fl.split("\n")
    readObj(ovejota)
    analizarCuadruplos()
