import turtle

len = input("lenght: ")
ln = int(len)

g = 134
l = 120
i = 0

while i<ln:
    turtle.left(g)
    turtle.forward(l)
    i+=1
turtle.done()
