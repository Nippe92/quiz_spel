from app.quiz_util import Choices
from config import Url


class PlayGame:

    choice = Choices()

    def fetch_choices(self):

        category = Choices.get_categories()
        difficulty = Choices.get_difficulties()
        question_amount = Choices.get_question_amount()

        return category, difficulty, question_amount

    def fetch_url(self, amount, category, difficulty):
        url = Url.build_url(amount, category, difficulty)

        return url

    def save_score(self, user_id, score):
        pass

class Scoreboard:
    
    def get_highscores(self, limit=15):
        pass