#!/usr/bin/env python3
"""
Import Close CRM CSV exports into Google Sheets CRM.

Usage:
    python scripts/import_crm.py --sheet-url "URL" [--clear] [--dry-run]
"""

import csv
import sys
from pathlib import Path
from datetime import datetime

import typer
from rich.console import Console
from rich.table import Table

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from auth import authenticate
from sheets import SheetManager

app = typer.Typer()
console = Console()

# File paths
LOCAL_FILES_DIR = Path(__file__).parent.parent / "local-files"
LEADS_CSV = LOCAL_FILES_DIR / "Vinci leads 2026-01-16 20-12.csv"
OPPORTUNITIES_CSV = LOCAL_FILES_DIR / "Vinci opportunities 2026-01-16 20-12.csv"


def parse_date(date_str: str) -> str:
    """Convert ISO datetime to YYYY-MM-DD format."""
    if not date_str:
        return ""
    try:
        # Handle various formats
        for fmt in [
            "%Y-%m-%d %H:%M:%S.%f%z",
            "%Y-%m-%d %H:%M:%S%z",
            "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%dT%H:%M:%S.%f%z",
            "%Y-%m-%d",
        ]:
            try:
                dt = datetime.strptime(date_str, fmt)
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                continue
        return date_str[:10] if len(date_str) >= 10 else date_str
    except Exception:
        return date_str


def read_csv(filepath: Path) -> list[dict]:
    """Read CSV file and return list of dicts."""
    if not filepath.exists():
        console.print(f"[red]File not found: {filepath}[/red]")
        return []
    
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def transform_leads(rows: list[dict]) -> list[list[str]]:
    """Transform Close leads CSV to target sheet format."""
    transformed = []
    
    for row in rows:
        lead_row = [
            row.get("id", ""),                                    # lead_id
            row.get("display_name", "") or row.get("lead_name", ""),  # company_name
            row.get("primary_contact_name", ""),                  # contact_name
            row.get("primary_contact_primary_email", ""),         # contact_email
            row.get("primary_contact_primary_phone", ""),         # contact_phone
            row.get("status_label", ""),                          # status
            "Close Import",                                       # source
            "",                                                   # industry (not in source)
            "",                                                   # company_size (not in source)
            row.get("description", ""),                           # notes
            parse_date(row.get("date_created", "")),              # created_at
            parse_date(row.get("date_updated", "")),              # updated_at
            row.get("created_by_name", ""),                       # owner
        ]
        transformed.append(lead_row)
    
    return transformed


def transform_opportunities(rows: list[dict]) -> list[list[str]]:
    """Transform Close opportunities CSV to target sheet format."""
    transformed = []
    
    for row in rows:
        value = row.get("value", "") or "0"
        confidence = row.get("confidence", "") or "0"
        
        # Calculate expected value
        try:
            value_num = float(value)
            confidence_num = float(confidence)
            expected_value = value_num * confidence_num / 100
        except (ValueError, TypeError):
            expected_value = 0
        
        opp_row = [
            row.get("id", ""),                          # opp_id
            row.get("lead_id", ""),                     # lead_id
            row.get("note", "") or row.get("lead_name", ""),  # title
            row.get("status_label", ""),                # stage
            value,                                      # value
            confidence,                                 # probability
            str(expected_value),                        # expected_value
            parse_date(row.get("date_won", "")),        # close_date
            "",                                         # product (not in source)
            row.get("note", ""),                        # notes
            parse_date(row.get("date_created", "")),    # created_at
            parse_date(row.get("date_updated", "")),    # updated_at
            parse_date(row.get("date_won", "")),        # closed_at
            row.get("user_name", ""),                   # owner
        ]
        transformed.append(opp_row)
    
    return transformed


def preview_data(data: list[list[str]], title: str, headers: list[str]):
    """Show a preview of the data."""
    table = Table(title=title)
    for h in headers[:6]:
        table.add_column(h, style="bold", overflow="ellipsis", max_width=20)
    
    for row in data[:5]:
        table.add_row(*[str(c)[:20] for c in row[:6]])
    
    console.print(table)
    console.print(f"[dim]...and {len(data) - 5} more rows[/dim]" if len(data) > 5 else "")


@app.command()
def import_data(
    sheet_url: str = typer.Option(..., "--sheet-url", help="Google Sheets URL"),
    clear: bool = typer.Option(False, "--clear", help="Clear existing data before import"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview without uploading"),
    profile: str = typer.Option("default", "--profile", help="Auth profile"),
):
    """Import Close CRM data into Google Sheets."""
    
    console.print("[bold blue]Close CRM → Google Sheets Import[/bold blue]\n")
    
    # Read CSVs
    console.print("[yellow]Reading CSV files...[/yellow]")
    leads_raw = read_csv(LEADS_CSV)
    opps_raw = read_csv(OPPORTUNITIES_CSV)
    
    console.print(f"  Found {len(leads_raw)} leads, {len(opps_raw)} opportunities\n")
    
    # Transform data
    console.print("[yellow]Transforming data...[/yellow]")
    leads_data = transform_leads(leads_raw)
    opps_data = transform_opportunities(opps_raw)
    
    # Preview
    leads_headers = ["lead_id", "company_name", "contact_name", "contact_email", "contact_phone", "status", "source", "industry", "company_size", "notes", "created_at", "updated_at", "owner"]
    opps_headers = ["opp_id", "lead_id", "title", "stage", "value", "probability", "expected_value", "close_date", "product", "notes", "created_at", "updated_at", "closed_at", "owner"]
    
    console.print()
    preview_data(leads_data, "Leads Preview", leads_headers)
    console.print()
    preview_data(opps_data, "Opportunities Preview", opps_headers)
    console.print()
    
    if dry_run:
        console.print("[yellow]Dry run complete. No data uploaded.[/yellow]")
        return
    
    # Authenticate and upload
    console.print("[yellow]Authenticating...[/yellow]")
    gc, _ = authenticate(profile)
    manager = SheetManager(gc)
    
    # Open spreadsheet
    sh = manager.get_sheet(sheet_url)
    if not sh:
        console.print("[red]Failed to open spreadsheet[/red]")
        raise typer.Exit(1)
    
    # Upload Leads
    console.print("\n[yellow]Uploading leads...[/yellow]")
    try:
        leads_ws = sh.worksheet("Leads")
        if clear:
            # Clear all data except header
            leads_ws.batch_clear(["A2:Z1000"])
            console.print("  Cleared existing leads data")
        leads_ws.append_rows(leads_data, value_input_option="RAW")
        console.print(f"[green]  ✓ Uploaded {len(leads_data)} leads[/green]")
    except Exception as e:
        console.print(f"[red]Error uploading leads: {e}[/red]")
    
    # Upload Opportunities
    console.print("\n[yellow]Uploading opportunities...[/yellow]")
    try:
        opps_ws = sh.worksheet("Opportunities")
        if clear:
            opps_ws.batch_clear(["A2:Z1000"])
            console.print("  Cleared existing opportunities data")
        opps_ws.append_rows(opps_data, value_input_option="RAW")
        console.print(f"[green]  ✓ Uploaded {len(opps_data)} opportunities[/green]")
    except Exception as e:
        console.print(f"[red]Error uploading opportunities: {e}[/red]")
    
    console.print("\n[bold green]Import complete![/bold green]")
    console.print(f"View your data: {sheet_url}")


if __name__ == "__main__":
    app()
