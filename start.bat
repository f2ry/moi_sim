@echo off
:: Упрощённый и надёжный вариант
chcp 65001 > nul
setlocal enabledelayedexpansion

echo.
echo [1/3] Инициализация...
python --version > nul 2>&1 && (
    echo   УСПЕХ: Python установлен
) || (
    echo   ОШИБКА: Python не найден!
    pause
    exit /b 1
)

echo.
echo [2/3] Активация окружения...
if not exist "venv\Scripts\activate.bat" (
    echo   Создаём виртуальное окружение...
    python -m venv venv || (
        echo   ОШИБКА: Не удалось создать VENV
        pause
        exit /b 1
    )
)
call "venv\Scripts\activate.bat"

echo.
echo [3/3] Запуск программы...
venv\Scripts\python.exe main.py

pause