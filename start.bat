@echo off
REM ==================================================
REM  Автозапуск симулятора сетей с проверками
REM ==================================================

:: Конфигурация
set PY_SCRIPT=main.py
set VENV_DIR=venv
set REQUIREMENTS=requirements.txt
set DEFAULT_PY=python
chcp 65001 > nul
set PYTHONIOENCODING=utf-8
set LC_ALL=ru_RU.UTF-8

REM Установка совместимого шрифта (если доступно)
reg add "HKCU\Console\%CD%start.bat" /v "FaceName" /t REG_SZ /d "Lucida Console" /f > nul 2>&1
reg add "HKCU\Console\%CD%start.bat" /v "CodePage" /t REG_DWORD /d 65001 /f > nul 2>&1


:: Проверка Python
echo.
echo [1/4] Проверка установки Python...
for /f "tokens=2 delims==" %%v in ('%DEFAULT_PY% --version 2^>^&1') do (
    if "%%v" LSS "3.7" (
        echo Ошибка: Требуется Python 3.7+
        pause
        exit /b 1
    )
)

:: Активация VENV
echo.
echo [2/4] Активация виртуального окружения...
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo Создание VENV...
    %DEFAULT_PY% -m venv %VENV_DIR%
    if errorlevel 1 (
        echo Ошибка при создании VENV!
        pause
        exit /b 1
    )
)
call "%VENV_DIR%\Scripts\activate.bat"

:: Установка зависимостей
echo.
echo [3/4] Установка зависимостей...
"%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip
"%VENV_DIR%\Scripts\python.exe" -m pip install -r "%REQUIREMENTS%"
if errorlevel 1 (
    echo Ошибка установки зависимостей!
    pause
    exit /b 1
)

:: Запуск
echo.
echo [4/4] Запуск симулятора...
echo ==================================================
"%VENV_DIR%\Scripts\python.exe" "%PY_SCRIPT%"
echo ==================================================

pause