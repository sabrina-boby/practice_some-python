import turtle

turtle.shape("turtle")
turtle.speed(5)

for j in range(50,100,10):
    for i in range(5):       
        turtle.forward(j)
        turtle.left(90)

# turtle.left(45)
# turtle.forward(200)
turtle.exitonclick()        