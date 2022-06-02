PROJECT_DIR = caopanheiro
django_run:
	cd $(PROJECT_DIR) && poetry run python manage.py runserver

django_makemigrations:
	cd $(PROJECT_DIR) && poetry run python manage.py makemigrations

django_migrate:
	cd $(PROJECT_DIR) && poetry run python manage.py migrate

style:
	cd $(PROJECT_DIR) && flake8 .
	cd $(PROJECT_DIR) && isort .  
	cd $(PROJECT_DIR) && black . 