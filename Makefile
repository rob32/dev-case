.DEFAULT_GOAL := help
.PHONY: help deps format migrations migrate superuser docker-createsuperuser

deps:  ## Install dependencies
	pip install --upgrade pip
	pip install -r requirements-dev.txt

pre-commit:  ## Run pre-commit on all files
	pre-commit run -a -v

makemigrations:  ## Run manage.py makemigrations
	python3 manage.py makemigrations

migrate:  ## Run manage.py migrate
	python3 manage.py migrate

superuser:  ## Run manage.py createsuperuser
	python3 manage.py createsuperuser

docker-createsuperuser: ## Run createsuperuser inside docker-container
	docker-compose exec web python manage.py createsuperuser

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "----" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
