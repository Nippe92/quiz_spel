from app.quiz_util import Choices
from config import Url

class PlayGame:

    def fetch_choices(self):

        choice = Choices()

        category = choice.get_categories()
        difficulty = choice.get_difficulties()
        question_amount = choice.get_question_amount()

        return category, difficulty, question_amount

    def fetch_url(self, amount, category, difficulty):
        url = Url.build_url(amount, category, difficulty)

        return url


