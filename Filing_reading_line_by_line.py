file = open("text.txt","r")
# print(file.readlines())
# or we can use for loop
for line in file:
    print(line)
    
print(len(open("text.txt").readlines())) 
#output will be the number of lines in a file

file.close()