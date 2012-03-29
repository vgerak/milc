version=0.1
projectname=milc
distfolder=dist
srcfolders=pylex lexer
files=$(shell find $(srcfolders) -type f -not -name "*.pyc" -not -name "*.pyo" -not -name "*.so" -not -name "*.o")

.PHONY: dist

dist:	
	zip --quiet $(distfolder)/$(projectname)-$(version).zip $(files)
	tar -czf $(distfolder)/$(projectname)-$(version).tar.gz $(files)

