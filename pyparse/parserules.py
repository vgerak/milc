#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : parserules.py
# Creation Date : 02-04-2012
# Last Modified : Mon 02 Apr 2012 11:47:33 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
# Created By : Vasilis Gerakaris <vgerak@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from tokrules import *

def p_empty(p):
    '''empty :'''
    pass

def p_programm(p):
    '''program  :   empty
                |   letdef program
                |   typedef program
                ;'''
    pass

def p_letdef(p):
    '''letdef   :   'let' def repdef
                |   'let' 'rec' def repdef
                ;'''
    pass

def p_repdef(p):
    '''repdef   :   empty
                |   'and' def repdef
                ;'''
    pass

def p_def(p):
    '''def      :   id reppar '=' expr
                |   id reppar ':' type '=' expr
                |   'mutable' id
                |   'mutable' id ':' type
                |   'mutable' id '[' expr repexpr ']'
                |   'mutable' id '[' expr repexpr ']' ':' type
                ;'''
    pass

def p_reppar(p):
    '''reppar   :   empty
                |   par   
                ;'''
    pass
def p_repexpr(p):
    '''repexpr  :   empty
                |   ',' expr repexpr
                ;'''
    pass

def p_typedef(p):
    '''typedef  :   id '=' tdef reptdef'''
    pass

def p_reptdef(p):
    '''reptdef  :   empty
                |   'and' tdef reptdef
                ;'''
    pass
def p_tdef(p):
    '''tdef     :   id '=' constr repconstr'''
    pass

def p_repconstr(p):
    '''repconstr:   empty
                |   '|' constr repconstr
                ;'''
    pass

def p_constr(p):
    '''constr   :   Id
                |   Id 'of' type reptype
                ;'''
    pass

def p_reptype(p):
    '''reptype  :   empty
                |   type reptype
                ;'''
    pass

def p_par(p):
    '''par      :   id
                |   '(' id ':' type ')'
                ;'''
    pass

def p_type(p):
    '''type     :   'unit'
                |   'int'
                |   'char'
                |   'bool'
                |   'float'
                |   '(' type ')'
                |    type '->' type
                |   type 'ref'
                |   'array'
                |   'array' '[' '*' repstar ']' 'of' type
                |   id
                ;'''
    pass

def p_repstar(p):
    '''repstar  :   empty
                |   ',' '*' repstar
                ;'''
    pass


def p_expr(p):
    '''expr     :   int-const
                |   float-const
                |   char-const
                |   string-literal
                |   'true'
                |   'false'
                |   '(' ')'
                |   '(' expr ')'
                |   unop expr
                |   binop expr
                |   id
                |   id expr
                |   Id
                |   Id expr
                |   id '[' expr repexpr ']'
                |   'dim' id
                |   'dim' int-const id
                |   'new' type
                |   'delete' expr
                |   letdef 'in' expr
                |   'begin' expr 'end'
                |   'if' expr 'then' expr
                |   'if' expr 'then' expr 'else' expr
                |   'while' expr 'do' expr 'done'
                |   'for' id '=' expr 'to' expr 'do' expr 'done'
                |   'for' id '=' expr 'downto' expr 'do' expr 'done'
                |   'match' expr 'with' clause repclause 'end'
                ;'''
    pass

def p_repclause(p):
    '''repclause:   empty
                |   '|' clause repclause
                ;'''
    pass

def p_unop(p):
    '''unop     :   '+'
                |   '-'
                |   '+.'
                |   '-.'
                |   '!'
                |   'not'
                ;'''
    pass

def p_binop(p):
    '''binop    :   '+'
                |   '-'
                |   '*'
                |   '/'
                |   '+.'
                |   '-.'
                |   '*.'
                |   '/.'
                |   'mod'
                |   '**'
                |   '='
                |   '<>'
                |   '<'
                |   '>'
                |   '<='
                |   '>='
                |   '=='
                |   '!='
                |   '&&'
                |   '||'
                |   ';'
                |   ':='
                ;'''
    pass

def p_clause(p):
    '''clause   :   pattern '->' expr'''
    pass

def p_pattern(p):
    '''pattern  :   int-const
                |   '+' int-const
                |   '-' int-const
                |   '+.' float-const
                |   '-.' float-const
                |   char-const
                |   'true'
                |   'false'
                |   id
                |   '(' pattern ')'
                |   Id reppattern
                ;'''
    pass

def p_reppattern(p):
    '''reppattern   :   empty
                    |   pattern reppattern
                    ;'''
    pass
