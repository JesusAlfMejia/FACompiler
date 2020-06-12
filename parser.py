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
dirParamCounter = {}
pilaLlamadasFuncion = []
pilaCounter = []

def p_PROGRAMA(p):
    '''
    PROGRAMA : crearFuncGlobal PROGRAM NAME SEMICOLON scopeGlobal VARS F agregarLocalVarGlobal PRINCIPAL printTodo
    F : FUNCION F
    | empty
    '''

def p_VARS(p):
    '''
    VARS : borrarListaVar VAR V1
    | empty
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
    FUNCION : FUNC TIPO_FUNCION NAME agregarFunc LPAREN borrarListaVar scopeLocal PARAMS agregarParamTable agregarVariables RPAREN VARS agregarLocalVar CUERPO terminarFunc 
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
    PRINCIPAL : MAIN LPAREN crearFuncMain RPAREN CUERPO terminarFunc
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
    LLAMADA : NAME verificarFuncVoid LPAREN meterFondoFalso generarEra E4 verificarParam RPAREN quitarFondoFalso generarGosub SEMICOLON
    E4 : EXP generarParam
    | EXP generarParam COMMA E4
    | empty
    '''

def p_LLAMADAF(p):
    '''
    LLAMADAF : NAME verificarFunc LPAREN meterFondoFalso generarEra E4 verificarParam RPAREN quitarFondoFalso verificarLlamada generarGosub
    '''

def p_RETORNO(p):
    '''
    RETORNO : RETURN LPAREN EXP popReturn RPAREN SEMICOLON
    '''

def p_LECTURA(p):
    '''
    LECTURA : READ LPAREN V4 RPAREN SEMICOLON
    V4 : VARIABLE popRead COMMA V4
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
    CICLO_F : FROM VARIABLE agregarFrom EQUALS meterOperador EXP popIgual agregarWhile TO EXP crearCompFrom DO gotoIf CUERPO sumarFrom terminarWhile
    '''

def p_H_EXP(p):
    '''
    H_EXP : T_EXP
    | T_EXP OR meterOperador H_EXP popComp
    '''

