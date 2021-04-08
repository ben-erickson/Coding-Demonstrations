import random
from turtle import Turtle

def recursive_lines(turtle, angle_start, angle, turn, line_max, iterations=0):
    colors = ["red", "orange", "brown", "green", "blue", "purple"]
    turtle.setheading(angle)
    color = random.randint(0, len(colors)-1)
    turtle.color(colors[color])

    x = turtle.xcor()
    y = turtle.ycor()

    line_len = random.randint(line_max / 2, line_max)
    turtle.forward(line_len)
    turtle.setheading(angle + 180)
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

    new_angle = angle + turn

    if iterations <= 1440 / turn:
        recursive_lines(turtle, angle_start, new_angle, turn, line_max, (iterations+1))

def main():
    ANIMATION_SPEED = 0
    billy_bob = Turtle()
    billy_bob.speed(ANIMATION_SPEED)
    line_len = random.randrange(100, 2000, 2)
    turn = random.randint(10,  30)
    recursive_lines(billy_bob, 0, 0, turn, 300)

main()
