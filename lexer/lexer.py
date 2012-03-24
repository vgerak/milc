#!/bin/env python
# -*- coding: utf-8
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : lexer.py
#
#* Purpose :
#
#* Creation Date : 21-03-2012
#
#* Last Modified : Sat 20 Dec 2008 09:37:30 AM PST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

from ctypes import *
import os
path = os.path.dirname(os.path.realpath(__file__))
lib=CDLL("%s/liblex.yy.so"%path)
types=dict()
typelist=[ 't_And', 't_Array', 't_Begin', 't_Bool', 't_Char', 
't_Delete', 't_Dim', 't_Do', 't_Done', 't_Downto', 't_Else', 't_End',
't_False', 't_Float', 't_For', 't_If', 't_In', 't_Int', 't_Let', 't_Match', 
't_Mod', 't_Mutable', 't_New', 't_Not', 't_Of', 't_Rec', 't_Ref',
't_Then', 't_To', 't_True', 't_Type', 't_Unit', 't_While', 't_With', 't_Func', 't_RealPlus',
't_RealMinus', 't_RealMul', 't_RealDiv', 't_Pow', 't_AND', 't_OR',
't_DomEQ', 't_LEQ', 't_GEQ', 't_EQ', 't_NOT', 't_ASSIGN',
't_Constructor','t_Const_str','t_Const_int','t_Const_float','t_Const_char', 't_Identifier' ]
for value,name in enumerate (typelist):
    types[value+128]=name;

types[-1]='t_ERROR'
    


def yylex():
    return lib.yylex()
def yytext():
    return c_char_p.in_dll(lib,"yytext").value
def yyline():
    return c_int.in_dll(lib,"lines").value

