from rich.progress import track
import time
from core.state import game_state
from core.devices import Computer, Router

def create_network():
    """Создает и возвращает устройства сети"""
    return {
        'pc1': Computer("PC-1", "192.168.1.1"),
        'pc2': Computer("PC-2", "192.168.1.2"),
        'router': Router("192.168.1.254")
    }

def test_connection(device1, device2):
    """Проверяет соединение между устройствами"""
    if not device1.connected_to or not device2.connected_to:
        return False
    
    # Анимация проверки связи
    for _ in track(range(5), description=f"Пинг {device1.name} -> {device2.name}"):
        time.sleep(0.5)
    
    # Проверяем, что устройства подключены друг к другу
    # ИЛИ оба подключены к роутеру
    return (device1.connected_to == device2 or 
            (isinstance(device1.connected_to, Router) and 
             isinstance(device2.connected_to, Router)))

def configure_internet(gateway_ip, dns_ip):
    """Настройка интернет-подключения"""
    if gateway_ip == "192.168.1.254":
        game_state.is_internet_ready = True
        return True
    return False