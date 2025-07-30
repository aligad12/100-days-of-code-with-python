class Quiz:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.quiz_logo = """
 _____       _        ___               ______          ___  _ _   _____           _ 
|  _  |     (_)      / _ \              | ___ \        / _ \| (_) |  __ \         | |
| | | |_   _ _ ____ / /_\ \_ __  _ __   | |_/ /_   _  / /_\ \ |_  | |  \/ __ _  __| |
| | | | | | | |_  / |  _  | '_ \| '_ \  | ___ \ | | | |  _  | | | | | __ / _` |/ _` |
\ \/' / |_| | |/ /  | | | | |_) | |_) | | |_/ / |_| | | | | | | | | |_\ \ (_| | (_| |
 \_/\_\\__,_|_/___| \_| |_/ .__/| .__/  \____/ \__, | \_| |_/_|_|  \____/\__,_|\__,_|
                          | |   | |             __/ |                                
                          |_|   |_|            |___/                                 
"""


    
    def next_question(self):
        valid_answer = ['True','False','T','F']
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        while True:
            answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").capitalize().strip()
            if answer == 'T':
                answer = "True"
            elif answer == 'F':
                answer = "False"
            if answer in valid_answer:
                break
            else:
                print("That was not a valid answer!")
        return answer,current_question
    

    def check_answer(self,answer,question):
        if answer == question.answer:
            self.score+=1
            return True
        else:
            return False

    def check_end_quiz(self):
      if self.question_number == len(self.question_list):
          return True
      else:
          return False
      
    def print_final_score(self):
        q_num = len(self.question_list)
        if self.check_end_quiz():
            print(f"The quiz has ended and you scored: {self.score}/{q_num}")

    def print_current_score(self):
        q_num = len(self.question_list)
        print(f"your current score is: {self.score}/{q_num}")
    
    def new_quiz(self):
        while True:
            user_input = input("Do you want to retake the quiz?(y/n)").lower().strip()
            if user_input =='y':
                return True
            elif user_input =='n':
                return False
            else:
                print("That was an invalid input!!")