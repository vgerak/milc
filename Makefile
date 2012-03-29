folders=pylex lexer
files=$(shell find $(folders) -type f -not -name "*.pyc" -not -name "*.pyo" -not -name "*.so" -not -name "*.o")

dist:
	echo $(files)
	#zip milc.zip $(files)

