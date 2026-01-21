#!/bin/bash

# Define paths
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_PYTHON="$PROJECT_ROOT/mcp-servers/.venv/bin/python"
INGEST_SCRIPT="$PROJECT_ROOT/memory-system/ingest.py"
LOG_FILE="$PROJECT_ROOT/memory_ingest.log"

# Define the cron command (Hourly)
# 0 * * * * cd /path/to/project && /path/to/python /path/to/ingest.py >> /path/to/log 2>&1
CRON_CMD="0 * * * * cd $PROJECT_ROOT && $VENV_PYTHON $INGEST_SCRIPT >> $LOG_FILE 2>&1"

# Check if job already exists
(crontab -l 2>/dev/null | grep -F "$INGEST_SCRIPT") && echo "Job already exists in crontab" && exit 0

# Add job to crontab
(crontab -l 2>/dev/null; echo "$CRON_CMD") | crontab -

echo "✅ Installed hourly cron job:"
echo "$CRON_CMD"
