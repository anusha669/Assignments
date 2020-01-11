from DA_2_1 import Person,Staff,Student

lst = []

lst.append(Student(1,"Ana","Udupi","ISE",56000))
lst.append(Student(2,"Dick","Mangalore","CSE",60000))
lst.append(Staff(1,"Elsa","Moodabidri",2019,40000))
lst.append(Staff(2,"Harry","Karkala",2010,90000))
lst.append(Staff(3,"Tom","Bajpe",2017,58000))

for obj in lst:
    obj.displayDetails()