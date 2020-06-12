
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDErightEQUALSleftANDORAND CHAR COMMA C_CHAR C_FLOAT C_INT C_STRING DIVIDE DO ELSE EQUALS FLOAT FROM FUNC GREATER_OR_EQUAL GREATER_THAN IF INT IS_EQUAL LBRACKET LESS_OR_EQUAL LESS_THAN LPAREN LSBRACKET MAIN MINUS MULTIPLY NAME NOT_EQUAL OR PLUS PRINT PROGRAM RBRACKET READ RETURN RPAREN RSBRACKET SEMICOLON THEN TO VAR VOID WHILE\n    PROGRAMA : crearFuncGlobal PROGRAM NAME SEMICOLON scopeGlobal VARS F agregarLocalVarGlobal PRINCIPAL printTodo\n    F : FUNCION F\n    | empty\n    \n    VARS : borrarListaVar VAR V1\n    | empty\n    \n    V1 : TIPO VARIABLEDer V2 SEMICOLON V3\n    \n    V2 : COMMA VARIABLEDer V2\n    | empty\n    \n    V3 : V1\n    | empty\n    \n    FUNCION : FUNC TIPO_FUNCION NAME agregarFunc LPAREN borrarListaVar scopeLocal PARAMS agregarParamTable agregarVariables RPAREN VARS agregarLocalVar CUERPO terminarFunc \n    \n    PARAMS : TIPO NAME agregarVarLista P1\n    \n    P1 : P2\n    | empty\n    \n    P2 : COMMA PARAMS P1\n    \n    CUERPO : LBRACKET E RBRACKET\n    E : E1\n    | empty\n    E1 : ESTATUTO \n    | ESTATUTO E1\n    \n    TIPO : INT\n    | FLOAT\n    | CHAR\n    \n    TIPO_FUNCION : INT\n    | FLOAT\n    | CHAR\n    | VOID\n    \n    PRINCIPAL : MAIN LPAREN crearFuncMain RPAREN CUERPO terminarFunc\n    \n    VARIABLE : NAME agregarPilaOp E2\n    \n    E2 : LSBRACKET guardarArreglo meterFondoFalso EXP RSBRACKET verificarArreglo quitarFondoFalso\n    | empty\n    \n    VARIABLEDer : NAME agregarVarLista agregarVariables borrarListaVar E2Der\n    \n    E2Der : LSBRACKET C_INT declararArray RSBRACKET\n    | empty\n    \n    ESTATUTO : ASIGNACION\n    | LLAMADA\n    | RETORNO\n    | LECTURA\n    | ESCRITURA\n    | CONDICION\n    | CICLO_W\n    | CICLO_F\n    \n    ASIGNACION : VARIABLE EQUALS meterOperador EXP popIgual SEMICOLON\n    \n    LLAMADA : NAME verificarFuncVoid LPAREN meterFondoFalso generarEra E4 verificarParam RPAREN quitarFondoFalso generarGosub SEMICOLON\n    E4 : EXP generarParam\n    | EXP generarParam COMMA E4\n    | empty\n    \n    LLAMADAF : NAME verificarFunc LPAREN meterFondoFalso generarEra E4 verificarParam RPAREN quitarFondoFalso verificarLlamada generarGosub\n    \n    RETORNO : RETURN LPAREN EXP popReturn RPAREN SEMICOLON\n    \n    LECTURA : READ LPAREN V4 RPAREN SEMICOLON\n    V4 : VARIABLE popRead COMMA V4\n    | VARIABLE popRead\n    \n    ESCRITURA : PRINT LPAREN E3 RPAREN SEMICOLON\n    E3 : S_EXP popPrint\n    | S_EXP popPrint COMMA E3\n    \n    CONDICION : IF LPAREN H_EXP RPAREN gotoIf THEN CUERPO ELSE1 terminarGoto\n    ELSE1 : ELSE gotoElse CUERPO\n    | empty\n    \n    CICLO_W : WHILE agregarWhile LPAREN H_EXP RPAREN DO gotoIf CUERPO terminarWhile\n    \n    CICLO_F : FROM VARIABLE agregarFrom EQUALS meterOperador EXP popIgual agregarWhile TO EXP crearCompFrom DO gotoIf CUERPO sumarFrom terminarWhile\n    \n    H_EXP : T_EXP\n    | T_EXP OR meterOperador H_EXP popComp\n    \n    T_EXP : G_EXP\n    | G_EXP AND meterOperador T_EXP popComp\n    \n    G_EXP : EXP B popBool\n    B : GREATER_OR_EQUAL meterOperador G_EXP\n    | LESS_OR_EQUAL meterOperador G_EXP\n    | GREATER_THAN meterOperador G_EXP\n    | LESS_THAN meterOperador G_EXP\n    | IS_EQUAL meterOperador G_EXP\n    | NOT_EQUAL meterOperador G_EXP\n    | empty\n    \n    S_EXP : C_STRING agregarConstString\n    | EXP\n    \n    EXP : TERMINO popSumaResta T \n    T : PLUS meterOperador EXP\n    | MINUS meterOperador EXP\n    | empty\n    \n    TERMINO : FACTOR popMultDiv F2 \n    F2 : DIVIDE meterOperador TERMINO\n    | MULTIPLY meterOperador TERMINO\n    | empty\n    \n    FACTOR : LPAREN meterFondoFalso H_EXP RPAREN quitarFondoFalso\n    | C_INT agregarConstInt\n    | C_FLOAT agregarConstFloat\n    | C_CHAR agregarConstChar\n    | VARIABLE\n    | LLAMADAF\n    \n    empty :\n     generarGosub : verificarLlamada :  verificarParam :  generarParam :  generarEra : verificarFunc : verificarFuncVoid :  terminarFunc :  agregarLocalVar :  agregarLocalVarGlobal : agregarParamTable : guardarArreglo : verificarArreglo :  declararArray : agregarFrom : crearCompFrom : sumarFrom : agregarConstInt : agregarConstFloat : agregarConstChar : agregarConstString : scopeGlobal : scopeLocal : scopeTemp : scopeConst : gotoIf : terminarGoto :  agregarWhile : terminarWhile : gotoElse : meterFondoFalso : quitarFondoFalso :   agregarPilaOp : popPrint : popRead : popReturn : popComp : popBool : popIgual : popMultDiv : popSumaResta :  meterIgual :  meterBool :  meterMultDiv :  meterSumaResta :  meterOperador : crearFuncGlobal : crearFuncMain :  agregarFunc : agregarVariables : printFunciones : printTodo : agregarVarLista :  borrarListaVar : '
    
