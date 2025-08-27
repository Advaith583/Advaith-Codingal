# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     iterations = 0

#     while  left <= right:
#         iterations += 1
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             print(f"Found {target} in {iterations} iterations")
#             return
    
# #         elif arr[mid] < target:
# #             left = mid + 1
# #         else:
# #             right = mid - 1

# #     print(f"{target} not found after {iterations} iterations")

# # numbers = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
# # binary_search(numbers, 7)

# def timer(n):
#     if n == 0:
#         print(n)
#         timer(n-1)

# timer(5)

def create_list(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    print(numbers)

create_list(5)
