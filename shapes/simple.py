import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

# square
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)

# triangle
crush.color("red")
crush.penup()
crush.goto(-70,-70)
crush.pendown()
crush.forward(50)
crush.right(120)

crush.forward(50)
crush.right(120)

crush.forward(50)
crush.right(120)

# hexagon
crush.color("green")
crush.penup()
crush.goto(-50,80)
crush.pendown()

crush.forward(10)
crush.right(60)
crush.forward(10)
crush.right(60)
crush.forward(10)
crush.right(60)
crush.forward(10)
crush.right(60)
crush.forward(10)
crush.right(60)
crush.forward(10)
crush.right(60)



wn.exitonclick()
wn.mainloop()