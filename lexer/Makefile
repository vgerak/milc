TARGET=llama

liblex.yy.so:	$(TARGET).l
	flex -s -8 -F $(TARGET).l
	gcc -c lex.yy.c
	ld -G lex.yy.o -lfl -o liblex.yy.so
clean:
	rm -f *.o *.so
