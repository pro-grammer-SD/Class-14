import turtle

turtle.getscreen().bgcolor("#f3a43f")
turtle.color("black")

turtle.hideturtle()

s = int(input("Sides: "))

for i in range(s):
    turtle.seth(i*360/s)
    turtle.forward(100)

turtle.done()