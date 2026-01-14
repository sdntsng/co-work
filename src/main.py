import typer
from rich.console import Console

from .auth import authenticate
from .sheets import SheetManager
from .drive import DriveManager
from .docs import DocsManager
from .workflows import WorkflowManager

app = typer.Typer()
console = Console()

@app.command()
def setup():
    """Helps set up the Google Workspace credentials."""
    console.print("[bold yellow]Setup Instructions:[/bold yellow]")
    console.print("1. Go to [link=https://console.cloud.google.com/]Google Cloud Console[/link].")
    console.print("2. Create a new project or select an existing one.")
    console.print("3. Enable [bold]Google Sheets API[/bold] and [bold]Google Drive API[/bold].")
    console.print("4. Configure OAuth Consent Screen (External, Add your email as tester).")
    console.print("5. Create Credentials > OAuth Client ID > Desktop App.")
    console.print("6. Download JSON and save as [bold]credentials.json[/bold] in this directory.")
    console.print("7. Run [bold]python src/main.py login[/bold].")

@app.command()
def login(profile: str = typer.Option("default", help="Profile name (e.g., personal, work)")):
    """Authenticates with Google."""
    try:
        authenticate(profile)
        console.print(f"[green]Successfully authenticated profile: {profile}![/green]")
    except Exception as e:
        console.print(f"[red]Authentication failed: {e}[/red]")

@app.command()
def whoami(profile: str = typer.Option("default", help="Profile name")):
    """Shows the currently logged in email for the profile."""
    try:
        _, creds = authenticate(profile)
        if creds and hasattr(creds, 'id_token') and creds.id_token:
            # Note: creds.id_token might be JWT, simplistic check here or use service endpoint
            pass
        
        # Simpler method: use the drive service to get 'about' info
        manager = DriveManager(creds)
        about = manager.service.about().get(fields="user").execute()
        email = about['user']['emailAddress']
        console.print(f"Profile '[bold]{profile}[/bold]' is logged in as: [green]{email}[/green]")

    except Exception as e:
        console.print(f"[red]Not logged in or error: {e}[/red]")

@app.command()
def list_sheets(profile: str = typer.Option("default", help="Profile name")):
    """Lists all Google Sheets."""
    try:
        gc, _ = authenticate(profile)
        manager = SheetManager(gc)
        manager.list_files()
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def read_data(sheet: str, profile: str = typer.Option("default", help="Profile name")):
    """Reads all data from a sheet."""
    try:
        gc, _ = authenticate(profile)
        manager = SheetManager(gc)
        data = manager.read_data(sheet)
        if data:
            console.print(data)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def read_doc(doc_id: str, profile: str = typer.Option("default", help="Profile name")):
    """Reads a Google Doc and prints content."""
    try:
        _, creds = authenticate(profile)
        manager = DocsManager(creds)
        content = manager.read_doc(doc_id)
        if content:
            console.print(content)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def list_files(query: str = typer.Option(None, help="Search query"), profile: str = typer.Option("default", help="Profile name")):
    """Lists files in Google Drive."""
    try:
        _, creds = authenticate(profile)
        manager = DriveManager(creds)
        manager.list_files(query=query)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def create_project(name: str, profile: str = typer.Option("default", help="Profile name")):
    """Workflow: Creates a new project workspace (Sheet + Folder)."""
    try:
        gc, creds = authenticate(profile)
        workflow = WorkflowManager(gc, creds)
        workflow.create_project_workspace(name)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def update_cell(sheet: str, cell: str, value: str, profile: str = typer.Option("default", help="Profile name")):
    """Updates a single cell."""
    try:
        gc, _ = authenticate(profile)
        manager = SheetManager(gc)
        manager.update_cell(sheet, cell, value)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def append_row(sheet: str, values: str = typer.Argument(..., help="Comma separated values"), profile: str = typer.Option("default", help="Profile name")):
    """Appends a row. Usage: append_row 'SheetName' 'Value1,Value2'"""
    try:
        gc, _ = authenticate(profile)
        manager = SheetManager(gc)
        data = [v.strip() for v in values.split(",")]
        manager.append_row(sheet, data)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    app()
