# Saraswati
+ Program
  ```python
    from turtle import *

    speed(0)
    bgcolor("black")
    pensize(1)
    color("yellow")

    def shapeShape(angle=6, aglen=1):
        for i in range(angle):
            left(360/angle)
            for i in range(angle*aglen):
                forward(1000/angle)
                left(360/(angle/aglen))

    if "__main__"==__name__:
            for i in range(2,15):
                shapeShape(i)
            done()
  ```

