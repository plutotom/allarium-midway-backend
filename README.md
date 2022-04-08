# midway-backend: Steps to run it locally 

## to enable virtual env 
source venv/bin/active 

## install the requirements
pip install -r requirements.txt

### verify that the python version is expected - must be 3.10.2 or higher
python --version 

## For creating the initial data: some users and tenants
python manage.py shell < devexperiments/load_data.py 


## to start the server
python manage.py runrver 


## Important links in the application:
admin section
http://localhost:8000/admin/

api
http://localhost:8000/api/docs/


