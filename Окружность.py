import turtle

turtle.speed(5)
turtle.shape('turtle')

dlina = 10
x = 0
y = 0
for i in range(10):
    dlina += 20
    x -= 10
    y -= 10
    for i in range(4):
        turtle.pendown()
        turtle.forward(dlina)
        turtle.left(90)
        turtle.penup()
    turtle.setx(x)
    turtle.sety(y)

t.done()