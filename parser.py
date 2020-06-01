from scaner import tokens
import ply.yacc as yacc
import codecs
from DirFunciones import DirFunciones
from CuboSemantico import CuboSemantico
from Cuadruplo import Cuadruplo
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

def p_PROGRAMA(p):
    '''
    PROGRAMA : crearFuncGlobal PROGRAM NAME SEMICOLON VARS F PRINCIPAL printTodo
    F : FUNCION F
    | empty
    '''

def p_VARS(p):
    '''
    VARS : borrarListaVar VAR V1
    '''
    

def p_V1(p):
    '''
    V1 : TIPO VARIABLE agregarVarLista V2 SEMICOLON agregarVariables V3
    '''
    

def p_V2(p):
    '''
    V2 : COMMA VARIABLE agregarVarLista V2
    | empty
    '''

def p_V3(p):
    '''
    V3 : borrarListaVar V1
    | empty
    '''
    

def p_FUNCION(p):
    '''
    FUNCION : FUNC TIPO_FUNCION NAME agregarFunc LPAREN borrarListaVar PARAMS agregarVariables RPAREN V4 CUERPO 
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
    VARIABLE : NAME E2
    '''
    p[0] = p[1]

def p_E2(p):
    '''
    E2 : LSBRACKET EXP RSBRACKET
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
    ASIGNACION : VARIABLE agregarPilaOp EQUALS meterOperador EXP popIgual SEMICOLON
    '''
    p[0] = p[1]

def p_LLAMADA(p):
    '''
    LLAMADA : NAME LPAREN E1 RPAREN SEMICOLON
    E1 : EXP 
    | EXP COMMA E1
    '''

def p_LLAMADAF(p):
    '''
    LLAMADAF : NAME LPAREN E1 RPAREN
    '''

def p_RETORNO(p):
    '''
    RETORNO : RETURN LPAREN EXP RPAREN SEMICOLON
    '''

def p_LECTURA(p):
    '''
    LECTURA : READ LPAREN V3 RPAREN SEMICOLON
    V3 : VARIABLE COMMA V3
    | VARIABLE
    '''

def p_ESCRITURA(p):
    '''
    ESCRITURA : PRINT LPAREN E2 RPAREN SEMICOLON
    E2 : S_EXP
    | S_EXP COMMA E2
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
    CICLO_F : FROM NAME EQUALS C_INT TO C_INT DO CUERPO
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
    | LESS_OR_EQUAL meterOperador EXP
    | GREATER_THAN meterOperador EXP
    | LESS_THAN meterOperador EXP
    | IS_EQUAL meterOperador EXP
    | NOT_EQUAL meterOperador EXP
    | empty
    '''

def p_S_EXP(p):
    '''
    S_EXP : C_STRING
    | EXP
    '''
    
def p_EXP(p):
    '''
    EXP : TERMINO T popSumaResta
    T : PLUS meterOperador EXP
    | MINUS meterOperador EXP
    | empty
    '''

def p_TERMINO(p):
    '''
    TERMINO : FACTOR F2 popMultDiv
    F2 : DIVIDE meterOperador TERMINO
    | MULTIPLY meterOperador TERMINO
    | empty
    '''

def p_FACTOR(p):
    '''
    FACTOR : LPAREN meterFondoFalso H_EXP RPAREN quitarFondoFalso
    | C_INT
    | C_FLOAT
    | C_CHAR
    | VARIABLE agregarPilaOp
    | LLAMADAF
    '''

def p_empty(p):
    '''
    empty :
    '''
#Puntos Neuralgicos

def p_gotoIf(p):
    '''gotoIf : '''
    global pilaPoper
    global pilaTipos
    global pilaOp
    global pilaSaltos
    global cuadruplos
    expRes = pilaTipos.pop()
    if expRes != 'bool':
        print("Type Mismatch error: If requiere de una expresión booleana")
        sys.exit()
    else:
        res = pilaOp.pop()
        cuadruplos.generarCuad("gotof", res, "", "")
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
    cuadruplos.generarCuad("goto", "", "", retorno)
    cuadruplos.rellenar(final, cuadruplos.contador)

def p_gotoElse(p):
    '''gotoElse : '''
    global pilaSaltos
    global cuadruplos
    cuadruplos.generarCuad("goto","","","")
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
        pilaOp.append(varName)
        pilaTipos.append(variable["type"])
    else:
        print("La variable", varName, "no ha sido declarada")
        sys.exit()

def p_popBool(p):
    '''popBool : '''
    global pilaPoper
    global pilaOp
    global pilaTipos
    global cuadruplos
    global cuboSem
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
            cuadruplos.generarCuad(op, opdo_izq, opdo_der, "temporal")
            pilaOp.append("temporal")
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
                cuadruplos.printCuads()
                print(op, opdo_izq, opdo_der, tipo_izq, tipo_der, tipoRes)
                print("Type mismatch error: Los tipos de los operandos no son compatibles")
                sys.exit()
            cuadruplos.generarCuad(op, opdo_der, "", opdo_izq)
            pilaOp.append("temporal")
            pilaTipos.append(tipoRes)

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
            cuadruplos.generarCuad(op, opdo_izq, opdo_der, "temporal")
            pilaOp.append("temporal")
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
            cuadruplos.generarCuad(op, opdo_izq, opdo_der, "temporal")
            pilaOp.append("temporal")
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
    directorioFunc.printTodo()
    cuadruplos.printCuads()

def p_agregarVarLista(p):
    '''agregarVarLista : '''
    global listaVariables
    global nombreVar
    global tipoVarLeido
    nombreVar = p[-1]
    listaVariables.append([nombreVar, tipoVarLeido])

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
