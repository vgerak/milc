version=0.1
projectname=milc
distfolder=dist
srcfolders=pylex lexer
files=$(shell find $(srcfolders) -type f -not -name "*.pyc" -not -name "*.pyo" -not -name "*.so" -not -name "*.o")

.PHONY: dist

dist:	
	zip $(distfolder)/$(projectname).zip $(files)

