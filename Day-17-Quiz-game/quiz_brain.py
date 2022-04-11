
class quiz_controller:
    def __init__(self, q_list):
        self.q_no = 0
        self.list = q_list
        self.score = 0

    def next_ques(self):
        curr_ques = self.list[self.q_no]
        self.q_no += 1
        user = input(f"Q. {self.q_no} : {curr_ques.txt} (True/False) :  ")
        self.check_answer(user, curr_ques.ans)

    def ques_left(self):
        if self.q_no < len(self.list):
            return True
        else:
            return False

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You are right!!")
            self.score += 1
        else:
            print("You are wrong")
            self.score += 0
        print(f"The right answer is {correct_ans}")
        print(f"The score is {self.score} / {self.q_no}")
        print("\n")
