
.PHONY: setup login run lint kill-ports

PYTHON = ./venv/bin/python
MODULE = src.main

# =============================================================================
# Setup & Auth
# =============================================================================

setup:
	$(PYTHON) -m $(MODULE) setup

login:
	$(PYTHON) -m $(MODULE) login

whoami:
	$(PYTHON) -m $(MODULE) whoami

# =============================================================================
# Google Workspace Operations
# =============================================================================

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

# =============================================================================
# Agent Commands
# =============================================================================

# Add agent-specific commands here if needed

