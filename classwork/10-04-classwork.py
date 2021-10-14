# expection handling
# try:
# catch:
import random

def build_random_list(size,minval,maxval):
    l = []
    for i in range(size):
        l.append(random.randrange(minval,maxval))
    return l


def find_min(l):
    if (len(l)<1):
        return None
    smallest_so_far = l[0]
    for item in l:
        if item < smallest_so_far:
            smallest_so_far = item
    return smallest_so_far

def combine(l1,l2):
    len1 = len(l1)
    len2 = len(l2)
    if len1 < len2:
        shorter = len1
    else:
        shorter = len2
    result = []
    i = 0
    while i < shorter:
        result.append(l1[i] + l2[i])
        i = i + 1
    if shorter == len1:
        result = result + l2[i:]
    else:
        result = result + l1[i:]
    return result

def list_sum(l):
    sum = 0
    for item in l:
        sum = sum + item
    return sum

def sub_sum(l):
    result = []
    for item in l:
        result.append(list_sum(item))
    return result

def f(v1,v2):
    v3 = 0
    for v4 in v1:
        if v4 == v2:
            v3 = v3 + 1
    return v3
# print(f([1,5], 5))

def frequency(l,value):
    """
    count the number of times value appears
    in list l
    def f does the same thing as def frequency
    """
    count = 0
    for item in l:
        if item == value:
            count = count + 1
    return count
    
# list processing idioms
#    filter -> i.e. keeps odds , keep > 90
#    map -> i.e. add 1 to every item, subsums
#    reduce -> i.e. sum

def myfilter(l):
    result = []
    for item in l:
        if item % 2 == 0:
            result.append(item) 
    return result
# print (myfilter([1,2,3,4,5,6,7,8]))
# learning about predicates where we can call functions from other places
def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def apply(func, var1, var2):
    return func(var1,var2)
    
# print(apply(plus,100,200))

def isOdd(x):
    return x % 2 == 0

def mymap(l,func):
    result = []
    for item in l:
        result.append(func(item))
    return result


def myreduce(l,func,startValue):
    result = startValue
    for item in l:
        result = func(result,item)
    return result
print(myreduce([1,2,3,4,5],plus,0))
# python map filter reduce
# list comprehensions

print([x+10 for x in range(10)])