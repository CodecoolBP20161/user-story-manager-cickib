from peewee import *
import os
import pwd


DATABASE = 'sprint_reporter'
# database = PostgresqlDatabase(DATABASE)
user = pwd.getpwuid(os.getuid()).pw_name
database = PostgresqlDatabase(user)


class Basemodel(Model):
    class Meta:
        database = database


class UserStory(Basemodel):
    story_title = CharField()
    user_story = TextField()
    acceptance_criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()
