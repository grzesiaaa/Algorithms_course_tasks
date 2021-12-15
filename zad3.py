import turtle

def hilbert_curve(degree, angle, length):
    if degree > 0:
        turtle.right(angle)
        hilbert_curve(degree - 1, -angle, length)
        turtle.forward(length)
        turtle.left(angle)
        hilbert_curve(degree - 1, angle, length)
        turtle.forward(length)
        hilbert_curve(degree - 1, angle, length)
        turtle.left(angle)
        turtle.forward(length)
        hilbert_curve(degree - 1, -angle, length)
        turtle.right(angle)

def main(degree, length):
    window = turtle.Screen()
    window.screensize(640, 480)
    window.bgcolor("lightgreen")
    window.title("Hilbert curve")
    turtle.penup()
    turtle.speed(0)
    turtle.goto(-350, 300)
    turtle.pendown()
    hilbert_curve(degree, 90, length)
    turtle.done()

