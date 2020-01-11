

details = {}

def add():
    id = input("Enter id : ")
    name = input("name : ")
    details[id] = name

def displayAll():
    if len(details) == 0:
        print("NO details found.\n")
    else:
        print("Student details:\nID\t\tName")
        for k,v in details.items():
            print(f"{k}\t\t{v}")
        print()

def display(id):
    if id in details:
        print(f"ID:{id}\t\t{details[id]}\n")
    else:
        print("Entered student_id doesnot exist\n")

while True:
    ch = int(input("Enter your choice\n1:Add student details\n2:Display all student details\n3:Display a student details\n"))
    if ch == 1:
        add()
    elif ch == 2:
        displayAll()
    elif ch == 3:
        id = input("Enter student id: ")
        display(id)
    else :
        break
