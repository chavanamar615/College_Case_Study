from Q1 import Student
class Enngstud(Student):
    def __init__(self, name, id, age, percentage,branch,internalmarks):
        super().__init__(name, id, age, percentage)
        self.branch=branch
        self.internal=internalmarks
    def __str__(self):
        return f"{super().__str__()},branch={self.branch},internalmarks={self.internal}"
    
    def Calculaterank(self):
        if (self.percentage>=75 and self.internal>=40):
            return "Distinction"
        elif(self.percentage>=60 and self.internal>=30):
            return "First class"
        elif(self.percentage>=50 and self.internal>=20):
            return "second class"
        elif(self.percentage>=40 and self.internal>=10):
            return "Pass"
        else:
            return "fail"
        
# obj1=Enngstud("amar",1,23,78,"engineer",30)
# print(obj1)
# obj1.Calculaterank()
