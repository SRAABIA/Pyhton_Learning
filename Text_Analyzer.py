filename = input("Enter a file name: ")
with open(filename) as f:
    text = f.read()
# print(text)

# This part of the program shows a function that counts how many times a character occurs in a string.
def count_char(text,char):
    count=0
    for c in text:
        if c==char:
            count+=1
    return count

# print(count_char(text,"r"))

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text,char)/len(text)
    print("{0}-{1}%".format(char,round(perc,2)))