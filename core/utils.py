import os
import platform

def init_console():
    """Настройка консоли"""
    if platform.system() == "Windows":
        os.system('mode con: cols=100 lines=30')
    else:
        os.system('resize -s 30 100')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')