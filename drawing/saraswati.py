import turtle

t = turtle.Turtle()
t.getscreen().bgcolor('black')
t.color('orange')
t.penup()
t.speed(5)

t.backward(50)
t.left(60)
t.forward(550)

def hand(i):
	
	t.pendown()
	t.circle(15)
	t.backward(550-i)
	t.right(60)
	t.forward(100+i)
	t.left(120)
	t.forward(500-i)
	
	t.right(120)
	t.penup()
	t.circle(50,extent=180)
	t.pendown()
	t.circle(50,extent=180)
	
	t.penup()
	t.forward(300-(i*2))
	t.left(60)
	
	t.forward(50 if i < 400 else 600)

if __name__ == "__main__" :
	for i in range(0,500,100):
		hand(i)
		
	turtle.done()
