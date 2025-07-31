@echo off
echo ========================================
echo Project Bondhu - Setup Script
echo ========================================

echo.
echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

echo.
echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setting up environment file...
if not exist .env (
    copy .env.example .env
    echo Created .env file from template
    echo Please edit .env file with your configuration
) else (
    echo .env file already exists
)

echo.
echo Setup completed successfully!
echo.
echo Next steps:
echo 1. Edit .env file with your database credentials
echo 2. Create PostgreSQL database 'predico2f'
echo 3. Run: python manage.py migrate
echo 4. Run: python manage.py createsuperuser
echo 5. Run: python manage.py runserver
echo.
pause
