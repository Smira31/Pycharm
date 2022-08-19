import turtle
import turtle as t

t.shape('turtle')
x = 0
y = 0
dlina = 10
for i in range(10):
    dlina += 20
    x -= 10
    y -= 10
    for i in range(4):
        t.pendown()
        t.forward(dlina)
        t.left(90)
        t.penup()












t.done()
