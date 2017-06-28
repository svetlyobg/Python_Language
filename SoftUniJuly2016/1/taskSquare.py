import turtle

sqLen = input("Please enter the lenght:")
num = int(sqLen)

turtle.speed('fastest')

for b in range (1,100):
    turtle.forward(num)
    turtle.left(90)

turtle.done()