# Returns the sum of num1 and num2
def add(num1, num2):
    print(num1)
    print(num2)
    print(num1 + num2)
    return num1 + num2


# Returns the value by substracting num2 from num1
def sub(num1, num2):
    return num1 - num2


# Returns the value by multiplying num2 from num1
def mul(num1, num2):
    return num1 * num2


# Returns the value by dividing num1 by num2
def div(num1, num2):
    return num1 / num2


def main():
    operation = input("What do you want to do (+,-,*,/): ")
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
        # invalid operation
        print("you must enter a valid operation")
    else:
        var1 = int(input("Enter Firt Number: "))
        var2 = int(input("Enter Second Number: "))
        if (operation == '+'):
            print(add(var1, var2))
        if (operation == '-'):
            print(sub(var1, var2))
        if (operation == '*'):
            print(mul(var1, var2))
        if (operation == '/'):
            print(div(var1, var2))


main()
# this is a modified version to test GitHub Braching process
