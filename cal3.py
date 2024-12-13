def add(x,y):
    result = num1 + num2
    return result

def subtract(x,y):
    result = num1 - num2
    return result

def multiply(x,y):
    result = num1 * num2
    return result

def divide(x,y):
    result = num1/num2
    return result
for i in range(5):
    print("Choose an operation:")
    print("the options are 1.addition\n 2.substraction\n 3.multiplication\n 4.division\n 5.exit\n" )
    choice = int(input("Enter choice (1/2/3/4/5): "))

    if choice == 1:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        c=add(num1,num2)
        print(c)
    elif choice == 2:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        c=subtract(num1,num2)
        print(c)
    elif choice == 3:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        c=multiply(num1,num2)
        print(c)

    elif choice == 4:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        c=divide(num1,num2)
    elif choice == 5:
        exit
        break
    else:
        print("Invalid choice")
