def add_new_stud():
    print("Enter your name:",end="")
    name=input()
    print("Enter your enrollment number:",end="")
    enum = input()
    print("Enter your Email id:",end="")
    email = input()
    print("Enter your mobile number:",end="")
    mnum= input()
    fobj= open("Students_info.txt","a")
    fobj.write(enum+","+name+","+email+","+mnum+"\n")
    fobj.close
    input()

def show_info():
    flag=False
    enum=input("Enter your enrolment number: ")
    fobj=open("Students_info.txt","r")
    alllines=fobj.readlines()
    for eachline in alllines:
        words=eachline.split(",")
        if words[0]==enum:
            flag=True
            break
    if flag==False:
        print("No such enrolment nummber exists")
    else:
        print("Enrolment number:",words[0],"\nName:",words[1],"\nEmail_Id:",words[2],"\nMobile Number:",words[3])
    fobj.close()
    input()

def remove_info():
    enum=input("Enter your enrolment number: ")
    fobj=open("Students_info.txt","r")
    alllines=fobj.readlines()
    for eachline in alllines:
        words=eachline.split(",")
        if words[0]==enum:
            alllines.remove(eachline)
            break
    fobj.close()
    fobj= open("Students_info.txt","w")
    fobj.writelines(alllines)
    fobj.close()
    print("Removed:",eachline)
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
