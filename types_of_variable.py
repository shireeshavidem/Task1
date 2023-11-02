class Employee:
    #statis variable
    No_of_employees = 0
    def __init__(self,name,domain,salary):
        #instance variable
        self.name = name
        self.domain = domain
        self.salary = salary
        Employee.No_of_employees += 1
    def display(self):
        #local variable
        employee_id = Employee.No_of_employees
        print(self.name,self.domain,self.salary,employee_id)
            
siri = Employee("Siri","Python",15000)
siri.display()
shireesha = Employee("Shireesha",".Net",10000)
shireesha.display()
print(Employee.No_of_employees)