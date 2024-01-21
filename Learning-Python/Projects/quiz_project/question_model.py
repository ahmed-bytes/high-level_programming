from random import shuffle


class Question:
    def __init__(self, user_text, user_answer, question_type, options):
        self.text = user_text
        self.answer = user_answer
        self.q_type = question_type
        self.choices = list(options)
        self.choices.append(user_answer)
        shuffle(self.choices)
