from app.quiz_util import Choices

choices_instance = Choices()

def test_get_question_amount():
    
    result = choices_instance.get_question_amount()
    assert result == [5, 10, 15]


def test_get_categories():

    cat_amount = choices_instance.get_categories()

    assert len(cat_amount) == 5



