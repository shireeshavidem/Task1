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
emp_details = {} 
def add_employee():
  domain = input("Enter the employee's domain: ")
  name = input("Enter the employee's name: ")
  emp_id = input("Enter the employee's ID: ")
  email = input("Enter the employee's email address: ")
  employee = {
    "domain": domain,
    "name": name,
    "emp_id": emp_id,
    "email": email
  }
  emp_details = dict(employee)
  if emp_id in employee:
    print("Employee details already exists.")
  else:
    emp_details.update("\n")
    print(emp_details)
  print("Employee added successfully!")
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