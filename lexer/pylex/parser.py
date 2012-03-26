#!/usr/bin/python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : parser.py
# Creation Date : 26-03-2012
# Last Modified : Mon 26 Mar 2012 08:03:14 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/
from lexer import *
import ply.yacc as yacc

yacc.yacc()

precedence = (  ('left','And','Array'),
                ('left','','DIVIDE'),
                ('right','UMINUS'),
        )



def main():
    while 1:
        try:
            s = input("lol me > ")
        except EOFError:
            break
    yacc.parse(s)

if __name__=="__main__":
    main()

