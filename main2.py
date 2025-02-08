import turtle

turtle.getscreen().bgcolor("#6cfaf8")
turtle.color("black")

turtle.hideturtle()

# turtle.draw("star") DAMN

for i in range(3):
    turtle.seth(i*120)
    turtle.forward(100)

turtle.penup()
turtle.sety(turtle.ycor()+50)

turtle.pendown()

for i in range(3):
    turtle.seth(360-(i*120))
    turtle.forward(100)

turtle.done()