import turtle


#First big triangle
t_side_len = 500

turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.right(120)
turtle.forward(t_side_len)
turtle.left(120)
turtle.forward(t_side_len)
turtle.left(120)
turtle.forward(t_side_len)

#Inner triangle
turtle.left(120)
turtle.forward(t_side_len / 2)
turtle.left(60)
turtle.forward(t_side_len / 2)
turtle.left(120)
turtle.forward(t_side_len / 2)
turtle.left(120)
turtle.forward(t_side_len / 2)
