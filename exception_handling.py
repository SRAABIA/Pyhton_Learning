#except
try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")


#multiple excepts
try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")

# using finally with try/except
try:
    print(1)
except:
    print(4)
finally:
    print("always executed even if unhandled exception has occured")