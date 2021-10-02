import turtle

t = turtle.Turtle()
t.getscreen().bgcolor("black")
t.pendown()
t.color("yellow")
t.speed(25)

def shape(pen, size, i):
    for j in range(i):
        pen.forward(size)
        pen.left(360 / i)
    turtle.done()
    
if __name__ == "__main__":
    for i in range(3, 20, 1):
        shape(t, 120, i)
