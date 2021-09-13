# Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False


if is_even(21):
  print("This is an even number")
else:
  print("This is not an even number")