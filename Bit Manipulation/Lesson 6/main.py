# def flips(num1,num2):
#   flip = 0
#   while (num1 > 0 or num2 > 0):
#     t1 = num1 & 1
#     t2 = num2 & 1
#     if t1 != t2:
#       flip += 1
#       num1 >>= 1
#       num2 >>= 1
#     return flip
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# print("Number of flips needed:", flips(num1, num2))

def generate_power_set(input_set):
    n = len(input_set)
    power_set = []

    for i in range(2**n):
        subset = []
        for j in range(n):
          if i & (1 << j) !=0:
             subset.append(input_set[j])
        power_set.append(subset)

    return power_set

print("Power set of [x, y] is: ")
for s in generate_power_set(['x','y']):
  print(s)
