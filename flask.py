$ pip install python-dotenv

# .flaskenv: Environment variables for flask command
# FLASK_APP=wsgi.py

#-- to run:
$ export FLASK_ENV=development
$ export FLASK_APP=wsgi.py
$ flask run
# -- or --
(venv) $ FLASK_APP=run.py FLASK_DEBUG=1 flask run

#-- to enable debug
$ export FLASK_DEBUG=1
#------------------------------------------------------------------------------------------------

#--------------------
# DATABASE
#--------------------
$ pip install flask-sqlalchemy
$ pip install flask-migrate
#----------------------------

# config.py: Flask-SQLAlchemy configuration
# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

# class Config(object):
#     # ...
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'app.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#----------------------------

# https://ondras.zarovi.cz/sql/demo/  -  db designer tool

$ flask db init
$ flask db migrate -m "users table"
$ flask db upgrade
#------------------------------------------------------------------------------------------------

#--------------------
# LOGGING
#--------------------
# Logging to file (order of severity: DEBUG, INFO, WARNING, ERROR and CRITICAL)
# ...
from logging.handlers import RotatingFileHandler
import os

# ...
if not app.debug:
    # ...
	if not os.path.exists('logs'):
	    os.mkdir('logs')
	file_handler = RotatingFileHandler('logs/myapp.log', maxBytes=10240, backupCount=10)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.setLevel(logging.INFO)
	app.logger.info('MyApp startup')
#------------------------------------------------------------------------------------------------

#--------------------
# EMAIL SUPPORT  (https://pythonhosted.org/Flask-Mail/)
#--------------------
$ pip install flask-mail  	# Flask-Mail
$ pip install pyjwt 		# JSON Web Tokens

# env variables
$ export MAIL_SERVER=smtp.googlemail.com
$ export MAIL_PORT=587
$ export MAIL_USE_TLS=1
$ export MAIL_USERNAME=<your-gmail-username>
$ export MAIL_PASSWORD=<your-gmail-password>

# snippet (should run inside flask shell)
from flask_mail import Message
from app import mail
msg = Message('test subject', sender=app.config['ADMINS'][0], recipients=['your-email@example.com'])
msg.body = 'text body'
msg.html = '<h1>HTML body</h1>'
mail.send(msg)
#------------------------------------------------------------------------------------------------

#--------------------
# JSON Web Token (jwt)  (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)
#--------------------
>>> import jwt
>>> token = jwt.encode({'a': 'b'}, 'my-secret', algorithm='HS256') #.decode('utf-8')
>>> token
b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhIjoiYiJ9.dvOo58OBDHiuSHD4uW88nfJikhYAXc_sfUHq1mDi4G0'
>>> jwt.decode(token, 'my-secret', algorithms=['HS256'])
{'a': 'b'}

# decoder tool: https://jwt.io/#debugger-io
#------------------------------------------------------------------------------------------------

#--------------------
# ASYNC TASK (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)
#--------------------
from threading import Thread
# ...

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()
#------------------------------------------------------------------------------------------------

#--------------------
# APP FACTORY (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)
#--------------------
current_app._get_current_object() # extracts the actual application instance from inside the proxy object, so that is what I passed to the thread as an argument.
#------------------------------------------------------------------------------------------------

#--------------------
# ENVIRONMENT VARIABLE (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)
#--------------------
#- environment variables is to store these in a ".env" file in the root application directory
#- It is important that you do not add your .env file to source control.
$ pip install python-dotenv	# python-dotenv

# sample config.py file content
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # ...

# sample .env file content
SECRET_KEY=52cb883e323b48d78a0a36e8e951ba4a
MAIL_SERVER=localhost
MAIL_PORT=25
DATABASE_URL=mysql+pymysql://microblog:<db-password>@localhost:3306/microblog

# configure secret_key
python -c 'import os; print(os.urandom(16))'		# b'_5#y2L"F4Q8z\n\xec]/'
# -- or --
python -c "import uuid; print(uuid.uuid4().hex)"	# 52cb883e323b48d78a0a36e8e951ba4a
#------------------------------------------------------------------------------------------------

#--------------------
# ELASTICSEARCH (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search)
#--------------------
#------------------------------------------------------------------------------------------------

#--------------------
# SETUP MYSQL (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux)
#--------------------
$ mysql -u root -p
mysql> create database microblog character set utf8 collate utf8_bin;
mysql> create user 'microblog'@'localhost' identified by '<db-password>';
mysql> grant all privileges on microblog.* to 'microblog'@'localhost';
mysql> flush privileges;
mysql> quit;
#------------------------------------------------------------------------------------------------

#--------------------
# LINUX DEPLOYMENT (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux)
#--------------------
# gunicorn
(venv) $ gunicorn -b localhost:8000 -w 4 microblog:app

# supervisor
$ sudo supervisorctl reload

# nginx
$ sudo service nginx reload

# SSL certificate  (https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https)
$ mkdir certs
$ openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
  -keyout certs/key.pem -out certs/cert.pem
#------------------------------------------------------------------------------------------------

#--------------------
# HEROKU DEPLOYMENT (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku)
#--------------------
$ heroku login
$ heroku apps:create flask-microblog

$ git remote -v

$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku config:set LOG_TO_STDOUT=1

# procfile content
web: flask db upgrade; flask translate compile; gunicorn microblog:app

$ heroku config:set FLASK_APP=microblog.py
$ git push heroku master

# if has code changes
$ git push heroku master
#------------------------------------------------------------------------------------------------

#--------------------
# USING CELERY (https://blog.miguelgrinberg.com/post/using-celery-with-flask)
#--------------------
#------------------------------------------------------------------------------------------------

#--------------------
# REST API (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis)
#--------------------
# HTTP Method	Action									Examples
GET				Obtain information about a resource		http://example.com/api/orders 		#(retrieve order list)
GET				Obtain information about a resource		http://example.com/api/orders/123   #(retrieve order #123)
POST			Create a new resource					http://example.com/api/orders 		#(create a new order, from data provided with the request)
PUT				Update a resource						http://example.com/api/orders/123   #(update order #123, from data provided with the request)
DELETE			Delete a resource						http://example.com/api/orders/123 	#(delete order #123)

# https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
# https://flask-restful.readthedocs.io/en/latest/quickstart.html
# https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
# https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb

# api token
(venv) $ pip install flask-httpauth
#------------------------------------------------------------------------------------------------

#--------------------
#
#--------------------
#------------------------------------------------------------------------------------------------
