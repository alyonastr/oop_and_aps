class Ball:
 
    def __init__(self, mass):
 
        self.mass = mass
        self.x = 0
        self.y = 0 

    def drop(self):
        print('Я подбросился')
        self.y = 2

    def kick(self):
        print('Я пнулся')
        self.y += 1
 
    def fail(self):
        self.mass = self.mass - 0.3
 
ball = Ball(0.5)
ball.drop()
ball.kick()
ball.fail()
print(ball.y)
print(ball.mass)

 