SCHEMAS = {
    "local_network": {
        "title": "Локальная сеть",
        "schema": r"""
           [ПК1] (192.168.1.1)
             │
           [Роутер] (192.168.1.254)
             │
           [ПК2] (192.168.1.2)
        """,
        "description": "Базовая топология из проекта",
        "parts": {
            "[ПК1]": "Компьютер с Windows 10",
            "[Роутер]": "Маршрутизатор TP-Link",
            "│": "Кабель CAT6"
        }
    },
    "wifi_network": {
        "title": "Wi-Fi сеть",
        "schema": r"""
           [Смартфон]━┓
                      ┣[Роутер]━[Интернет]
           [Ноутбук] ━┛
        """,
        "description": "Типовая домашняя сеть"
    }
}