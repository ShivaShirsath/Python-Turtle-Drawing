# Shapes
+ Program
  ```python

import turtle

t = turtle.Turtle()
t.getscreen().bgcolor("black")
t.pendown


def shape(pen, size, j):
	t.color('yellow')
	for i in range(j):
		pen.forward(size)
		pen.left(360 / j)


if __name__ == "__main__":
    for i in range(3, 19, 1):
        shape(t, 120, i)
    turtle.done()
```
+ Output 
  ![](../output/shapes.png)
