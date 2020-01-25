date = input("Date :")
if date.find('/'):
    print(date.replace('/','-',3))
else:
    print(date.replace('-','/',3))
