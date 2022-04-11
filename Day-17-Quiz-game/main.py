from question_model import question
from data import question_data
from quiz_brain import quiz_controller

q_bank = []

for ques in question_data:
    q_text = ques['question']
    q_ans = ques["correct_answer"]
    new_question = question(q_text, q_ans)
    q_bank.append(new_question)

controller = quiz_controller(q_bank)

end_check = False

while controller.ques_left() or not end_check:
    controller.next_ques()
    desc = input("Do you wanna continue? Y/N   ").lower()
    if desc == "n":
        end_check = True

print("You have completed the quiz")
print(f"Your final Score is {controller.score} / {controller.q_no}")
