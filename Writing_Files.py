file = open("text.txt","w")
# file.write("Hello this is raabia")
amount_written = file.write("Hello this is raabia")
# The write method returns the number of bytes written to a file, if successful.
print(amount_written)
file.close()




# write mode deletes already written data from file and overwrites it   
file=open("text.txt","r")
print(file.read())
file.close()