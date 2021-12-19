import turtle


def koch_curve(degree, length):
    if degree == 0:
        turtle.forward(length)
    elif degree > 0:
        length /= 3
        koch_curve(degree - 1, length)
        turtle.left(60)
        koch_curve(degree - 1, length)
        turtle.right(120)
        koch_curve(degree - 1, length)
        turtle.left(60)
        koch_curve(degree - 1, length)


def main(degree, length):
    turtle.hideturtle()
    window = turtle.Screen()
    window.screensize(640, 480)
    window.bgcolor("lightpink")
    window.title("Koch curve")
    turtle.penup()
    turtle.speed(6)
    turtle.backward(length / 2)
    turtle.pendown()
    turtle.showturtle()
    koch_curve(degree, length)
    turtle.mainloop()
    turtle.done()
    window.exitonclick()


main(3,300)


def snowflake(degree, length):

    turtle.hideturtle()
    window = turtle.Screen()
    window.screensize(640, 480)
    window.bgcolor("lightpink")
    window.title("Koch snowflake")
    turtle.penup()
    turtle.speed(0)
    turtle.goto(-length/2, length/2)
    turtle.pendown()
    turtle.showturtle()
    for _ in range(3):
        koch_curve(degree, length)
        turtle.right(120)
    turtle.done()
    window.exitonclick()


snowflake(4,300)
