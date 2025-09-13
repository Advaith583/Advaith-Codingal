def  power8(number):
 if number <= 0:
    return False
 return (number & (number - 1)) == 0 and (number - 1) % 7 == 0

n = int(input("enter a number"))
if power8(n):
    print("\nThe number is a power of 8")
else:
   print("\nThe number is not a power of 864")
4