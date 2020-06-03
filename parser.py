from scaner import tokens
import ply.yacc as yacc
import codecs
from DirFunciones import DirFunciones
from CuboSemantico import CuboSemantico
from Cuadruplo import Cuadruplo
from TablaDirecciones import TablaDirecciones
from TablaConstantes import TablaConstantes
import sys

tipoFuncionLeido = ""
tipoVarLeido = ""
nombreFuncion = ""
nombreVar = ""
listaVariables = []
directorioFunc = DirFunciones()
cuboSem = CuboSemantico()
pilaPoper = []
pilaOp = []
pilaTipos = []
pilaSaltos = []
cuadruplos = Cuadruplo()
dicDirecciones = {
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
}
scopeActual = "global"
tablaConstantes = TablaConstantes()
tieneReturn = False
paramCounter = 0

def p_PROGRAMA(p):
    '''
    PROGRAMA : crearFuncGlobal PROGRAM NAME SEMICOLON scopeGlobal VARS F PRINCIPAL printTodo
    F : FUNCION F
    | empty
    '''

def p_VARS(p):
    '''
    VARS : borrarListaVar VAR V1
    '''
    

def p_V1(p):
    '''
    V1 : TIPO VARIABLEDer V2 SEMICOLON V3
    '''
    

def p_V2(p):
    '''
    V2 : COMMA VARIABLEDer V2
    | empty
    '''

def p_V3(p):
    '''
    V3 : V1
    | empty
    '''
    

def p_FUNCION(p):
    '''
    FUNCION : FUNC TIPO_FUNCION NAME agregarFunc LPAREN borrarListaVar scopeLocal PARAMS agregarParamTable agregarVariables RPAREN V4 agregarLocalVar CUERPO terminarFunc 
    V4 : VARS
    | empty
    '''

def p_PARAMS(p):
    '''
    PARAMS : TIPO NAME agregarVarLista P1
    '''

def p_P1(p):
    '''
    P1 : P2
    | empty
    '''

def p_P2(p):
    '''
    P2 : COMMA PARAMS P1
    '''
    
def p_CUERPO(p):
    '''
    CUERPO : LBRACKET E RBRACKET
    E : E1
    | empty
    E1 : ESTATUTO 
    | ESTATUTO E1
    '''

def p_TIPO(p):
    '''
    TIPO : INT
    | FLOAT
    | CHAR
    '''
    global tipoVarLeido
    tipoVarLeido = p[1]

def p_TIPO_FUNCION(p):
    '''
    TIPO_FUNCION : INT
    | FLOAT
    | CHAR
    | VOID
    '''
    global tipoFuncionLeido
    tipoFuncionLeido = p[1]

def p_PRINCIPAL(p):
    '''
    PRINCIPAL : MAIN LPAREN crearFuncMain RPAREN CUERPO
    '''

def p_VARIABLE(p):
    '''
    VARIABLE : NAME agregarPilaOp E2
    '''
    p[0] = p[1]

def p_E2(p):
    '''
    E2 : LSBRACKET guardarArreglo meterFondoFalso EXP RSBRACKET verificarArreglo quitarFondoFalso
    | empty
    '''

def p_VARIABLEDer(p):
    '''
    VARIABLEDer : NAME agregarVarLista agregarVariables borrarListaVar E2Der
    '''
    p[0] = p[1]

def p_E2Der(p):
    '''
    E2Der : LSBRACKET C_INT declararArray RSBRACKET
    | empty
    '''

def p_ESTATUTO(p):
    '''
    ESTATUTO : ASIGNACION
    | LLAMADA
    | RETORNO
    | LECTURA
    | ESCRITURA
    | CONDICION
    | CICLO_W
    | CICLO_F
    '''

def p_ASIGNACION(p):
    '''
    ASIGNACION : VARIABLE EQUALS meterOperador EXP popIgual SEMICOLON
    '''

def p_LLAMADA(p):
    '''
    LLAMADA : NAME verificarFunc LPAREN meterFondoFalso generarEra E4 verificarParam RPAREN quitarFondoFalso generarGosub SEMICOLON
    E4 : EXP generarParam
    | EXP generarParam COMMA E4
    | empty
    '''

def p_LLAMADAF(p):
    '''
    LLAMADAF : NAME verificarFunc LPAREN meterFondoFalso generarEra E4 verificarParam RPAREN generarGosub quitarFondoFalso
    '''

