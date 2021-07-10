import turtle

t = turtle.Turtle()
t.getscreen().bgcolor("black")
t.pendown()
t.color("yellow")


def shape(pen, size, i):
    if size <= i:
        return
    else:
        for j in range(i):
            pen.forward(size)
            pen.left(360 / i)


if __name__ == "__main__":
    for i in range(3, 19, 1):
        shape(t, 120, i)
    turtle.done()
