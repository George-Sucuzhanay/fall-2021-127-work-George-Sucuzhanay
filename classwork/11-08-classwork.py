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

def remove_stop_words(bag,stopwordfilename):
    # read a list of stopwords from stopwordfilename
    f = open("classwork/stopwords.txt").read()
    f.split
    # (grab the list from the class web site)
    for stopword in list(bag.key()):
    # remove all the words in the stoplist word list from the bag dictionary
        pass
    return bag

def main():
    load_bow("classwork/chapter1.txt")

    k = list(bag.keys())
    v = list(bag.values())
    m = find_max(v)
    print(m)
    # find the most frequent word
    position = v.index(124)
    print(k[position])
    print(get_words_more_frequent(bag,25))
    print(get_words_more_frequent_dict(bag,25))

if __name__ == "__main__":
    main()