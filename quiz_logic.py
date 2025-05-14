class QuizBrain:

    def __init__(self, question_list):
        self.q_num = 0
        self.score = 0
        self.q_list = question_list

    def quiz_continues(self):
        return self.q_num < len(self.q_list)

    def check_answer(self):
        current_question = self.q_list[self.q_num]
        correct_ans = current_question.answer

        self.q_num += 1
        user_ans = input(f"Q{self.q_num}: {current_question.text}. (True/False): ")

        if correct_ans.lower() == user_ans.lower():
            self.score += 1
            print("Hurrah! You got it!")
        else:
            print("Opps. Wrong Answer")

        print(f"The correct answer is '{correct_ans}'")
        print(f"Your current score is: {self.score}/{self.q_num}")
        print("\n")

