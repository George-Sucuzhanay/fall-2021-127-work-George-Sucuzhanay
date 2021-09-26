# Make a new file named fizzbuzz.py. That function should perform the fizzbuzz test. That is, it should test each of the numbers from 1 to 100 (inclusive).
# If the number is divisible by 3, print "fizz"
# if it's divisible by 5 print "buzz"
# if it's divisible by 3 and 5 print "fizzbuzz"
# otherwise just print the number

import random

# using if and elif statements
def fizzbuzz():
    num1 = random.randint(1,101)
    if (num1 % 3 == 0 and num1 % 5 == 0):
        return "fizzbuzz"

    elif (num1 % 3 == 0):
        return "fizz"

    elif (num1 % 5 == 0):
        return "buzz"
    else:
        return num1

print(fizzbuzz())

# Using while loops
count = random.randint(1,101)
while (count < 101):
    if (count % 5) == 0 and (count % 3) == 0:
        print ("FizzBuzz")
    elif (count % 3) == 0:
        print ("Fizz")
    elif (count % 5) == 0:
        print ("Buzz")
    else:
        print (count)
    break

