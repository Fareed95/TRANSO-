import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Railway Animation")
screen.bgcolor("black")

# Create a turtle for the railway
railway_turtle = turtle.Turtle()
railway_turtle.speed(2)
railway_turtle.color("gray")
railway_turtle.pensize(5)

# Create a turtle for the elegant 3D animation
elegant_turtle = turtle.Turtle()
elegant_turtle.speed(2)
elegant_turtle.pensize(2)
elegant_turtle.color("purple")

# Function to draw the railway track
def draw_railway():
    railway_turtle.penup()
    railway_turtle.goto(-300, -50)
    railway_turtle.pendown()
    railway_turtle.forward(600)

# Function to draw an elegant 3D letter
def draw_elegant_3d_letter(letter, size, position):
    elegant_turtle.penup()
    elegant_turtle.goto(position, 0)  # Adjust the starting position
    elegant_turtle.pendown()
    
    # Draw the elegant 3D effect
    elegant_turtle.left(90)
    elegant_turtle.forward(size / 2)
    elegant_turtle.right(90)
    elegant_turtle.write(letter, align="center", font=("Times New Roman", int(size), "normal"))
    elegant_turtle.left(90)
    elegant_turtle.backward(size / 2)
    elegant_turtle.right(90)

# Function to display the name "Transo" moving on the railway
def display_transo_on_railway():
    positions = [-250, -180, -110,-40,30, 100,180,190,200]
    for letter, position in zip("Transo !!!", positions):
        draw_railway()
        for previous_letter in "Transo !!!":
            draw_elegant_3d_letter(previous_letter, 50, positions["Transo !!!".index(previous_letter)])
        draw_elegant_3d_letter(letter, 50, position)
        screen.update()
        screen.ontimer(clear_screen, 300)

# Function to clear the screen
def clear_screen():
    elegant_turtle.clear()

# Draw the initial railway track
draw_railway()

# Display the name "Transo" moving on the railway
display_transo_on_railway()

# Close the window when clicked
screen.exitonclick()
