import sqlite3
import datetime

def fire_query(q):
    con=sqlite3.connect("library_db.db")
    con.execute(q)
    con.commit()
    con.close()

def create_table():
    bissu_qur=""" create table if not exists book_issue
                 (
                    enr number(10),
                    bnum number(10),
                    idate varchar (16),
                    rdate varchar (16)
                 )
    """
    all_b="""
                 create table if not exists all_books
                 (
                   bnum number (10),
                   btitle varchar (25),
                   bauthor varchar (20),
                   bpublication varcchar(30)
                 )
    """
    stud="""             
                 create table if not exists students
                 (
                    senr number(10),
                    sname varchar(25),
                    sclass varchar(10),
                    semail varchar(35),
                    smob varchar(25)
                 )
    """
    fire_query(bissu_qur)
    print("Created book issue table.....")
    fire_query(stud)
    print("Created students table.....")
    fire_query(all_b)
    print("Created all_books table.....")

def issue_book():
    pass



def return_book():
    pass

def view_not_ret_book():
    pass

def search_student():
    pass

def search_book():
    pass

def add_new_stud():
    pass

def add_new_book():
    pass

def view_stud_history():
    pass

def view_book_history():
    pass

create_table()
while True:
    print("Select operation")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - View Not Returned Books")
    print("4 - Search Student")
    print("5 - Search Book")
    print("6 - Add New Student")
    print("7 - Add New Book")
    print("8 - View Student History")
    print("9 - View Book History")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))
    if ch==1: issue_book()
    elif ch==2: return_book()
    elif ch==3: view_not_ret_book()
    elif ch==4: search_student()
    elif ch==5: search_book()
    elif ch==6: add_new_stud()
    elif ch==7: add_new_book()
    elif ch==8: view_stud_history()
    elif ch==9: view_book_history()
    elif ch==0: exit(0)