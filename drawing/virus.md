# Virus
+ Program
  ```python
  import turtle
  
  t = turtle.Turtle()
  t.getscreen().bgcolor("black")
  t.pendown()
  
  def virus():
    t.color('green')
    t.speed(25)
    for i in range(200):
      t.right(i)
      t.forward(i*5)
      if i == 199:
        t.backward(i)
    turtle.done()
    
  if __name__=="__main__":
    virus()
  ```
+ Output
  ![](output/virus.png)
