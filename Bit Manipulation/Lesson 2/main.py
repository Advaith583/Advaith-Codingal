# def numberOfBits(n):
#     ones = 0
#     zeroes = 0
#     while (n):
#         if (n & 1 == 1):
#             ones += 1
#         else:
#             zeroes += 1
#         n >>= 1
#     print("Number of ones =", ones, "\nNumber of zeroes = ", zeroes)

# number = int(input("Enter your number:"))
# numberOfBits(number)

def setOrNot(number, n):
    if (n & 1) == 1 or (n & 1) == 0:
      if number & (1 << (n - 1)):
         print("SET")
      else:
         print("NOT SET")
number = int(input("Enter the number:"))
n = int(input("Enter the  it position:"))
setOrNot(number , n)
         
      