def p_RETORNO(p):
    '''
    RETORNO : RETURN LPAREN EXP popReturn RPAREN SEMICOLON
    '''

def p_LECTURA(p):
    '''
    LECTURA : READ LPAREN V3 RPAREN SEMICOLON
    V3 : VARIABLE popRead COMMA V3
    | VARIABLE popRead
    '''

def p_ESCRITURA(p):
    '''
    ESCRITURA : PRINT LPAREN E3 RPAREN SEMICOLON
    E3 : S_EXP popPrint
    | S_EXP popPrint COMMA E3
    '''

def p_CONDICION(p):
    '''
    CONDICION : IF LPAREN H_EXP RPAREN gotoIf THEN CUERPO ELSE1 terminarGoto
    ELSE1 : ELSE gotoElse CUERPO
    | empty
    '''

def p_CICLO_W(p):
    '''
    CICLO_W : WHILE agregarWhile LPAREN H_EXP RPAREN DO gotoIf CUERPO terminarWhile
    '''

def p_CICLO_F(p):
    '''
    CICLO_F : FROM agregarWhile VARIABLE agregarFrom EQUALS meterOperador EXP popIgual TO EXP crearCompFrom DO gotoIf CUERPO sumarFrom terminarWhile
    '''

def p_H_EXP(p):
    '''
    H_EXP : T_EXP
    | T_EXP OR H_EXP
    '''

def p_T_EXP(p):
    '''
    T_EXP : G_EXP
    | G_EXP AND T_EXP
    '''

def p_G_EXP(p):
    '''
    G_EXP : EXP B popBool
    B : GREATER_OR_EQUAL meterOperador G_EXP
    | LESS_OR_EQUAL meterOperador G_EXP
    | GREATER_THAN meterOperador G_EXP
    | LESS_THAN meterOperador G_EXP
    | IS_EQUAL meterOperador G_EXP
    | NOT_EQUAL meterOperador G_EXP
    | empty
    '''

def p_S_EXP(p):
    '''
    S_EXP : C_STRING agregarConstString
    | EXP
    '''
    
def p_EXP(p):
    '''
    EXP : TERMINO popSumaResta T 
    T : PLUS meterOperador EXP
    | MINUS meterOperador EXP
    | empty
    '''

def p_TERMINO(p):
    '''
    TERMINO : FACTOR popMultDiv F2 
    F2 : DIVIDE meterOperador TERMINO
    | MULTIPLY meterOperador TERMINO
    | empty
    '''

def p_FACTOR(p):
    '''
    FACTOR : LPAREN meterFondoFalso H_EXP RPAREN quitarFondoFalso
    | C_INT agregarConstInt
    | C_FLOAT agregarConstFloat
    | C_CHAR agregarConstChar
    | VARIABLE
    | LLAMADAF
    '''

def p_empty(p):
    '''
    empty :
    '''
#Puntos Neuralgicos
def p_generarGosub(p):
    ''' generarGosub : '''
    global cuadruplos
    global nombreFuncion
    global directorioFunc
    global tieneReturn
    global tipoFuncionLeido
    global pilaOp
    global pilaTipos
    dirInicial = directorioFunc.obtenerDireccion(nombreFuncion)
    cuadruplos.generarCuad("gosub", nombreFuncion, -1, dirInicial)
    variable = directorioFunc.buscarVariable(nombreFuncion, "global")
    dirVariable = variable["dir"]
    nuevaDir = 0
    print("El tiene return de", nombreFuncion, "es", tieneReturn)
    if tieneReturn == True:
        if tipoFuncionLeido == "int":
            nuevaDir = dicDirecciones["tempInt"].obtenerDir()
        elif tipoFuncionLeido == "float":
            nuevaDir = dicDirecciones["tempFloat"].obtenerDir()
        elif tipoFuncionLeido == "char":
            nuevaDir = dicDirecciones["tempChar"].obtenerDir()
        if nuevaDir == -1:
            print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
            sys.exit()
        cuadruplos.generarCuad("=", dirVariable, -1, nuevaDir)
        pilaOp.append(nuevaDir)
        print("pilaop:", pilaOp)
        pilaTipos.append(tipoFuncionLeido)


