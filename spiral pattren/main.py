import turtle 
turtle.Screen().bgcolor("lime")
turtle.Screen().screensize(100,100)
turtle.Screen().title("sprial pattern")
pen=turtle.Turtle()
size=0
for i in range(50):
    pen.fd(size)
    pen.left(90)
    size=size+5
turtle.done()