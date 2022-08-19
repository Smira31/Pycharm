import turtle as t
t.shape('turtle')
t.color('red')
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.forward(200)
t.pendown()
t.color('green')
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()



t.done()