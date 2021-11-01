# 12.4
# What is the longest word in Alice in Wonderland? How many characters does it have?

word = "Alice in Wonderland"
newArr = word.split()

def bigWords(newArr):
    largestWord = ""
    for word in newArr:       
        if len(largestWord) < len(word):
            largestWord = word
    lengthOfLongWord = len(largestWord)
    return "The longest word is " + largestWord + ". And it has " + str(lengthOfLongWord) + " characters." 

print(bigWords(newArr))