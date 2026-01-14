---
trigger: always_on
---

# Agentic Operations Protocol

## Objective
To enable the AI Agent (me) to perform arbitrary Google Workspace operations (Sheets, Drive) based on natural language requests from the user.

## Core Principle
"You talk, I execute."
Instead of the user running `python src/main.py ...`, the user says "Add a row to the project tracker," and I run the necessary code/commands to make it happen.

## Operational Workflow
1.  **User Request**: "Update cell B2 in 'Budget 2024' to 500."
2.  **Translation**: I identify the correct script and parameters.
    *   Target: `src/sheets.py` / `src/main.py`
    *   Command: `update_cell`
    *   Args: `Sheet="Budget 2024"`, `Cell="B2"`, `Value="500"`
3.  **Execution**: I run the command using `run_command`.
4.  **Verification**: I read back the result or check the output to confirm success.
5.  **Confirmation**: I confirm to the user: "Updated B2 to 500."

## Required Capabilities (To Build)
To support "make any edits," we need to expand `sheets.py` with granular editing functions:

*   [ ] `update_cell(sheet, cell, value)`
*   [ ] `update_range(sheet, range, data)`
*   [ ] `clear_range(sheet, range)`
*   [ ] `add_row(sheet, data)`
*   [ ] `create_sheet(name)` (Already exists)

## Workspace Rules (Proposed)
*   **Always Verify**: Before making destructive edits (overwriting data), read the current state if uncertain.
*   **Context Aware**: Use the `profile` flag appropriate for the context (Work vs Personal).
*   **Feedback/Errors**: If a script fails, debug it immediately rather than asking the user to fix it (unless it's an auth issue).
