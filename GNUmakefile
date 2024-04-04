.POSIX:
.SUFFIXES:
PROJECT=py-tictactui
VERSION=1.0.0
PYTHON3 = python3
PREFIX=/usr/local

all:
clean:
install:
check:
## -- BLOCK:license --
install: install-license
install-license: 
	mkdir -p $(DESTDIR)$(PREFIX)/share/doc/$(PROJECT)
	cp LICENSE $(DESTDIR)$(PREFIX)/share/doc/$(PROJECT)
## -- BLOCK:license --
## -- BLOCK:python --
all:
	$(PYTHON3) setup.py build
install:
	$(PYTHON3) setup.py install -O2 --prefix=$(PREFIX) $(if $(DESTDIR),--root=$(DESTDIR)) 
clean:
	rm -rf build dist/*.egg *.egg-info
	rm -rf $$(find . -type d -iname __pycache__)
	rmdir dist 2>/dev/null || true
## -- BLOCK:python --
