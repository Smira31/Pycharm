import turtle as t
t.shape('turtle')

radius = 10
t.left(90)
for i in range(10):
    t.circle(radius)
    t.circle(-radius)
    radius += 10

