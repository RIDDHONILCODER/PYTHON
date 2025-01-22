#Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?
import turtle
turtle.Screen().bgcolor("light blue")
turtle.Screen().screensize(100,100)
hex=turtle.Turtle()

angle=360/6
for i in range(6):
    hex.forward(100)
    hex.right(angle)
turtle.done()