# class Employee:
#     #statis variable
#     No_of_employees = 0
#     def __init__(self,name,domain,salary):
#         #instance variable
#         self.name = name
#         self.domain = domain
#         self.salary = salary
#         Employee.No_of_employees += 1
#     def display(self):
#         #local variable
#         employee_id = Employee.No_of_employees
#         print(self.name,self.domain,self.salary,employee_id)
            
# siri = Employee("Siri","Python",15000)
# siri.display()
# shireesha = Employee("Shireesha",".Net",10000)
# shireesha.display()
# print(Employee.No_of_employees)


#instance variable
class Employee:
    def __init__(self,ID,name):
        # Inside of the constructer using self
        self.ID = ID
        self.domain = "Python"
        self.name = name
    def details(self):
       # Inside of the instance method
       self.Email = "siri@gmail.com"
e = Employee("02047","siri")
# e1 = Employee("02048","java","ramya")
e.details()
print(e.domain)
print(e.name)
# Out side of the class using object reference variable
e.company = "Marolix technology"
print(e.company)
print(e.Email)


#Static variable
# class Employee:
#     # within the class
#     company = "marolix technology"
#     def __init__(self):
#         self.Employee = name
#         self.domain = domain
#     def emp_details(self):