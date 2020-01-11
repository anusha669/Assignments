class Person:
    def __init__(self,id,name,address):
        self._id = id
        self._name = name
        self._address = address
    def displayDetails(self):
        print(f"{self._id}\t{self._name}\t{self._address}",end = "\t")

class Student(Person):
    def __init__(self,id,name,address,course,fee):
        Person.__init__(self,id,name,address)
        self._course = course
        self._fee = fee 
    def displayDetails(self):
        Person.displayDetails(self)
        print(f"{self._course}\t{self._fee}")

class Staff(Person):
    def __init__(self,id,name,address,yr_join,sal):       
        Person.__init__(self,id,name,address)
        self._year = yr_join
        self._sal = sal
    def displayDetails(self):
        Person.displayDetails(self)
        print(f"{self._year}\t{self._sal}")
  