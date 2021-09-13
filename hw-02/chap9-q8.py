# Write a function that removes all occurrences of a given letter from a string.

def removeLetter(s,l):
  for character in s:
    print(character)
    if character == l:
      newString = s.replace(l," ")
      # return s
    else:
      print(s)
      # return
  
print(removeLetter("Coding", "o"))


# prefixes = "JKLMNOPQ"
# suffix = "ack"

# for p in prefixes:
#   if p == "O":
#     print(p + "u" + suffix)
#   else:
#     print(p + suffix)

