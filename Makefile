include ./env/.env
export $(shell sed -E '/^\s*#/d;/^\s*$$/d;s/=.*//' ./env/.env)

msg?=new migration
START_DOCK=docker-compose
MIG=migrations
DB=postgres
ENV_FILE=--env-file ./env/.env
APP=api
AIR=airflow-webserver
POSTGRES=postgres

up:
	$(START_DOCK) $(ENV_FILE) up
upb:
	$(START_DOCK) $(ENV_FILE) up --build
upd:
	$(START_DOCK) $(ENV_FILE) down
api_shell:
	$(START_DOCK) exec $(APP) sh 
psql:
	docker-compose exec $(DB) sh -c "psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)"
gen_migration:
	$(START_DOCK) $(ENV_FILE) run $(MIG) sh -c "alembic revision --autogenerate -m '$(msg)'"
	$(START_DOCK) stop $(MIG)
