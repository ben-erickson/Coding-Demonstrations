import turtle

myPen = turtle.Turtle()
myPen.speed(10)
myPen.color("#000000")

def box(boxSize):
    myPen.begin_fill()
    # 0 deg
    myPen.forward(boxSize)
    myPen.left(90)
    # 90 deg
    myPen.forward(boxSize)
    myPen.left(90)
    # 180 deg
    myPen.forward(boxSize)
    myPen.left(90)
    # 270 deg
    myPen.forward(boxSize)
    myPen.end_fill()
    myPen.setheading(0)

#Position myPen in center of the screen
myPen.penup()
myPen.goto(-50,-50)
myPen.pendown()

#declare increment variable
i = 0

boxSize = 100

box(boxSize)
    
#This is not done. It is meant to draw Sierpinski Carpet, but I'm stuck
#right now, it just draws one box and stops.
#If I want to come back and take a stab at it, go right ahead.
