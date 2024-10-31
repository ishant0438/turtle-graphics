import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Fastest drawing speed

# Define colors for the spiral
colors = ["red", "yellow", "blue", "green", "orange", "purple"]

# Draw a colorful spiral
for i in range(360):
    spiral_turtle.pencolor(colors[i % 6])  # Change color every iteration
    spiral_turtle.width(i / 100 + 1)  # Change width of the pen
    spiral_turtle.forward(i)  # Move the turtle forward
    spiral_turtle.right(59)  # Turn the turtle right

# Hide the turtle and finish
spiral_turtle.hideturtle()
turtle.done()
