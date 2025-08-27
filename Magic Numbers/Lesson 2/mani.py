# n = int(input("enter a number:"))
# count = 0

# for i in range(1, n+1):
#     if n % i == 0:
#         count+= 1
# if count == 2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n+1, i):
                primes[j] = False

    for i in range(n + 1):
        if primes[i]:
            print(i, end =' ')

limit = int(input("Enter the limits:"))
sieve_of_eratosthenes(limit)