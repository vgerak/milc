TARGET=test

liblex:	$(TARGET).l
	flex $(TARGET).l
	gcc -c lex.yy.c
	ld -G lex.yy.o -lfl -o liblex.yy.so
clean:
	rm -f *.o *.so
