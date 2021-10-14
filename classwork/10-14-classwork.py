def mode(l):
# assume the first one is the mode so far
# for each item,
    # count how many tiems it sppears
    # if it appears more than the mode so far
    # it becomes the new mode so far

# return the values in the list that occurs most frequently
# if the mode is not unique, return any of them
# think about the list processing routines we already written    
    count = 0
    if (len(l) < 1):
        return None
    nextIndex = l[1]
    for item in l:
        if item == nextIndex:
            nextIndex = item
            count += 1
    return nextIndex

# This is a class example
import random
l = [random.randrange(10) for x in range(20)]

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

def mode2(L):
    mode_so_far = L[0]
    count_so_far = frequency(L,mode_so_far)
    for value in L:
        count_value: frequency(L,value)
        if count_value > count_so_far:
            count_so_far = count_value
            mode_so_far = value
    return mode_so_far


def tests():
    print(mode([3,8,2,8,4,6]))


if __name__== "__main__":
    tests()

# def find_min(l):
#     if (len(l)<1):
#         return None
#     smallest_so_far = l[0]
#     for item in l:
#         if item < smallest_so_far:
#             smallest_so_far = item
#     return smallest_so_far


# l = [random.randrange(10) for x in range(30000)]

