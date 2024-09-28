class Puppy:
    states = ['Болеет', 'Выздоравливает', 'Здоров']

    def __init__(self, index, state):
        self.index = index
        self.state = state[0]

    def get_treatment(self):
        self.state = self.state[1]

    def is_healthy(self):
        if self.state == states[2]:
            print('Здоров')

class Dog:

    puppies = []

    def __init__(self, amt):
        self.puppies = puppies

    def heal_all(self):
        self.index = index[1]

    def all_are_healthy(self):

        if self.state == self.state[2]:
            print('True')

    def give_away_all(self):
        puppies = []

class Vet:

    def __init__(self, name, plant):
        

