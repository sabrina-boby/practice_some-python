import turtle

turtle.color("yellow")

def function(a,b):
	for i in range(4):
		turtle.forward(a)
		turtle.left(b)
	turtle.right(30)

n = 0
while n<12:
	function(100,90)	
	n+=1

turtle.exitonclick()	