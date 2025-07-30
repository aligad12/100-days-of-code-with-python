from question_model import Question
from data import question_data
from quiz_brain import Quiz
import os
import random

"""question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))
print(question_bank) #this is going to be a list of object we can
for question in question_bank:
    print(f"Q:{question.text}\n__A:{question.answer}") #like this we created a question bank
"""

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

random.shuffle(question_bank)
quiz = Quiz(question_bank)
inside_quiz = True
print(quiz.quiz_logo)
print(f"{'*'*50}Welcome to the Quiz App!!{'*'*50}")
while inside_quiz:
    while not quiz.check_end_quiz():
        answer,question = quiz.next_question()
        quiz.check_answer(answer,question)
        quiz.print_current_score()
        print("\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(quiz.quiz_logo)
    quiz.print_final_score()
    if quiz.new_quiz():
        print("Welcome to a new quiz!!")
        random.shuffle(question_bank)
        quiz = Quiz(question_bank)
    
    else:
        print("exiting the quiz app...")
        inside_quiz = False