def p_verificarParam(p):
    ''' verificarParam : '''
    global paramCounter
    global directorioFunc
    global nombreFuncion
    if directorioFunc.obtenerParam(nombreFuncion, paramCounter) != None:
        print("Syntax error: El número de parametros no es el correcto")
        sys.exit()


def p_generarParam(p):
    ''' generarParam : '''
    global pilaOp
    global pilaTipos
    global directorioFunc
    global nombreFuncion
    global paramCounter
    argumento = pilaOp.pop()
    tipoArgumento = pilaTipos.pop()
    numParams = directorioFunc.obtenerNumParams(nombreFuncion)
    if numParams < paramCounter + 1:
        print("Syntax error: El número de parametros es mayor al requerido")
        sys.exit()
    if directorioFunc.obtenerParam(nombreFuncion, paramCounter) != tipoArgumento:
        print("Type mismatch: El paramentro #", paramCounter+1, "de la función", nombreFuncion, "es del tipo incorrecto")
        sys.exit()
    else:
        paramCounter += 1
        cuadruplos.generarCuad("parameter", argumento, -1, paramCounter)

def p_generarEra(p):
    ''' generarEra : '''
    global nombreFuncion
    global cuadruplos
    global paramCounter
    cuadruplos.generarCuad("era", nombreFuncion, -1, -1)
    paramCounter = 0

def p_verificarFunc(p):
    '''verificarFunc : '''
    global directorioFunc
    global nombreFuncion
    global tipoFuncionLeido
    global tieneReturn
    nombreFuncion = p[-1]
    if directorioFunc.funcionExiste(nombreFuncion) == False:
        print("Syntax error: La funcion", nombreFuncion, "no existe")
        sys.exit()
    tipoFuncionLeido = directorioFunc.obtenerTipoRetorno(nombreFuncion)
    if tipoFuncionLeido != "void":
        tieneReturn = True
    #print("El tipo de funcion leido es", nombreFuncion, tipoFuncionLeido)

def p_terminarFunc(p):
    ''' terminarFunc : '''
    global tipoFuncionLeido
    global tieneReturn
    global cuadruplos
    global directorioFunc
    global nombreFuncion
    global dicDirecciones
    if tipoFuncionLeido != "void" and tieneReturn == False:
        print("Syntax error: La función", nombreFuncion, "necesita de un estatuto return")
        sys.exit()
    
    tieneReturn = False
    cuadruplos.generarCuad("Endfunc", -1, -1, -1)
    directorioFunc.calcularTemporales(nombreFuncion, dicDirecciones["tempInt"].calcularTam(), "int")
    directorioFunc.calcularTemporales(nombreFuncion, dicDirecciones["tempFloat"].calcularTam(), "float")
    directorioFunc.calcularTemporales(nombreFuncion, dicDirecciones["tempChar"].calcularTam(), "char")
    directorioFunc.calcularTemporales(nombreFuncion, dicDirecciones["tempBool"].calcularTam(), "bool")
    dicDirecciones["localInt"].calcularTam()
    dicDirecciones["localFloat"].calcularTam()
    dicDirecciones["localChar"].calcularTam()
    

def p_agregarLocalVar(p):
    ''' agregarLocalVar : '''
    global directorioFunc
    global nombreFuncion
    global cuadruplos
    directorioFunc.calcularLocales(nombreFuncion)
    directorioFunc.agregarDir(nombreFuncion, cuadruplos.contador)

def p_agregarParamTable(p):
    '''agregarParamTable : '''
    global listaVariables
    global directorioFunc
    global nombreFuncion
    directorioFunc.agregarParamTable(nombreFuncion, listaVariables)

def p_guardarArreglo(p):
    '''guardarArreglo : '''
    global pilaOp
    global pilaTipos
    global nombreVar
    global nombreFuncion
    global directorioFunc
    id = pilaOp.pop()
    tipo = pilaTipos.pop()
    variable = directorioFunc.buscarVariableDir(id, nombreFuncion)
    idArray = variable["isArray"]
    if idArray == False:
        print("No se puede indexar una variable que no fue declarada como un arreglo")
        sys.exit()
    else:
        nombreVar = variable
    

