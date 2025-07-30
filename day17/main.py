from question_model import Question
from data import question_data

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))
print(question_bank) #this is going to be a list of object we can
for question in question_bank:
    print(f"Q:{question.text}\n__A:{question.answer}") #like this we created a question bank

q2_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    q2_bank.append(new_question)
    