import turtle

#Set the size of the turtle window
turtle.setup(350,350)

#Move turtle down by the radius of circle
turtle.penup()
turtle.setheading(270)
turtle.forward(30)
turtle.setheading(0)
turtle.pendown()

#Draw the central circle
turtle.circle(30)

#Write Sarah in the upper left out of the way
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.write('Sarah')

#Draw x and y axis
turtle.penup()
turtle.goto(0,125)
turtle.pendown()
turtle.goto(0,-125)
turtle.penup()
turtle.goto(125,0)
turtle.pendown()
turtle.goto(-125,0)

#Write North, South, East, and West
turtle.penup()
turtle.goto(-10,130)
turtle.write('North')
turtle.goto(130,-5)
turtle.write('East')
turtle.goto(-15,-140)
turtle.write('South')
turtle.goto(-150,-5)
turtle.write('West')
