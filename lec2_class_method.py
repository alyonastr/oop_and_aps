class Myclass:
    counts = 0

    def __init__(self):
        Myclass.counts = Myclass.counts + 1

    @classmethod
    def classmethod(cls):
        print(cls.counts)

Myclass.classmethod()
mc1 = Myclass()
mc2 = Myclass()
mc3 = Myclass()

Myclass.classmethod()