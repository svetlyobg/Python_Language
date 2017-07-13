import turtle
a = 0
colors = ['red','green','blue','purple']
i = 10
while True:
    turtle.left(i%24)
    turtle.forward(20)
    i+=1
    a+=1
    turtle.color(colors[a%4])
turtle.done()
