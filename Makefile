PYVENV_PREFIX=pipenv run
LOG_MODE=INFO
db?=odoo
md?=sanlong_prod_info
# Logging reference
# https://www.odoo.com/documentation/14.0/reference/cmdline.html
# https://odoo-development.readthedocs.io/en/latest/admin/log-handler.html#usefull-logs

format:
	$(PYVENV_PREFIX) black custom
	$(PYVENV_PREFIX) isort custom

lint:
	$(PYVENV_PREFIX) flake8 custom

run:
	$(PYVENV_PREFIX) python3 odoo-server/odoo-bin -c /etc/odoo-server.conf

migrate:
	$(PYVENV_PREFIX) python3 odoo-server/odoo-bin -u $(md) -d $(db) --dev=all

start_service:
	sudo service postgresql start
	sudo service mysql start
	sudo service apache2 start

stop_service:
	sudo service postgresql stop
	sudo service mysql stop
	sudo service apache2 stop

restart_service:
	sudo service postgresql restart
	sudo service mysql restart
	sudo service apache2 restart