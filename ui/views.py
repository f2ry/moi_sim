from rich import print
from rich.panel import Panel
from ui.styles import ICONS, COLORS

def show_topology(pc1, pc2, router):
    print("\n[bold]Топология сети:[/bold]")
    print(f"  {ICONS['pc']} {pc1.name} {'->' if pc1.connected_to else ICONS['disconnected']} {router.name}")
    print(f"  {ICONS['pc']} {pc2.name} {'->' if pc2.connected_to else ICONS['disconnected']} {router.name}")

def show_message(text, msg_type="info"):
    print(f"[{COLORS[msg_type]}]{text}[/{COLORS[msg_type]}]")