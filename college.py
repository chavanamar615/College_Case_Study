from Q1 import Student
from medicalstud import Medistud
from enngstud import Enngstud
class College:
    def __init__(self):  
        self.list_students=[]
        
    def addStudent(self):
        print("1.You have to insert Student:")
        print("2. insert Engineer student:")
        print("3. insert Medical student:")
        ch=int(input("Enter a choice:"))
        if(ch==1):
            name=input("enter student name:")
            id=int(input("enter student id:"))
            age=int(input("enter student age:"))
            percentage=int(input("enter student percentage:"))
            s=Student(name,id,age,percentage)  
            self.list_students.append(s)
        elif(ch==2):
            Enname=input("enter student name:")
            Enid=int(input("enter student id:"))
            Enage=int(input("enter student age:"))
            Enpercentage=int(input("enter student percentage:"))
            Branch=int(input("enter student branch:"))
            EnInternalmarks=int(input("enter student internalmarks:"))
            s=Enngstud(Enname,Enid,Enage,Enpercentage,Branch,EnInternalmarks)
            self.list_students.append(s) 
        elif(ch==3):
            Mediname=input("enter student name:")
            Mediid=int(input("enter student id:"))
            Mediage=int(input("enter student age:"))
            Medipercentage=int(input("enter student percentage:"))
            specialization=input("enter student branch:")
            Marksinternship=int(input("enter student internship marks:"))
            s=Medistud(Mediname,Mediid,Mediage,Medipercentage,specialization,Marksinternship)
            self.list_students.append(s)
        else:
            return "Choice is Invalid"
        
    def getStud(self):
        for Stud in self.list_students:
            print(Stud)
    
    def removestud(self):
        id=int(input("enter a id which you have to remove:"))
        for student in self.list_students:
            if(student.id==id):
                self.list_students.remove(student)
                break
        else:
            print("not found")
            
    def display(self):
        for i in self.list_students:
            print(i)
            

