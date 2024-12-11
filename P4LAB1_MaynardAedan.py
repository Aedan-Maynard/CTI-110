#Aedan Maynard

#11/3/24

# Turtles

# using turtles to draw shapes


import turtle

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.right(120)

# Set up the turtle
turtle.speed(1)  # Set the drawing speed

# Draw a square
turtle.penup()
turtle.goto(-100, 0)# Move the turtle to start position
turtle.pendown()
draw_square(100)

# Draw a triangle
turtle.penup()
turtle.goto(50, 0)  # Move the turtle to start position
turtle.pendown()
draw_triangle(100)

# Finish up
turtle.done()
