def  checkIfSame(number1,number2):
    if((number1 ^ number2)== 0) :
        print("both numbers are equal")
    else:
        print("numbers are not equal")

number1 = int(input("Enter first number to compare"))
number2 = int(input("Enter second number to compare"))
checkIfSame(number1,number2)