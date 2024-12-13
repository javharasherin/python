def add(x,y):
    result = num1 + num2
    print("The sum is: ",result)

def subtract(x,y):
    result = num1 - num2
    print("The difference is:",result)

def multiply(x,y):
    result = num1 * num2
    print("The product is:",result)

def divide(x,y):
    if num2 != 0:
        result = num1 / num2
        print("The quotient is:",result)
    else:
        print(" Cannot divide by zero")
for i in range(5):
    print("Choose an operation:")
    print("the options are 1.addition\n 2.substraction\n 3.multiplication\n 4.division\n 5.exit\n" )
    choice = int(input("Enter choice (1/2/3/4/5): "))

    if choice == 1:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        add(num1,num2)
    elif choice == 2:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        subtract(num1,num2)
    elif choice == 3:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        multiply(num1,num2)
    elif choice == 4:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        divide(num1,num2)
    elif choice == 5:
        exit
    else:
        print("Invalid choice")
