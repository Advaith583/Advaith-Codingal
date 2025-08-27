num  = int(input("enter a number :"))

print(f"Factors of {num} are :", end=" 1" )

for i in range (1, num +1):
    if num % i == 0:
        print(i, end=" ")