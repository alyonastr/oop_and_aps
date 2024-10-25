class SummatorClass:
    @staticmethod
    def sum_1(a, b):
        return a + b
    
    def sum_2(self, a, b):
        return a + b
    
    def sum_3(self, a, b):
        return SummatorClass.sum_1(a, b)
    
print(SummatorClass.sum_1(5, 10))
sum_num = SummatorClass()
print(sum_num.sum_2(10, 15))
print(sum_num.sum_1(20, 25))
print(sum_num.sum_3(30, 35))