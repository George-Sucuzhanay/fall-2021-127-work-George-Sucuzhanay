# #  Then complete the function line. Line should accept five parameters:
# - The first represents a turtle, 
# - the next two, x and y a starting location, - then a color like "red" or "green"
# - then a length or distance. 

# The function should move the turtle to x,y and draw a line by moving forward the specified amount. There are already lines to test your solution in the started code.

import turtle

def line(t,x,y,color,len):
  # for i in range(4):
    t.goto(x,y)
    t.color(color)
    t.forward(len)

wn = turtle.Screen()
crush = turtle.Turtle()

line(crush,10,10,"red",50)
crush.right(35)
line(crush,50,-10,"green",40)

wn.exitonclick()
wn.mainloop()





# def line(x,y,color,len):
#   for i in range(3):
#     crush.goto(x,y)
#     crush.color(color)
#     crush.forward(len)


# wn = turtle.Screen()
# crush = turtle.Turtle()

# line(10,10,"red",50)
# crush.right(35)
# line(50,-10,"green",40)

# wn.exitonclick()
# wn.mainloop()
