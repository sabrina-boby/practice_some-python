import turtle


height = 5

turtle.speed(1)

# turtle.penup()
for y in range(5):
    for x in range(5):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*5)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()