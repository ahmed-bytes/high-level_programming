class QuizBrain:
    def __init__(self, question_list):
        self.num = 0
        self.quiz_list = question_list
        self.score = 0

    def next_question(self):
        question = self.quiz_list[self.num]
        self.num += 1
        if question.q_type == "boolean":
            user_answer = input(f"Q{self.num}: {question.text} (True/False)?: ")
        else:
            print(f"Q{self.num}: {question.text}")
            print("\n")
            for options in question.choices:
                print(f"{options}", end=",  ")
            print("\n")
            user_answer = input("Type your answer: ")
            print("\n")
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        if self.num < len(self.quiz_list):
            return True
        return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!!")
            self.score += 1
        else:
            print("Wrong answer!!")
            print(f"The correct answer is {correct_answer}")
        print(f"Your Score is {self.score}/{self.num}")
        print("\n")
