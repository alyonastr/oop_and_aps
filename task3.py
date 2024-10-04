class Puppy:
    states = ['Болеет', 'Выздоравливает','Здоров']

    def __init__(self, index, state):
        self.index = index
        self.state = states[0]

    def get_treatment(self):
        if self.state == self.states[0]:
            self.state = self.states[1]
        elif self.state == self.states[1]:
            self.state = self.states[2]

    def is_healthy(self):
        if self.state == self.states[2]:
            print('Здоров')

class Dog:

    def __init__(self, n, index):
        self.n = n
        self.puppies = []
        self.index = index
        self.state = self.states[0]
        for i in range(n+1):
            p = Puppy(i)
            self.puppies.append(p)

    def heal_all(self):
        for i in range(len(self.puppies)):
            p = self.puppies[i] 
            p.get_treatment()

    def get_treatment(self):
        if self.state == self.states[0]:
            self.state = self.states[1]
        elif self.state == self.states[1]:
            self.state = self.states[2]

    def all_are_healthy(self):
        healthy = 0
        for i in range(len(self.puppies)):
            p = self.puppies[i]
            if p == self.state[2]:
                healthy += 1
            if healthy == len(self.puppies):
                print('True')
            else:
                print('False')

    def give_away_all(self):
        self.puppies = puppies.clear()

class Vet:

    def __init__(self, name, plant):
        self.name = name
        self.plant = Dog()

    def work(self):
        self.plant.get_treatment()

    def care(self):
        self.all_are_healthy()
        if healthy == len(self.puppies):
            print('Пристроить в хорошие руки')
        else:
            print('Не все щенки здоровы')
        

        

