import os
from difflib import get_close_matches
from ui.menus import clear_screen
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from data.search_knowledge import SEARCH_KNOWLEDGE


def get_suggestions(user_input):
    """Находит 3 наиболее похожих термина"""
    all_terms = list(SEARCH_KNOWLEDGE.keys())
    # Добавляем связанные термины в поиск
    for term_data in SEARCH_KNOWLEDGE.values():
        all_terms.extend(term_data.get("related", []))
    return get_close_matches(user_input, all_terms, n=3, cutoff=0.4)

def show_search_help():
    """Показывает доступные термины по категориям"""
    clear_screen()
    categories = {
        "Основные": ["ip", "роутер", "подсеть", "шлюз"],
        "Протоколы": ["dns", "http", "https", "ftp"],
        "Инструменты": ["ping", "трассировка", "nslookup"],
        "Безопасность": ["пароль", "антивирус", "брандмауэр"]
    }
    
    print("\n[bold]Доступные термины:[/bold]")
    print("[dim]Для выбора введите точное название[/dim]\n")
    
    panels = []
    for category, terms in categories.items():
        panel = Panel.fit(
            "\n".join(f"• {term}" for term in terms),
            title=f"[cyan]{category}[/cyan]",
            border_style="blue",
            padding=(0, 2)
        )
        panels.append(panel)
    
    print(Columns(panels, equal=True, expand=True))

def show_search_result(term):
    """Выводит отформатированный результат"""
    clear_screen()
    if term not in SEARCH_KNOWLEDGE:
        print(
            Panel("Термин не найден", title="⚠️ Ошибка", border_style="red")
        )
        return
    
    data = SEARCH_KNOWLEDGE[term]
    content = Text.from_markup(
        f"[bold]{data['title']}[/bold]\n\n{data['content']}\n\n"
        f"[dim]Связанные термины: {', '.join(data.get('related', [])) or 'нет'}[/dim]"
    )
    print(Panel(content, title="📚 Результат", border_style="green", padding=(1, 3)))

def show_search():
    """Главная функция поиска"""
    clear_screen()
    while True:
        print("\n" + "="*50)
        print("[bold]🔍 Поиск по сетевым терминам[/bold]")
        print("[dim]Команды: 'помощь' - список, 'выход' - назад[/dim]")
        
        query = input("\nВведите термин: ").strip().lower()
        
        if query == "выход":
            clear_screen()
            break
            
        if query == "помощь":
            show_search_help()
            input("\nНажмите Enter чтобы продолжить...")
            clear_screen()
            continue
        
        if not query:
            continue
            
        # Поиск точного совпадения
        if query in SEARCH_KNOWLEDGE:
            show_search_result(query)
            input("\nНажмите Enter чтобы продолжить...")
            clear_screen()
            continue
            
        # Автодополнение
        suggestions = get_suggestions(query)
        if suggestions:
            clear_screen()
            print(f"\n[dim]Возможно вы имели в виду:[/dim]")
            for i, term in enumerate(suggestions, 1):
                print(f"[bold]{i}.[/bold] {term}")
            
            choice = input("\nВыберите номер (1-3) или Enter для нового поиска: ")
            if choice.isdigit() and 1 <= int(choice) <= 3:
                show_search_result(suggestions[int(choice)-1])
                input("\nНажмите Enter чтобы продолжить...")
            clear_screen()
        else:
            clear_screen()
            print(
                Panel(
                    "Термин не найден. Попробуйте:\n"
                    "- Проверить орфографию\n"
                    "- Ввести 'помощь' для списка терминов",
                    title="⚠️ Ошибка",
                    border_style="red"
                )
            )
            input("\nНажмите Enter чтобы продолжить...")
            clear_screen()