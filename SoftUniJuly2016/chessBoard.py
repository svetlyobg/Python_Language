import turtle

side=40
turtle.speed('fastest')
fourDoubleRows = 0
while fourDoubleRows<4:
    fourSquares =0:
    for j in range(4):
        for i in range(4)
            if i%2==0:
                turtle.begin_fill()
                turtle.forward(side)
                turtle.left(90)
                turtle.forward(side)
                turtle.left(90)
                turtle.forward(side)
                turtle.left(90)
                turtle.end_fill()
                turtle.forward(side)
                #turtle.exitonclick()
            if j < 3:
                turtle.penup()
                turtle.forward(2*side)
                turtle.pendown()
            fourSquares+=1
        if fourDoubleRows <3:
            turtle.penup()
            turtle.left(180)
            turtle.forward(6*side)
