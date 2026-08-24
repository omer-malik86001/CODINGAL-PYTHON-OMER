import turtle

turtle.Screen().bgcolor("black")
turtle.Screen().setup(500, 500)

pen = turtle.Turtle()
pen.color("white")
# FOR FORWARD THE NUMBER DENOTES HOW BIG THE LINE SHOULD BE


# FOR LEFT/RIGHT THE NUMBER DENOTED THE ANGLE BY WHICH TURTLE SHOULD TURN
for i in range(4):
    pen.forward(100)
    pen.left(90)

turtle.done()

