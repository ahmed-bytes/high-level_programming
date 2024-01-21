# -*- coding=utf-8 -*-

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
options = []

for question in question_data:
    question_text = question["question"]
    answer_text = question["correct_answer"]
    question_type = question["type"]
    choices = list(question["incorrect_answers"])

    new_question = Question(question_text, answer_text, question_type, choices)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz :) !!")
print(f"Your score is {quiz.score}/{quiz.num}")
