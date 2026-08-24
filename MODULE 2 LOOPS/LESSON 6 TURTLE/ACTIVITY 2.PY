import turtle

turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(500, 500)

pen = turtle.Turtle()
pen.color("black")

pen.forward(150)
pen.left(120)

pen.forward(150)
pen.left(120)

pen.forward(150)

pen.penup()
pen.right(150)
pen.forward(80)
pen.pendown()

pen.right(90)
pen.forward(150)

pen.right(120)
pen.forward(150)

pen.right(120)
pen.forward(150)

turtle.done()