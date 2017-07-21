from turtle import *
import math

# Name your Turtle.


### Write your code below:
def draw_shape(num_sides):
    bubbles = Turtle()

    # Set Up your screen and starting position.
    setup(800, 500)
    x_pos = 0
    y_pos = 0
    bubbles.setposition(x_pos, y_pos)

    bubbles.pendown()
    angle = 360 / num_sides

    for side in range(num_sides):
        bubbles.forward(100)
        bubbles.left(angle)

user_input = input("What number")
user_input = int(user_input)
draw_shape(user_input)
# Close window on click.
exitonclick()
