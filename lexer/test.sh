#!/bin/sh
for i in `ls $1`
do
    ./main.py < $1/$i | grep ERROR
    read
done
