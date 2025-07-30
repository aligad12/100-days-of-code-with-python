from data import question_data

class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))
print(question_bank) #this is going to be a list of object we can
for question in question_bank:
    print(f"Q:{question.text}\n__A:{question.answer}") #like this we created a question bank
