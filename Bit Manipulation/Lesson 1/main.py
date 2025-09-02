# def numberOfBits(n):
#     count = 0
#     while (n):
#         count = count + 1
#         n = n >> 1
#     return count

# n = int(input("Enter a number:"))
# print("Number of bits:", numberOfBits(n))

# num1 = 10
# num2 = 4
# print("num1 & num2 are:", num1 & num2)
# print("num1 | num2 are:", num1 | num2)
# print("num1 ^ num2 are:", num1 ^ num2)
# print("num1 << num2 are:", num1 << num2)
# print("num1 >> num2 are:", num1 >> num2)
# print("~num1 are:", ~num1)
# print("~num2 are:", ~num2)

def isEvenOdd(n):
    if(n ^ 1 == n + 1):
      return True;
    else:
      return  Flase;

number = int(input("enter your number:"))
if isEvenOdd(number):
   print(number, "is even")

else:
   print(number, "is odd")1