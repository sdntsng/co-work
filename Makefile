
.PHONY: setup login run lint

PYTHON = ./venv/bin/python
MODULE = src.main

setup:
	$(PYTHON) -m $(MODULE) setup

login:
	$(PYTHON) -m $(MODULE) login

run:
	$(PYTHON) -m $(MODULE)

whoami:
	$(PYTHON) -m $(MODULE) whoami

list-sheets:
	$(PYTHON) -m $(MODULE) list-sheets

list-files:
	$(PYTHON) -m $(MODULE) list-files

update-cell:
	$(PYTHON) -m $(MODULE) update-cell

append-row:
	$(PYTHON) -m $(MODULE) append-row

read-doc:
	$(PYTHON) -m $(MODULE) read-doc
