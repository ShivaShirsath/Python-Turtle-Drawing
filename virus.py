import turtle

t = turtle.Turtle()
t.getscreen().bgcolor("black")
t.pendown()
t.speed(25)
t.color("green")

def virus():
  for i in range(0,200):
		t.left(i)
		t.forward(i)
		if i == 198:
			turtle.done()
	
if __name__=="__main__":
  virus()
