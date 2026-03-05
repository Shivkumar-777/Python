'''
Closing A File

In Python, you can close a file using the close() method. It is important to close a file after you are done with it to free up system resources. Here is an example of how to open a file, read its contents, and then close it:

'''

'''fileObj = open("python.txt", "r")

data = fileObj.read()

print(data)

fileObj.close()

'''

with open("python.txt", "r") as fileObj:

    data = fileObj.read()

    print(data)