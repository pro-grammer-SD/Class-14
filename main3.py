import turtle

turtle.getscreen().bgcolor("#abd6e3")
turtle.color("black")

turtle.hideturtle()

fan_of_carol_ma_am = True

if fan_of_carol_ma_am: 
    for i in range(50):
        turtle.forward(i * 5)
        turtle.left(90)
        
turtle.done()