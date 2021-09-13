# Write a function that removes all occurrences of a given letter from a string.

def removeLetter(word, letter):
    return word.replace(letter, '')

print(removeLetter("Coding", "o"))
