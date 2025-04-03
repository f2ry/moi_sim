# Инициализация модуля core
from .state import game_state
from .network import create_network, test_connection, configure_internet
from .devices import Computer, Router

__all__ = ['game_state', 'create_network', 'test_connection', 'configure_internet', 'Computer', 'Router']