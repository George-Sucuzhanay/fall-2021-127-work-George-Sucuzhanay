import csv

def clean(line):
    """
    takes in a string and returns a cleaned string.
    1. convert to lower case
    2. only keep letters and tab,space,newline
    """
    line = line.lower()
    letters_to_keep = 'abcdefghijklmnopqrstuvwxyz\t \n'
    # result = ""
    # for letter in line:
    #     if letter in letters_to_keep:
    #         result = result + letter
    result = [x for x in line if x in letters_to_keep]
    cleaned = "".join(result)
    return cleaned

def remove_stop_words(line):
    f = open("classwork/stopwords.txt")
    stopwords = f.read().split()
    result = [x for x in line.split() if x not in stopwords]
    line = " ".join(result)
    return line

def add_statement(index,key,statement):
    for word in statement.split():
        index.setdefault(word,[])
        if key not in index[word]:
            index[word].append(key)
    return index
f = open("classwork/last_statements_20.csv", encoding='Latin-1')

reader = csv.DictReader(f)
people = {}
index = {}
for item in reader:
    key = item['TDCJNumber']
    people[key] = item
    statement = clean(item['LastStatement'])
    # we might not want to remove the stop words
    statement = remove_stop_words(statement)
    index = add_statement(index,key,statement)

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

print('father', len(index['father']), index['father'])
print('mother', len(index['mother']), index['mother'])
print()
result = s_or(index, ['mother','father'])
print('both',len(result),result)
print()
print()
result = s_and(index,['mother','father'])
print(result)
