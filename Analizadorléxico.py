import ply.lex as lex
import re
import codecs
import os
import sys


reservadas = ['ROBOT_R','BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST',
		'VARS','PROCS','OUT','IN','ELSE', 'ASSIGNTO','GOTO','MOVE', 'TURN', 'FACE', 'PUT',
		'PICK', 'MOVETOTHE', 'MOVEINDIR', 'JUMPTOTHE', 'JUMPINDIR', 'NOP','FACING','CANPUT',
		'CANPICK','CANMOVEINDIR','CANJUMPINDIR', 'CANMOVETOTHE','CANJUMPTOTHE', 'NOT', 
		]
D= ['SOUTH','NORTH','WEST','EAST']
O=['FRONT','RIGHT','LEFT','BACK']
X=['CHIPS','BALLOONS']

tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
		'ODD','ASSIGN','NE','LT','LTE','GT','GTE',
		'LPARENT', 'RPARENT','LBRACKED','RBRACKED', 'SEPARATOR','COMMA','SEMMICOLOM',
		'DOT','UPDATE', 'SENTIDOS', 'DIRECTIONS', 'COLON', 'X'
		]
t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKED = r'\['
t_RBRACKED = r'\]'
t_SEPARATOR = r'\|'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_COLON = r':'
t_DOT = r'\.'
t_UPDATE = r':='


def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
	elif t.value.upper() in D:
		t.value = t.value
		t.type = 'SENTIDOS'
	elif t.value.upper() in O:
		t.value = t.value
		t.type = 'DIRECTIONS'
	elif t.value.upper() in X:
		t.value = t.value
		t.type = 'X'
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def espacio(t):
	r'\" "*'
	pass


def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)




test = "ROBOT_R.txt"
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok : break
	print (tok)