def p_verificarArreglo(p):
    '''verificarArreglo : '''
    global cuadruplos
    global pilaOp
    global pilaTipos
    global dicDirecciones
    topOp = pilaOp[-1]
    tamArray = nombreVar["arraySize"]
    dirArray = nombreVar["dir"]
    tipoArray = nombreVar["type"]
    cuadruplos.generarCuad("verify", tamArray ,-1, topOp)
    aux1 = pilaOp.pop()
    tipo = pilaTipos.pop()
    nuevaDir = dicDirecciones["tempInt"].obtenerDir()
    dirArray = str(dirArray)
    dirArray = '(' + dirArray + ')'
    cuadruplos.generarCuad("+", aux1, dirArray, nuevaDir)
    #print("nuevaDir:",nuevaDir)
    pilaOp.append(nuevaDir)
    #print("pilaDeOperandos:", pilaOp)
    pilaTipos.append(tipoArray)

def p_declararArray(p):
    ''' declararArray : '''
    global directorioFunc
    global nombreFuncion
    global nombreVar
    global scopeActual
    global tipoVarLeido
    tamArray = p[-1]
    directorioFunc.agregarArray(nombreFuncion, nombreVar, tamArray)
    nuevaDir = 0
    if scopeActual == "global":
        if tipoVarLeido == "int":
            nuevaDir = dicDirecciones["globalInt"].aumentarDir(tamArray -1)
        elif tipoVarLeido == "float":
            nuevaDir = dicDirecciones["globalFloat"].aumentarDir(tamArray-1)
        elif tipoVarLeido == "char":
            nuevaDir = dicDirecciones["globalChar"].aumentarDir(tamArray-1)
    elif scopeActual == "local":
        if tipoVarLeido == "int":
            nuevaDir = dicDirecciones["localInt"].aumentarDir(tamArray -1)
        elif tipoVarLeido == "float":
            nuevaDir = dicDirecciones["localFloat"].aumentarDir(tamArray -1)
        elif tipoVarLeido == "char":
            nuevaDir = dicDirecciones["localChar"].aumentarDir(tamArray -1)
    if nuevaDir == -1:
        print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
        sys.exit()


def p_agregarFrom(p):
    '''agregarFrom : '''
    global pilaOp
    global pilaTipos
    varFrom = pilaOp.pop()
    tipoVarFrom = pilaTipos.pop()
    for x in range(3):
        pilaOp.append(varFrom)
        pilaTipos.append(tipoVarFrom)
    
def p_crearCompFrom(p):
    '''crearCompFrom : '''
    global tipoVarLeido
    global cuadruplos
    global pilaOp
    global pilaTipos
    global cuboSem
    global dicDirecciones
    limitante = pilaOp.pop()
    tipoLimit = pilaTipos.pop()
    fromVar = pilaOp.pop()
    tipoVar = pilaTipos.pop()
    tipoRes = cuboSem.obtenerSem(tipoVar, tipoLimit, ">")
    if tipoRes == "error":
        print("Type mismatch: Las variables en el from no son compatibles")
        sys.exit()
    else:
        nuevaDir = 0
        if tipoRes == "bool":
            nuevaDir = dicDirecciones["tempBool"].obtenerDir()
        if nuevaDir == -1:
            print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
            sys.exit()
        cuadruplos.generarCuad("<", fromVar, limitante, nuevaDir)
        pilaOp.append(nuevaDir)
        pilaTipos.append(tipoRes)
        

def p_sumarFrom(p):
    '''sumarFrom : '''
    global cuadruplos
    global tablaConstantes
    global dicDirecciones
    global cuboSem
    global pilaTipos
    global pilaOp
    fromVar = pilaOp.pop()
    tipoFromVar = pilaTipos.pop()
    constUno = tablaConstantes.buscarElemento(1)
    if constUno == "ERROR":
        constUno = dicDirecciones["constInt"].obtenerDir()
        tablaConstantes.agregarConstante(1, "int", constUno)
    nuevaDir = 0
    tipoRes = cuboSem.obtenerSem(tipoFromVar, "int", "+")
    if tipoRes == "error":
        print("Type mismatch: Las variables en el from no son compatibles")
        sys.exit()
    else:
        if tipoRes == "int":
            nuevaDir = dicDirecciones["tempInt"].obtenerDir()
        elif tipoRes == "float":
            nuevaDir = dicDirecciones["tempFloat"].obtenerDir()
        elif tipoRes == "char":
            nuevaDir = dicDirecciones["tempChar"].obtenerDir()
        elif tipoRes == "bool":
            nuevaDir = dicDirecciones["tempBool"].obtenerDir()
        if nuevaDir == -1:
            print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
            sys.exit()
    cuadruplos.generarCuad("+", fromVar, constUno, nuevaDir)
    cuadruplos.generarCuad("=", nuevaDir, -1, fromVar)

