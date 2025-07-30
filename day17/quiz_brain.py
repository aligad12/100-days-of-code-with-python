from question_model import question_bank

class Quiz:
    def __init__(self,questions):
        self.question_list = question_bank
        self.question_number = 0
         #i think this is going to be the question bank we created before
#this is a list of questions and there answers here

    def check_if_answer_is_correct(question,u_answer):
        if question.text == u_answer:
            print("Correct answer!")
            return True
        else:
            print("Wrong answer!")
            return False
        
    def check_end_of_quiz(question):
        if question == question_bank[-1]:
            return True 
        else:
            return False

    def take_answer(question):
        user_answer = input("T or F? ").lower().strip()
        return user_answer