import turtle

# Create a turtle object
hexagon_turtle = turtle.Turtle()

# Number of sides
sides = 6
angle = 360 / sides

# Length of each side
side_length = 100

# Draw a hexagon
for _ in range(sides):
    hexagon_turtle.forward(side_length)
    hexagon_turtle.right(angle)

# Hide the turtle and display the window
hexagon_turtle.hideturtle()
turtle.done()
