#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : tokrules.py
# Creation Date : 29-03-2012
# Last Modified : Thu 29 Mar 2012 10:40:18 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/
from sys import argv

reserved = {
'array'     : 'Array',
'begin'     : 'Begin',
'bool'      : 'Bool',
'char'      : 'Char',
'delete'    : 'Delete',
'dim'       : 'Dim',
'do'        : 'Do',
'done'      : 'Done',
'downto'    : 'Downto',
'else'      : 'Else',
'end'       : 'End',
'false'     : 'False',
'float'     : 'Float',
'for'       : 'For',
'if'        : 'If',
'in'        : 'In',
'int'       : 'Int',
'let'       : 'Let',
'match'     : 'Match',
'mod'       : 'Mod',
'mutable'   : 'Mutable',
'new'       : 'New',
'not'       : 'Not',
'of'        : 'Of',
'rec'       : 'Rec',
'ref'       : 'Ref',
'then'      : 'Then',
'to'        : 'To',
'true'      : 'True',
'type'      : 'Type',
'unit'      : 'Unit',
'while'     : 'While',
'with'      : 'With'
}

literals = [ '+', '-', '*', '/', '=', '(', ')', '|', ';', '!', '<', '>', '[', ']', ',', ':' ]

tokens = [ 'Func', 'Plus', 'Minus', 'Mul', 'Div', 'Equals', 'LPAREN', 'RPAREN',
'VBar', 'Semicolon', 'Bang', 'Less', 'Greater', 'LSQPAREN',
'RSQPAREN', 'BSlash', 'Comma', 'Colon',

'RealPlus', 'RealMinus', 'RealMul', 'RealDiv', 'Pow', 'AND', 'OR',
'DomEQ', 'LEQ', 'GEQ', 'EQ', 'NOT', 'ASSIGN',
'Constructor','Const_str','Const_int','Const_float','Const_char', 'Comment', 'MlComment',
'Identifier' , 'literals' ] + list(reserved.values())

# Tokens

t_Func           =  r'->'
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
t_Const_str      =  r'\"([^\\\n]|(\\.))*?\"'
t_Const_int      =  r'[0-9]+'
t_Const_float    =  r'[0-9]+\.?[0-9]+([eE][+-]?[0-9]+)?'
t_Const_char     =  r'\'(\\[nrt0\\\"\']|\\x[0-9a-fA-F]{2}|[^\'\"\\])\''
t_ignore_Comment =  r'--.*'
t_ignore         =  " \t"

# Declare the state
states = (
    ('mlcomment','exclusive'),
)

def t_mlcomment(t):
    r'\(\*'
    try:
        if t.lexer.level == 0:                           
            t.lexer.code_start = t.lexer.lexpos         # Record the starting position
            t.lexer.level = 1                           # Initial brace level
            t.lexer.begin('mlcomment')                  # Enter 'mlcomment' state
        else:
            t.lexer.level += 1
    except AttributeError:
        t.lexer.code_start = t.lexer.lexpos         # Record the starting position
        t.lexer.level = 1                           # Initial brace level
        t.lexer.begin('mlcomment')                  # Enter 'mlcomment' state

# Rules for the comment state
def t_mlcomment_start(t):
    r'\(\*'
    t.lexer.level +=1

def t_mlcomment_end(t):
    r'\*\)'
    t.lexer.level -=1

    # If closing brace, return the comment fragment
    if t.lexer.level == 0:
         t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos+1]
         t.type = "MlComment"
         t.lexer.lineno += t.value.count('\n')
         t.lexer.begin('INITIAL')
         pass
         #return t

def t_mlcomment_anydata(t):
    r'.+'

def t_mlcomment_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Ignored characters (whitespace)
t_mlcomment_ignore = " \t"

# For bad characters, we just skip over it
def t_mlcomment_error(t):
    t.lexer.skip(1)

def t_Reserved(t):
    r'[a-z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'Identifier')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    if len(argv) > 1:
        fname = argv[1]
    else:
        fname = "stdin"
    print("%s:%s:%s #> Illegal character '%s'" % (fname, t.lexer.lineno, t.lexpos, t.value[0]))
    t.lexer.skip(1)
