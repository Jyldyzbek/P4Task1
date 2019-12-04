class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def result(self):
        print(f'{self.name} {self.lastname} enteret the {self.department} in {self.year_of_entrance}')

# class get_student_info(Student):


History = Student('Baygazy', 'Tashtanov', 'Electric', '2008')
History.result()

