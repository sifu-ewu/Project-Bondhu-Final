# Project Bondhu - Makefile

.PHONY: help install migrate runserver test clean

help:
	@echo "Available commands:"
	@echo "  install    - Install dependencies"
	@echo "  migrate    - Run database migrations"
	@echo "  runserver  - Start development server"
	@echo "  test       - Run tests"
	@echo "  clean      - Clean cache and temporary files"
	@echo "  setup      - Complete project setup"

install:
	pip install -r requirements.txt

migrate:
	python manage.py makemigrations
	python manage.py migrate

runserver:
	python manage.py runserver

test:
	python manage.py test

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

setup: install migrate
	python manage.py collectstatic --noinput
	@echo "Setup completed! Create superuser with: python manage.py createsuperuser"

superuser:
	python manage.py createsuperuser

collectstatic:
	python manage.py collectstatic --noinput

shell:
	python manage.py shell

dbshell:
	python manage.py dbshell
