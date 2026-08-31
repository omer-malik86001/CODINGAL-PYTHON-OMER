import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(500, 500)

pen = turtle.Turtle()
pen.color("white")

for i in range(6):
    pen.forward(100)
    pen.right(60)

turtle.done()