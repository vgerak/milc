#!/usr/bin/python
# -*- coding: utf-8
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : main.py
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

import sys
from lexer import types, yylex,yytext,yyline

def main():
    i = yylex()
    while i:
        try:
            print types[i], "\t\t\t",yytext()
        except KeyError:
            print i, "\t\t\t", yytext()

        i = yylex()

if __name__=="__main__":
    main()

