def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

def main():
    print("Choose operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = int(input("Enter choice from(1,2,3,4): "))

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