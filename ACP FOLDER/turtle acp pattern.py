# creating a square
import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(200,200)
polygon=turtle.Turtle()
polygon.pencolor("green")
s=4
s_len=300
a=360.0/s
# itrate loop for total number side
for i in range(s):
    polygon.forward(s_len)
    polygon.right(a)
turtle.done()