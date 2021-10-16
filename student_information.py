def addStudent():
    fp=open('student.txt','a')
    rno=input("Enter student roll number")
    name=input("Enter student name")
    address=input("Enter address")
    department=input("Enter dept")
    contactNum=input("Enter contact details")
    fp.write("{} {} {} {} {}\n".format(rno,name,address,department,contactNum))
    fp.close()
    print("Successfully info added")

def AllStudentInfo():
    fp=open('student.txt','r')
    content=fp.read() #Read the data from file and store in content varaible
    print(content)
    fp.close()
    
def OneStudentInfo():
    fp=open('student.txt','r')
    rno=input("Whose details want to get")
    data=fp.readlines()
    for i in data:
        r=i.split(' ')
        if r[0]==rno:
            print(i)
    #print(data)
    fp.close()

def DelStudent():
    fp=open('student.txt','r')
    rno=input("whose detais want to delete")    # if we give input as 333
    data =fp.readlines()   #source
    updated_list=[]    # after remvoing 333 record list will be stored
    for i in data:
        r=i.split(' ')
        if r[0]!=rno:
            updated_list.append(i)    # if rno !=333 .. adding record
    fp.close() # reading information completed then after classmethod
    
    fp=open('student.txt','w')
    fp.writelines(updated_list)
    fp.close()
            
    
    
    
def UpdateStudent():
    fp=open('student.txt','r')
    rno = input('whose details want to update')
    data =fp.readlines()  # source data reading
    updated_list = []
    for i in data:
        r = i.split(' ')
        if r[0]!=rno:
            updated_list.append(i)
        else:
            name=input("Enter Name")
            address= input("Enter Address")
            dept = input("Enter department")
            contact = input("Enter contact Number")
            
            updated_list.append("{} {} {} {} {}\n".format(rno,name,address,dept,contact))
    
    fp.close()
    fp=open('student.txt','w')
    fp.writelines(updated_list)
    fp.close()
    
    
    
    
while True:
    print("\n1.Add student \n2.Get all students info \n3.Get one student info \n4.Delete Student \n5.Update student Info")
    choice=int(input("Enter your choice"))
    if choice==1:
        addStudent()
    elif choice==2:
        AllStudentInfo()
    elif choice==3:
        OneStudentInfo()
    elif choice==4:
        DelStudent()
    elif choice==5:
        UpdateStudent()
    else:
        print("Wrong choice")

    flag=input("If you want to continue press (Y/y)")

    if flag=='Y' or flag=='y':
        pass
    else:
        print("Thank You for Using Serivces")
        break     
