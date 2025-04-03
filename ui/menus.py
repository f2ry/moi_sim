import os
from rich import print
from core.utils import clear_screen
from rich.panel import Panel
from core.state import game_state
from core.network import create_network, test_connection
from ui.views import show_topology, show_message
from ui.manual import show_manual
from ui.schemas import show_network_schemas
from data.manual import MANUAL
from ui.styles import ICONS


def network_menu():
    clear_screen()
    print(Panel.fit("Настройка локальной сети", style="bold blue"))
    
    devices = create_network()
    pc1, pc2, router = devices['pc1'], devices['pc2'], devices['router']
    
    # Подключение устройств
    if input("1. Подключить ПК1 к роутеру? (да/нет): ").lower() == 'да':
        pc1.connected_to = router
        show_message(f"ПК1 подключён к роутеру", "success")
    
    if input("2. Подключить ПК2 к роутеру? (да/нет): ").lower() == 'да':
        pc2.connected_to = router
        show_message(f"ПК2 подключён к роутеру", "success")
    
    # Проверка связи
    if pc1.connected_to and pc2.connected_to:
        if pc1.can_ping(pc2) and test_connection(pc1, pc2):
            game_state.is_network_ready = True
            show_message("Сеть настроена успешно! ПК могут общаться", "success")
        else:
            show_message("Ошибка: Проверьте IP-адреса и подключения", "error")
    
    show_topology(pc1, pc2, router)
    input("\nНажмите Enter чтобы продолжить...")

def internet_menu():
    clear_screen()
    print(Panel.fit("Настройка интернета", style="bold green"))
    
    if not game_state.is_network_ready:
        show_message("Сначала настройте локальную сеть!", "error")
        input("\nНажмите Enter чтобы продолжить...")

        return
    
    print("1. Настроить шлюз (192.168.1.254)")
    print("2. Указать DNS (8.8.8.8)")
    
    choice = input("Выберите действие: ")
    if choice == "1":
        if input("Введите IP шлюза: ") == "192.168.1.254":
            game_state.is_internet_ready = True
            show_message("Шлюз настроен!", "success")
    
    input("\nНажмите Enter чтобы продолжить...")


def main_menu():
    while True:
        clear_screen()
        print(Panel.fit("Главное меню", style="bold red"))
        
        status = {
            "network": ICONS["success"] if game_state.is_network_ready else ICONS["error"],
            "internet": ICONS["success"] if game_state.is_internet_ready else ICONS["error"]
        }
        
        print(f"1. Настройка сети {status['network']}")
        print(f"2. Выход в интернет {status['internet']}")
        print("3. Справка")
        print("4. Схемы сетей")
        if game_state.is_internet_ready:
            print("5. Поиск в интернете")
        print("0. Выход")
        
        choice = input("ВВОД > ")
        if choice == "1":
            network_menu()
        elif choice == "2":
            internet_menu()
        elif choice == "3":
            show_manual()
        elif choice == "4":
            show_network_schemas()
        elif choice == "5" and game_state.is_internet_ready:
            from ui.search import show_search
            show_search()
        elif choice == "0":
            break