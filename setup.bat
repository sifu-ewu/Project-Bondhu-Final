@echo off
echo ========================================
echo Project Bondhu - Secure Setup Script
echo ========================================

echo.
echo SECURITY WARNING: This script will help you set up the project securely.
echo Make sure you NEVER commit .env files or credentials to Git!
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
echo Generating secure secret key...
python -c "from django.core.management.utils import get_random_secret_key; print('Generated Secret Key:'); print(get_random_secret_key())" > temp_key.txt
echo.
echo A secure secret key has been generated. Please copy it from temp_key.txt

echo.
echo Setting up environment file...
if not exist .env (
    copy .env.example .env
    echo Created .env file from template
    echo.
    echo IMPORTANT: Edit .env file with your secure configuration:
    echo 1. Replace SECRET_KEY with the generated key from temp_key.txt
    echo 2. Set strong database credentials
    echo 3. Configure your domain for ALLOWED_HOSTS
    echo 4. Set DEBUG=False for production
) else (
    echo .env file already exists
    echo Please verify it contains secure credentials
)

echo.
echo Security checklist:
echo [x] Virtual environment created
echo [x] Dependencies installed
echo [x] Secure secret key generated
echo [ ] .env file configured with secure values
echo [ ] PostgreSQL database created
echo [ ] Database migrations run
echo [ ] Superuser created
echo.
echo Next steps:
echo 1. Edit .env file with secure values (NEVER commit this file!)
echo 2. Create PostgreSQL database with strong credentials
echo 3. Run: python manage.py migrate
echo 4. Run: python manage.py createsuperuser
echo 5. Run: python manage.py collectstatic
echo 6. Run: python manage.py runserver
echo.
echo Remember: NEVER commit .env files or credentials to version control!
echo.

del temp_key.txt 2>nul
pause
