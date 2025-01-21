from college import College
ch=0
c=College()
while(ch!=4):
    print("1.addstudent","2.removestudent","3.getstudent","4.Exit")
    ch=int(input("enter your choice:"))
    if(ch==1):
        c.addStudent()
    elif(ch==2):
        c.removestud()
    elif(ch==3):
        c.getStud()    

