import turtle

# Set up the screen
turtle.Screen().bgcolor("pink")

# Create a turtle object
hexagon_turtle = turtle.Turtle()

# Draw a hexagon
for _ in range(6):
    hexagon_turtle.forward(100)
    hexagon_turtle.left(60)

# Hide the turtle and finish drawing
hexagon_turtle.hideturtle()
turtle.done()
