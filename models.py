from peewee import *


DATABASE = 'sprint_reporter'
database = PostgresqlDatabase(DATABASE)


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
