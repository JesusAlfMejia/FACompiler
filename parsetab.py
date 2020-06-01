
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDErightEQUALSleftANDORAND CHAR COMMA C_CHAR C_FLOAT C_INT C_STRING DIVIDE DO ELSE EQUALS FLOAT FROM FUNC GREATER_OR_EQUAL GREATER_THAN IF INT IS_EQUAL LBRACKET LESS_OR_EQUAL LESS_THAN LPAREN LSBRACKET MAIN MINUS MULTIPLY NAME NOT_EQUAL OR PLUS PRINT PROGRAM RBRACKET READ RETURN RPAREN RSBRACKET SEMICOLON THEN TO VAR VOID WHILE\n    PROGRAMA : crearFuncGlobal PROGRAM NAME SEMICOLON VARS F PRINCIPAL printTodo\n    F : FUNCION F\n    | empty\n    \n    VARS : borrarListaVar VAR V1\n    \n    V1 : TIPO VARIABLE agregarVarLista V2 SEMICOLON agregarVariables V3\n    \n    V2 : COMMA VARIABLE agregarVarLista V2\n    | empty\n    \n    V3 : borrarListaVar V1\n    | empty\n    \n    FUNCION : FUNC TIPO_FUNCION NAME agregarFunc LPAREN borrarListaVar PARAMS agregarVariables RPAREN V4 CUERPO \n    V4 : VARS\n    | empty\n    \n    PARAMS : TIPO NAME agregarVarLista P1\n    \n    P1 : P2\n    | empty\n    \n    P2 : COMMA PARAMS P1\n    \n    CUERPO : LBRACKET E RBRACKET\n    E : E1\n    | empty\n    E1 : ESTATUTO \n    | ESTATUTO E1\n    \n    TIPO : INT\n    | FLOAT\n    | CHAR\n    \n    TIPO_FUNCION : INT\n    | FLOAT\n    | CHAR\n    | VOID\n    \n    PRINCIPAL : MAIN LPAREN crearFuncMain RPAREN CUERPO\n    \n    VARIABLE : NAME E2\n    \n    E2 : LSBRACKET EXP RSBRACKET\n    | empty\n    \n    ESTATUTO : ASIGNACION\n    | LLAMADA\n    | RETORNO\n    | LECTURA\n    | ESCRITURA\n    | CONDICION\n    | CICLO_W\n    | CICLO_F\n    \n    ASIGNACION : VARIABLE agregarPilaOp EQUALS meterOperador EXP popIgual SEMICOLON\n    \n    LLAMADA : NAME LPAREN E1 RPAREN SEMICOLON\n    E1 : EXP \n    | EXP COMMA E1\n    \n    LLAMADAF : NAME LPAREN E1 RPAREN\n    \n    RETORNO : RETURN LPAREN EXP RPAREN SEMICOLON\n    \n    LECTURA : READ LPAREN V3 RPAREN SEMICOLON\n    V3 : VARIABLE COMMA V3\n    | VARIABLE\n    \n    ESCRITURA : PRINT LPAREN E2 RPAREN SEMICOLON\n    E2 : S_EXP\n    | S_EXP COMMA E2\n    \n    CONDICION : IF LPAREN H_EXP RPAREN gotoIf THEN CUERPO ELSE1 terminarGoto\n    ELSE1 : ELSE gotoElse CUERPO\n    | empty\n    \n    CICLO_W : WHILE agregarWhile LPAREN H_EXP RPAREN DO gotoIf CUERPO terminarWhile\n    \n    CICLO_F : FROM NAME EQUALS C_INT TO C_INT DO CUERPO\n    \n    H_EXP : T_EXP\n    | T_EXP OR H_EXP\n    \n    T_EXP : G_EXP\n    | G_EXP AND T_EXP\n    \n    G_EXP : EXP B popBool\n    B : GREATER_OR_EQUAL meterOperador G_EXP\n    | LESS_OR_EQUAL meterOperador EXP\n    | GREATER_THAN meterOperador EXP\n    | LESS_THAN meterOperador EXP\n    | IS_EQUAL meterOperador EXP\n    | NOT_EQUAL meterOperador EXP\n    | empty\n    \n    S_EXP : C_STRING\n    | EXP\n    \n    EXP : TERMINO T popSumaResta\n    T : PLUS meterOperador EXP\n    | MINUS meterOperador EXP\n    | empty\n    \n    TERMINO : FACTOR F2 popMultDiv\n    F2 : DIVIDE meterOperador TERMINO\n    | MULTIPLY meterOperador TERMINO\n    | empty\n    \n    FACTOR : LPAREN meterFondoFalso H_EXP RPAREN quitarFondoFalso\n    | C_INT\n    | C_FLOAT\n    | C_CHAR\n    | VARIABLE agregarPilaOp\n    | LLAMADAF\n    \n    empty :\n    gotoIf : terminarGoto :  agregarWhile : terminarWhile : gotoElse : meterFondoFalso : quitarFondoFalso :   agregarPilaOp : popBool : popIgual : popMultDiv : popSumaResta :  meterIgual :  meterBool :  meterMultDiv :  meterSumaResta :  meterOperador : crearFuncGlobal : crearFuncMain :  agregarFunc : agregarVariables : printFunciones : printTodo : agregarVarLista :  borrarListaVar : '
    
