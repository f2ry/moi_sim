# Инициализация модуля ui
from .menus import main_menu, network_menu, internet_menu, show_manual
from .views import show_topology, show_message
from .styles import ICONS, COLORS

__all__ = ['main_menu', 'network_menu', 'internet_menu', 'show_manual', 
           'show_topology', 'show_message', 'ICONS', 'COLORS']