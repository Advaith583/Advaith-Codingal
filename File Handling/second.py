# file = open("sample.txt", "r")
# text = file.read()
# print(text)
# file.close()


# file = open("sample.txt","r")
# text = file.read(5)
# print(text)
# print(file.tell())
# file.close()

# file = open("sample.txt","r")
# line1 = file.readline()
# line2 = file.readline()
# print(line1)
# print(line2)
# file.close()

# file = open("sample.txt", "r")
# line = file.readlines()
# print(line)
# file.close()

# file = open("sample.txt", "r")
# lines = file.readlines()
# for i in lines:
#     print(i.strip())

file = open('sample.txt','r')
print("Reading first line...")
print(file.readline())


file = open('sample.txt', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('sample.txt','r')
print("Looping through the lines...")
for line in file:
  print(line)
file.close()