def p_agregarConstInt(p):
    '''agregarConstInt : '''
    global pilaOp
    global pilaTipos
    global tablaConstantes
    constante = p[-1]
    dirConstante = tablaConstantes.buscarElemento(constante)
    if dirConstante == "ERROR":
        dirConstante = dicDirecciones["constInt"].obtenerDir()
        tablaConstantes.agregarConstante(constante, "int", dirConstante)
        pilaOp.append(dirConstante)
        pilaTipos.append("int")
    else:
        pilaOp.append(dirConstante)
        pilaTipos.append("int")

def p_agregarConstFloat(p):
    '''agregarConstFloat : '''
    global pilaOp
    global pilaTipos
    global tablaConstantes
    constante = p[-1]
    dirConstante = tablaConstantes.buscarElemento(constante)
    if dirConstante == "ERROR":
        dirConstante = dicDirecciones["constFloat"].obtenerDir()
        tablaConstantes.agregarConstante(constante, "float", dirConstante)
        pilaOp.append(dirConstante)
        pilaTipos.append("float")
    else:
        pilaOp.append(dirConstante)
        pilaTipos.append("float")

def p_agregarConstChar(p):
    '''agregarConstChar : '''
    global pilaOp
    global pilaTipos
    global tablaConstantes
    constante = p[-1]
    dirConstante = tablaConstantes.buscarElemento(constante)
    if dirConstante == "ERROR":
        dirConstante = dicDirecciones["constChar"].obtenerDir()
        tablaConstantes.agregarConstante(constante, "char", dirConstante)
        pilaOp.append(dirConstante)
        pilaTipos.append("char")
    else:
        pilaOp.append(dirConstante)
        pilaTipos.append("char")

def p_agregarConstString(p):
    '''agregarConstString : '''
    global pilaOp
    global pilaTipos
    global tablaConstantes
    constante = p[-1]
    dirConstante = tablaConstantes.buscarElemento(constante)
    if dirConstante == "ERROR":
        dirConstante = dicDirecciones["constString"].obtenerDir()
        tablaConstantes.agregarConstante(constante, "string", dirConstante)
        pilaOp.append(dirConstante)
        pilaTipos.append("string")
    else:
        pilaOp.append(dirConstante)
        pilaTipos.append("string")

def p_scopeGlobal(p):
    '''scopeGlobal : '''
    global scopeActual
    scopeActual = "global"

def p_scopeLocal(p):
    '''scopeLocal : '''
    global scopeActual
    scopeActual = "local"

def p_scopeTemp(p):
    '''scopeTemp : '''
    global scopeActual
    scopeActual = "temp"

def p_scopeConst(p):
    '''scopeConst : '''
    global scopeActual
    scopeActual = "const"

def p_gotoIf(p):
    '''gotoIf : '''
    global pilaPoper
    global pilaTipos
    global pilaOp
    global pilaSaltos
    global cuadruplos
    expRes = pilaTipos.pop()
    if expRes != 'bool':
        print("Type Mismatch error: La expresión asignada no es de tipo booleana")
        sys.exit()
    else:
        res = pilaOp.pop()
        cuadruplos.generarCuad("gotof", res, -1, -1)
        pilaSaltos.append(cuadruplos.contador-1)

def p_terminaGoto(p):
    '''terminarGoto : '''
    global pilaSaltos
    global cuadruplos
    final = pilaSaltos.pop()
    cuadruplos.rellenar(final, cuadruplos.contador)

def p_agregarWhile(p):
    ''' agregarWhile : '''
    global pilaSaltos
    pilaSaltos.append(cuadruplos.contador)

def p_terminaWhile(p):
    '''terminarWhile : '''
    global pilaSaltos
    global cuadruplos
    final = pilaSaltos.pop()
    retorno = pilaSaltos.pop()
    cuadruplos.generarCuad("goto", -1, -1, retorno)
    cuadruplos.rellenar(final, cuadruplos.contador)

def p_gotoElse(p):
    '''gotoElse : '''
    global pilaSaltos
    global cuadruplos
    cuadruplos.generarCuad("goto",-1,-1,-1)
    falso = pilaSaltos.pop()
    pilaSaltos.append(cuadruplos.contador - 1)
    #print(cuadruplos.contador)
    #cuadruplos.printCuads()
    cuadruplos.rellenar(falso, cuadruplos.contador)

