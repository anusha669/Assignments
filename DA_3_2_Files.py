def read():
    try:
        with open("Demonetization.txt","r") as dm:
            para = dm.readlines()
            for p in para:
                print(p)
    except(FileNotFoundError):
        print("File has not been created...\n")

def write():
    try:
        with open("Demonetization.txt",'x') as dm:
            string = input("Demonetization : ")
            dm.writelines(string)
    except(FileExistsError):
        print("File already exists...\n")

    
while True:
    choice = input("Enter a.create and write a file\nb.display contents of file\nc.Exit\n")
    if choice == 'c':
        exit(0)
    elif choice == 'a':
        write()
    else:
        read()