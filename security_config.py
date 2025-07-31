"""
Security configuration utilities for Project Bondhu
"""
import os
import secrets
from django.core.management.utils import get_random_secret_key


def generate_secret_key():
    """Generate a new Django secret key"""
    return get_random_secret_key()


def validate_environment():
    """Validate that all required environment variables are set"""
    required_vars = [
        'SECRET_KEY',
        'DB_NAME',
        'DB_USER', 
        'DB_PASSWORD'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            f"Please set these in your .env file or environment."
        )


def check_debug_in_production():
    """Ensure DEBUG is not enabled in production"""
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    allowed_hosts = os.environ.get('ALLOWED_HOSTS', '')
    
    if debug and ('localhost' not in allowed_hosts):
        raise ValueError(
            "DEBUG should not be enabled in production. "
            "Set DEBUG=False in your environment variables."
        )


def validate_database_credentials():
    """Validate database credentials are not using defaults"""
    db_password = os.environ.get('DB_PASSWORD', '')
    weak_passwords = [
        'password',
        'admin',
        'postgres',
        '123456',
        'ashraful123',  # Remove the exposed password
        'password123'
    ]
    
    if db_password.lower() in weak_passwords:
        raise ValueError(
            "Database password is too weak or uses a default value. "
            "Please use a strong, unique password."
        )


def security_check():
    """Run all security validations"""
    try:
        validate_environment()
        check_debug_in_production()
        validate_database_credentials()
        print("✅ Security validation passed")
        return True
    except ValueError as e:
        print(f"❌ Security validation failed: {e}")
        return False


if __name__ == "__main__":
    # Generate a new secret key
    print("Generated Secret Key:")
    print(generate_secret_key())
    print("\nCopy this to your .env file as SECRET_KEY=<generated_key>")
    
    # Run security check
    print("\nRunning security check...")
    security_check()
