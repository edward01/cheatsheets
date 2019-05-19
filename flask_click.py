#--------------------
# Using Click (command line interface)
# http://flask.pocoo.org/docs/1.0/cli/#custom-commands
# https://click.palletsprojects.com/en/7.x/quickstart/#basic-concepts-creating-a-command
#--------------------

# project/wsgi.py
from webapp import create_app, db, cli
...
app = create_app()
cli.register(app)

# project/webapp/cli.py
#---> to list commands generated, type "$ flask"
import click
from flask.cli import AppGroup

def register(app):
    # -- $ flask deploy
    @app.cli.command()
    def deploy():
        print('--> deploy')

    # -- $ flask create_user edward
    @app.cli.command('create_user')
    @click.argument('name')
    def create_user(name):
        print(f'--> create_user {name}')

    # -- $ flask create_employees -c 10
    @app.cli.command('create_employess')
    @click.option('-c', '--count', 'count', default=10)
    def employees(count):
        pass

    # --- Using group (will use this as: "$ flask user initdb")
    @app.cli.group()
    def user():
        pass

    @user.command()
    def initdb():
        print('Initialized the database')

    @user.command()
    def dropdb():
        print('Dropped the database')
#------------------------------------------------------------------------------------------------

#--------------------
#
#--------------------
#------------------------------------------------------------------------------------------------
