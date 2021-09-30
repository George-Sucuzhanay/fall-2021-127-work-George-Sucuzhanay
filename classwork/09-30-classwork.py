# Renaming file names in the terminal
# git mv oldname newname
# git commit
# git push

import random

def build_random_list(size,minval,maxval):
    l = []
    for i in range(size):
        l.append(random.randrange(minval,maxval))
    return l

def keep_odds(l):
    result = []
    for number in l:
        if number %2 !=0:
            result.append(number)

    return result

def sum_to_first_even(l):
    pass

def count_words_of_len_5(s):
    word_list = s.split()
    count = 0
    for word in word_list:
        if len(word) == 5:
            count = count + 1
    return count

def count_words_to_sam(s):
    word_list = s.split()
    count = 0
    for word in word_list:
        if word == "sam":
            break
    return count

def cwts2(s):
    word_list =  s.split()
    i = word_list.index("sam")
    return i


word_string="hello frog aaaaa ddd ddddd grr ertyu 234"

# filter routine
# using a dataset to filter to a result

# reduce routine
# taking a list and reducing to a result (you will use count)


