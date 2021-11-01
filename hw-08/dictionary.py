# 12.1 
# Write a program that allows the user to enter a string. 
# It then prints a table of the letters of the alphabet in alphabetical order which occur in the string 
# together with the number of times each letter occurs. 
# Case should be ignored. 

word = input("Please enter a string: ")

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","x"]

myCountofLetter = {}

def example(alphabet, word):
  for char in word:
    for letters in alphabet:
      if char == letters:
        if letters in myCountofLetter:
          myCountofLetter[letters] = myCountofLetter[letters] + 1
        else:
          myCountofLetter[letters] = 1
  return myCountofLetter

print(example(alphabet, word))

keys = myCountofLetter.keys()
count = myCountofLetter.values()
for keyValue in sorted(keys):
  print(keyValue, myCountofLetter[keyValue])