def p_T_EXP(p):
    '''
    T_EXP : G_EXP
    | G_EXP AND meterOperador T_EXP popComp
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

#Crea el cuadruplo gosub y otro cuadruplo con el operador "=" donde se le asigna la dirección de la variable global con el nombre de la función a una dirección temporal
def p_generarGosub(p):
    ''' generarGosub : '''
    global cuadruplos
    global pilaLlamadasFuncion
    global directorioFunc
    global tieneReturn
    global tipoFuncionLeido
    global pilaOp
    global pilaTipos
    global pilaCounter
    nombreFuncion = pilaLlamadasFuncion.pop()
    dirInicial = directorioFunc.obtenerDireccion(nombreFuncion)
    cuadruplos.generarCuad("gosub", nombreFuncion, -1, dirInicial)
    variable = directorioFunc.buscarVariable(nombreFuncion, "global")
    dirVariable = variable["dir"]
    nuevaDir = 0
    if pilaCounter:
        pilaCounter.pop()
    if tieneReturn == True:
        if tipoFuncionLeido == "int":
            nuevaDir = dicDirecciones["tempInt"].obtenerDir()
        elif tipoFuncionLeido == "float":
            nuevaDir = dicDirecciones["tempFloat"].obtenerDir()
        elif tipoFuncionLeido == "char":
            nuevaDir = dicDirecciones["tempChar"].obtenerDir()
        if nuevaDir == -1:
            print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea:", p.lineno(0))
            sys.exit()
        cuadruplos.generarCuad("=", dirVariable, -1, nuevaDir)
        pilaOp.append(nuevaDir)
        pilaTipos.append(tipoFuncionLeido)

#Verifica que llamada no sea de tipo void
def p_verificarLlamada(p):
    '''verificarLlamada : '''
    global pilaPoper
    global pilaLlamadasFuncion
    global tieneReturn
    nombreFuncion = pilaLlamadasFuncion[-1]
    if pilaPoper and tieneReturn == False:
        print("La funcion", nombreFuncion,"es de tipo void y no puede ser asignada en linea", p.lineno(0))
        sys.exit()

#Verifica que el número de parametros asignados sea igual al de los que fueron declarados en la función
def p_verificarParam(p):
    ''' verificarParam : '''
    global dirParamCounter
    global directorioFunc
    global pilaLlamadasFuncion
    global pilaCounter
    nombreFuncion = pilaLlamadasFuncion[-1]
    if directorioFunc.obtenerParam(nombreFuncion, pilaCounter[-1]) != None:
        print("Syntax error: El numero de parametros en la funcion", nombreFuncion, "no es el correcto en linea", p.lineno(0))
        sys.exit()

#Verifica que los parametros sean del mismo tipo que con los que fueron declarados y que no sobrepase el número de posibles parametros
def p_generarParam(p):
    ''' generarParam : '''
    global pilaOp
    global pilaTipos
    global directorioFunc
    global pilaLlamadasFuncion
    global dirParamCounter
    global pilaCounter
    global cuadruplos
    nombreFuncion = pilaLlamadasFuncion[-1]
    argumento = pilaOp.pop()
    tipoArgumento = pilaTipos.pop()
    numParams = directorioFunc.obtenerNumParams(nombreFuncion)
    if numParams < pilaCounter[-1] + 1:
        print("Syntax error: El numero de parametros en la funcion",nombreFuncion,"es mayor al requerido en linea", p.lineno(0))
        sys.exit()
    if directorioFunc.obtenerParam(nombreFuncion, pilaCounter[-1]) != tipoArgumento:
        print("Type mismatch: El paramentro #", pilaCounter[-1]+1, "de la funcion", nombreFuncion, "es del tipo incorrecto en linea", p.lineno(0))
        sys.exit()
    else:
        pilaCounter[-1] += 1
        cuadruplos.generarCuad("parameter", argumento, nombreFuncion, pilaCounter[-1])

#Genera el cuadruplo era y agrega un contador a la pila de contadores de parametros
def p_generarEra(p):
    ''' generarEra : '''
    global cuadruplos
    global dirParamCounter
    global pilaLlamadasFuncion
    global pilaCounter
    nombreFuncion = pilaLlamadasFuncion[-1]
    cuadruplos.generarCuad("era", nombreFuncion, -1, -1)
    pilaCounter.append(0)

#Verifica que la función no exista previamente y si tiene un tipo de retorno diferente a void setea la variable tieneReturn a True
def p_verificarFunc(p):
    '''verificarFunc : '''
    global directorioFunc
    global pilaLlamadasFuncion
    global tipoFuncionLeido
    global tieneReturn
    pilaLlamadasFuncion.append(p[-1])
    nombreFuncion = pilaLlamadasFuncion[-1]
    if directorioFunc.funcionExiste(nombreFuncion) == False:
        print("Syntax error: La funcion", nombreFuncion, "no existe en linea:", p.lineno(0))
        sys.exit()
    tipoFuncionLeido = directorioFunc.obtenerTipoRetorno(nombreFuncion)
    if tipoFuncionLeido != "void":
        tieneReturn = True

#Verifica que la función exista y que si la función tiene un valor de retorno entones debe estar asignada a alguna dirección
def p_verificarFuncVoid(p):
    '''verificarFuncVoid : '''
    global directorioFunc
    global pilaLlamadasFuncion
    global tipoFuncionLeido
    global tieneReturn
    pilaLlamadasFuncion.append(p[-1])
    nombreFuncion = pilaLlamadasFuncion[-1]
    if tipoFuncionLeido != "void":
        print("La funcion", nombreFuncion, "tiene un valor de retorno y necesita ser asignado en linea", p.lineno(0))
        sys.exit()
    if directorioFunc.funcionExiste(nombreFuncion) == False:
        print("Syntax error: La funcion", nombreFuncion, "no existe en linea:", p.lineno(0))
        sys.exit()
    tipoFuncionLeido = directorioFunc.obtenerTipoRetorno(nombreFuncion)
    if tipoFuncionLeido != "void":
        tieneReturn = True
    
#Verifica que si la función es diferente a void que tenga un estatuto return y crea el cuadruplo Endfunc
def p_terminarFunc(p):
    ''' terminarFunc : '''
    global tipoFuncionLeido
    global tieneReturn
    global cuadruplos
    global directorioFunc
    global nombreFuncion
    global dicDirecciones
    if tipoFuncionLeido != "void" and tieneReturn == False:
        print("Syntax error: La funcion", nombreFuncion, "necesita de un estatuto return en linea", p.lineno(0))
        sys.exit()
    
    tieneReturn = False
    if nombreFuncion != "main":
        cuadruplos.generarCuad("Endfunc", -1, -1, -1)
    directorioFunc.calcularTemporales(nombreFuncion, dicDirecciones["tempInt"].calcularTam(), "int")
    directorioFunc.calcularTemporales(nombreFuncion, dicDirecciones["tempFloat"].calcularTam(), "float")
    directorioFunc.calcularTemporales(nombreFuncion, dicDirecciones["tempChar"].calcularTam(), "char")
    directorioFunc.calcularTemporales(nombreFuncion, dicDirecciones["tempBool"].calcularTam(), "bool")
    dicDirecciones["localInt"].calcularTam()
    dicDirecciones["localFloat"].calcularTam()
    dicDirecciones["localChar"].calcularTam()

    
#Agrega las variables locales que necesitará la función en ejecución 
def p_agregarLocalVar(p):
    ''' agregarLocalVar : '''
    global directorioFunc
    global nombreFuncion
    global cuadruplos
    directorioFunc.calcularLocales(nombreFuncion)
    directorioFunc.agregarDir(nombreFuncion, cuadruplos.contador)

#Calcula las variables globales que se necesitarán en la ejecución
def p_agregarLocalVarGlobal(p):
    ''' agregarLocalVarGlobal : '''
    global directorioFunc
    global nombreFuncion
    global cuadruplos
    directorioFunc.calcularLocales("global")

#Agrega los parametros declarados a la función que se encuentra en el directorio de funciones
def p_agregarParamTable(p):
    '''agregarParamTable : '''
    global listaVariables
    global directorioFunc
    global nombreFuncion
    directorioFunc.agregarParamTable(nombreFuncion, listaVariables)

#Verifica que la variable que se llama sea un arreglo 
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
        print("No se puede indexar una variable que no fue declarada como un arreglo en linea", p.lineno(0))
        sys.exit()
    else:
        nombreVar = variable
    
#Agrega el cuadruplo de verify y de addArray
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
    cuadruplos.generarCuad("addArray", aux1, dirArray, nuevaDir)
    nuevaDir = str(nuevaDir)
    nuevaDir = "(" + nuevaDir + ")"
    pilaOp.append(nuevaDir)
    pilaTipos.append(tipoArray)

#Agrega el array declarado a la función en el directorio de funciones
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
        print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea:", p.lineno(0))
        sys.exit()

#Añade 3 direcciones de variables a la pila de operandos para ser ejecutados por el from
def p_agregarFrom(p):
    '''agregarFrom : '''
    global pilaOp
    global pilaTipos
    varFrom = pilaOp.pop()
    tipoVarFrom = pilaTipos.pop()
    for x in range(3):
        pilaOp.append(varFrom)
        pilaTipos.append(tipoVarFrom)
    
#Agrega el cuadruplo < para verificar que la variable de from no sea mayor a la expresión escrita
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
        print("Type mismatch: Las variables en el from no son compatibles en linea:", p.lineno(0))
        sys.exit()
    else:
        nuevaDir = 0
        if tipoRes == "bool":
            nuevaDir = dicDirecciones["tempBool"].obtenerDir()
        if nuevaDir == -1:
            print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea", p.lineno(0))
            sys.exit()
        cuadruplos.generarCuad("<", fromVar, limitante, nuevaDir)
        pilaOp.append(nuevaDir)
        pilaTipos.append(tipoRes)
        
#Suma por 1 a la variable declarada en el from y genera los cuadruplos correspondientes
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
        print("Type mismatch: Las variables en el from no son compatibles en linea", p.lineno(0))
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
            print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea", p.lineno(0))
            sys.exit()
    cuadruplos.generarCuad("+", fromVar, constUno, nuevaDir)
    cuadruplos.generarCuad("=", nuevaDir, -1, fromVar)

#Agrega una constante entera a la tabla de constantes y lo añade a la pila de operandos
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

#Agrega una constante flotante a la tabla de constantes y lo añade a la pila de operandos
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

#Agrega una constante caracter a la tabla de constantes y lo añade a la pila de operandos
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

#Agrega una constante string a la tabla de constantes y lo añade a la pila de operandos
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

#Cambia la variable scopeActual a "global"
def p_scopeGlobal(p):
    '''scopeGlobal : '''
    global scopeActual
    scopeActual = "global"

#Cambia la variable scopeActual a "local"
def p_scopeLocal(p):
    '''scopeLocal : '''
    global scopeActual
    scopeActual = "local"

#Cambia la variable scopeActual a "temp"
def p_scopeTemp(p):
    '''scopeTemp : '''
    global scopeActual
    scopeActual = "temp"

#Cambia la variable scopeActual a "const"
def p_scopeConst(p):
    '''scopeConst : '''
    global scopeActual
    scopeActual = "const"

#Crea el cuadruplo gotof y añade el contador actual a la pila de saltos
def p_gotoIf(p):
    '''gotoIf : '''
    global pilaPoper
    global pilaTipos
    global pilaOp
    global pilaSaltos
    global cuadruplos
    expRes = pilaTipos.pop()
    if expRes != 'bool':
        print("Type Mismatch error: La expresión asignada no es de tipo booleana en linea:", p.lineno(0))
        sys.exit()
    else:
        res = pilaOp.pop()
        cuadruplos.generarCuad("gotof", res, -1, -1)
        pilaSaltos.append(cuadruplos.contador-1)

#Rellena el cuadruplo con el ultimo numero que se encuentra en la pila de saltos
def p_terminaGoto(p):
    '''terminarGoto : '''
    global pilaSaltos
    global cuadruplos
    final = pilaSaltos.pop()
    cuadruplos.rellenar(final, cuadruplos.contador)

#Agrega el contador de cuadruplo actual a la pila de saltos
def p_agregarWhile(p):
    ''' agregarWhile : '''
    global pilaSaltos
    pilaSaltos.append(cuadruplos.contador)

#Crea el cuadruplo goto y lo rellena con los dos ultimos elementos de la pila de saltos
def p_terminaWhile(p):
    '''terminarWhile : '''
    global pilaSaltos
    global cuadruplos
    final = pilaSaltos.pop()
    retorno = pilaSaltos.pop()
    cuadruplos.generarCuad("goto", -1, -1, retorno)
    cuadruplos.rellenar(final, cuadruplos.contador)

#Crea el cuadruplo goto y lo rellena con el ultimo elemento de la pila de saltos
def p_gotoElse(p):
    '''gotoElse : '''
    global pilaSaltos
    global cuadruplos
    cuadruplos.generarCuad("goto",-1,-1,-1)
    falso = pilaSaltos.pop()
    pilaSaltos.append(cuadruplos.contador - 1)
    cuadruplos.rellenar(falso, cuadruplos.contador)

# Añade un fondo falso a la pila de operandos con el simbolo "("
def p_meterFondoFalso(p):
    '''meterFondoFalso : '''
    global pilaPoper
    pilaPoper.append('(')

#Elimina el fondo falso de la pila de operandos
def p_quitarFondoFalso(p):
    '''quitarFondoFalso : '''
    global pilaPoper
    if len(pilaPoper) > 0:
        topPoper = pilaPoper[-1]
    else: topPoper = "None"
    if topPoper == '(':
        pilaPoper.pop()

#Agrega un elemento a la pila de operandos y verifica que la variable haya sido declarada
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
        print("La variable", varName, "no ha sido declarada en linea", p.lineno(0))
        sys.exit()

#Crea el cuadruplo print
def p_popPrint(p):
    '''popPrint : '''
    global pilaOp
    global cuadruplos
    elem = pilaOp.pop()
    tipo = pilaTipos.pop()
    cuadruplos.generarCuad("print", -1, -1, elem)

#Crea el cuadruplo read
def p_popRead(p):
    '''popRead : '''
    global pilaOp
    global cuadruplos
    elem = pilaOp.pop()
    cuadruplos.generarCuad("read", -1, -1, elem)

#Crea el cuadruplo return
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
        print("Type mismatch: El elemento retornado es diferente al tipo de funcion declarada en linea", p.lineno(0))
        sys.exit()
    variable = directorioFunc.buscarVariable(nombreFuncion, "global")
    dirVariable = variable["dir"]
    cuadruplos.generarCuad("return", elem, -1, dirVariable)
    #cuadruplos.generarCuad("=", elem, -1, dirVariable)

#Crea el cuadruplo para los operadores && y || 
def p_popComp(p):
    '''popComp : '''
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
        if  topPoper == '&&' or topPoper == '||':
            op = pilaPoper.pop()
            opdo_der = pilaOp.pop()
            opdo_izq = pilaOp.pop()
            tipo_der = pilaTipos.pop()
            tipo_izq = pilaTipos.pop()
            tipoRes = cuboSem.obtenerSem(tipo_izq, tipo_der, op)
            if  tipoRes == "error":
                print("Type mismatch error: Los tipos de los operandos no son compatibles en linea:", p.lineno(0))
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
                print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea", p.lineno(0))
                sys.exit()
            cuadruplos.generarCuad(op, opdo_izq, opdo_der, nuevaDir)
            pilaOp.append(nuevaDir)
            pilaTipos.append(tipoRes)

#Crea el cuadruplo para las operadores booleanos
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
                print("Type mismatch error: Los tipos de los operandos no son compatibles en linea", p.lineno(0))
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
                print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea", p.lineno(0))
                sys.exit()
            cuadruplos.generarCuad(op, opdo_izq, opdo_der, nuevaDir)
            pilaOp.append(nuevaDir)
            pilaTipos.append(tipoRes)

#Crea el cuadruplo para el operador "="
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
                print("Type mismatch error: Se esta asignando un tipo de variable diferente a la declarada en linea:", p.lineno(0))
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
                print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea", p.lineno(0))
                sys.exit()
            cuadruplos.generarCuad(op, opdo_der, -1, opdo_izq)
            #pilaOp.append(nuevaDir)
            #pilaTipos.append(tipoRes)

#Crea el cuadruplo para los operadores "*" y "/"
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
                print("La muchacha no baila con el señor en linea:", p.lineno(0))
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
                print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea", p.lineno(0))
                sys.exit()
            cuadruplos.generarCuad(op, opdo_izq, opdo_der, nuevaDir)
            pilaOp.append(nuevaDir)
            pilaTipos.append(tipoRes)

#Crea el cuadruplo para los operadores "+" y "-"
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
                print("La muchacha no baila con el señor en linea", p.lineno(0))
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
                print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea:", p.lineno(0))
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

#Añade el operador leido a la pila Poper
def p_meterOperador(p):
    ''' meterOperador : '''
    global pilaPoper
    pilaPoper.append(p[-1])

#Crea la funcion global en el directorio de funciones
def p_crearFuncGlobal(p):
    '''crearFuncGlobal : '''
    global directorioFunc
    global nombreFuncion
    nombreFuncion = "global"
    directorioFunc.agregarFuncion(nombreFuncion, "void")

#Crea la funcion main en el directorio de funciones
def p_crearFuncMain(p):
    '''crearFuncMain : '''
    global directorioFunc
    global nombreFuncion
    global cuadruplos
    global tipoFuncionLeido
    nombreFuncion = "main"
    tipoFuncionLeido = "void"
    directorioFunc.agregarFuncion(nombreFuncion, "void")
    directorioFunc.agregarDir(nombreFuncion, cuadruplos.contador)

#Agrega la función declarada al directorio de funciones y agrega una variable global con el mismo nombre
def p_agregarFunc(p):
    ''' agregarFunc : '''
    global directorioFunc
    global nombreFuncion
    global tipoFuncionLeido
    nombreFuncion = p[-1]
    resultado = directorioFunc.agregarFuncion(nombreFuncion, tipoFuncionLeido)
    if resultado == "global":
        print("No se puede declarar una funcion con el nombre de global en linea:", p.lineno(0))
        sys.exit()
    elif resultado == "main":
        print("No se puede declarar una funcion con el nombre de main", p.lineno(0))
        sys.exit()
    elif resultado != "OK":
        print("Ya existe una funcion con el nombre ", resultado, "en linea" , p.lineno(0))
        sys.exit()
    nuevaDir = 0
    if tipoFuncionLeido == "int":
        nuevaDir = dicDirecciones["globalInt"].obtenerDir()
    elif tipoFuncionLeido == "float":
        nuevaDir = dicDirecciones["globalFloat"].obtenerDir()
    elif tipoFuncionLeido == "char":
        nuevaDir = dicDirecciones["globalChar"].obtenerDir()
    if nuevaDir == -1:
        print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea", p.lineno(0))
        sys.exit()
    directorioFunc.agregarVariables("global", [[nombreFuncion, tipoFuncionLeido, nuevaDir]])

#Añade las variables que se encuentran en la lista de variables a la función correspondiente
def p_agregarVariables(p):
    '''agregarVariables : '''
    global directorioFunc
    global listaVariables
    global nombreFuncion
    resultado = directorioFunc.agregarVariables(nombreFuncion, listaVariables)
    if resultado != "OK":
        print("Ya existe una variable con el nombre", resultado, "en linea:", p.lineno(0))
        sys.exit()

#Imprime las funciones que se encuentra en el directorio de funciones
def p_printFunciones(p):
    '''printFunciones : '''
    global directorioFunc
    directorioFunc.printFunciones()

#Exporta todos los elementos de los cuadruplos, tabla de constantes y directorio de funciones al archivo codigo.obj
def p_printTodo(p):
    '''printTodo : '''
    global directorioFunc
    global cuadruplos
    global pilaOp
    #directorioFunc.printTodo()
    #cuadruplos.printCuads()
    #tablaConstantes.printConstantes()
    filename = "codigo.obj"
    cuadruplos.exportarCuad(filename)
    tablaConstantes.exportarConstantes(filename)
    directorioFunc.exportarFunciones(filename)
    
#Agrega una variable declarada a la lista de variables
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
        print("Stack overflow: Sobrepasaste el espacio de memoria para las variables en linea:", p.lineno(0))
        sys.exit()
    listaVariables.append([nombreVar, tipoVarLeido, nuevaDir])
    

#Borra los elementos que se encuentran en la lista de variables
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


filename = sys.argv[1]

f = open(filename,'r')
data = f.read()
f.close()

parser.parse(data, tracking=True)

""" while True:
    try:
        s = input('')
    except EOFError:
        break """
