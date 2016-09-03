from flask import Flask, g, redirect, request, session, url_for, abort, render_template, flash
from models import *
from peewee import *


DEBUG = True  # set it to False when done!!
SECRET_KEY = 'tr3d3cimo1a'

app = Flask(__name__)
app.config.from_object(__name__)

DATABASE = 'sprint_reporter'
database = PostgresqlDatabase(DATABASE)


@app.before_request
def before_request():
    g.database = database
    g.database.connect()
    if UserStory.table_exists():
        pass
    else:
        g.database.create_tables([UserStory], safe=True)


@app.after_request
def after_request(response):
    g.database.close()
    return response


@app.route('/')
def homepage():
    return list_all_user_stories()


@app.route('/list/')
def list_all_user_stories():
    stories = UserStory.select()
    return render_template('list.html', stories=stories)



if __name__ == '__main__':
    app.run()
