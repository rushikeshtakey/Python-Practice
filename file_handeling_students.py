
def add_new_stud():
    # accept enrollment number, name, email and mobile
    # of student and write into file "stud_info.txt"
    enroll= input("Enter enrollment number:")
    name =input("Enter name:")
    email = input("Enter email")
    mobile = input("Enter mobile number:")
    stud_info= enroll + "," + name + "," + email +","+ mobile 
    sobj=open("Students_info.txt","a")
    sobj.writelines(stud_info)
    sobj.close()
    

def show_info():
    # accept enrollment number and search and show
    # information of that student from file "stud_info.txt"
    flag=False
    enum=input("Enter your enrollment number")
    fobj=open("Students_info.txt","r")
    stdls=fobj.readlines()
    fobj.close()
    for student in stdls:
        words=student.split(",")
        if words[0]==enum:
            print("Enrolment number: "+words[0],"\nName: "+words[1],"\nEmailId: "+words[2],"\nPhone number: "+words[3])
            flag=True
            break
    if flag==False:
        print("Invalid Enrollment number")
    input()
            



def remove_info():
    # accept enrollment number and search and remove
    # information of that student from file "stud_info.txt"
    flag=False
    enum=input("Enter your enrollment number")
    fobj=open("Students_info.txt","r")
    stdls=fobj.readlines()
    fobj.close()
    for student in stdls:
        words=student.split(",")
        if words[0]==enum:
            stdls.remove(student)
            fobj=open("Students_info.txt","w")
            fobj.writelines(stdls)
            fobj.close()
            print("removed :\n","Enrolment number: "+words[0],"\nName: "+words[1],"\nEmailId: "+words[2],"\nPhone number: "+words[3])
            flag=True
            break
    if flag==False:
        print("Invalid Enrollment number")
    input()
    

while True:
    print("Select operation")
    print("1 - Add New Student")
    print("2 - Display Student Information")
    print("3 - Remove student Information")
    print("4 - Exit")
    ch = int(input("Provide your choice : "))
    if ch==1:
        add_new_stud()
    elif ch==2:
        show_info()
    elif ch==3:
        remove_info()
    elif ch==4:
        exit(0)
