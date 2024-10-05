import random

class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
        self.h = 0 
        self.bricks_row = [i for i in range(max_h, 0, -1)]
        self.all_bricks = sum(self.bricks_row)
        self.bricks_in_row_now = 0

    
    def add_bricks(self, bricks):
        self.bricks_count += bricks
        bricks_in_row = self.bricks_row[self.h-1]
        if self.bricks_in_row_now > bricks_in_row:
            self.h +=1
            dop_bricks = self.bricks_in_row_now - bricks_in_row
            self.bricks_in_row_now = 0
            self.bricks_in_row_now += dop_bricks
            bricks += dop_bricks 

        else:
            self.bricks_in_row_now += bricks
             
           
    def get_height(self):
        print(self.h)

    def is_done(self):
        self.done = (self.h/ self.max_h) * 100
        print(self.done)
        return self.done
      

class Builder:

    def __init__(self, bricks):
        self.bricks = bricks
        self.my_pyramid = Pyramid(15)
        self.day = 0
    
    def buy_bricks(self):
        self.bricks += 15 - self.bricks
        
                
    def build_pyramyd(self, N_bricks):
        if self.bricks >= N_bricks:
            self.my_pyramid.add_bricks(N_bricks)
            self.bricks -= N_bricks
        else: 
            self.buy_bricks()

    def work_day(self):
        bricks_list = [1, 2, 3, 4, 5]
        self.day += 1
        c = random.choice(bricks_list)
        print(c, 'выложил')
        print(self.day, 'день')
        self.build_pyramyd(c)
        self.my_pyramid.get_height()
        print(self.bricks, 'кирпичей у сроителя')
        s = self.my_pyramid.is_done()
        if s == 100:
            exit(0)
        

    
    

if __name__ == '__main__':
    b = Builder(13)
    while True:
        b.work_day()


     
