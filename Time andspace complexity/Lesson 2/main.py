# constant time complexity
def BigOhConstant(n):
    iteration = 0
    print("The value of n is:",)
    iteration += 1
    print("The value of iteration is:", iteration)

BigOhConstant(10)

# linear time complexity
def BigOhLinear(n):
    iteration = 0
    for i in range(1, n+1):
        print("The value of i is:", i)
        iteration += 1

    print("The value of iteration is:", iteration)

BigOhLinear(10)