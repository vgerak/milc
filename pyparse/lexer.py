#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : lexer.py
# Creation Date : 21-03-2012
# Last Modified : Thu 29 Mar 2012 11:25:49 AM EEST
# Created By : Greg Liras <gregliras@gmail.com>
# Created By : Vasilis Gerakaris <vgerak@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

# Build the lexer
from tokrules import *
import ply.lex as lex
from sys import argv
import readline

lexer = lex.lex(optimize = 1)
def main():
    global lexer
    if len(argv) > 1:
        f = open(argv[1], "r")
        for line in f:
            lexer.input(line)
            while 1:
                tok = lexer.token()
                if not tok: 
                    break
                #uncomment to print tokens
                #print tok
    else:
        print "Interactive mode"
        while 1:
            try:
                sometext = raw_input("> ")
                lexer.input(sometext)
                while 1:
                    tok = lexer.token()
                    if not tok:
                        break
                    #uncomment to print tokens
                    print tok
            except EOFError:
                print "EOF"
                break

if __name__ == "__main__":
    main()

### Stuff for Parser later on ###

## Precedence rules for the arithmetic operators
#precedence = (
#    ('left','Plus','Minus','RealPlus','RealMinus'),
#    ('left','Mul','Div','RealMul','RealDiv'),
#    ('left','Pow')
#    )
#
## dictionary of names (for storing variables)
#names = { }
#
#
#def p_error(p):
#    print("Syntax error at '%s'" % p.value)
#
#import ply.yacc as yacc
#yacc.yacc()
#
#while 1:
#    try:
#        s = raw_input('test test:')
#    except EOFError:
#        break
#    yacc.parse(s)