def p_meterFondoFalso(p):
    '''meterFondoFalso : '''
    global pilaPoper
    pilaPoper.append('(')

def p_quitarFondoFalso(p):
    '''quitarFondoFalso : '''
    global pilaPoper
    if len(pilaPoper) > 0:
        topPoper = pilaPoper[-1]
    else: topPoper = "None"
    if topPoper == '(':
        pilaPoper.pop()

def p_agregarPilaOp(p):
    '''  agregarPilaOp : '''
    global directorioFunc
    global nombreFuncion
    global pilaOp
    global pilaTipos
    varName = p[-1]
    variable = directorioFunc.buscarVariable(varName, nombreFuncion) 
    if variable != "ERROR":
        pilaOp.append(variable["dir"])
        pilaTipos.append(variable["type"])
    else:
        print("La variable", varName, "no ha sido declarada")
        sys.exit()

def p_popPrint(p):
    '''popPrint : '''
    global pilaOp
    global cuadruplos
    elem = pilaOp.pop()
    cuadruplos.generarCuad("print", -1, -1, elem)

def p_popRead(p):
    '''popRead : '''
    global pilaOp
    global cuadruplos
    elem = pilaOp.pop()
    cuadruplos.generarCuad("read", -1, -1, elem)

def p_popReturn(p):
    '''popReturn : '''
    global pilaOp
    global cuadruplos
    global tieneReturn
    global pilaTipos
    global tipoFuncionLeido
    global directorioFunc
    global nombreFuncion
    elem = pilaOp.pop()
    elemTipo = pilaTipos.pop()
    tieneReturn = True
    if tipoFuncionLeido != elemTipo:
        print("Type mismatch: El elemento retornado es diferente al tipo de función declarada")
        sys.exit()
    cuadruplos.generarCuad("return", -1, -1, elem)
    variable = directorioFunc.buscarVariable(nombreFuncion, "global")
    dirVariable = variable["dir"]
    cuadruplos.generarCuad("=", elem, -1, dirVariable)

def p_popBool(p):
    '''popBool : '''
    global pilaPoper
    global pilaOp
    global pilaTipos
    global cuadruplos
    global cuboSem
    global dicDirecciones
    if len(pilaPoper) > 0:
        topPoper = pilaPoper[-1]
    else: topPoper = "None"
    if topPoper != '(':
        if  topPoper == '<=' or topPoper == '<' or topPoper == '>=' or topPoper == '>' or topPoper == '==' or topPoper == '!=':
            op = pilaPoper.pop()
            opdo_der = pilaOp.pop()
            opdo_izq = pilaOp.pop()
            tipo_der = pilaTipos.pop()
            tipo_izq = pilaTipos.pop()
            tipoRes = cuboSem.obtenerSem(tipo_izq, tipo_der, op)
            if  tipoRes == "error":
                print("Type mismatch error: Los tipos de los operandos no son compatibles")
                sys.exit()
            nuevaDir = 0
            if tipoRes == "int":
                nuevaDir = dicDirecciones["tempInt"].obtenerDir()
            elif tipoRes == "float":
                nuevaDir = dicDirecciones["tempFloat"].obtenerDir()
            elif tipoRes == "char":
                nuevaDir = dicDirecciones["tempChar"].obtenerDir()
            elif tipoRes == "bool":
                nuevaDir = dicDirecciones["tempBool"].obtenerDir()
            if nuevaDir == -1:
                print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
                sys.exit()
            cuadruplos.generarCuad(op, opdo_izq, opdo_der, nuevaDir)
            pilaOp.append(nuevaDir)
            pilaTipos.append(tipoRes)

