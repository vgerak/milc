#!/bin/sh
for i in `ls $1`
do
    echo $i
    ./main.py < $1/$i | grep ERROR
    read
done