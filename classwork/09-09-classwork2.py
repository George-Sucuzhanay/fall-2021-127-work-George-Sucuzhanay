import turtle

wn = turtle.Screen()
crush = turtle.Turtle()

def drawpoly(t, numsides, x,y,sidelen,color):
  # go to the right location
  t.penup()
  t.goto(x,y)
  t.color(color)
  t.pendown()

  # loop numsides times
    # draw by moving forward
    # turn the right amount
  for i in range(numsides):
    t.forward(sidelen)
    t.left(360/numsides)
    

drawpoly(crush,6,10,10,50, "red")
drawpoly(crush,3,5,5,20,"green")
drawpoly(crush,5,10,10,50,"purple")
drawpoly(crush,4,-20,20,30,"orange")

wn.exitonclick()
wn.mainloop()

# t.goto(x,y)
# t.color(color)
# t.forward(len)



