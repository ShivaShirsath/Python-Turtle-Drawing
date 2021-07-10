<h1 align=center>Python Turtle for Shape drawing </h1>

<p align=center> Program </p>

```python
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
```
<p align=center> Output </p>

![](output.png)
## Use mobile to run it without error. (install pydroid)
# [►](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)
