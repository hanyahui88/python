from visual import *

scene.title = "bounding ball"
scene.background = (1, 1, 1)
scene.center = (0, 5, 0)
scene.autoscale = False
floor = box(pos=(0, 0, 0), length=4, height=0.5, width=4, color=color.blue)
ball = sphere(pos=(0, 6, 0), radius=1, color=color.red)
ball.velocity = vector(0, -2, 0)
dt = 0.1
while 1:
    rate(100)
    ball.pos = ball.pos + ball.velocity * dt
    if ball.y < ball.radius:
        ball.velocity.y = -ball.velocity.y
    else:
        ball.velocity.y = ball.velocity - 9.8 * dt
