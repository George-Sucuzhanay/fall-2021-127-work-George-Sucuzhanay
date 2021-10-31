# 12.1 
# Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample run of the program might look this this:

sentence = input("Please enter a string: ")

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","w"]


myCountofLetter = {}

for letter in sentence:
    if letter in alphabet:
        pass