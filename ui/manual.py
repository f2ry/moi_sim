from ui.menus import clear_screen 
from ui.schemas import show_schema
from data.manual import MANUAL

def show_manual():
    """Структурированная справка без эмодзи"""
    while True:
        clear_screen()
        print("\n" + "="*50)
        print("ОБРАЗОВАТЕЛЬНАЯ СПРАВКА")
        print("="*50)
        
        # Вывод категорий
        categories = list(MANUAL.keys())
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        print("\n0. Выход")
        
        # Выбор раздела
        try:
            choice = int(input("\nВыберите раздел: "))
            if choice == 0:
                break
            selected_category = categories[choice-1]
            show_category(selected_category)
        except (ValueError, IndexError):
            input("\nОшибка выбора. Нажмите Enter...")

def show_category(category):
    """Показывает содержимое раздела"""
    while True:
        clear_screen()
        print(f"\nРАЗДЕЛ: {category.upper()}")
        print("="*50)
        
        data = MANUAL[category]
        for section, content in data["sections"].items():
            print(f"\n{section}:")
            print("-" * len(section))
            for item in content:
                print(f"  • {item}")
        
        input("\nНажмите Enter чтобы вернуться...")
        break

def show_network_schemas():
    """Меню выбора схем"""
    while True:
        clear_screen()
        print("ДОСТУПНЫЕ СХЕМЫ:")
        print("1. Локальная сеть")
        print("2. Wi-Fi сеть")
        print("0. Назад")
        
        choice = input("Выберите схему: ")
        
        if choice == "0":
            break
        elif choice == "1":
            show_schema("local_network")
        elif choice == "2":
            show_schema("wifi_network")