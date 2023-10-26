# write a python program that allows you to add an employee 
# with domain, name, empid, and email details using user 
# input and then print the employee's details. 

# emp_details = []
# n = int(input("No.of entries: "))
# for i in range(0,n):
#     emp_name = input("Enter emp name: ")
#     emp_id = input("Enter emp id: ")
#     emp_domain = input("Enter emp domain: ")
#     Email = input("Enter emp email: ")
#     details = emp_name,emp_id,emp_domain,Email
#     emp_details.append(details)
# print("Employee details: \n"emp_details)


#2 

def add_employee():
  domain = input("Enter the employee's domain: ")
  name = input("Enter the employee's name: ")
  emp_id = input("Enter the employee's ID: ")
  email = input("Enter the employee's email address: ")
  employee = domain,name,emp_id,email
  employee.save()
def add_emp_details():
  employees = employee.all()
  for employee in employees:
    employee = {
      "domain": domain,
      "name": name,
      "emp_id": emp_id,
      "email": email
    }
    for emp_id in employees:
      print("Employee details already exists.")
  print("Employee added successfully!")
def main():
  while True:
    print("What would you like to do?")
    print("1. Add an employee")
    print("2. Add details to database")
    print("3. Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
      add_employee()
    elif choice == "2":
      add_emp_details()
    elif choice == "3":
      break
main()