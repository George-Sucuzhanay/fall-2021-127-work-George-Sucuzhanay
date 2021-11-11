# -*- coding: utf-8 -*-
bag = {}

def load_bow(filename):
    f = open(filename).read()
    for word in f.split():
        word = word.rstrip(".;?,\n")
        word = word.lower()
        bag.setdefault(word,0)
        bag[word] = bag[word] + 1
    return bag

# find the letter mode of bag
def find_max(l):
    m = l[0]
    for item in l:
        if item > m:
            m = item
    return m

# m = find_max(list(v))

# words that appear > n times 

def get_words_more_frequent(bag,count):
    result = [ x for x in bag.keys() if bag[x]  >= count]
    return result

def get_words_more_frequent_dict(bag,count):
    result = {}
    for word in bag.keys():
        if bag[word] >= count:
            result[word] = bag[word]
    return result

# def remove_stop_words(bag,stopwordfilename):
#     # read a list of stopwords from stopwordfilename
#     f = open(stopwordfilename)
#     stopwords = f.read().split()
#     print(stopwords)
#     # (grab the list from the class web site)
#     keys = bag.key()
#     for word in stopwords:
#         if word in bag.words():
#             del bag[word]
#     # remove all the words in the stoplist word list from the bag dictionary
        
#     return bag

# alternative
def alter(bag,stopwordfilename):
    f = open(stopwordfilename)
    stopwords = f.read().split()
    newbag = {}
    for word in bag.keys():
        if word not in stopwords:
            newbag[word]=bag[word]
    return newbag

def sentiment(bag,wordlistfile):
    # first, read in wordlistfile ino a list

    # Version 1: calculate the total number of words in bag
    # Version 2: calculate the # of different words in bag

    # Version 1: calculate the number of words in bag that are in wordlistfile
    # Version 2: calculate the number of different words in bag tht are in wordlistfile

    # Version 1: return the number from wordlistfile / total words
    # Version 2: return the same ratio but with v2 numbers

    pass

def main():
    load_bow("classwork/chapter1.txt")

    k = list(bag.keys())
    v = list(bag.values())
    m = find_max(v)
    # print(m)
    # find the most frequent word
    position = v.index(124)
    # print(k[position])
    # print(get_words_more_frequent(bag,25))
    # print(get_words_more_frequent_dict(bag,25))
    print(alter(bag,"classwork/stopwords.txt"))
if __name__ == "__main__":
    main()