_lr_action_items = {'PROGRAM':([0,2,],[-104,3,]),'$end':([1,13,26,67,136,],[0,-109,-1,-29,-17,]),'NAME':([3,16,17,18,19,20,22,23,24,25,30,34,36,43,52,54,56,58,59,62,63,65,68,70,72,74,76,77,78,79,80,81,82,83,90,94,95,97,98,107,108,110,113,115,116,117,118,126,127,129,130,131,132,133,134,136,146,151,157,158,159,160,161,162,165,168,189,191,192,193,204,205,208,210,211,212,213,215,216,],[4,28,-25,-26,-27,-28,30,-22,-23,-24,34,34,34,-92,30,72,34,-103,-103,-103,-103,34,72,-107,34,72,-33,-34,-35,-36,-37,-38,-39,-40,120,34,34,34,34,138,30,72,72,34,30,34,34,34,34,-103,-103,-103,-103,-103,-103,-17,-103,34,34,34,34,34,34,34,30,34,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'SEMICOLON':([4,29,30,33,34,35,37,38,39,40,41,42,44,45,46,47,48,51,53,56,57,60,61,64,66,71,91,92,93,96,109,111,121,122,123,124,125,143,153,167,169,170,171,190,199,],[5,-110,-86,-86,-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,70,-7,-86,-98,-75,-97,-79,-84,-110,-31,-52,-72,-76,-86,-45,-73,-74,-77,-78,-93,-6,-80,189,191,192,193,-96,204,]),'VAR':([5,7,163,],[-111,12,-111,]),'FUNC':([6,9,21,30,34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,70,91,92,93,96,108,111,121,122,123,124,125,136,139,140,142,153,165,166,188,197,],[11,11,-4,-86,-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-107,-31,-52,-72,-76,-86,-45,-73,-74,-77,-78,-93,-17,-49,-5,-9,-80,-86,-8,-48,-10,]),'MAIN':([6,8,9,10,15,21,30,34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,70,91,92,93,96,108,111,121,122,123,124,125,136,139,140,142,153,165,166,188,197,],[-86,14,-86,-3,-2,-4,-86,-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-107,-31,-52,-72,-76,-86,-45,-73,-74,-77,-78,-93,-17,-49,-5,-9,-80,-86,-8,-48,-10,]),'INT':([11,12,50,69,70,108,116,141,165,187,],[17,23,-111,23,-107,-111,-111,23,-111,23,]),'FLOAT':([11,12,50,69,70,108,116,141,165,187,],[18,24,-111,24,-107,-111,-111,24,-111,24,]),'CHAR':([11,12,50,69,70,108,116,141,165,187,],[19,25,-111,25,-107,-111,-111,25,-111,25,]),'VOID':([11,],[20,]),'LPAREN':([14,28,30,32,34,36,43,54,56,58,59,62,63,65,68,72,74,76,77,78,79,80,81,82,83,85,86,87,88,89,94,95,97,98,110,113,115,117,118,119,126,127,129,130,131,132,133,134,136,146,151,157,158,159,160,161,162,168,189,191,192,193,204,205,208,210,211,212,213,215,216,],[27,-106,43,50,54,43,-92,43,43,-103,-103,-103,-103,43,43,110,43,-33,-34,-35,-36,-37,-38,-39,-40,115,116,117,118,-89,43,43,43,43,43,43,43,43,43,151,43,43,-103,-103,-103,-103,-103,-103,-17,-103,43,43,43,43,43,43,43,43,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'LBRACKET':([21,30,34,35,37,38,39,40,41,42,44,45,46,47,48,49,56,57,60,61,64,66,70,91,92,93,96,108,111,121,122,123,124,125,139,140,142,153,163,165,166,181,182,183,188,200,201,206,207,209,214,],[-4,-86,-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,68,-86,-98,-75,-97,-79,-84,-107,-31,-52,-72,-76,-86,-45,-73,-74,-77,-78,-93,-49,-5,-9,-80,-86,-86,-8,68,-11,-12,-48,68,-87,68,68,-91,68,]),'RPAREN':([27,30,31,34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,70,72,73,74,75,76,77,78,79,80,81,82,83,84,91,92,93,96,99,100,101,102,106,108,111,112,114,116,117,121,122,123,124,125,128,135,136,137,138,139,140,142,144,145,147,148,149,150,153,154,155,156,164,165,166,167,173,175,176,177,178,179,180,184,185,186,188,189,191,192,193,198,203,204,205,208,210,211,212,213,215,216,],[-105,-86,49,-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-107,-86,111,-20,-43,-33,-34,-35,-36,-37,-38,-39,-40,-94,-31,-52,-72,-76,125,-58,-60,-86,-107,-86,-45,-21,-84,-86,-86,-73,-74,-77,-78,-93,-95,-69,-17,163,-110,-49,-5,-9,167,-44,169,170,171,172,-80,-59,-61,-62,-86,-86,-8,-45,195,-63,-64,-65,-66,-67,-68,-13,-14,-15,-48,-42,-46,-47,-50,-86,-16,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'COMMA':([29,30,33,34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,71,72,75,84,91,92,93,96,109,111,114,121,122,123,124,125,138,139,153,164,167,184,185,186,198,203,],[-110,-86,52,-86,-30,-71,-32,56,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-110,-86,113,-94,-31,-52,-72,-76,52,-45,-84,-73,-74,-77,-78,-93,-110,165,-80,187,-45,-13,-14,-15,187,-16,]),'LSBRACKET':([30,34,56,72,117,],[36,36,36,36,36,]),'DIVIDE':([30,34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,72,84,91,92,93,96,111,114,121,122,123,124,125,153,167,],[-86,-86,-30,-71,-32,-51,-70,-86,62,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-86,-94,-31,-52,-72,-76,-45,-84,-73,-74,-77,-78,-93,-80,-45,]),'MULTIPLY':([30,34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,72,84,91,92,93,96,111,114,121,122,123,124,125,153,167,],[-86,-86,-30,-71,-32,-51,-70,-86,63,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-86,-94,-31,-52,-72,-76,-45,-84,-73,-74,-77,-78,-93,-80,-45,]),'PLUS':([30,34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,72,84,91,92,93,96,111,114,121,122,123,124,125,153,167,],[-86,-86,-30,-71,-32,-51,-70,58,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-86,-94,-31,-52,-72,-76,-45,-84,-73,-74,-77,-78,-93,-80,-45,]),'MINUS':([30,34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,72,84,91,92,93,96,111,114,121,122,123,124,125,153,167,],[-86,-86,-30,-71,-32,-51,-70,59,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-86,-94,-31,-52,-72,-76,-45,-84,-73,-74,-77,-78,-93,-80,-45,]),'C_STRING':([30,34,56,72,117,],[40,40,40,40,40,]),'C_INT':([30,34,36,43,54,56,58,59,62,63,65,68,72,74,76,77,78,79,80,81,82,83,94,95,97,98,110,113,115,117,118,126,127,129,130,131,132,133,134,136,146,151,152,157,158,159,160,161,162,168,189,191,192,193,196,204,205,208,210,211,212,213,215,216,],[44,44,44,-92,44,44,-103,-103,-103,-103,44,44,44,44,-33,-34,-35,-36,-37,-38,-39,-40,44,44,44,44,44,44,44,44,44,44,44,-103,-103,-103,-103,-103,-103,-17,-103,44,174,44,44,44,44,44,44,44,-42,-46,-47,-50,202,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'C_FLOAT':([30,34,36,43,54,56,58,59,62,63,65,68,72,74,76,77,78,79,80,81,82,83,94,95,97,98,110,113,115,117,118,126,127,129,130,131,132,133,134,136,146,151,157,158,159,160,161,162,168,189,191,192,193,204,205,208,210,211,212,213,215,216,],[45,45,45,-92,45,45,-103,-103,-103,-103,45,45,45,45,-33,-34,-35,-36,-37,-38,-39,-40,45,45,45,45,45,45,45,45,45,45,45,-103,-103,-103,-103,-103,-103,-17,-103,45,45,45,45,45,45,45,45,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'C_CHAR':([30,34,36,43,54,56,58,59,62,63,65,68,72,74,76,77,78,79,80,81,82,83,94,95,97,98,110,113,115,117,118,126,127,129,130,131,132,133,134,136,146,151,157,158,159,160,161,162,168,189,191,192,193,204,205,208,210,211,212,213,215,216,],[46,46,46,-92,46,46,-103,-103,-103,-103,46,46,46,46,-33,-34,-35,-36,-37,-38,-39,-40,46,46,46,46,46,46,46,46,46,46,46,-103,-103,-103,-103,-103,-103,-17,-103,46,46,46,46,46,46,46,46,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'RSBRACKET':([34,35,37,38,39,40,41,42,44,45,46,47,48,55,56,57,60,61,64,66,91,92,93,96,111,121,122,123,124,125,153,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,91,-86,-98,-75,-97,-79,-84,-31,-52,-72,-76,-45,-73,-74,-77,-78,-93,-80,]),'EQUALS':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,72,84,91,92,93,96,111,114,120,121,122,123,124,125,153,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-86,-94,-31,-52,-72,-76,-45,146,152,-73,-74,-77,-78,-93,-80,]),'RBRACKET':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,68,72,74,75,76,77,78,79,80,81,82,83,84,91,92,93,96,103,104,105,111,112,114,121,122,123,124,125,136,145,153,167,189,191,192,193,204,205,208,210,211,212,213,215,216,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-86,-86,-20,-43,-33,-34,-35,-36,-37,-38,-39,-40,-94,-31,-52,-72,-76,136,-18,-19,-45,-21,-84,-73,-74,-77,-78,-93,-17,-44,-80,-45,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'GREATER_OR_EQUAL':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,91,92,93,96,102,111,121,122,123,124,125,153,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-31,-52,-72,-76,129,-45,-73,-74,-77,-78,-93,-80,]),'LESS_OR_EQUAL':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,91,92,93,96,102,111,121,122,123,124,125,153,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-31,-52,-72,-76,130,-45,-73,-74,-77,-78,-93,-80,]),'GREATER_THAN':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,91,92,93,96,102,111,121,122,123,124,125,153,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-31,-52,-72,-76,131,-45,-73,-74,-77,-78,-93,-80,]),'LESS_THAN':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,91,92,93,96,102,111,121,122,123,124,125,153,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-31,-52,-72,-76,132,-45,-73,-74,-77,-78,-93,-80,]),'IS_EQUAL':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,91,92,93,96,102,111,121,122,123,124,125,153,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-31,-52,-72,-76,133,-45,-73,-74,-77,-78,-93,-80,]),'NOT_EQUAL':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,91,92,93,96,102,111,121,122,123,124,125,153,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-31,-52,-72,-76,134,-45,-73,-74,-77,-78,-93,-80,]),'AND':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,91,92,93,96,101,102,111,121,122,123,124,125,128,135,153,156,175,176,177,178,179,180,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-31,-52,-72,-76,127,-86,-45,-73,-74,-77,-78,-93,-95,-69,-80,-62,-63,-64,-65,-66,-67,-68,]),'OR':([34,35,37,38,39,40,41,42,44,45,46,47,48,56,57,60,61,64,66,91,92,93,96,100,101,102,111,121,122,123,124,125,128,135,153,155,156,175,176,177,178,179,180,],[-86,-30,-71,-32,-51,-70,-86,-86,-81,-82,-83,-94,-85,-86,-98,-75,-97,-79,-84,-31,-52,-72,-76,126,-60,-86,-45,-73,-74,-77,-78,-93,-95,-69,-80,-61,-62,-63,-64,-65,-66,-67,-68,]),'RETURN':([54,68,74,76,77,78,79,80,81,82,83,110,113,136,189,191,192,193,204,205,208,210,211,212,213,215,216,],[85,85,85,-33,-34,-35,-36,-37,-38,-39,-40,85,85,-17,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'READ':([54,68,74,76,77,78,79,80,81,82,83,110,113,136,189,191,192,193,204,205,208,210,211,212,213,215,216,],[86,86,86,-33,-34,-35,-36,-37,-38,-39,-40,86,86,-17,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'PRINT':([54,68,74,76,77,78,79,80,81,82,83,110,113,136,189,191,192,193,204,205,208,210,211,212,213,215,216,],[87,87,87,-33,-34,-35,-36,-37,-38,-39,-40,87,87,-17,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'IF':([54,68,74,76,77,78,79,80,81,82,83,110,113,136,189,191,192,193,204,205,208,210,211,212,213,215,216,],[88,88,88,-33,-34,-35,-36,-37,-38,-39,-40,88,88,-17,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'WHILE':([54,68,74,76,77,78,79,80,81,82,83,110,113,136,189,191,192,193,204,205,208,210,211,212,213,215,216,],[89,89,89,-33,-34,-35,-36,-37,-38,-39,-40,89,89,-17,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'FROM':([54,68,74,76,77,78,79,80,81,82,83,110,113,136,189,191,192,193,204,205,208,210,211,212,213,215,216,],[90,90,90,-33,-34,-35,-36,-37,-38,-39,-40,90,90,-17,-42,-46,-47,-50,-41,-86,-88,-55,-90,-57,-53,-56,-54,]),'ELSE':([136,205,],[-17,209,]),'THEN':([172,194,],[-87,200,]),'TO':([174,],[196,]),'DO':([195,202,],[201,207,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'crearFuncGlobal':([0,],[2,]),'VARS':([5,163,],[6,182,]),'borrarListaVar':([5,50,108,116,163,165,],[7,69,141,141,7,141,]),'F':([6,9,],[8,15,]),'FUNCION':([6,9,],[9,9,]),'empty':([6,9,30,33,34,41,42,56,68,72,102,108,109,116,117,163,164,165,198,205,],[10,10,38,53,38,60,64,38,105,38,135,142,53,142,38,183,186,142,186,210,]),'PRINCIPAL':([8,],[13,]),'TIPO_FUNCION':([11,],[16,]),'V1':([12,141,],[21,166,]),'TIPO':([12,69,141,187,],[22,107,22,107,]),'printTodo':([13,],[26,]),'VARIABLE':([22,30,34,36,52,54,56,65,68,72,74,94,95,97,98,108,110,113,115,116,117,118,126,127,151,157,158,159,160,161,162,165,168,],[29,47,47,47,71,84,47,47,84,47,84,47,47,47,47,139,84,84,47,139,47,47,47,47,47,47,47,47,47,47,47,139,47,]),'crearFuncMain':([27,],[31,]),'agregarFunc':([28,],[32,]),'agregarVarLista':([29,71,138,],[33,109,164,]),'E2':([30,34,56,72,117,],[35,35,92,35,149,]),'EXP':([30,34,36,54,56,65,68,72,74,94,95,110,113,115,117,118,126,127,151,157,158,159,160,161,162,168,],[37,37,55,75,37,102,75,37,75,121,122,75,75,147,37,102,102,102,102,102,176,177,178,179,180,190,]),'S_EXP':([30,34,56,72,117,],[39,39,39,39,39,]),'TERMINO':([30,34,36,54,56,65,68,72,74,94,95,97,98,110,113,115,117,118,126,127,151,157,158,159,160,161,162,168,],[41,41,41,41,41,41,41,41,41,41,41,123,124,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'FACTOR':([30,34,36,54,56,65,68,72,74,94,95,97,98,110,113,115,117,118,126,127,151,157,158,159,160,161,162,168,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'LLAMADAF':([30,34,36,54,56,65,68,72,74,94,95,97,98,110,113,115,117,118,126,127,151,157,158,159,160,161,162,168,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'V2':([33,109,],[51,143,]),'T':([41,],[57,]),'F2':([42,],[61,]),'meterFondoFalso':([43,54,110,],[65,65,65,]),'agregarPilaOp':([47,84,],[66,114,]),'CUERPO':([49,181,200,206,207,214,],[67,197,205,211,212,216,]),'E1':([54,68,74,110,113,],[73,104,112,144,145,]),'ESTATUTO':([54,68,74,110,113,],[74,74,74,74,74,]),'ASIGNACION':([54,68,74,110,113,],[76,76,76,76,76,]),'LLAMADA':([54,68,74,110,113,],[77,77,77,77,77,]),'RETORNO':([54,68,74,110,113,],[78,78,78,78,78,]),'LECTURA':([54,68,74,110,113,],[79,79,79,79,79,]),'ESCRITURA':([54,68,74,110,113,],[80,80,80,80,80,]),'CONDICION':([54,68,74,110,113,],[81,81,81,81,81,]),'CICLO_W':([54,68,74,110,113,],[82,82,82,82,82,]),'CICLO_F':([54,68,74,110,113,],[83,83,83,83,83,]),'popSumaResta':([57,],[93,]),'meterOperador':([58,59,62,63,129,130,131,132,133,134,146,],[94,95,97,98,157,158,159,160,161,162,168,]),'popMultDiv':([61,],[96,]),'H_EXP':([65,118,126,151,],[99,150,154,173,]),'T_EXP':([65,118,126,127,151,],[100,100,100,155,100,]),'G_EXP':([65,118,126,127,151,157,],[101,101,101,101,101,175,]),'E':([68,],[103,]),'PARAMS':([69,187,],[106,198,]),'agregarVariables':([70,106,],[108,137,]),'agregarWhile':([89,],[119,]),'B':([102,],[128,]),'V3':([108,116,165,],[140,148,188,]),'quitarFondoFalso':([125,],[153,]),'popBool':([128,],[156,]),'V4':([163,],[181,]),'P1':([164,198,],[184,203,]),'P2':([164,198,],[185,185,]),'gotoIf':([172,201,],[194,206,]),'popIgual':([190,],[199,]),'ELSE1':([205,],[208,]),'terminarGoto':([208,],[213,]),'gotoElse':([209,],[214,]),'terminarWhile':([211,],[215,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> crearFuncGlobal PROGRAM NAME SEMICOLON VARS F PRINCIPAL printTodo','PROGRAMA',8,'p_PROGRAMA','parser.py',24),
  ('F -> FUNCION F','F',2,'p_PROGRAMA','parser.py',25),
  ('F -> empty','F',1,'p_PROGRAMA','parser.py',26),
  ('VARS -> borrarListaVar VAR V1','VARS',3,'p_VARS','parser.py',31),
  ('V1 -> TIPO VARIABLE agregarVarLista V2 SEMICOLON agregarVariables V3','V1',7,'p_V1','parser.py',37),
  ('V2 -> COMMA VARIABLE agregarVarLista V2','V2',4,'p_V2','parser.py',43),
  ('V2 -> empty','V2',1,'p_V2','parser.py',44),
  ('V3 -> borrarListaVar V1','V3',2,'p_V3','parser.py',49),
  ('V3 -> empty','V3',1,'p_V3','parser.py',50),
  ('FUNCION -> FUNC TIPO_FUNCION NAME agregarFunc LPAREN borrarListaVar PARAMS agregarVariables RPAREN V4 CUERPO','FUNCION',11,'p_FUNCION','parser.py',56),
  ('V4 -> VARS','V4',1,'p_FUNCION','parser.py',57),
  ('V4 -> empty','V4',1,'p_FUNCION','parser.py',58),
  ('PARAMS -> TIPO NAME agregarVarLista P1','PARAMS',4,'p_PARAMS','parser.py',62),
  ('P1 -> P2','P1',1,'p_P1','parser.py',67),
  ('P1 -> empty','P1',1,'p_P1','parser.py',68),
  ('P2 -> COMMA PARAMS P1','P2',3,'p_P2','parser.py',73),
  ('CUERPO -> LBRACKET E RBRACKET','CUERPO',3,'p_CUERPO','parser.py',78),
  ('E -> E1','E',1,'p_CUERPO','parser.py',79),
  ('E -> empty','E',1,'p_CUERPO','parser.py',80),
  ('E1 -> ESTATUTO','E1',1,'p_CUERPO','parser.py',81),
  ('E1 -> ESTATUTO E1','E1',2,'p_CUERPO','parser.py',82),
  ('TIPO -> INT','TIPO',1,'p_TIPO','parser.py',87),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','parser.py',88),
  ('TIPO -> CHAR','TIPO',1,'p_TIPO','parser.py',89),
  ('TIPO_FUNCION -> INT','TIPO_FUNCION',1,'p_TIPO_FUNCION','parser.py',96),
  ('TIPO_FUNCION -> FLOAT','TIPO_FUNCION',1,'p_TIPO_FUNCION','parser.py',97),
  ('TIPO_FUNCION -> CHAR','TIPO_FUNCION',1,'p_TIPO_FUNCION','parser.py',98),
  ('TIPO_FUNCION -> VOID','TIPO_FUNCION',1,'p_TIPO_FUNCION','parser.py',99),
  ('PRINCIPAL -> MAIN LPAREN crearFuncMain RPAREN CUERPO','PRINCIPAL',5,'p_PRINCIPAL','parser.py',106),
  ('VARIABLE -> NAME E2','VARIABLE',2,'p_VARIABLE','parser.py',111),
  ('E2 -> LSBRACKET EXP RSBRACKET','E2',3,'p_E2','parser.py',117),
  ('E2 -> empty','E2',1,'p_E2','parser.py',118),
  ('ESTATUTO -> ASIGNACION','ESTATUTO',1,'p_ESTATUTO','parser.py',123),
  ('ESTATUTO -> LLAMADA','ESTATUTO',1,'p_ESTATUTO','parser.py',124),
  ('ESTATUTO -> RETORNO','ESTATUTO',1,'p_ESTATUTO','parser.py',125),
  ('ESTATUTO -> LECTURA','ESTATUTO',1,'p_ESTATUTO','parser.py',126),
  ('ESTATUTO -> ESCRITURA','ESTATUTO',1,'p_ESTATUTO','parser.py',127),
  ('ESTATUTO -> CONDICION','ESTATUTO',1,'p_ESTATUTO','parser.py',128),
  ('ESTATUTO -> CICLO_W','ESTATUTO',1,'p_ESTATUTO','parser.py',129),
  ('ESTATUTO -> CICLO_F','ESTATUTO',1,'p_ESTATUTO','parser.py',130),
  ('ASIGNACION -> VARIABLE agregarPilaOp EQUALS meterOperador EXP popIgual SEMICOLON','ASIGNACION',7,'p_ASIGNACION','parser.py',135),
  ('LLAMADA -> NAME LPAREN E1 RPAREN SEMICOLON','LLAMADA',5,'p_LLAMADA','parser.py',140),
  ('E1 -> EXP','E1',1,'p_LLAMADA','parser.py',141),
  ('E1 -> EXP COMMA E1','E1',3,'p_LLAMADA','parser.py',142),
  ('LLAMADAF -> NAME LPAREN E1 RPAREN','LLAMADAF',4,'p_LLAMADAF','parser.py',147),
  ('RETORNO -> RETURN LPAREN EXP RPAREN SEMICOLON','RETORNO',5,'p_RETORNO','parser.py',152),
  ('LECTURA -> READ LPAREN V3 RPAREN SEMICOLON','LECTURA',5,'p_LECTURA','parser.py',157),
  ('V3 -> VARIABLE COMMA V3','V3',3,'p_LECTURA','parser.py',158),
  ('V3 -> VARIABLE','V3',1,'p_LECTURA','parser.py',159),
  ('ESCRITURA -> PRINT LPAREN E2 RPAREN SEMICOLON','ESCRITURA',5,'p_ESCRITURA','parser.py',164),
  ('E2 -> S_EXP','E2',1,'p_ESCRITURA','parser.py',165),
  ('E2 -> S_EXP COMMA E2','E2',3,'p_ESCRITURA','parser.py',166),
  ('CONDICION -> IF LPAREN H_EXP RPAREN gotoIf THEN CUERPO ELSE1 terminarGoto','CONDICION',9,'p_CONDICION','parser.py',171),
  ('ELSE1 -> ELSE gotoElse CUERPO','ELSE1',3,'p_CONDICION','parser.py',172),
  ('ELSE1 -> empty','ELSE1',1,'p_CONDICION','parser.py',173),
  ('CICLO_W -> WHILE agregarWhile LPAREN H_EXP RPAREN DO gotoIf CUERPO terminarWhile','CICLO_W',9,'p_CICLO_W','parser.py',178),
  ('CICLO_F -> FROM NAME EQUALS C_INT TO C_INT DO CUERPO','CICLO_F',8,'p_CICLO_F','parser.py',183),
  ('H_EXP -> T_EXP','H_EXP',1,'p_H_EXP','parser.py',188),
  ('H_EXP -> T_EXP OR H_EXP','H_EXP',3,'p_H_EXP','parser.py',189),
  ('T_EXP -> G_EXP','T_EXP',1,'p_T_EXP','parser.py',194),
  ('T_EXP -> G_EXP AND T_EXP','T_EXP',3,'p_T_EXP','parser.py',195),
  ('G_EXP -> EXP B popBool','G_EXP',3,'p_G_EXP','parser.py',200),
  ('B -> GREATER_OR_EQUAL meterOperador G_EXP','B',3,'p_G_EXP','parser.py',201),
  ('B -> LESS_OR_EQUAL meterOperador EXP','B',3,'p_G_EXP','parser.py',202),
  ('B -> GREATER_THAN meterOperador EXP','B',3,'p_G_EXP','parser.py',203),
  ('B -> LESS_THAN meterOperador EXP','B',3,'p_G_EXP','parser.py',204),
  ('B -> IS_EQUAL meterOperador EXP','B',3,'p_G_EXP','parser.py',205),
  ('B -> NOT_EQUAL meterOperador EXP','B',3,'p_G_EXP','parser.py',206),
  ('B -> empty','B',1,'p_G_EXP','parser.py',207),
  ('S_EXP -> C_STRING','S_EXP',1,'p_S_EXP','parser.py',212),
  ('S_EXP -> EXP','S_EXP',1,'p_S_EXP','parser.py',213),
  ('EXP -> TERMINO T popSumaResta','EXP',3,'p_EXP','parser.py',218),
  ('T -> PLUS meterOperador EXP','T',3,'p_EXP','parser.py',219),
  ('T -> MINUS meterOperador EXP','T',3,'p_EXP','parser.py',220),
  ('T -> empty','T',1,'p_EXP','parser.py',221),
  ('TERMINO -> FACTOR F2 popMultDiv','TERMINO',3,'p_TERMINO','parser.py',226),
  ('F2 -> DIVIDE meterOperador TERMINO','F2',3,'p_TERMINO','parser.py',227),
  ('F2 -> MULTIPLY meterOperador TERMINO','F2',3,'p_TERMINO','parser.py',228),
  ('F2 -> empty','F2',1,'p_TERMINO','parser.py',229),
  ('FACTOR -> LPAREN meterFondoFalso H_EXP RPAREN quitarFondoFalso','FACTOR',5,'p_FACTOR','parser.py',234),
  ('FACTOR -> C_INT','FACTOR',1,'p_FACTOR','parser.py',235),
  ('FACTOR -> C_FLOAT','FACTOR',1,'p_FACTOR','parser.py',236),
  ('FACTOR -> C_CHAR','FACTOR',1,'p_FACTOR','parser.py',237),
  ('FACTOR -> VARIABLE agregarPilaOp','FACTOR',2,'p_FACTOR','parser.py',238),
  ('FACTOR -> LLAMADAF','FACTOR',1,'p_FACTOR','parser.py',239),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',244),
  ('gotoIf -> <empty>','gotoIf',0,'p_gotoIf','parser.py',249),
  ('terminarGoto -> <empty>','terminarGoto',0,'p_terminaGoto','parser.py',265),
  ('agregarWhile -> <empty>','agregarWhile',0,'p_agregarWhile','parser.py',272),
  ('terminarWhile -> <empty>','terminarWhile',0,'p_terminaWhile','parser.py',277),
  ('gotoElse -> <empty>','gotoElse',0,'p_gotoElse','parser.py',286),
  ('meterFondoFalso -> <empty>','meterFondoFalso',0,'p_meterFondoFalso','parser.py',297),
  ('quitarFondoFalso -> <empty>','quitarFondoFalso',0,'p_quitarFondoFalso','parser.py',302),
  ('agregarPilaOp -> <empty>','agregarPilaOp',0,'p_agregarPilaOp','parser.py',311),
  ('popBool -> <empty>','popBool',0,'p_popBool','parser.py',326),
  ('popIgual -> <empty>','popIgual',0,'p_popIgual','parser.py',351),
  ('popMultDiv -> <empty>','popMultDiv',0,'p_popMultDiv','parser.py',378),
  ('popSumaResta -> <empty>','popSumaResta',0,'p_popSumaResta','parser.py',403),
  ('meterIgual -> <empty>','meterIgual',0,'p_meterIgual','parser.py',428),
  ('meterBool -> <empty>','meterBool',0,'p_meterBool','parser.py',433),
  ('meterMultDiv -> <empty>','meterMultDiv',0,'p_meterMultDiv','parser.py',438),
  ('meterSumaResta -> <empty>','meterSumaResta',0,'p_meterSumaResta','parser.py',443),
  ('meterOperador -> <empty>','meterOperador',0,'p_meterOperador','parser.py',448),
  ('crearFuncGlobal -> <empty>','crearFuncGlobal',0,'p_crearFuncGlobal','parser.py',454),
  ('crearFuncMain -> <empty>','crearFuncMain',0,'p_crearFuncMain','parser.py',461),
  ('agregarFunc -> <empty>','agregarFunc',0,'p_agregarFunc','parser.py',468),
  ('agregarVariables -> <empty>','agregarVariables',0,'p_agregarVariables','parser.py',485),
  ('printFunciones -> <empty>','printFunciones',0,'p_printFunciones','parser.py',496),
  ('printTodo -> <empty>','printTodo',0,'p_printTodo','parser.py',501),
  ('agregarVarLista -> <empty>','agregarVarLista',0,'p_agregarVarLista','parser.py',508),
  ('borrarListaVar -> <empty>','borrarListaVar',0,'p_borrarListaVar','parser.py',516),
]
