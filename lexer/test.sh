#!/bin/bash
for i in `ls $1`
do
    echo $i
    ./main.py $1/$i
    read
done
