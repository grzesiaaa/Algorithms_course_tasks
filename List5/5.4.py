import turtle


def koch(degree, length):
    if degree == 0:
        turtle.forward(length)
    elif degree > 0:
        length /= 3
        koch(degree - 1, length)
        turtle.left(60)
        koch(degree - 1, length)
        turtle.right(120)
        koch(degree - 1, length)
        turtle.left(60)
        koch(degree - 1, length)


def curve(degree, length):
    turtle.hideturtle()
    window = turtle.Screen()
    window.screensize(640, 480)
    window.bgcolor("lightpink")
    window.title("Koch curve")
    turtle.penup()
    turtle.speed(30)
    turtle.backward(length / 2)
    turtle.pendown()
    turtle.showturtle()
    koch(degree, length)
    window.exitonclick()


def snowflake(degree, length):
    turtle.hideturtle()
    window = turtle.Screen()
    window.screensize(640, 480)
    window.bgcolor("lightpink")
    window.title("Koch snowflake")
    turtle.penup()
    turtle.speed(100)
    turtle.goto(-length/2, length/2)
    turtle.pendown()
    turtle.showturtle()
    for _ in range(3):
        koch(degree, length)
        turtle.right(120)
    window.exitonclick()
