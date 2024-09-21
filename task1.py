class SchoolJournal:

    def __init__(self, subject, student):
        self.subject = subject
        self.student = student
        grade_list = []

    def grade(self):
        g = int(input())
        grade_list[-1] = g

    def printer(self):
        print(SchoolJournal.student)
        print(SchoolJournal.subject)
        print(grade_list)

    def final_grade(self):
        print(sum(grade_list)// len(grade_list))