
# Project instruction
a quiz game where you can choose categories, diffuculty and number of questions. 
users are saved in a database using SQLAlchemy and each user will get scores depending on how many right answers they get.
There will also be highscores from all users that have played the game.

Make sure that you create an account to start using the site.
Database will be located in a folder called instance once you start the app for the first time.
Please read all the information below to get started!
Have fun!

## Get started:
1. create a virtual envireoment `python -m venv venv` in the main folder
2. enter the virtual enviroment `venv\Scripts\activate` (make sure you're in the right directory)
3. install the required packages in requirements.txt by typing the following in terminal: `pip install -r requirements.txt` 
4. Doublecheck the config.py file that it has both the API and database.
5. start the app by typing python run.py in the terminal (if there is any issues see "import issues" below what might cause it)
6. enter the IP adress that pops up in the terminal
7. If you use the app for the first time make sure to create an account.
8. now you can use the quiz app by logging in or creating an account

### Config.py:
In this file you will locate the API and also the config class.

#### Import issues:
Please make sure that the config.py file i located in the main map (Quiz_spel)
if issue persists please check that the imports in the the following files are only config and not quiz_spel.config
The import issue might be in the following files:
__init__.py
play_game.py
routes.py
So to clarify in above files the config import should look like this:
from config import Url
unless in file __init__.py cause then import is:
from config import Config

#### Choice of course elements:
Here are the following course elements ive used in this project:

API-integration - 
Ive used the open trivia database as my API and uses it to create questions based on the users choices.
the API is located in the config.py file. No need for an api key since its an open API.
Im using requests and JSON to use the API.

Webb-development - 
I have used flask to create my quiz site. I create the site by using routes views and html templates.

SQL-with-python - 
Ive used SQLAlchemy as my database where i store users and scores. Ive also made an relationship with the tables.

File management/encryption/decryption - 
using bcrypt to hash passwords.

pytest - 
tested 2 functions from the quiz_util file. 
* One test was from the function question_amount where i wanted to see that the number of questions to choose from was correct.
* second test was to check that there actually was a total of 5 categories. Test from test_get_categories.