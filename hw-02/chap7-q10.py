# Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

# Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as

# if  abs(x - y) < 0.001:      # if x is approximately equal to y


# def is_rightangled(x,y,z):
#   if  abs(x - y) < 0.001:
#     return 

# function is_rightangled  (parameters x,y,z):



def is_rightangled(a, b, c):
  if max(a,b,c) == a:
    return abs((a**2)-(b**2+c**2)) < 0.001
  elif max(a,b,c) == b:
    return abs((b**2)-(a**2+c**2)) < 0.001
  else:
    return abs((c**2)-(a**2+b**2)) < 0.001