class Puppy:
    states = ['Болеет', 'Выздоравливает', 'Здоров']

    def __init__(self, state):
        self.states = ['Болеет', 'Выздоравливает', 'Здоров']
        self.state = self.states[0]

    def get_treatment(self):
        if self.state == self.states[0]:
            self.state = self.states[1]
        elif self.state == self.states[1]:
            self.state = self.states[2]

    def is_healthy(self):
        if self.state == self.states[2]:
            return True
        else: 
            return False

class Dog:
    states = ['Болеет', 'Выздоравливает', 'Здоров']

    def __init__(self, qty, index):
        states = ['Болеет', 'Выздоравливает', 'Здоров']
        self.qty = qty
        self.index = index
        self.puppies = []
        self.state = states[0]
        for i in range(qty+1):
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

    healthy_p = 0
    def all_are_healthy(self):
        healthy_p = 0
        for i in range(len(self.puppies)):
            p = self.puppies[i]
            if p == self.state[2]:
                healthy_p += 1
            if healthy_p == len(self.puppies):
                return True
            else:
                return False

    def give_away_all(self):
        self.puppies = puppies.clear()

class Vet:

    def __init__(self, name, dog):
        self.name = name
        self.dog = Dog(3, 2)

    def work(self):
        self.dog.get_treatment()

    def care(self):
        self.dog.all_are_healthy()
        if Dog.healthy_p == len(self.dog.puppies):
            print('Пристроить в хорошие руки')
        else:
            print('Не все щенки здоровы')
        
    def knowledge_base(self):
        if Dog.healthy_p == len(self.dog.puppies):
            print('Щенки в хороших руках')
        else:
            print('Щенки на лечении')
        
if __name__=='__main__':
    f = Vet('Вася', 3)
    f.dog.heal_all()
    f.work()
    f.care()
    f.dog.heal_all()
    f.care()
    f.knowledge_base()
        
    