# Given a text as input, find and output the longest word.
txt = input().split()

print(max(txt, key = len))