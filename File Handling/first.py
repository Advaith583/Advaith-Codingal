file = open("sample.txt", "r")
text = file.read()
print(text)
file.close()

file = open("sample.txt", "w")
file.write("Hi this is gaurav.\nI hope you're doing well.\nI am using the write mode right now")
file.close()

file = open("sample.txt", "a")
file.write("\nadding new lines to your file.\nHope you enjoy learning filehandling.")
file.close()