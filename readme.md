
# Project instruction
a quiz game where you can choose categories, diffuculty and number of questions. 
users are saved in a database using SQLAlchemy and each user will get scores depending on how many right quiestions they get.
There will also be highscores from all users that have played the game.

Make sure that you create an account to start using the site.
Database will be located in a folder called instance once you start the app for the first time.
Please read all the information below to get started!
Have fun!

## Get started:
1. create a virtual envireoment `python -m venv venv` in the main folder
2. enter the virtual enviroment `venv\Scripts\activate` (make sure you're in the right directory)
3. install the required packages in requirements.txt by typing the following in terminal: `pip install -r requirements.txt` 
4. create a config.py. See below for more information.
5. start the app by typing python run.py in the terminal (if there is any issues see "import issues" below what might cause it)
6. enter the IP adress that pops up in the terminal
7. now you can use the quiz app.

### Config.py:
Please check your email to see what to put in the config file.
You should have received an Config class containing API-key and database.
Copy this information and paste it in the config file that you create.
Make sure that you create the config.py file in the main folder called quiz_spel
otherwise there will be issues.

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

##### Choice of course elements:
Here are the following course elemts ive used in this project:
API-integration - 
I felt like i wanted to learn more about API because it is used alot for working developers.
I believe that most project being made in the work life atleast have some API-integration so i felt that its very good to be
learning and using it the right way.
The api i chose is located in the config.py file.

Webb-development - 
I chose Flask because i wanted to make a project that i felt could actually be used by others and to make it more realistic.

SQL-with-python - 
SQLAlchemy is the database i chose cause i think it was the most reasonable to chose for this project and its easy to navigate through.
