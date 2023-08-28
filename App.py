from Question import Question
from DATA import question_data
from Controller import Controller
from UI import UserInterface
all_question = []

#กำหนดโจทย์ปัญหา
for item in question_data :
    text=item["text"]
    answer=item["answer"]
    question=Question(text,answer)
    all_question.append(question)

#สร้างแผงควบคุม
controller=Controller(all_question)
userInterface=UserInterface(controller)




