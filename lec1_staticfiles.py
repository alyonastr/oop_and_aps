class Ball:
    color = 'green'
    radius = 5

ball = Ball()

ball.color = 'red'

print(ball.color)
print(Ball.color)
 
Ball.color = 'white'
new_ball = Ball()
print(Ball.color)

print(dir(ball))