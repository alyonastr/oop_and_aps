class Puppy:

    def __init__(self, index):
        states = {'1': 'Болеет', 
                  '2': 'Выздоравливает',
                  '3': 'Здоров'}
        self.index = index
        self.state = states['1']

    def get_treatment(self):
        if self.state == self.states['1']:
            self.state = self.states['2']
        elif self.state == self.states['2']:
            self.state = self.states['3']

    def is_healthy(self):
        if self.state == self.states['3']:
            return True
        else: 
            return False

class Dog:

    def __init__(self, n, index):
        states = {'1': 'Болеет', 
                  '2': 'Выздоравливает',
                  '3': 'Здоров'}
        self.n = n
        self.index = index
        self.puppies = []
        self.state = states['1']
        for i in range(n+1):
            p = Puppy(i)
            self.puppies.append(p)

    def heal_all(self):
        for i in range(len(self.puppies)):
            p = self.puppies[i] 
            p.get_treatment()

    def get_treatment(self):
        if self.state == self.states['1']:
            self.state = self.states['2']
        elif self.state == self.states['2']:
            self.state = self.states['3']

    def all_are_healthy(self):
        healthy = 0
        for i in range(len(self.puppies)):
            p = self.puppies[i]
            if p == self.state['3']:
                healthy += 1
            if healthy == len(self.puppies):
                return True
            else:
                return False

    def give_away_all(self):
        self.puppies = puppies.clear()

class Vet:

    def __init__(self, name, plant):
        self.name = name
        self.plant = Dog(3, 2)

    def work(self):
        self.plant.get_treatment()

    def care(self):
        self.all_are_healthy()
        if healthy == len(self.puppies):
            print('Пристроить в хорошие руки')
        else:
            print('Не все щенки здоровы')
        
    def knowledge_base(self):
        if healthy == len(self.puppies):
            print('Щенки в хороших руках')
        else:
            print('Щенки на лечении')
        
if __name__=='__main__':
    f = Vet('Вася', 3)
    f.plant.heal_all()
    f.work()
    f.care()
    f.plant.heal_all()
    f.care()
    f.knowledge_base()
        
    