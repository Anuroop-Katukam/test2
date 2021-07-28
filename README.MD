-------------------------------------------------------------
-> Please use python3.6 or above

1) Create a virtual environment
	virtualenv -p python .env

2) Activate virtual env.
	source .env/bin/activate

3) Install required dependancies
	pip install -r requirements.txt

4) If you create a new database then run this command other you can ignore it
	python manage.py makemigrations
	python manage.py migrate

///////////////////////////////////////////////////////////////////////////////////////
* Note:- Please activate your environment of all below commands and run in different terminal
///////////////////////////////////////////////////////////////////////////////////////

5) Run python server
	python manage.py runserver

6) Run celery server for background process
	celery --app=simpleproject worker --loglevel=INFO
					(or)
	celery --app=simpleproject worker --loglevel=INFO --concurrency=10 ( you can change it to  run any number to run a job parallel)



7) Add the postman collect in postman app  import for this link--> https://www.getpostman.com/collections/617893cbf532ed7aa779

8) Attach the only csv file in our field_name --> simpleproject/freeformResponses.csv
hit the post request



