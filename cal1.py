num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
def add():
    result = num1 + num2
    print("The sum is: ",result)

def subtract():
    result = num1 - num2
    print("The difference is:",result)

def multiply():
    result = num1 * num2
    print("The product is:",result)

def divide():
    if num2 != 0:
        result = num1 / num2
        print("The quotient is:",result)
    else:
        print(" Cannot divide by zero")
for i in range(5):
    print("Choose an operation:")
    print("the options are 1.addition\n 2.substraction\n 3.multiplication\n 4.division\n 5.exit\n" )
    choice = int(input("Enter choice (1/2/3/4/5): "))

    if choice ==1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    elif choice == 5:
        exit
        break
    else:
        print("Invalid choice")
