

class Choices:
    def __init__(self):
        
        self.categories = {
            9: "General Knowledge",
            27: "Animals",
            23: "History",
            11: "Movies",
            17: "Science & Nature"
        }
        self.difficulties = ["easy", "medium", "hard"]

        self.question_amount = [5, 10, 15]

    def get_categories(self):
        
        return self.categories

    def get_difficulties(self):
        
        return self.difficulties
    
    def get_question_amount(self):

        return self.question_amount