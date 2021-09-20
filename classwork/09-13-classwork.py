# Git
# Setting up ssh key
# Do:
# ssh-keygen in the terminal
# cat .ssh/id_rsa.pub
# git clone git@github.com:hunter-classes/fall-2021-127-work-George-Sucuzhanay.git (repo ssh)

# Notes:
# copies repo from Github to local machine
#
# print("I made a change")

# Remove files:
# git checkout file_name.py

# Commit Files:
# git commit file_name.py -m "add a comment here


# Workflow:
# only once:
    # git clone ssh repo link

# everytime you sit down
# to work:
    # 1) cd repofolder     (thonny)
    # 2) git pull       (thonny)
    
# Normal Workflow:
    # 1) edit files (thonny)
    # 2) run/test (thonny)
    # 3) git commit file_name.py -m "message"              (terminal)
    # 4) git push                (terminal)


# Review:
# git clone -> first time copy
# git push -> send updates to github
# git pull -> get updates from github
# git commit -> send local changes to local git
# mkdir -> makes a new folder
# git add -> to add a file to git control
# git rm file_name.py -> remove a file
# git mu oldname newname -> this renames and moves a file
# git commit -a -m "message" -> commits all edited files at once

# Sept 20, 2021 (Mon)

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def isEvenTerse(number):
    return number % 2 == 0

def isOdd(number):
    return not isEven(number)

longString ="""
Street bands have been picking up the slack for the last year in NYC, performing for outside diners and more throughout the city. This festival celebrates them and puts them front and center.
Email readers can see the video 
"""
def countLetters(s,letter):
    """ 
    count the number of times letter occurs in string s
    """
    count = 0
    for l in s:
        print(l)


longString ="""
Street bands have been picking up the slack for the last year in NYC, performing for outside diners and more throughout the city. This festival celebrates them and puts them front and center.
Email readers can see the video 
"""
def countLetters(s,letter):
    """ 
    count the number of times letter occurs in string s
    """
    count = 0
    print(s)
    for l in s:
        if l==letter.lower() or l==letter.upper():
            count = count + 1
    return count 


def tests():
    print("IsEven tests")
    print("isEven(23)",isEven(23))
    print("isEven(24)",isEven(24))
    print()
    print("IsEvenTerse tests")
    print("isEvenTerse(23)",isEvenTerse(23))
    print("isEvenTerse(24)",isEvenTerse(24))
    print()
    print("IsOdd tests")
    print("isOdd(23)",isOdd(23))
    print("isOdd(24)",isOdd(24))
    print()
    print("Count letters a in longString")
    print(countLetters(longString,'A'))

if __name__=="__main__":
    # put the stuff here to be run automatically if you
    # run this file as a program 
    tests()
    
# Resources
# docs.python.org
# w3schools Python string methods
# String Methods help with string manipulation
# codingbat.com for extra programming exercises for python