def p_popIgual(p):
    '''popIgual : '''
    global pilaPoper
    global pilaOp
    global pilaTipos
    global cuadruplos
    global cuboSem
    if len(pilaPoper) > 0:
        topPoper = pilaPoper[-1]
    else: topPoper = "None"
    if topPoper != '(':
        if  topPoper == '=':
            op = pilaPoper.pop()
            opdo_der = pilaOp.pop()
            opdo_izq = pilaOp.pop()
            tipo_der = pilaTipos.pop()
            tipo_izq = pilaTipos.pop()
            tipoRes = cuboSem.obtenerSem(tipo_izq, tipo_der, op)
            if  tipoRes == "error":
                print(op, opdo_izq, opdo_der, tipo_izq, tipo_der, tipoRes)
                print("Type mismatch error: Se esta asignando un tipo de variable diferente a la declarada")
                sys.exit()
            nuevaDir = 0
            if tipoRes == "int":
                nuevaDir = dicDirecciones["tempInt"].obtenerDir()
            elif tipoRes == "float":
                nuevaDir = dicDirecciones["tempFloat"].obtenerDir()
            elif tipoRes == "char":
                nuevaDir = dicDirecciones["tempChar"].obtenerDir()
            elif tipoRes == "bool":
                nuevaDir = dicDirecciones["tempBool"].obtenerDir()
            if nuevaDir == -1:
                print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
                sys.exit()
            cuadruplos.generarCuad(op, opdo_der, -1, opdo_izq)
            #pilaOp.append(nuevaDir)
            #pilaTipos.append(tipoRes)

def p_popMultDiv(p):
    '''popMultDiv : '''
    global pilaPoper
    global pilaOp
    global pilaTipos
    global cuadruplos
    global cuboSem
    if len(pilaPoper) > 0:
        topPoper = pilaPoper[-1]
    else: topPoper = "None"
    if topPoper != '(':
        if  topPoper == '*' or topPoper == '/':
            op = pilaPoper.pop()
            opdo_der = pilaOp.pop()
            opdo_izq = pilaOp.pop()
            tipo_der = pilaTipos.pop()
            tipo_izq = pilaTipos.pop()
            tipoRes = cuboSem.obtenerSem(tipo_izq, tipo_der, op)
            if  tipoRes == "error":
                print("La muchacha no baila con el señor")
                sys.exit()
            nuevaDir = 0
            if tipoRes == "int":
                nuevaDir = dicDirecciones["tempInt"].obtenerDir()
            elif tipoRes == "float":
                nuevaDir = dicDirecciones["tempFloat"].obtenerDir()
            elif tipoRes == "char":
                nuevaDir = dicDirecciones["tempChar"].obtenerDir()
            elif tipoRes == "bool":
                nuevaDir = dicDirecciones["tempBool"].obtenerDir()
            if nuevaDir == -1:
                print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
                sys.exit()
            cuadruplos.generarCuad(op, opdo_izq, opdo_der, nuevaDir)
            pilaOp.append(nuevaDir)
            pilaTipos.append(tipoRes)

def p_popSumaResta(p):
    '''popSumaResta : '''
    global pilaPoper
    global pilaOp
    global pilaTipos
    global cuadruplos
    global cuboSem
    if len(pilaPoper) > 0:
        topPoper = pilaPoper[-1]
    else: topPoper = "None"
    if topPoper != '(':
        if  topPoper == '+' or topPoper == '-':
            op = pilaPoper.pop()
            opdo_der = pilaOp.pop()
            opdo_izq = pilaOp.pop()
            tipo_der = pilaTipos.pop()
            tipo_izq = pilaTipos.pop()
            tipoRes = cuboSem.obtenerSem(tipo_izq, tipo_der, op)
            if  tipoRes == "error":
                print("La muchacha no baila con el señor")
                sys.exit()
            nuevaDir = 0
            if tipoRes == "int":
                nuevaDir = dicDirecciones["tempInt"].obtenerDir()
            elif tipoRes == "float":
                nuevaDir = dicDirecciones["tempFloat"].obtenerDir()
            elif tipoRes == "char":
                nuevaDir = dicDirecciones["tempChar"].obtenerDir()
            elif tipoRes == "bool":
                nuevaDir = dicDirecciones["tempBool"].obtenerDir()
            if nuevaDir == -1:
                print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
                sys.exit()
            cuadruplos.generarCuad(op, opdo_izq, opdo_der, nuevaDir)
            pilaOp.append(nuevaDir)
            pilaTipos.append(tipoRes)

def p_meterIgual(p):
    ''' meterIgual : '''
    global pilaPoper
    pilaPoper.append(p[-1])

def p_meterBool(p):
    ''' meterBool : '''
    global pilaPoper
    pilaPoper.append(p[-1])

def p_meterMultDiv(p):
    ''' meterMultDiv : '''
    global pilaPoper
    pilaPoper.append(p[-1])

