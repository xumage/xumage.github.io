migrate:
	cd xumage && python3 manage.py migrate

load_env:
	source ./env/bin/activate

start_in_docker:
	docker-compose up