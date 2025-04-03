from rich import print
from rich.panel import Panel
from data.schemas import SCHEMAS
from ui.menus import clear_screen  # Используем существующую функцию

def show_components(schema_name):
    """Детализация компонентов схемы"""
    schema = SCHEMAS[schema_name]
    clear_screen()
    
    print(f"Компоненты схемы '{schema['title']}':")
    for component, desc in schema.get("parts", {}).items():
        print(f"\n{component}: {desc}")
    
    input("\nНажмите Enter чтобы вернуться...")

def show_config_example(schema_name):
    """Примеры конфигурации для схемы"""
    config_examples = {
        "local_network": [
            "1. Настройка IP на ПК1:",
            "   > netsh interface ip set address name='Ethernet' static 192.168.1.1 255.255.255.0 192.168.1.254",
            "2. Проверка связи:",
            "   > ping 192.168.1.254"
        ],
        "wifi_network": [
            "1. Подключение к Wi-Fi:",
            "   > netsh wlan connect name='HomeWiFi'",
            "2. Проверка сигнала:",
            "   > netsh wlan show interfaces"
        ]
    }
    
    clear_screen()
    print(f"Примеры настройки для '{SCHEMAS[schema_name]['title']}':\n")
    for line in config_examples.get(schema_name, ["Примеры отсутствуют"]):
        print(line)
    
    input("\nНажмите Enter чтобы вернуться...")

def show_schema(schema_name):
    """Основная функция отображения схемы"""
    schema = SCHEMAS[schema_name]
    
    while True:
        clear_screen()
        print(Panel.fit(
            schema["schema"],
            title=schema["title"],
            subtitle=schema["description"],
            border_style="blue"
        ))
        
        print("\n1. Исследовать компоненты")
        print("2. Пример настройки")
        print("0. Назад")
        
        choice = input("\nВыберите действие: ")
        
        if choice == "0":
            break
        elif choice == "1":
            show_components(schema_name)
        elif choice == "2":
            show_config_example(schema_name)

def show_network_schemas():
    """Меню выбора доступных схем"""
    while True:
        clear_screen()
        print("ДОСТУПНЫЕ СХЕМЫ:")
        for i, key in enumerate(SCHEMAS.keys(), 1):
            print(f"{i}. {SCHEMAS[key]['title']}")
        print("0. Назад")
        
        choice = input("\nВыберите схему: ")
        
        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(SCHEMAS):
            show_schema(list(SCHEMAS.keys())[int(choice)-1])
