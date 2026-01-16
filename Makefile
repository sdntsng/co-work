
.PHONY: setup login run lint crm-init crm-api crm-dashboard crm-dev

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
# CRM Commands
# =============================================================================

crm-init:
	$(PYTHON) -m $(MODULE) crm-init --name "Sales Pipeline 2026"

crm-add-lead:
	@echo "Usage: make crm-add-lead COMPANY='Acme' CONTACT='John' EMAIL='john@acme.com'"
	$(PYTHON) -m $(MODULE) crm-add-lead --company "$(COMPANY)" --contact "$(CONTACT)" --email "$(EMAIL)"

crm-list:
	$(PYTHON) -m $(MODULE) crm-list leads

crm-pipeline:
	$(PYTHON) -m $(MODULE) crm-pipeline

# =============================================================================
# CRM Servers (run these in separate terminals)
# =============================================================================

crm-api:
	@echo "Starting CRM API server on http://localhost:8001..."
	./venv/bin/uvicorn api.server:app --reload --port 8001

crm-dashboard:
	@echo "Starting CRM Dashboard on http://localhost:3000..."
	cd crm-dashboard && npm run dev

# Start both servers (API in background, dashboard in foreground)
crm-dev:
	@echo "=== CRM Development Mode ==="
	@echo "Starting API server in background..."
	@./venv/bin/uvicorn api.server:app --reload --port 8001 & echo $$! > .api.pid
	@echo "API running at http://localhost:8001"
	@echo ""
	@echo "Starting dashboard..."
	@cd crm-dashboard && npm run dev
	@# Cleanup on exit
	@kill $$(cat .api.pid) 2>/dev/null; rm -f .api.pid

crm-stop:
	@kill $$(cat .api.pid) 2>/dev/null; rm -f .api.pid || true
	@echo "Stopped CRM servers"
