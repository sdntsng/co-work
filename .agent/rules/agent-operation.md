
# Agentic Operations Protocol

## Objective
Enable the AI Agent to perform Google Workspace operations AND manage the Sales CRM based on natural language requests.

## Core Principle
"You talk, I execute."

---

## Sales CRM System

### Architecture
```
Google Sheets (Data) ←→ Python CRM Module ←→ FastAPI Server ←→ Next.js Dashboard
```

### Quick Start
```bash
# One command to start everything:
make crm-dev

# Or separately:
make crm-api        # API on http://localhost:8001
make crm-dashboard  # Dashboard on http://localhost:3000
```

### CRM CLI Commands
| Command | Description |
|---------|-------------|
| `make crm-init` | Create CRM Google Sheet |
| `make crm-list` | List all leads |
| `make crm-pipeline` | Show pipeline summary |
| `make crm-add-lead COMPANY="X" CONTACT="Y" EMAIL="z@x.com"` | Add lead |

### Google Sheet
- **Name**: `Sales Pipeline 2026`
- **Tabs**: Leads, Opportunities, Activities, Summary
- **URL**: Check output of `make crm-init`

### Pipeline Stages
1. Prospecting → 2. Discovery → 3. Proposal → 4. Negotiation
5. Closed Won / Closed Lost
6. Delivery → 7. Invoicing → 8. Cash in Bank

---

## Agentic CRM Operations

### Adding Leads
**User**: "Add Stripe as a lead, contact is Patrick Collison, email patrick@stripe.com"
**Agent runs**:
```bash
./venv/bin/python -m src.main crm-add-lead --company "Stripe" --contact "Patrick Collison" --email "patrick@stripe.com"
```

### Adding Opportunities
**User**: "Create a $50k deal for Stripe, 60% probability"
**Agent runs**:
```bash
./venv/bin/python -m src.main crm-add-opp --lead-id "<lead_id>" --title "Stripe Enterprise Deal" --value 50000 --probability 60
```

### Viewing Pipeline
**User**: "Show me the pipeline"
**Agent runs**:
```bash
./venv/bin/python -m src.main crm-pipeline
```

---

## Google Workspace Operations

### Sheets Operations
| Operation | Command |
|-----------|---------|
| List sheets | `./venv/bin/python -m src.main list-sheets` |
| Read data | `./venv/bin/python -m src.main read-data "Sheet Name"` |
| Update cell | `./venv/bin/python -m src.main update-cell "Sheet" "A1" "value"` |
| Append row | `./venv/bin/python -m src.main append-row "Sheet" "val1,val2,val3"` |

### Drive Operations
| Operation | Command |
|-----------|---------|
| List files | `./venv/bin/python -m src.main list-files` |
| Search | `./venv/bin/python -m src.main list-files --query "keyword"` |

---

## Rules
- **Always use venv**: Commands must use `./venv/bin/python`
- **Verify destructive ops**: Read before overwriting data
- **Handle errors**: Debug failed scripts immediately
- **CRM Sheet Name**: Default is "Sales Pipeline 2026"
