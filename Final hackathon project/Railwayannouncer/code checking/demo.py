import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("3D Turtle Animation")
screen.bgcolor("black")

# Create a turtle for the 3D animation
transo_turtle = turtle.Turtle()
transo_turtle.hideturtle()
transo_turtle.speed(2)
transo_turtle.pensize(2)
transo_turtle.color("cyan")

# Function to draw a 3D letter
def draw_3d_letter(letter, size):
    transo_turtle.penup()
    transo_turtle.forward(size)
    transo_turtle.pendown()
    
    # Draw the 3D effect
    transo_turtle.left(90)
    transo_turtle.forward(size / 2)
    transo_turtle.right(90)
    transo_turtle.write(letter, align="center", font=("Arial", int(size), "normal"))
    transo_turtle.left(90)
    transo_turtle.backward(size / 2)
    transo_turtle.right(90)

# Draw the name "Transo"
transo_turtle.penup()
transo_turtle.goto(-200,0)  # Adjust the starting position
draw_3d_letter("T", 50)

transo_turtle.penup()
transo_turtle.goto(-140, 0)
draw_3d_letter("R", 50)

transo_turtle.penup()
transo_turtle.goto(-80, 0)
draw_3d_letter("A", 50)

transo_turtle.penup()
transo_turtle.goto(-20, 0)
draw_3d_letter("N", 50)

transo_turtle.penup()
transo_turtle.goto(40, 0)
draw_3d_letter("S", 50)

transo_turtle.penup()
transo_turtle.goto(100, 0)
draw_3d_letter("0", 50)

transo_turtle.penup()
transo_turtle.goto(180, 0)
draw_3d_letter("!!!", 50)

# Close the window when clicked
# screen.exitonclick()
screen = turtle.Screen()
screen.title("Rotating Arrow Animation")
screen.bgcolor("white")

# Create a turtle for the rotating arrow
arrow_turtle = turtle.Turtle()
arrow_turtle.speed(2)
arrow_turtle.color("blue")
arrow_turtle.pensize(3)

# Function to draw an arrow
def draw_arrow():
    arrow_turtle.clear()
    arrow_turtle.forward(100)
    arrow_turtle.right(120)
    arrow_turtle.forward(100)
    arrow_turtle.right(120)
    arrow_turtle.forward(100)

# Function to rotate the arrow
def rotate_arrow():
    arrow_turtle.right(5)
    draw_arrow()
    screen.update()
    screen.ontimer(rotate_arrow, 50)

# Initial drawing of the arrow
draw_arrow()

# Start the rotation
rotate_arrow()

# Close the window when clicked
screen.exitonclick()
