#!/usr/bin/python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : main.py
# Creation Date : 21-03-2012
# Last Modified : Sat 24 Mar 2012 02:21:22 PM EET
# Created By : Greg Liras <gregliras@gmail.com>
# Created By : Vasilis Gerakaris <vgerak@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys
from lexer import types, yylex,yytext,yyline

def main():
    i = yylex()
    while i:
        try:
            print "line: %d\t\t\t%s\t\t\t%s"%(yyline(),types[i],yytext())
        except KeyError:
            print "line: %d\t\t\t%s\t\t\t%s"%(yyline(),i,yytext())

        i = yylex()

if __name__=="__main__":
    main()

