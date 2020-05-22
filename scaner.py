import ply.lex as lex

import sys

reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void':'VOID',
    'var': 'VAR',
    'program': 'PROGRAM',
    'func': 'FUNC',
    'return': 'RETURN',
    'read': 'READ',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'from': 'FROM',
    'to': 'TO',
    'do': 'DO',
    'then': 'THEN',
    'main': 'MAIN'
}

tokens = [
    'C_INT',
    'C_FLOAT',
    'C_CHAR',
    'C_STRING',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'COMMA',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'AND',
    'OR',
    'GREATER_THAN',
    'LESS_THAN',
    'LSBRACKET',
    'RSBRACKET',
    'GREATER_OR_EQUAL',
    'LESS_OR_EQUAL',
    'IS_EQUAL',
    'NOT_EQUAL'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_IS_EQUAL = r'\=\='
t_NOT_EQUAL = r'\!\='
t_GREATER_OR_EQUAL = r'\>\='
t_LESS_OR_EQUAL = r'\<\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_EQUALS = r'\='
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LSBRACKET = r'\['
t_RSBRACKET = r'\]'
t_AND = r'\&\&'
t_OR = r'\|\|'

t_ignore = " \t\n"

def t_C_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_C_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_C_STRING(t):
    r'\".*\"'
    return t

def t_C_CHAR(t):
    r'\'[a-zA-z_0-9]\''
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_error(t):
    print("Illegal characters:", t.value)
    t.lexer.skip(1)

lexer = lex.lex()



""" while True:
    try:
        s = input('')
    except EOFError:
        break """

