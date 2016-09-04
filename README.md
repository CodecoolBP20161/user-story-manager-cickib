### user-story-manager-cickib

# User Story Manager

## Description
Please run the ```app.py``` file. It creates the table for UserStory model at the root database which by default should be your ```username``` (equals to the ```whoami``` cli command).


### UserStory model

#### Columns

* ```story_title```
  * field type: ```CharField```
  * description: title of the user story
* ```user_story```
  * field type: ```TextField```
  * description: purpose of the user story
* ```acceptance_criteria```
  * field type: ```TextField```
  * description: details of the user story
* ```business_value```
  * field type: ```IntegerField```
  * description: business value of the user story
* ```estimation```
  * field type: ```FloatField```
  * description: estimated time to complete the user story
* ```status```
  * field type: ```CharField```
  * description: current status of development


### Logics to perform

* list all user stories
* create new user story
* update an existing story
* delete a story
