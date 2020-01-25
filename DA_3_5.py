lst = ['does','do','is','are']
stmt = input("Enter a statement : ")
for l in lst:
    if stmt.find(l) == 0:
        print("Interogative")
        break
else:
    print("Assertive")