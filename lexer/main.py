#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : main.py
# Creation Date : 21-03-2012
# Last Modified : Sat 24 Mar 2012 08:47:26 PM EET
# Created By : Greg Liras <gregliras@gmail.com>
# Created By : Vasilis Gerakaris <vgerak@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys
from lexer import types, yylex,yytext,yyline,yyopenIO,yycloseIO

def main():
    if len(sys.argv) > 1:
        yyopenIO(sys.argv[1])
    i = yylex()
    while i:
        try:
            print "line: %d\t\t\t%s\t\t\t%s"%(yyline(),types[i],yytext())
        except KeyError:
            print "line: %d\t\t\t%s\t\t\t%s"%(yyline(),i,yytext())

        i = yylex()
    if len(sys.argv) > 1:
        yycloseIO()
    return 0

if __name__=="__main__":
    main()

