TARGET=llama
TESTDIR=../samples/

liblex.yy.so:	$(TARGET).l
	flex -8 -F $(TARGET).l
	gcc -c lex.yy.c
	ld -G lex.yy.o -lfl -o liblex.yy.so
clean:
	rm -f *.o *.so
tests:
	./test.sh $(TESTDIR)
