DESTDIR =
PREFIX  =/usr/local
PYTHON3 =python3


all:
clean:
install:
update:
## -- PYTHON --
all: all-python
all-python:
	$(PYTHON3) setup.py build
install: install-python
install-python:
	$(PYTHON3) setup.py install -O2 $(if \
	    $(DESTDIR),--root=$(DESTDIR) \
	    )--prefix=$(PREFIX)
clean: clean-python
clean-python:
	rm -rf build dist/*.egg *.egg-info
	rm -rf `find . -type d -iname __pycache__`
	rmdir dist 2>/dev/null || true
## -- PYTHON --
