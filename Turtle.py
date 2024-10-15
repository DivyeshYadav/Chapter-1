import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,300)
t = turtle.Turtle()
for i in range(5):
    t.forward(40)
    t.right(90)
    i = i+1
t.penup()
t.goto(-100,100)
t.pendown()
for i in range(3):
    t.forward(40)
    t.left(120)
    i = i+1
turtle.done()

