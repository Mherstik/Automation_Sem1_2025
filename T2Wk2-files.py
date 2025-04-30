## Open file and read

file = open('NewFile.txt')
print(file.read())
file.close()

## Write to the file a new line
# file = open('file1.txt','t')
file = open('NewFile.txt','w')
# print(file.read())
file.write("\t")
file.write("Hello, world\nThis is a new line\n\tTabbed new \\line")
file.write(" This is a test")
file.close()
print("I wrote to the file")

  
  
## Open file and read

file = open('NewFile.txt')
print(file.read())
file.close()