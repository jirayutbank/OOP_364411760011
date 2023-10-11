class Person:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def info(self):
        print(f'{self.id} {self.name} {self.age}')

class Student(Person):
    def __init__(self,id,name,age,major,gpa):
        super().__init__(id,name,age)
        self.major = major
        self.gpa = gpa
        self.list_advisor = list()

    def info(self):
        print(f'{self.id} {self.name}'
              f'{self.age} {self.major} {self.gpa}')

    def display_advisor(self):
        print(f'Advisor of {self.name}: ')
        for x in self.list_advisor:
            x.info()

    def add_advisor(self,Teacher):
        self.list_advisor.append(Teacher)

class Teacher(Person):
    def __init__(self,id,name,age,faculty):
        super().__init__(id,name,age)
        self.faculty = faculty
        self.list_advisee = list()

    def info(self):
        print(f'{self.id} {self.name}'
              f'{self.age} {self.faculty} ')

    def display_advisee(self):
        print(f'Advisee of {self.name}: ')
        for x in self.list_advisee:
            x.info()

    def add_advisee(self, Teacher):
        self.list_advisee.append(Teacher)

# create object 1 person and 2 students. After that, display all info of object bu using loop

if __name__ == '__main__':

    p1 = Person("P001","Bank",21)
    s1 = Student("S001","Best",21,"MIT",3.50)
    s2 = Student("S002","Mork",23,"MIT",3.50)
    lst_obj = [p1,s1,s2]

    for x in lst_obj:
        x.info()