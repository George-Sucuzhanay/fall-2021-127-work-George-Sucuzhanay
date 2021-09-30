# -*- coding: utf-8 -*-
# do exercises 10, 11, and 12 from the text (in chapter 10)
# 10) Count how many words in a list have length 5.
def wordsInSentence(sentence):
    count = 0;
    for i in sentence: 
      if len(i) == 5: 
        count += 1
    return count


# 11) Sum all the elements in a list up to but not including the first even number.
def sumUntilEven(listNum):
    sumCount = 0
    for i in listNum:
        if i % 2 != 0:
            sumCount += i
        else:
            return sumCount
    return sumCount

# 12) Count how many words occur in a list up to and including the first occurrence of the word “sam”.
def countWords(listNames):
    count = 0
    for i in listNames:
        count +=1
        if i == "sam":
            break
    return count

def tests():
    # add tests here
    print(wordsInSentence(["how", "good", "wonderful", "excited", "joyful"]))
    print(sumUntilEven([1,3,5,7,9,10]))
    print(countWords(["momama","dad","son","cousin", "sam", "great"]))

if __name__== "__main__":
    tests()