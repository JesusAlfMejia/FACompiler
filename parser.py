from scaner import tokens
import ply.yacc as yacc
import codecs

def p_PROGRAMA(p):
    '''
    PROGRAMA : PROGRAM NAME SEMICOLON VARS F PRINCIPAL
    F : FUNCION F
    | empty
    '''

def p_VARS(p):
    '''
    VARS : VAR TIPO VARIABLE V2 V3
    V2 : COMMA VARIABLE V2
    | SEMICOLON
    V3 : TIPO VARIABLE V2 V3
    | empty
    '''

def p_FUNCION(p):
    '''
    FUNCION : FUNC TIPO_FUNCION NAME LPAREN PARAMS RPAREN V4 CUERPO 
    V4 : VARS
    | empty
    '''
def p_PARAMS(p):
    '''
    PARAMS : TIPO NAME P1
    P1 : COMMA PARAMS P1
    | empty

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

def p_TIPO_FUNCION(p):
    '''
    TIPO_FUNCION : INT
    | FLOAT
    | CHAR
    | VOID
    '''

def p_PRINCIPAL(p):
    '''
    PRINCIPAL : MAIN LPAREN RPAREN CUERPO
    '''

def p_VARIABLE(p):
    '''
    VARIABLE : NAME E2
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
    ASIGNACION : VARIABLE EQUALS EXP SEMICOLON
    '''

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
    CONDICION : IF LPAREN H_EXP RPAREN THEN CUERPO ELSE1
    ELSE1 : ELSE CUERPO
    | empty
    '''

def p_CICLO_W(p):
    '''
    CICLO_W : WHILE LPAREN H_EXP RPAREN DO CUERPO
    '''

def p_CICLO_F(p):
    '''
    CICLO_F : FROM NAME EQUALS C_INT TO C_INT DO CUERPO
    '''

def p_H_EXP(p):
    '''
    H_EXP : T
    T : T_EXP
    | T_EXP OR T
    '''

def p_T_EXP(p):
    '''
    T_EXP : G
    G : G_EXP
    | G_EXP AND G
    '''

def p_G_EXP(p):
    '''
    G_EXP : EXP B
    B : GREATER_OR_EQUAL EXP
    | LESS_OR_EQUAL EXP
    | GREATER_THAN EXP
    | LESS_THAN EXP
    | IS_EQUAL EXP
    | NOT_EQUAL EXP
    | empty
    '''

def p_S_EXP(p):
    '''
    S_EXP : C_STRING
    | EXP
    '''
    
def p_EXP(p):
    '''
    EXP : TERMINO T
    T : PLUS TERMINO T
    | MINUS TERMINO T
    | empty
    '''

def p_TERMINO(p):
    '''
    TERMINO : FACTOR F2
    F2 : DIVIDE FACTOR F2
    | MULTIPLY FACTOR F2
    | empty
    '''

def p_FACTOR(p):
    '''
    FACTOR : LPAREN H_EXP RPAREN
    | C_INT
    | C_FLOAT
    | C_CHAR
    | VARIABLE
    | LLAMADAF
    '''

def p_empty(p):
    '''
    empty :
    '''

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
