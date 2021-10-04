# put all functions in a file named liststuff.py

# Finish the find_min(l) routine we discussed in class (it returns the smallest value from a list of numbers

# Write a function combine(l1,l2) which takes two lists of numbers and returns a new list that adds corresponding elements . That is combine([1,2,3],[10,20,30]) would return a list with [11,22,33]. Do something sensible if the lists are not of the same length

# Write a function list_sum(l) that returns the sum of the values of the list (don't use the built in sum function.

# Write a function subsum(l) which will take a list where each element is a list, for example [ [1,2], [3,4] , [5,6]] and returns a new list where each item is the sum of it's lists elements. For the previous example list, it would return [3,7,11].

def find_min(l):
    l.sort()
    return l[:1]

def combineList(l1, l2):
    count = 0
    result = []
    for i in l1:
        i = l1[count] + l2[count]
        result.append(i)
        count = count + 1
    return result
    
def list_sum(l):
    total = 0
    for i in l:
        total += i
    return total

# Write a function subsum(l) which will take a list where each element is a list, for example [ [1,2], [3,4] , [5,6]] and returns a new list where each item is the sum of it's lists elements. For the previous example list, it would return [3,7,11].

def subsum(l):
    total = 0
    newList = []
    for i in l:
        total = i[0] + i[1]
        newList.append(total)
    return newList

def tests():
    # add tests here
    print(find_min([8,9,7,4,5,6,3,5,2]))
    print(combineList([1,2,3],[10,20,30]))
    print(list_sum([1, 2, 3, 4, 5, 6]))
    print(subsum([ [1,2], [3,4] , [5,6]]))

if __name__== "__main__":
    tests()