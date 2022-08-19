import turtle as t
t.speed(10)

# circle
t.begin_fill()
t.color('yellow')
t.circle(100)
t.penup()
t.end_fill()
# left eys
t.begin_fill()
t.color('blue')
t.goto(40, 150)
t.pendown()
t.circle(-15)
t.end_fill()
t.penup()
#right eys
t.begin_fill()
t.color('blue')
t.goto(-40, 150)
t.pendown()
t.circle(-15)
t.end_fill()
t.penup()
# nose
t.goto(0,80)
t.pendown()
t.color('black')
t.width(5)
t.left(90)
t.forward(40)
t.penup()
#smile
t.goto(-50, 70)
t.color('red')
t.pendown()
t.right(180)
t.circle(50, 180)









t.done()