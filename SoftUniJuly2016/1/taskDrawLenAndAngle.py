import turtle

lenghtUser = input("Enter lenght of a line: ")
lenght = int(lenghtUser)
angleUser = input("Enter angle: ")
angle = int(angleUser)

turtle.speed('fastest')
turtle.color('red')

while True:
    turtle.left(angle)
    turtle.forward(lenght)
turtle.done()