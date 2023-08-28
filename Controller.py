class Controller :
    def __init__(self,data) :
        self.question_list = data
        self.question_number = 0
        self.score = 0
        self.current = None
    
    #ไปยังข้อถัดไป
    def nextQuestion(self):
        self.current = self.question_list[self.question_number]
        self.question_number += 1 
        #print(self.question_number,":",current.text," = (True/Flase)")
        #user_answer=input("ป้อนคำตอบ")
        #self.checkAnswer(user_answer,current.answer)
        return f"{self.question_number}){self.current.text}"
    
    #เช็คว่าใช้ nextquestion เกินกว่าข้อที่มีไหม?
    def hasquestion(self) : 
        return self.question_number<len(self.question_list)
    
    #เช็คคำตอบ
    def checkAnswer(self,userInput):
        correct_Answer=self.current.answer
        if(userInput.lower() == correct_Answer.lower()) :
            self.score += 1
            return True
        else :
            return False
