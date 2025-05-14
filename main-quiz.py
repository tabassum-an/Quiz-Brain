from quiz_data import quiz_question_data
from question_model import Question
from quiz_logic import QuizBrain


# TODO 1: create an object from class Question that contains the keys and values of the data
question_bank = []

# TODO 2: loop to iterate over the quiz_question_data.
for elements in quiz_question_data:
    quiz_question = elements["question"]
    quiz_answer = elements["correct_answer"]
    add_question = Question(quiz_question, quiz_answer)
    question_bank.append(add_question)


# TODO 3: create functions for user input
quiz = QuizBrain(question_bank)

while quiz.quiz_continues():
    quiz.check_answer()

print("You've completed the game.")
print(f"Final score: {quiz.score}/{quiz.q_num}")
