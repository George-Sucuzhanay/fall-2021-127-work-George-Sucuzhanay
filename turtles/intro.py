import turtle

wn = turtle.Screen()

crush = turtle.Turtle()
alex = turtle.Turtle()          
john = turtle.Turtle()

crush.shape("turtle")
crush.color("blue")
crush.forward(50)
crush.left(50)
crush.forward(50)


# Add a second turtle to intro.py. Try to make it draw a red square with sides of length 50.
alex.goto(-2,-30)
alex.shape("turtle")

for i in (0, 1, 2, 3):
  alex.stamp()
  alex.color("red")
  alex.forward(50)
  alex.left(90)

# Then, add a third turtle. Try to make it draw a green triangle (equilateral) with sides of length 60
john.goto(0,20)
john.shape("turtle")

for i in (0, 1, 2):
  john.stamp()
  john.color("green")
  john.forward(50)
  john.left(120)


wn.exitonclick()
wn.mainloop()


