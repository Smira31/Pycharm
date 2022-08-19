import turtle as t
t.shape("triangle")
side_width = 20
padding = 10

for x in range(10):
     for i in range(4):
          t.forward(side_width)
          t.left(90)

     t.penup()
     t.right(90)
     t.forward(padding)
     t.left(90)
     t.backward(padding)
     t.pendown()

     side_width += 2 * padding


t.done()