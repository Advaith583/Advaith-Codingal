# age = int(input("enter your age:"))

# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")

# num = int(input("enter a number:"))
# if num % 2 == 0:
#         print(f"{num} is even number")
# else:
#  print(f"{num} is odd number")
# number = int(input("enter a number :"))
# if number > 50:
#     print("number is greater than 50 and it is : -")
#     if number % 2 ==0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("number is smaller than 50")

# marks = int(input("Enter your marks :"))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("grade:B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("Grade:F ")
import datetime
currentTime = datetime.datetime.now()
print("Currnet date and Time:", currentTime)

formatted_time = currentTime.strftime("%d-%m-%Y %H:%M:%S")

print("Formatted Date and Time:", formatted_time)