_lr_action_items = {'PROGRAM':([0,2,],[-136,3,]),'$end':([1,27,32,51,57,81,],[0,-141,-1,-97,-28,-16,]),'NAME':([3,17,18,19,20,21,23,24,25,26,36,52,61,62,63,64,65,66,67,68,69,77,79,81,83,86,87,88,89,96,97,99,101,121,127,128,129,143,144,146,147,148,149,150,151,154,161,162,166,167,170,171,173,174,175,176,177,179,180,182,183,184,185,186,187,189,192,198,199,200,201,202,203,227,228,235,238,240,241,248,250,251,254,256,263,264,265,],[4,29,-24,-25,-26,-27,31,-21,-22,-23,31,71,71,-35,-36,-37,-38,-39,-40,-41,-42,92,94,-16,-135,110,92,110,110,110,-120,-101,-120,110,-94,-120,110,-135,-135,-135,-135,-135,-135,-135,-135,-135,110,110,-135,-135,-135,-135,-120,-50,92,-53,110,110,110,110,110,110,110,110,110,110,-43,-49,110,110,110,110,-94,110,-89,110,-116,-58,-118,-56,-59,110,-57,-44,-106,-118,-60,]),'SEMICOLON':([4,30,31,35,37,38,42,43,49,50,54,56,85,98,100,103,104,105,106,107,108,109,110,125,126,131,132,133,134,135,137,139,160,164,165,168,169,172,197,221,222,223,224,225,226,234,236,244,246,252,253,257,259,261,],[5,-89,-142,41,-8,-139,-89,-143,-7,-89,-32,-34,-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,-33,-128,-89,-89,-84,-85,-86,174,176,192,198,-75,-78,-79,-82,-121,-102,-83,-76,-77,-80,-81,-121,-121,-90,-30,256,-121,-91,-90,-48,]),'FUNC':([5,6,7,9,11,22,41,46,47,48,81,233,243,],[-111,-89,13,-5,13,-4,-89,-6,-9,-10,-16,-97,-11,]),'MAIN':([5,6,7,9,10,11,12,15,16,22,41,46,47,48,81,233,243,],[-111,-89,-89,-5,-99,-89,-3,28,-2,-4,-89,-6,-9,-10,-16,-97,-11,]),'VAR':([5,6,8,155,],[-111,-143,14,-143,]),'LBRACKET':([9,22,41,44,46,47,48,155,190,206,215,217,231,239,249,260,262,],[-5,-4,-89,52,-6,-9,-10,-89,-98,52,-115,52,52,-119,52,-115,52,]),'INT':([13,14,40,41,45,53,159,],[18,24,-143,24,-112,24,24,]),'FLOAT':([13,14,40,41,45,53,159,],[19,25,-143,25,-112,25,25,]),'CHAR':([13,14,40,41,45,53,159,],[20,26,-143,26,-112,26,26,]),'VOID':([13,],[21,]),'LPAREN':([28,29,34,71,72,73,74,75,76,83,84,86,88,89,90,96,97,99,101,110,121,127,128,129,136,143,144,146,147,148,149,150,151,154,161,162,166,167,170,171,173,177,179,180,182,183,184,185,186,187,189,199,200,201,202,203,227,235,251,],[33,-138,40,-96,86,87,88,89,-117,-135,97,101,101,101,121,101,-120,-101,-120,-95,101,-94,-120,101,173,-135,-135,-135,-135,-135,-135,-135,-135,-135,101,101,-135,-135,-135,-135,-120,101,101,101,101,101,101,101,101,101,101,101,101,101,101,-94,101,101,101,]),'COMMA':([30,31,38,42,43,50,54,56,85,92,94,98,100,103,104,105,106,107,108,109,110,112,114,115,116,124,125,131,132,133,134,135,138,140,141,156,157,158,165,168,169,172,191,194,197,218,220,221,222,223,224,225,226,236,246,253,257,259,261,],[36,-142,-139,36,-143,-89,-32,-34,-89,-122,-142,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,-124,-123,-110,-74,159,-33,-89,-89,-84,-85,-86,175,177,-73,-12,-13,-14,-75,-78,-79,-82,159,-93,-121,-15,235,-102,-83,-76,-77,-80,-81,-121,-30,-121,-91,-90,-48,]),'LSBRACKET':([31,38,43,50,71,85,92,110,],[-142,-139,-143,55,-122,99,-122,-122,]),'RPAREN':([33,39,78,85,92,93,94,97,98,100,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,123,124,127,130,131,132,133,134,135,138,140,141,145,152,153,156,157,158,161,163,165,168,169,172,173,181,191,193,194,195,197,203,204,205,207,208,209,210,211,212,213,214,218,219,220,221,222,223,224,225,226,227,229,230,235,236,237,245,246,247,253,257,259,261,],[-137,44,-100,-89,-122,-139,-142,-120,-29,-31,-125,-130,-129,-107,-108,-109,-87,-88,-122,137,-124,139,-123,-110,-74,142,-61,-63,-89,155,-89,-94,164,-89,-89,-84,-85,-86,-52,-54,-73,-127,-72,188,-12,-13,-14,-89,197,-75,-78,-79,-82,-120,-65,-89,-92,-93,-47,-121,-94,-51,-55,-126,-126,-66,-67,-68,-69,-70,-71,-15,234,-45,-102,-83,-76,-77,-80,-81,-89,-62,-64,-89,-121,-92,-46,-30,253,-121,-91,-90,-48,]),'RBRACKET':([52,58,59,60,61,62,63,64,65,66,67,68,69,81,82,174,176,192,198,228,238,240,241,248,250,254,256,263,264,265,],[-89,81,-17,-18,-19,-35,-36,-37,-38,-39,-40,-41,-42,-16,-20,-50,-53,-43,-49,-89,-116,-58,-118,-56,-59,-57,-44,-106,-118,-60,]),'RETURN':([52,61,62,63,64,65,66,67,68,69,81,174,176,192,198,228,238,240,241,248,250,254,256,263,264,265,],[72,72,-35,-36,-37,-38,-39,-40,-41,-42,-16,-50,-53,-43,-49,-89,-116,-58,-118,-56,-59,-57,-44,-106,-118,-60,]),'READ':([52,61,62,63,64,65,66,67,68,69,81,174,176,192,198,228,238,240,241,248,250,254,256,263,264,265,],[73,73,-35,-36,-37,-38,-39,-40,-41,-42,-16,-50,-53,-43,-49,-89,-116,-58,-118,-56,-59,-57,-44,-106,-118,-60,]),'PRINT':([52,61,62,63,64,65,66,67,68,69,81,174,176,192,198,228,238,240,241,248,250,254,256,263,264,265,],[74,74,-35,-36,-37,-38,-39,-40,-41,-42,-16,-50,-53,-43,-49,-89,-116,-58,-118,-56,-59,-57,-44,-106,-118,-60,]),'IF':([52,61,62,63,64,65,66,67,68,69,81,174,176,192,198,228,238,240,241,248,250,254,256,263,264,265,],[75,75,-35,-36,-37,-38,-39,-40,-41,-42,-16,-50,-53,-43,-49,-89,-116,-58,-118,-56,-59,-57,-44,-106,-118,-60,]),'WHILE':([52,61,62,63,64,65,66,67,68,69,81,174,176,192,198,228,238,240,241,248,250,254,256,263,264,265,],[76,76,-35,-36,-37,-38,-39,-40,-41,-42,-16,-50,-53,-43,-49,-89,-116,-58,-118,-56,-59,-57,-44,-106,-118,-60,]),'FROM':([52,61,62,63,64,65,66,67,68,69,81,174,176,192,198,228,238,240,241,248,250,254,256,263,264,265,],[77,77,-35,-36,-37,-38,-39,-40,-41,-42,-16,-50,-53,-43,-49,-89,-116,-58,-118,-56,-59,-57,-44,-106,-118,-60,]),'C_INT':([55,83,86,88,89,96,97,99,101,121,127,128,129,143,144,146,147,148,149,150,151,154,161,162,166,167,170,171,173,177,179,180,182,183,184,185,186,187,189,199,200,201,202,203,227,235,251,],[80,-135,105,105,105,105,-120,-101,-120,105,-94,-120,105,-135,-135,-135,-135,-135,-135,-135,-135,-135,105,105,-135,-135,-135,-135,-120,105,105,105,105,105,105,105,105,105,105,105,105,105,105,-94,105,105,105,]),'EQUALS':([70,71,85,91,92,98,100,122,221,236,246,],[83,-122,-89,-104,-122,-29,-31,154,-102,-121,-30,]),'RSBRACKET':([80,85,95,98,100,103,104,105,106,107,108,109,110,131,132,133,134,135,165,168,169,172,196,197,221,222,223,224,225,226,236,246,253,257,259,261,],[-103,-89,125,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,-89,-89,-84,-85,-86,-75,-78,-79,-82,221,-121,-102,-83,-76,-77,-80,-81,-121,-30,-121,-91,-90,-48,]),'ELSE':([81,228,],[-16,239,]),'C_FLOAT':([83,86,88,89,96,97,99,101,121,127,128,129,143,144,146,147,148,149,150,151,154,161,162,166,167,170,171,173,177,179,180,182,183,184,185,186,187,189,199,200,201,202,203,227,235,251,],[-135,106,106,106,106,-120,-101,-120,106,-94,-120,106,-135,-135,-135,-135,-135,-135,-135,-135,-135,106,106,-135,-135,-135,-135,-120,106,106,106,106,106,106,106,106,106,106,106,106,106,106,-94,106,106,106,]),'C_CHAR':([83,86,88,89,96,97,99,101,121,127,128,129,143,144,146,147,148,149,150,151,154,161,162,166,167,170,171,173,177,179,180,182,183,184,185,186,187,189,199,200,201,202,203,227,235,251,],[-135,107,107,107,107,-120,-101,-120,107,-94,-120,107,-135,-135,-135,-135,-135,-135,-135,-135,-135,107,107,-135,-135,-135,-135,-120,107,107,107,107,107,107,107,107,107,107,107,107,107,107,-94,107,107,107,]),'DIVIDE':([85,98,100,104,105,106,107,108,109,110,132,133,134,135,197,221,222,236,246,253,257,259,261,],[-89,-29,-31,-129,-107,-108,-109,-87,-88,-122,170,-84,-85,-86,-121,-102,-83,-121,-30,-121,-91,-90,-48,]),'MULTIPLY':([85,98,100,104,105,106,107,108,109,110,132,133,134,135,197,221,222,236,246,253,257,259,261,],[-89,-29,-31,-129,-107,-108,-109,-87,-88,-122,171,-84,-85,-86,-121,-102,-83,-121,-30,-121,-91,-90,-48,]),'PLUS':([85,98,100,103,104,105,106,107,108,109,110,131,132,133,134,135,169,172,197,221,222,225,226,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,166,-89,-84,-85,-86,-79,-82,-121,-102,-83,-80,-81,-121,-30,-121,-91,-90,-48,]),'MINUS':([85,98,100,103,104,105,106,107,108,109,110,131,132,133,134,135,169,172,197,221,222,225,226,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,167,-89,-84,-85,-86,-79,-82,-121,-102,-83,-80,-81,-121,-30,-121,-91,-90,-48,]),'GREATER_OR_EQUAL':([85,98,100,103,104,105,106,107,108,109,110,120,131,132,133,134,135,165,168,169,172,197,221,222,223,224,225,226,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,146,-89,-89,-84,-85,-86,-75,-78,-79,-82,-121,-102,-83,-76,-77,-80,-81,-121,-30,-121,-91,-90,-48,]),'LESS_OR_EQUAL':([85,98,100,103,104,105,106,107,108,109,110,120,131,132,133,134,135,165,168,169,172,197,221,222,223,224,225,226,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,147,-89,-89,-84,-85,-86,-75,-78,-79,-82,-121,-102,-83,-76,-77,-80,-81,-121,-30,-121,-91,-90,-48,]),'GREATER_THAN':([85,98,100,103,104,105,106,107,108,109,110,120,131,132,133,134,135,165,168,169,172,197,221,222,223,224,225,226,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,148,-89,-89,-84,-85,-86,-75,-78,-79,-82,-121,-102,-83,-76,-77,-80,-81,-121,-30,-121,-91,-90,-48,]),'LESS_THAN':([85,98,100,103,104,105,106,107,108,109,110,120,131,132,133,134,135,165,168,169,172,197,221,222,223,224,225,226,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,149,-89,-89,-84,-85,-86,-75,-78,-79,-82,-121,-102,-83,-76,-77,-80,-81,-121,-30,-121,-91,-90,-48,]),'IS_EQUAL':([85,98,100,103,104,105,106,107,108,109,110,120,131,132,133,134,135,165,168,169,172,197,221,222,223,224,225,226,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,150,-89,-89,-84,-85,-86,-75,-78,-79,-82,-121,-102,-83,-76,-77,-80,-81,-121,-30,-121,-91,-90,-48,]),'NOT_EQUAL':([85,98,100,103,104,105,106,107,108,109,110,120,131,132,133,134,135,165,168,169,172,197,221,222,223,224,225,226,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,151,-89,-89,-84,-85,-86,-75,-78,-79,-82,-121,-102,-83,-76,-77,-80,-81,-121,-30,-121,-91,-90,-48,]),'AND':([85,98,100,103,104,105,106,107,108,109,110,119,120,131,132,133,134,135,145,152,165,168,169,172,181,197,209,210,211,212,213,214,221,222,223,224,225,226,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,144,-89,-89,-89,-84,-85,-86,-127,-72,-75,-78,-79,-82,-65,-121,-66,-67,-68,-69,-70,-71,-102,-83,-76,-77,-80,-81,-121,-30,-121,-91,-90,-48,]),'OR':([85,98,100,103,104,105,106,107,108,109,110,118,119,120,131,132,133,134,135,145,152,165,168,169,172,181,197,208,209,210,211,212,213,214,221,222,223,224,225,226,230,236,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,143,-63,-89,-89,-89,-84,-85,-86,-127,-72,-75,-78,-79,-82,-65,-121,-126,-66,-67,-68,-69,-70,-71,-102,-83,-76,-77,-80,-81,-64,-121,-30,-121,-91,-90,-48,]),'TO':([85,98,100,103,104,105,106,107,108,109,110,131,132,133,134,135,165,168,169,172,197,216,221,222,223,224,225,226,232,236,242,246,253,257,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,-89,-89,-84,-85,-86,-75,-78,-79,-82,-121,-128,-102,-83,-76,-77,-80,-81,-117,-121,251,-30,-121,-91,-90,-48,]),'DO':([85,98,100,103,104,105,106,107,108,109,110,131,132,133,134,135,165,168,169,172,188,197,221,222,223,224,225,226,236,246,253,255,257,258,259,261,],[-89,-29,-31,-130,-129,-107,-108,-109,-87,-88,-122,-89,-89,-84,-85,-86,-75,-78,-79,-82,215,-121,-102,-83,-76,-77,-80,-81,-121,-30,-121,-105,-91,260,-90,-48,]),'C_STRING':([88,177,],[115,115,]),'THEN':([142,178,],[-115,206,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'crearFuncGlobal':([0,],[2,]),'scopeGlobal':([5,],[6,]),'VARS':([6,155,],[7,190,]),'borrarListaVar':([6,40,43,155,],[8,45,50,8,]),'empty':([6,7,11,30,41,42,50,52,85,120,124,131,132,155,161,191,227,228,235,],[9,12,12,37,48,37,56,60,100,152,158,168,172,9,195,158,195,240,195,]),'F':([7,11,],[10,16,]),'FUNCION':([7,11,],[11,11,]),'agregarLocalVarGlobal':([10,],[15,]),'TIPO_FUNCION':([13,],[17,]),'V1':([14,41,],[22,47,]),'TIPO':([14,41,53,159,],[23,23,79,79,]),'PRINCIPAL':([15,],[27,]),'VARIABLEDer':([23,36,],[30,42,]),'printTodo':([27,],[32,]),'agregarFunc':([29,],[34,]),'V2':([30,42,],[35,49,]),'agregarVarLista':([31,94,],[38,124,]),'crearFuncMain':([33,],[39,]),'agregarVariables':([38,93,],[43,123,]),'V3':([41,],[46,]),'CUERPO':([44,206,217,231,249,262,],[51,228,233,241,254,263,]),'scopeLocal':([45,],[53,]),'E2Der':([50,],[54,]),'terminarFunc':([51,233,],[57,243,]),'E':([52,],[58,]),'E1':([52,61,],[59,82,]),'ESTATUTO':([52,61,],[61,61,]),'ASIGNACION':([52,61,],[62,62,]),'LLAMADA':([52,61,],[63,63,]),'RETORNO':([52,61,],[64,64,]),'LECTURA':([52,61,],[65,65,]),'ESCRITURA':([52,61,],[66,66,]),'CONDICION':([52,61,],[67,67,]),'CICLO_W':([52,61,],[68,68,]),'CICLO_F':([52,61,],[69,69,]),'VARIABLE':([52,61,77,86,87,88,89,96,121,129,161,162,175,177,179,180,182,183,184,185,186,187,189,199,200,201,202,227,235,251,],[70,70,91,108,112,108,108,108,108,108,108,108,112,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,]),'PARAMS':([53,159,],[78,191,]),'verificarFuncVoid':([71,],[84,]),'agregarPilaOp':([71,92,110,],[85,85,85,]),'agregarWhile':([76,232,],[90,242,]),'agregarParamTable':([78,],[93,]),'declararArray':([80,],[95,]),'meterOperador':([83,143,144,146,147,148,149,150,151,154,166,167,170,171,],[96,179,180,182,183,184,185,186,187,189,199,200,201,202,]),'E2':([85,],[98,]),'EXP':([86,88,89,96,121,129,161,162,177,179,180,182,183,184,185,186,187,189,199,200,227,235,251,],[102,116,120,126,120,120,194,196,116,120,120,120,120,120,120,120,120,216,223,224,194,194,255,]),'TERMINO':([86,88,89,96,121,129,161,162,177,179,180,182,183,184,185,186,187,189,199,200,201,202,227,235,251,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,225,226,103,103,103,]),'FACTOR':([86,88,89,96,121,129,161,162,177,179,180,182,183,184,185,186,187,189,199,200,201,202,227,235,251,],[104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'LLAMADAF':([86,88,89,96,121,129,161,162,177,179,180,182,183,184,185,186,187,189,199,200,201,202,227,235,251,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'V4':([87,175,],[111,204,]),'E3':([88,177,],[113,205,]),'S_EXP':([88,177,],[114,114,]),'H_EXP':([89,121,129,179,],[117,153,163,207,]),'T_EXP':([89,121,129,179,180,],[118,118,118,118,208,]),'G_EXP':([89,121,129,179,180,182,183,184,185,186,187,],[119,119,119,119,119,209,210,211,212,213,214,]),'agregarFrom':([91,],[122,]),'meterFondoFalso':([97,101,128,173,],[127,129,162,203,]),'guardarArreglo':([99,],[128,]),'popReturn':([102,],[130,]),'popSumaResta':([103,],[131,]),'popMultDiv':([104,],[132,]),'agregarConstInt':([105,],[133,]),'agregarConstFloat':([106,],[134,]),'agregarConstChar':([107,],[135,]),'verificarFunc':([110,],[136,]),'popRead':([112,],[138,]),'popPrint':([114,],[140,]),'agregarConstString':([115,],[141,]),'B':([120,],[145,]),'P1':([124,191,],[156,218,]),'P2':([124,191,],[157,157,]),'popIgual':([126,216,],[160,232,]),'generarEra':([127,203,],[161,227,]),'T':([131,],[165,]),'F2':([132,],[169,]),'gotoIf':([142,215,260,],[178,231,262,]),'popBool':([145,],[181,]),'E4':([161,227,235,],[193,237,245,]),'agregarLocalVar':([190,],[217,]),'verificarParam':([193,237,],[219,247,]),'generarParam':([194,],[220,]),'quitarFondoFalso':([197,234,236,253,],[222,244,246,257,]),'popComp':([207,208,],[229,230,]),'verificarArreglo':([221,],[236,]),'ELSE1':([228,],[238,]),'terminarGoto':([238,],[248,]),'gotoElse':([239,],[249,]),'terminarWhile':([241,264,],[250,265,]),'generarGosub':([244,259,],[252,261,]),'crearCompFrom':([255,],[258,]),'verificarLlamada':([257,],[259,]),'sumarFrom':([263,],[264,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> crearFuncGlobal PROGRAM NAME SEMICOLON scopeGlobal VARS F agregarLocalVarGlobal PRINCIPAL printTodo','PROGRAMA',10,'p_PROGRAMA','ForeverAlone.py',49),
  ('F -> FUNCION F','F',2,'p_PROGRAMA','ForeverAlone.py',50),
  ('F -> empty','F',1,'p_PROGRAMA','ForeverAlone.py',51),
  ('VARS -> borrarListaVar VAR V1','VARS',3,'p_VARS','ForeverAlone.py',56),
  ('VARS -> empty','VARS',1,'p_VARS','ForeverAlone.py',57),
  ('V1 -> TIPO VARIABLEDer V2 SEMICOLON V3','V1',5,'p_V1','ForeverAlone.py',63),
  ('V2 -> COMMA VARIABLEDer V2','V2',3,'p_V2','ForeverAlone.py',69),
  ('V2 -> empty','V2',1,'p_V2','ForeverAlone.py',70),
  ('V3 -> V1','V3',1,'p_V3','ForeverAlone.py',75),
  ('V3 -> empty','V3',1,'p_V3','ForeverAlone.py',76),
  ('FUNCION -> FUNC TIPO_FUNCION NAME agregarFunc LPAREN borrarListaVar scopeLocal PARAMS agregarParamTable agregarVariables RPAREN VARS agregarLocalVar CUERPO terminarFunc','FUNCION',15,'p_FUNCION','ForeverAlone.py',82),
  ('PARAMS -> TIPO NAME agregarVarLista P1','PARAMS',4,'p_PARAMS','ForeverAlone.py',87),
  ('P1 -> P2','P1',1,'p_P1','ForeverAlone.py',92),
  ('P1 -> empty','P1',1,'p_P1','ForeverAlone.py',93),
  ('P2 -> COMMA PARAMS P1','P2',3,'p_P2','ForeverAlone.py',98),
  ('CUERPO -> LBRACKET E RBRACKET','CUERPO',3,'p_CUERPO','ForeverAlone.py',103),
  ('E -> E1','E',1,'p_CUERPO','ForeverAlone.py',104),
  ('E -> empty','E',1,'p_CUERPO','ForeverAlone.py',105),
  ('E1 -> ESTATUTO','E1',1,'p_CUERPO','ForeverAlone.py',106),
  ('E1 -> ESTATUTO E1','E1',2,'p_CUERPO','ForeverAlone.py',107),
  ('TIPO -> INT','TIPO',1,'p_TIPO','ForeverAlone.py',112),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','ForeverAlone.py',113),
  ('TIPO -> CHAR','TIPO',1,'p_TIPO','ForeverAlone.py',114),
  ('TIPO_FUNCION -> INT','TIPO_FUNCION',1,'p_TIPO_FUNCION','ForeverAlone.py',121),
  ('TIPO_FUNCION -> FLOAT','TIPO_FUNCION',1,'p_TIPO_FUNCION','ForeverAlone.py',122),
  ('TIPO_FUNCION -> CHAR','TIPO_FUNCION',1,'p_TIPO_FUNCION','ForeverAlone.py',123),
  ('TIPO_FUNCION -> VOID','TIPO_FUNCION',1,'p_TIPO_FUNCION','ForeverAlone.py',124),
  ('PRINCIPAL -> MAIN LPAREN crearFuncMain RPAREN CUERPO terminarFunc','PRINCIPAL',6,'p_PRINCIPAL','ForeverAlone.py',131),
  ('VARIABLE -> NAME agregarPilaOp E2','VARIABLE',3,'p_VARIABLE','ForeverAlone.py',136),
  ('E2 -> LSBRACKET guardarArreglo meterFondoFalso EXP RSBRACKET verificarArreglo quitarFondoFalso','E2',7,'p_E2','ForeverAlone.py',142),
  ('E2 -> empty','E2',1,'p_E2','ForeverAlone.py',143),
  ('VARIABLEDer -> NAME agregarVarLista agregarVariables borrarListaVar E2Der','VARIABLEDer',5,'p_VARIABLEDer','ForeverAlone.py',148),
  ('E2Der -> LSBRACKET C_INT declararArray RSBRACKET','E2Der',4,'p_E2Der','ForeverAlone.py',154),
  ('E2Der -> empty','E2Der',1,'p_E2Der','ForeverAlone.py',155),
  ('ESTATUTO -> ASIGNACION','ESTATUTO',1,'p_ESTATUTO','ForeverAlone.py',160),
  ('ESTATUTO -> LLAMADA','ESTATUTO',1,'p_ESTATUTO','ForeverAlone.py',161),
  ('ESTATUTO -> RETORNO','ESTATUTO',1,'p_ESTATUTO','ForeverAlone.py',162),
  ('ESTATUTO -> LECTURA','ESTATUTO',1,'p_ESTATUTO','ForeverAlone.py',163),
  ('ESTATUTO -> ESCRITURA','ESTATUTO',1,'p_ESTATUTO','ForeverAlone.py',164),
  ('ESTATUTO -> CONDICION','ESTATUTO',1,'p_ESTATUTO','ForeverAlone.py',165),
  ('ESTATUTO -> CICLO_W','ESTATUTO',1,'p_ESTATUTO','ForeverAlone.py',166),
  ('ESTATUTO -> CICLO_F','ESTATUTO',1,'p_ESTATUTO','ForeverAlone.py',167),
  ('ASIGNACION -> VARIABLE EQUALS meterOperador EXP popIgual SEMICOLON','ASIGNACION',6,'p_ASIGNACION','ForeverAlone.py',172),
  ('LLAMADA -> NAME verificarFuncVoid LPAREN meterFondoFalso generarEra E4 verificarParam RPAREN quitarFondoFalso generarGosub SEMICOLON','LLAMADA',11,'p_LLAMADA','ForeverAlone.py',177),
  ('E4 -> EXP generarParam','E4',2,'p_LLAMADA','ForeverAlone.py',178),
  ('E4 -> EXP generarParam COMMA E4','E4',4,'p_LLAMADA','ForeverAlone.py',179),
  ('E4 -> empty','E4',1,'p_LLAMADA','ForeverAlone.py',180),
  ('LLAMADAF -> NAME verificarFunc LPAREN meterFondoFalso generarEra E4 verificarParam RPAREN quitarFondoFalso verificarLlamada generarGosub','LLAMADAF',11,'p_LLAMADAF','ForeverAlone.py',185),
  ('RETORNO -> RETURN LPAREN EXP popReturn RPAREN SEMICOLON','RETORNO',6,'p_RETORNO','ForeverAlone.py',190),
  ('LECTURA -> READ LPAREN V4 RPAREN SEMICOLON','LECTURA',5,'p_LECTURA','ForeverAlone.py',195),
  ('V4 -> VARIABLE popRead COMMA V4','V4',4,'p_LECTURA','ForeverAlone.py',196),
  ('V4 -> VARIABLE popRead','V4',2,'p_LECTURA','ForeverAlone.py',197),
  ('ESCRITURA -> PRINT LPAREN E3 RPAREN SEMICOLON','ESCRITURA',5,'p_ESCRITURA','ForeverAlone.py',202),
  ('E3 -> S_EXP popPrint','E3',2,'p_ESCRITURA','ForeverAlone.py',203),
  ('E3 -> S_EXP popPrint COMMA E3','E3',4,'p_ESCRITURA','ForeverAlone.py',204),
  ('CONDICION -> IF LPAREN H_EXP RPAREN gotoIf THEN CUERPO ELSE1 terminarGoto','CONDICION',9,'p_CONDICION','ForeverAlone.py',209),
  ('ELSE1 -> ELSE gotoElse CUERPO','ELSE1',3,'p_CONDICION','ForeverAlone.py',210),
  ('ELSE1 -> empty','ELSE1',1,'p_CONDICION','ForeverAlone.py',211),
  ('CICLO_W -> WHILE agregarWhile LPAREN H_EXP RPAREN DO gotoIf CUERPO terminarWhile','CICLO_W',9,'p_CICLO_W','ForeverAlone.py',216),
  ('CICLO_F -> FROM VARIABLE agregarFrom EQUALS meterOperador EXP popIgual agregarWhile TO EXP crearCompFrom DO gotoIf CUERPO sumarFrom terminarWhile','CICLO_F',16,'p_CICLO_F','ForeverAlone.py',221),
  ('H_EXP -> T_EXP','H_EXP',1,'p_H_EXP','ForeverAlone.py',226),
  ('H_EXP -> T_EXP OR meterOperador H_EXP popComp','H_EXP',5,'p_H_EXP','ForeverAlone.py',227),
  ('T_EXP -> G_EXP','T_EXP',1,'p_T_EXP','ForeverAlone.py',232),
  ('T_EXP -> G_EXP AND meterOperador T_EXP popComp','T_EXP',5,'p_T_EXP','ForeverAlone.py',233),
  ('G_EXP -> EXP B popBool','G_EXP',3,'p_G_EXP','ForeverAlone.py',238),
  ('B -> GREATER_OR_EQUAL meterOperador G_EXP','B',3,'p_G_EXP','ForeverAlone.py',239),
  ('B -> LESS_OR_EQUAL meterOperador G_EXP','B',3,'p_G_EXP','ForeverAlone.py',240),
  ('B -> GREATER_THAN meterOperador G_EXP','B',3,'p_G_EXP','ForeverAlone.py',241),
  ('B -> LESS_THAN meterOperador G_EXP','B',3,'p_G_EXP','ForeverAlone.py',242),
  ('B -> IS_EQUAL meterOperador G_EXP','B',3,'p_G_EXP','ForeverAlone.py',243),
  ('B -> NOT_EQUAL meterOperador G_EXP','B',3,'p_G_EXP','ForeverAlone.py',244),
  ('B -> empty','B',1,'p_G_EXP','ForeverAlone.py',245),
  ('S_EXP -> C_STRING agregarConstString','S_EXP',2,'p_S_EXP','ForeverAlone.py',250),
  ('S_EXP -> EXP','S_EXP',1,'p_S_EXP','ForeverAlone.py',251),
  ('EXP -> TERMINO popSumaResta T','EXP',3,'p_EXP','ForeverAlone.py',256),
  ('T -> PLUS meterOperador EXP','T',3,'p_EXP','ForeverAlone.py',257),
  ('T -> MINUS meterOperador EXP','T',3,'p_EXP','ForeverAlone.py',258),
  ('T -> empty','T',1,'p_EXP','ForeverAlone.py',259),
  ('TERMINO -> FACTOR popMultDiv F2','TERMINO',3,'p_TERMINO','ForeverAlone.py',264),
  ('F2 -> DIVIDE meterOperador TERMINO','F2',3,'p_TERMINO','ForeverAlone.py',265),
  ('F2 -> MULTIPLY meterOperador TERMINO','F2',3,'p_TERMINO','ForeverAlone.py',266),
  ('F2 -> empty','F2',1,'p_TERMINO','ForeverAlone.py',267),
  ('FACTOR -> LPAREN meterFondoFalso H_EXP RPAREN quitarFondoFalso','FACTOR',5,'p_FACTOR','ForeverAlone.py',272),
  ('FACTOR -> C_INT agregarConstInt','FACTOR',2,'p_FACTOR','ForeverAlone.py',273),
  ('FACTOR -> C_FLOAT agregarConstFloat','FACTOR',2,'p_FACTOR','ForeverAlone.py',274),
  ('FACTOR -> C_CHAR agregarConstChar','FACTOR',2,'p_FACTOR','ForeverAlone.py',275),
  ('FACTOR -> VARIABLE','FACTOR',1,'p_FACTOR','ForeverAlone.py',276),
  ('FACTOR -> LLAMADAF','FACTOR',1,'p_FACTOR','ForeverAlone.py',277),
  ('empty -> <empty>','empty',0,'p_empty','ForeverAlone.py',282),
  ('generarGosub -> <empty>','generarGosub',0,'p_generarGosub','ForeverAlone.py',286),
  ('verificarLlamada -> <empty>','verificarLlamada',0,'p_verificarLlamada','ForeverAlone.py',318),
  ('verificarParam -> <empty>','verificarParam',0,'p_verificarParam','ForeverAlone.py',329),
  ('generarParam -> <empty>','generarParam',0,'p_generarParam','ForeverAlone.py',341),
  ('generarEra -> <empty>','generarEra',0,'p_generarEra','ForeverAlone.py',364),
  ('verificarFunc -> <empty>','verificarFunc',0,'p_verificarFunc','ForeverAlone.py',374),
  ('verificarFuncVoid -> <empty>','verificarFuncVoid',0,'p_verificarFuncVoid','ForeverAlone.py',389),
  ('terminarFunc -> <empty>','terminarFunc',0,'p_terminarFunc','ForeverAlone.py',408),
  ('agregarLocalVar -> <empty>','agregarLocalVar',0,'p_agregarLocalVar','ForeverAlone.py',433),
  ('agregarLocalVarGlobal -> <empty>','agregarLocalVarGlobal',0,'p_agregarLocalVarGlobal','ForeverAlone.py',441),
  ('agregarParamTable -> <empty>','agregarParamTable',0,'p_agregarParamTable','ForeverAlone.py',448),
  ('guardarArreglo -> <empty>','guardarArreglo',0,'p_guardarArreglo','ForeverAlone.py',455),
  ('verificarArreglo -> <empty>','verificarArreglo',0,'p_verificarArreglo','ForeverAlone.py',473),
  ('declararArray -> <empty>','declararArray',0,'p_declararArray','ForeverAlone.py',493),
  ('agregarFrom -> <empty>','agregarFrom',0,'p_agregarFrom','ForeverAlone.py',522),
  ('crearCompFrom -> <empty>','crearCompFrom',0,'p_crearCompFrom','ForeverAlone.py',532),
  ('sumarFrom -> <empty>','sumarFrom',0,'p_sumarFrom','ForeverAlone.py',560),
  ('agregarConstInt -> <empty>','agregarConstInt',0,'p_agregarConstInt','ForeverAlone.py',594),
  ('agregarConstFloat -> <empty>','agregarConstFloat',0,'p_agregarConstFloat','ForeverAlone.py',610),
  ('agregarConstChar -> <empty>','agregarConstChar',0,'p_agregarConstChar','ForeverAlone.py',626),
  ('agregarConstString -> <empty>','agregarConstString',0,'p_agregarConstString','ForeverAlone.py',642),
  ('scopeGlobal -> <empty>','scopeGlobal',0,'p_scopeGlobal','ForeverAlone.py',658),
  ('scopeLocal -> <empty>','scopeLocal',0,'p_scopeLocal','ForeverAlone.py',663),
  ('scopeTemp -> <empty>','scopeTemp',0,'p_scopeTemp','ForeverAlone.py',668),
  ('scopeConst -> <empty>','scopeConst',0,'p_scopeConst','ForeverAlone.py',673),
  ('gotoIf -> <empty>','gotoIf',0,'p_gotoIf','ForeverAlone.py',678),
  ('terminarGoto -> <empty>','terminarGoto',0,'p_terminaGoto','ForeverAlone.py',694),
  ('agregarWhile -> <empty>','agregarWhile',0,'p_agregarWhile','ForeverAlone.py',701),
  ('terminarWhile -> <empty>','terminarWhile',0,'p_terminaWhile','ForeverAlone.py',706),
  ('gotoElse -> <empty>','gotoElse',0,'p_gotoElse','ForeverAlone.py',715),
  ('meterFondoFalso -> <empty>','meterFondoFalso',0,'p_meterFondoFalso','ForeverAlone.py',724),
  ('quitarFondoFalso -> <empty>','quitarFondoFalso',0,'p_quitarFondoFalso','ForeverAlone.py',729),
  ('agregarPilaOp -> <empty>','agregarPilaOp',0,'p_agregarPilaOp','ForeverAlone.py',738),
  ('popPrint -> <empty>','popPrint',0,'p_popPrint','ForeverAlone.py',753),
  ('popRead -> <empty>','popRead',0,'p_popRead','ForeverAlone.py',761),
  ('popReturn -> <empty>','popReturn',0,'p_popReturn','ForeverAlone.py',768),
  ('popComp -> <empty>','popComp',0,'p_popComp','ForeverAlone.py',788),
  ('popBool -> <empty>','popBool',0,'p_popBool','ForeverAlone.py',826),
  ('popIgual -> <empty>','popIgual',0,'p_popIgual','ForeverAlone.py',864),
  ('popMultDiv -> <empty>','popMultDiv',0,'p_popMultDiv','ForeverAlone.py',901),
  ('popSumaResta -> <empty>','popSumaResta',0,'p_popSumaResta','ForeverAlone.py',938),
  ('meterIgual -> <empty>','meterIgual',0,'p_meterIgual','ForeverAlone.py',975),
  ('meterBool -> <empty>','meterBool',0,'p_meterBool','ForeverAlone.py',980),
  ('meterMultDiv -> <empty>','meterMultDiv',0,'p_meterMultDiv','ForeverAlone.py',985),
  ('meterSumaResta -> <empty>','meterSumaResta',0,'p_meterSumaResta','ForeverAlone.py',990),
  ('meterOperador -> <empty>','meterOperador',0,'p_meterOperador','ForeverAlone.py',995),
  ('crearFuncGlobal -> <empty>','crearFuncGlobal',0,'p_crearFuncGlobal','ForeverAlone.py',1001),
  ('crearFuncMain -> <empty>','crearFuncMain',0,'p_crearFuncMain','ForeverAlone.py',1008),
  ('agregarFunc -> <empty>','agregarFunc',0,'p_agregarFunc','ForeverAlone.py',1019),
  ('agregarVariables -> <empty>','agregarVariables',0,'p_agregarVariables','ForeverAlone.py',1047),
  ('printFunciones -> <empty>','printFunciones',0,'p_printFunciones','ForeverAlone.py',1057),
  ('printTodo -> <empty>','printTodo',0,'p_printTodo','ForeverAlone.py',1062),
  ('agregarVarLista -> <empty>','agregarVarLista',0,'p_agregarVarLista','ForeverAlone.py',1076),
  ('borrarListaVar -> <empty>','borrarListaVar',0,'p_borrarListaVar','ForeverAlone.py',1108),
]
