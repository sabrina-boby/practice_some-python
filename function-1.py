import turtle


turtle.color("green")

def draw_square(a,b):
    for i in range(4):
        turtle.forward(a)
        turtle.left(b)

counter = 0
while counter < 12:
    draw_square(100,90)
    turtle.right(30)
    counter += 1

turtle.exitonclick()