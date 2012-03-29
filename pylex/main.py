#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : main.py
# Creation Date : 29-03-2012
# Last Modified : Thu 29 Mar 2012 11:17:50 AM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/
from lexer import lexer
import readline
from sys import argv

def main():
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


if __name__=="__main__":
    main()

