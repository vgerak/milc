#!/bin/env python
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

import lexer
import sys

def main():
    i = lexer.yylex()
    while i:
        print i, lexer.yytext().value
        i = lexer.yylex()

if __name__=="__main__":
    main()

