# with open ("sample.txt","w") as file:
#     file.write("Hello, this is a test file.\n")
#     file.write("We are learning file handling in Python.\n")
# print("Data witten to sample.txt successfully")


# text = "Python is fun and easy to learn"
# with open("sample.txt","w") as file:
#     words = text.split()
#     for i in words:
#         file.write(i + "\n")
# print("Words written to words.txt successfully")

# import os

# try:
#     with open("newfile.txt","x") as file:
#         file.write("This is a newly created file.")
#     print("File created successfully.")
# except FileExistsError:
#     print("file already exists.")

# filename = "sample.txt"
# if os.path.exists(filename):
#     print(f"The file exists.")
# else:
#     print(f"The file name does not exist")

# filename = "data.txt"
# if not os.path.exists(filename):
#     with open(filename, "w") as file:
#         file.write("This is a newly created file.\n")
#     print("File was missing, so it has created.")
# else:
#     print("file already exists.")

import os

filename = "newfile.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"file '{filename}' dleted successfully.")
else:
    print(f"file '{filename}'does not exist.")

folder_name = "test_folder"
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"folder '{folder_name}' deleted successfully")
else:
    print(f"Folder '{folder_name}'does not exist")
