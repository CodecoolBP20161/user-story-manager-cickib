from flask import Flask, g, redirect, request, session, url_for, abort, render_template, flash
from models import *
from peewee import *


DEBUG = False
SECRET_KEY = 'tr3d3cimo1a'

app = Flask(__name__)
app.config.from_object(__name__)


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


@app.route('/story/', methods=['GET', 'POST'])
def add_user_story():
    if (request.method == "POST" and request.form["story_title"] and request.form["user_story"] and
            request.form["acceptance_criteria"] and request.form["business_value"] and request.form["estimation"] and
            request.form["status"]):
        UserStory.create(story_title=request.form["story_title"], user_story=request.form["user_story"],
                         acceptance_criteria=request.form["acceptance_criteria"],
                         business_value=request.form["business_value"], estimation=request.form["estimation"],
                         status=request.form["status"])
        return redirect('/list/')
    else:
        return render_template('add.html', options=UserStory.status_options)


@app.route('/story/<story_id>', methods=['POST', 'GET'])
def update_user_story(story_id):
    unselected_options = []
    edit_story = UserStory.select().where(UserStory.id == story_id).get()
    for option in UserStory.status_options:
        if edit_story.status == option:
            pass
        else:
            unselected_options.append(option)
    try:
        edit_story.story_title = request.form['story_title']
        edit_story.user_story = request.form['user_story']
        edit_story.acceptance_criteria = request.form['acceptance_criteria']
        edit_story.business_value = request.form['business_value']
        edit_story.estimation = request.form['estimation']
        edit_story.status = request.form['status']
        edit_story.save()
        return redirect('/list/')
    except:
        return render_template('update.html', edit_story=edit_story, options=unselected_options)


@app.route('/delete/', methods=['GET'])
def delete_user_story():
    UserStory.delete().where(UserStory.id == request.args.get("story_id")).execute()
    return redirect('/list/')

if __name__ == '__main__':
    app.run()
