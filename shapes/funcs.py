def addThree(x):
  print("I'm in the addThree function")
  return x + 3 

def addNumbers(a,b):
  result = a + b
  print("Hello")
  return result
  
a = 5
b = addThree(a)
print(a,b)

r = addNumbers(20,a)
print(r)