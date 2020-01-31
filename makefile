all:

run:
	cd src/ ; export FLASK_APP=run.py ; export FLASK_ENV=development ; cd .. ; flask run