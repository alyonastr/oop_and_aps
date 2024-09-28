class SchoolJournal:

    def __init__(self, subject, student):
        self.subject = subject
        self.student = student
        self.grade_list = []

    def grade(self, g):
        self.g = g 
        if g >=1 and g<=5:
            self.grade_list.append(g)


    def printer(self):
        print(self.student)
        print(self.subject)
        print(self.grade_list)

    def final_grade(self):
        print(sum(self.grade_list)/ len(self.grade_list))


funct = SchoolJournal('математика', 'юля')
funct.grade(4)
funct.grade(5)
funct.printer()
funct.final_grade()
