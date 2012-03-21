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

def yylex():
    return lib.yylex()
def yyline():
    return lib.line

