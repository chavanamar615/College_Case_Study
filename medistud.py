from Q1 import Student
class   Medistud(Student):
    def __init__(self, name, id, age, percentage,specialization,marksofinternship):
        super().__init__(name, id, age, percentage)
        self.specialization=specialization
        self.marksofinternship=marksofinternship
    
    def __str__(self):
        return f"{super().__str__()},Specialization={self.specialization},marksofinternship={self.marksofinternship}"
    
    def Calculaterank(self):
        if (self.percentage>=75 and self.marksofinternship>=40):
            return "Distinction"
        elif(self.percentage>=60 and self.marksofinternship>=30):
            return "First class"
        elif(self.percentage>=50 and self.marksofinternship>=20):
            return "second class"
        elif(self.percentage>=40 and self.marksofinternship>=10):
            return "Pass"
        else:
            return "fail"
