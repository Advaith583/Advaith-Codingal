# def OddOccuring(arr):
#     res = 0
#     for element in arr:
#         res = res ^ element
#     return res

# arr = []
# n = int(input("Enter arry size"))
# while(n):
#     num = int(input("Enter number:"))

#     arr.append(num)
#     n-=1

# print("OddOccuring number is", OddOccuring(arr))5

def TwoOdd(arr, size):
    xorof2 = arr[0]
    x = 0
    y = 0
    SetBit = 0
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]
        SetBit = xorof2 & ~(xorof2-1)
        for i in range(size):
            if(arr[i]& SetBit):
                x = x ^ arr[i]
            else:
                y = y ^ arr[i]
        
        print("TwoOddelements are" ,x,"&",y)


arr = []
n = int(input("Enter arry size"))
while(n):
    num = int(input("Enter number:"))

    arr.append(num)
    n-=1

TwoOdd(arr, n)
