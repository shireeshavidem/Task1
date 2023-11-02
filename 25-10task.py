# write a python program that allows you to add an employee 
# with domain, name, empid, and email details using user 
# input and then print the employee's details. 

emp_details = []
n = int(input("No.of entries: "))
def add_employee():
  for i in range(0,n):
    emp_domain = input("Enter emp domain: ")
    emp_id = input("Enter emp id: ")
    emp_name = input("Enter emp name: ")
    Email = input("Enter emp email: ")
    details = emp_name,emp_id,emp_domain,Email
    emp_details.append(details)
    if emp_id in emp_details:
      print("Employee ID already exists.")
    else: print("Employee added succesfully")
  print(emp_details)
def main():
  while True:
    print("What would you like to do?")
    print("1. Add an employee")
    print("2. Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
      add_employee()
    elif choice == "2":
      break
main()
# print("Employee details: \n"emp_details)


#2 

# def add_employee():
  # domain = input("Enter the employee's domain: ")
  # name = input("Enter the employee's name: ")
  # emp_id = input("Enter the employee's ID: ")
  # email = input("Enter the employee's email address: ")
  # employee = domain,name,emp_id,email
# def add_emp_details():
#   employees = dict(employees)
#   for emp_id in employee:
#     print("ID is already exists.")
#   print("Employee added successfully!")
# def main():
#   while True:
#     print("What would you like to do?")
#     print("1. Add an employee")
#     print("2. Add details to database")
#     print("3. Quit")

#     choice = input("Enter your choice: ")
#     if choice == "1":
#       add_employee()
#     elif choice == "2":
#       add_emp_details()
#     elif choice == "3":
#       break
# main()