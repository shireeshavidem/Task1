def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

def main():
    print("Choose operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice from(1,2,3,4): ")

    x = float(input("Enter fist number: "))
    y = float(input("Enter second number: "))

    if choice == "1":
        print(x, "+", y, "=", add(x, y))
    elif choice == "2":
        print(x, "-", y, "=", subtract(x, y))
    elif choice == "3":
        print(x, "*", y, "=", multiply(x, y)) 
    elif choice == "4":
        print(x, "/", y, "=", divide(x, y))

    else:
        print("Invalid Input")                     

if __name__=="__main__":
    main()

# This function adds two numbers
# def add(x, y):
#     return x + y

# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y

# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y

# # This function divides two numbers
# def divide(x, y):
#     return x / y


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     # take input from the user
#     choice = input("Enter choice(1/2/3/4): ")

#     # check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
#         # check if user wants another calculation
#         # break the while loop if answer is no
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
    # else:
    #     print("Invalid Input")

