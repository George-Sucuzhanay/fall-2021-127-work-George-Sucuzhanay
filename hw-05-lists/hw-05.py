# Create a file named hw05.py and in it write the following functions (and when the program is run, they should be tested and should return and pritn their output)

# 1) Write a function keep-odds that that will take a list of integers as a parameter. 
# 2) It wil create and then return a new list that includes only the odd numbers from the first list.

# do exercises 10, 11, and 12 from the text (in chapter 10)


def keepodds(num):
    oddlist = []
    for i in num:
        if (i % 2 != 0):
            oddlist.append(i) 
    return oddlist
    

def tests():
    # add tests here
    print(keepodds([1,2,3,4,5,6,7]))
    print(keepodds([10,11,12,13,14]))
    

if __name__== "__main__":
    tests()
