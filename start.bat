@echo off
REM ==============================================
REM Автозапуск симулятора сетей для Windows
REM ==============================================

REM Переключение на UTF-8 и настройка консоли
chcp 65001 > nul
set PYTHONIOENCODING=utf-8
set LC_ALL=ru_RU.UTF-8

REM Установка совместимого шрифта (если доступно)
reg add "HKCU\Console\%CD%start.bat" /v "FaceName" /t REG_SZ /d "Lucida Console" /f > nul 2>&1
reg add "HKCU\Console\%CD%start.bat" /v "CodePage" /t REG_DWORD /d 65001 /f > nul 2>&1

SET PY_SCRIPT=main.py
SET VENV_DIR=venv
SET REQUIREMENTS=requirements.txt

echo.
echo [1/3] Активация виртуального окружения...
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo Ошибка: Виртуальное окружение не найдено!
    echo Создайте его командой: python -m venv venv
    pause
    exit /b 1
)
call "%VENV_DIR%\Scripts\activate.bat"

echo.
echo [2/3] Проверка зависимостей...
"%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip
"%VENV_DIR%\Scripts\python.exe" -m pip install -r "%REQUIREMENTS%"
if errorlevel 1 (
    echo Ошибка при установке зависимостей!
    pause
    exit /b 1
)

echo.
echo [3/3] Запуск симулятора...
echo ==============================================
"%VENV_DIR%\Scripts\python.exe" "%PY_SCRIPT%"
echo ==============================================

pause