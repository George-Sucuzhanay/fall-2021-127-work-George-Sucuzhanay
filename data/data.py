# CSV Data Project
# Author: George Sucuzhanay
# Using NYC Open Data Unbanked Dataset: 
# https://data.cityofnewyork.us/Business/Where-Are-the-Unbanked-and-Underbanked-in-New-York/v5w4-adxa

import csv

# def clean(line):
#     """
#     takes in a string and returns a cleaned string.
#     1. convert to lower case
#     2. only keep letters and tab,space,newline
#     """
#     line = line.lower()
#     letters_to_keep = 'abcdefghijklmnopqrstuvwxyz\t \n'
#     # result = ""
#     # for letter in line:
#     #     if letter in letters_to_keep:
#     #         result = result + letter
#     result = [x for x in line if x in letters_to_keep]
#     cleaned = "".join(result)
#     return cleaned

# def remove_stop_words(line):
#     f = open("classwork/stopwords.txt")
#     stopwords = f.read().split()
#     result = [x for x in line.split() if x not in stopwords]
#     line = " ".join(result)
#     return line

def add_statement(index,key,statement):
    for word in statement.split():
        index.setdefault(word,[])
        if key not in index[word]:
            index[word].append(key)
    return index
f = open("data/underbanked.csv", encoding='Latin-1')

# Create a dictionary where
    # 1) Keys are the boroughs of NYC
    # 2) Values are the percentage of unbanked in such borought
reader = csv.reader(f)
people = {}
index = {}
mydict = dict((rows[0],rows[4]) for rows in reader)
print(mydict)

for item in reader:
    print(item['Sub Boro Name'])
    key = item['Sub Boro Name']
    # people[key] = item
    # statement = clean(item['Underbanked 2011'])
    # # we might not want to remove the stop words
    # statement = remove_stop_words(statement)
    # index = add_statement(index,key,statement)

# 1: ABCD
# 2: BCFG
# 3: BRS
# 4: XYZA
# A or C is a union search
# | 1, 4 |   | 2|
# A and C is a intersection search

# | 4 |  |1|  |2|

def s_or(index,words):
    """
    return a list of all keys in the index that contian any of the words
    """
    result = []
    for word in words:
        result = result + index[word]
    return list(set(result))

def s_and(index,words):
    """
    return a list of they keys such that they key has ALL
    the words in it
    """
    result = index[words[0]]
    for word in words[1:]:
        result = list(set(result) & set(index[word]))
    return result

# for key in index.keys():
#     if len(index[key]) > 50:
#         print(key,len(index[key]))









# print('father', len(index['father']), index['father'])
# print('mother', len(index['mother']), index['mother'])
# print()
# result = s_or(index, ['mother','father'])
# print('both',len(result),result)
# print()
# print()
# result = s_and(index,['mother','father'])
# print(result)






# Find the borough with the most underbanked will need the mode func
    # check to see it is also the borough with the highest percantage of foriegn born

# Find the borough with highest median income
    # compare it with the borough with the lowest median income
    # compare the underbanked perctanges of these 2 boroughs

