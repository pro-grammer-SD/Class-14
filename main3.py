import turtle

turtle.getscreen().bgcolor("#abd6e3")
turtle.color("black")

turtle.hideturtle()

fan_of_carol_ma_am = True

if fan_of_carol_ma_am: 
    for i in range(10):
        turtle.forward(i+i*3)
        turtle.seth(90)
        turtle.forward(i+i*3)
        turtle.seth(180)
        turtle.forward(i+i*3)
        turtle.seth(270)
        turtle.forward(i+i*3)
        turtle.seth(0)
        
turtle.done()