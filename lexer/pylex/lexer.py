#!/usr/bin/python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : lexer.py
# Creation Date : 21-03-2012
# Last Modified : Mon 26 Mar 2012 22:44:01 EEST
# Created By : Greg Liras <gregliras@gmail.com>
# Created By : Vasilis Gerakaris <vgerak@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

import ply.lex as lex

tokens=( 'And', 'Array', 'Begin', 'Bool', 'Char',
'Delete', 'Dim', 'Do', 'Done', 'Downto', 'Else', 'End',
'False', 'Float', 'For', 'If', 'In', 'Int', 'Let', 'Match',
'Mod', 'Mutable', 'New', 'Not', 'Of', 'Rec', 'Ref',
'Then', 'To', 'True', 'Type', 'Unit', 'While', 'With',

'Plus', 'Minus', 'Mul', 'Div', 'Equals', 'LPAREN', 'RPAREN',
'VBar', 'Semicolon', 'Bang', 'Less', 'Greater', 'LSQPAREN',
'RSQPAREN', 'BSlash', 'Comma', 'Colon',

'Func', 'RealPlus',
'RealMinus', 'RealMul', 'RealDiv', 'Pow', 'AND', 'OR',
'DomEQ', 'LEQ', 'GEQ', 'EQ', 'NOT', 'ASSIGN',
'Constructor','Const_str','Const_int','Const_float','Const_char', 'Comment', 'Identifier' )

# Tokens

t_And            =  r'and'
t_Array          =  r'array'
t_Begin          =  r'begin'
t_Bool           =  r'bool'
t_Char           =  r'char'
t_Delete         =  r'delete'
t_Dim            =  r'dim'
t_Do             =  r'do'
t_Done           =  r'done'
t_Downto         =  r'downto'
t_Else           =  r'else'
t_End            =  r'end'
t_False          =  r'false'
t_Float          =  r'float'
t_For            =  r'for'
t_If             =  r'if'
t_In             =  r'in'
t_Int            =  r'int'
t_Let            =  r'let'
t_Match          =  r'match'
t_Mod            =  r'mod'
t_Mutable        =  r'mutable'
t_New            =  r'new'
t_Not            =  r'not'
t_Of             =  r'of'
t_Rec            =  r'rec'
t_Ref            =  r'ref'
t_Then           =  r'then'
t_To             =  r'to'
t_True           =  r'true'
t_Type           =  r'type'
t_Unit           =  r'unit'
t_While          =  r'while'
t_With           =  r'with'
t_Func           =  r'−>'

t_Plus           =  r'\+'
t_Minus          =  r'-'
t_Mul            =  r'\*'
t_Div            =  r'/'
t_Equals         =  r'='
t_LPAREN         =  r'\('
t_RPAREN         =  r'\)'
t_VBar           =  r'\|'
t_Semicolon      =  r';'
t_Bang           =  r'!'
t_Less           =  r'<'
t_Greater        =  r'>'
t_LSQPAREN       =  r'\['
t_RSQPAREN       =  r'\]'
t_BSlash         =  r'\\'
t_Comma          =  r','
t_Colon          =  r':'

t_RealPlus       =  r'\+\.'
t_RealMinus      =  r'−\.'
t_RealMul        =  r'\*\.'
t_RealDiv        =  r'/\.'
t_Pow            =  r'\*\*'
t_AND            =  r'&&'
t_OR             =  r'\|\|'
t_DomEQ          =  r'<>'
t_LEQ            =  r'<='
t_GEQ            =  r'>='
t_EQ             =  r'=='
t_NOT            =  r'!='
t_ASSIGN         =  r':='
t_Constructor    =  r'[A-Z][a-zA-Z0-9_]*'
t_Const_str      =  r'".*"'
t_Const_int      =  r'[0-9]'
t_Const_float    =  r'[+-]?[0-9]+\.[0-9]+([Ee][+-]?[0-9]+)?]'
t_Const_char     =  r'(\'.\')|(\.\\[nrt0\'\"]\.)|(\'\\x[0-9a-fA-F]{2}\')'
t_Comment        =  r'(\*[^("(*"|"*)")]*\*)'
t_Identifier     =  r'[a-z][a-zA-Z0-9_]*'
t_ignore         =  " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

while 1:
    try:
        s = raw_input()
    except EOFError:
        break
    yacc.parse(s)
