#!/bin/env python
# -*- coding: utf-8
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : test.py
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

def main():
    lib=CDLL("%s/liblex.yy.so"%path)
    #flexlib = cdll.LoadLibary(lib)
    print lib.yylex()

if __name__=="__main__":
    main()

