class Pyramid:
    def __init__(self, max_h, bricks_count, line, bricks, h):
        self.max_h = max_h
        self.bricks_count = bricks_count
        self.line = line
        self.bricks = bricks
        self.h = h

    
    def add_bricks(self, h, bricks):
        self.line += 1
        self.bricks_count += 1
        self.bricks -= 1
        if self.line >= 5:
            self.h += 1
            self.line += self.bricks - 1

    def get_height(self):
        print(self.h)

    def is_done(self):
        self.done = (self.h/ self.max_h) * 100

        

class Builder:

    def __init__(self, bricks, my_pyramid, h, bricks_count):
        self.bricks = bricks
        self.my_pyramid = my_pyramid
        self.h = h
        self.bricks_count = bricks_count
    
    def buy_bricks(self):
        if self.bricks <= 15:
            self.bricks = self.bricks + (15 - self.bricks)
        
    def build_pyramyd(self):
        self.h += 1
        self.bricks_count += 1
        self.bricks -=1


    def work_day(self):
        print(day)
        print()
        print(self.bricks)
        print(self.done)

        if self.done == 100 and self.h == self.max_h:
            exit(0)



funct1 = Pyramid(13, 0, 0, 15, 0)
funct1.add_bricks(4,15)
funct1.get_height()
funct1.is_done()

funct2 = Builder(3, 15, 0, 0)
funct2.buy_bricks()
funct2.build_pyramyd()
funct2.work_day()