def p_meterSumaResta(p):
    ''' meterSumaResta : '''
    global pilaPoper
    pilaPoper.append(p[-1])

def p_meterOperador(p):
    ''' meterOperador : '''
    global pilaPoper
    pilaPoper.append(p[-1])


def p_crearFuncGlobal(p):
    '''crearFuncGlobal : '''
    global directorioFunc
    global nombreFuncion
    nombreFuncion = "global"
    directorioFunc.agregarFuncion(nombreFuncion, "void")

def p_crearFuncMain(p):
    '''crearFuncMain : '''
    global directorioFunc
    global nombreFuncion
    nombreFuncion = "main"
    directorioFunc.agregarFuncion(nombreFuncion, "void")

def p_agregarFunc(p):
    ''' agregarFunc : '''
    global directorioFunc
    global nombreFuncion
    global tipoFuncionLeido
    nombreFuncion = p[-1]
    resultado = directorioFunc.agregarFuncion(nombreFuncion, tipoFuncionLeido)
    if resultado == "global":
        print("No se puede declarar una funcion con el nombre de global")
        sys.exit()
    elif resultado == "main":
        print("No se puede declarar una funcion con el nombre de main")
        sys.exit()
    elif resultado != "OK":
        print("Ya existe una funcion con el nombre ", resultado)
        sys.exit()
    nuevaDir = 0
    if tipoFuncionLeido == "int":
        nuevaDir = dicDirecciones["globalInt"].obtenerDir()
    elif tipoFuncionLeido == "float":
        nuevaDir = dicDirecciones["globalFloat"].obtenerDir()
    elif tipoFuncionLeido == "char":
        nuevaDir = dicDirecciones["globalChar"].obtenerDir()
    if nuevaDir == -1:
        print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
        sys.exit()
    directorioFunc.agregarVariables("global", [[nombreFuncion, tipoFuncionLeido, nuevaDir]])

def p_agregarVariables(p):
    '''agregarVariables : '''
    global directorioFunc
    global listaVariables
    global nombreFuncion
    print(listaVariables)
    resultado = directorioFunc.agregarVariables(nombreFuncion, listaVariables)
    if resultado != "OK":
        print("Ya existe una variable con el nombre", resultado)
        sys.exit()

def p_printFunciones(p):
    '''printFunciones : '''
    global directorioFunc
    directorioFunc.printFunciones()

def p_printTodo(p):
    '''printTodo : '''
    global directorioFunc
    global cuadruplos
    global pilaOp
    directorioFunc.printTodo()
    cuadruplos.printCuads()

def p_agregarVarLista(p):
    '''agregarVarLista : '''
    global listaVariables
    global nombreVar
    global tipoVarLeido
    global dicDirecciones
    global directorioFunc
    global nombreFuncion
    global scopeActual
    nombreVar = p[-1]
    nuevaDir = 0
    if scopeActual == "global":
        if tipoVarLeido == "int":
            nuevaDir = dicDirecciones["globalInt"].obtenerDir()
        elif tipoVarLeido == "float":
            nuevaDir = dicDirecciones["globalFloat"].obtenerDir()
        elif tipoVarLeido == "char":
            nuevaDir = dicDirecciones["globalChar"].obtenerDir()
    elif scopeActual == "local":
        if tipoVarLeido == "int":
            nuevaDir = dicDirecciones["localInt"].obtenerDir()
        elif tipoVarLeido == "float":
            nuevaDir = dicDirecciones["localFloat"].obtenerDir()
        elif tipoVarLeido == "char":
            nuevaDir = dicDirecciones["localChar"].obtenerDir()
    if nuevaDir == -1:
        print("Stack overflow: Sobrepasaste el espacio de memoria para las variables")
        sys.exit()
    listaVariables.append([nombreVar, tipoVarLeido, nuevaDir])
    


def p_borrarListaVar(p):
    ''' borrarListaVar : '''
    global listaVariables
    del listaVariables[:]

def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print(f"Syntax error: Unexpected {token}")


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'EQUALS'),
    ('left', 'AND', 'OR'),
)

parser = yacc.yacc()

""" with open('prueba.txt', 'r') as file:
    data = file.read().replace('\n', '') """


filename = "prueba.txt"

f = open('prueba.txt','r')
data = f.read()
f.close()

parser.parse(data)

""" while True:
    try:
        s = input('')
    except EOFError:
        break """
