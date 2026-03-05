'''
 Reading and writing into a file

 readlinnes() - It reads all the lines of a file and returns a list of lines.
    readline() - It reads a single line from the file and returns it as a string.
    write() - It writes a string to the file.
    writelines() - It writes a list of strings to the file.
    seek() - It changes the file position to the specified byte offset.
    tell() - It returns the current file position in bytes.
'''

fileObj = open("Core2Web.txt", "r+")

data = fileObj.read()

print(data)

fileObj.write("Welcome to Core2Web")

fileObj.seek(0)

data = fileObj.read()

print(data)

fileObj.seek(0)
value = fileObj.readline()
print(value)