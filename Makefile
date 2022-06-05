PROJECT_DIR = caopanheiro
django_run:
	cd $(PROJECT_DIR) && poetry run python manage.py runserver

django_makemigrations:
	cd $(PROJECT_DIR) && poetry run python manage.py makemigrations

django_migrate:
	cd $(PROJECT_DIR) && poetry run python manage.py migrate

django_test:
	cd $(PROJECT_DIR) && python manage.py test

style:
	cd $(PROJECT_DIR) && flake8 .
	cd $(PROJECT_DIR) && isort .  
	cd $(PROJECT_DIR) && black . 

docker_run:
	docker-compose up

docker_build:
	docker-compose up --build

coverage_run:
	cd $(PROJECT_DIR) && coverage run manage.py test

coverage_report:
	cd $(PROJECT_DIR) && coverage report

coverage_html:
	cd $(PROJECT_DIR) && coverage html