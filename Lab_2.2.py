import turtle

# Function to draw the letter A
def draw_A():
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.left(70)
    turtle.forward(105)
    turtle.right(140)
    turtle.forward(105)
    turtle.backward(50)
    turtle.right(110)
    turtle.forward(39)
    turtle.hideturtle()

# Function to draw the letter B
def draw_B():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(-100)
    turtle.right(90)
    turtle.circle(25, -180)
    turtle.right(180)
    turtle.circle(25, -180)
    turtle.hideturtle()

# Main program
turtle.speed(1.5)

draw_A()
draw_B()

turtle.done()
