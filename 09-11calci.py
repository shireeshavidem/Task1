
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Choose Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == "1":
            print(x, "+", y, "=", add(x, y))
        elif choice == "2":
            print(x, "-", y, "=", subtract(x, y))
        elif choice == "3":
            print(x, "*", y, "=", multiply(x, y)) 
        elif choice == "4":
            print(x, "/", y, "=", divide(x, y))
        
        next_calculation = input("You want to do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

