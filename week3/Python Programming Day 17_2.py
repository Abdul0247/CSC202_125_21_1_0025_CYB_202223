<<<<<<< HEAD
from Python Programming Day 17 import Question
=======
from Day17 import Question
>>>>>>> f72f87dfff416513df1e7f77f73d4936e8d96d82
from Data import question_data
from Quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")