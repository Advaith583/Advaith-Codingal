def Greet(name):
    print( name + "is fat")

name = input("Enter your name :")
Greet(name) 

def sum(a,b):
    return a+b

num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))

ans = sum(num1,num2)
print("Your Answer is : " , ans)

# def greet(count):
#     if count == 11:
#         return
    
#     print("hello" , count)
#     greet(count + 1)

# greet(1)

# def Factorial(num):
#     if num == 1:
#         return 1
#     return num * Factorial(num - 1)

# num = int(input("Enter The Number :"))
# ans = Factorial(num)
# print(f"Factorial of {num} is : {ans}")