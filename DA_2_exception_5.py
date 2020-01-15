class LowBalanceException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return f"{__class__.__name__} : {self.msg}"
        
class Employee():
    designation = {'manager':0.1,'officer':0.12,"clerk":0.05}
    def __init__(self,empId,empName,desig,basicPay):
        self.empId = empId
        self.empName = empName
        self.desig = desig
        self.basicPay = basicPay
        if self.basicPay > 500:
            Employee.calculateHra(self)
        else:
            raise LowBalanceException("Low balance")

    def calculateHra(self):
        self.hra = self.basicPay*self.designation.get("manager")
        Employee.PrintDetails(self)

    def PrintDetails(self):
        print(f"{self.empId}\t{self.empName}\t{self.desig}\t\t{self.basicPay}\t{self.hra}")

Employee(10,"Tom","manager",40000)
Employee(11,"Dick","officer",45000)
Employee(12,"Harry","clerk",15000)
Employee(13,"Ana","clerk",300)