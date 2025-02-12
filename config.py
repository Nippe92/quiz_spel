import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///quizgame.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Url:
    def build_url(self, question_amount, category, difficulty):
    
        url = f"https://opentdb.com/api.php?amount={question_amount}&category={category}&difficulty={difficulty}&type=multiple"
        
        return url