class person():
    def __init__(self):
        #list of attributes
        self.name = ""
        self.age = 0
        self.gender = ""

    def info(self):
        print(f'Name: {self.name} Age; {self.age} Gender: {self.gender}')

class Employee():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.emp_id = ""
        self.position = ""

class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.studentID = 0
        self.major = ""
        self.university = ""

    def info(self):
        print(f'Name: {self.name} '
              f'Age: {self.age} '
              f'Gender: {self.gender}'
              f'StudentID: {self.studentID}'
              f'Major: {self.major}'
              f'University: {self.university}')

p1 = person()
p1.name = "Jirayut Jeebjong"
p1.age = 21
p1.gender = "Male"

emp1 = Employee()
emp1.name = "Yuttana"
emp1.age = 23
emp1.gender = "Male"
emp1.emp_id = "EMPMT01"
emp1.position = "CEO"

std1 = Student()
std1.name = "Jirayut Jeebjong"
std1.age = 21
std1.gender = "Male"
std1.studentID = 364411760011
std1.major = "MIT431"
std1.university = "RUTS"

p1.info()
emp1.info()
std1.info()

lst = [p1, emp1, std1]
for obj in lst:
    print(obj.__class__.__name__, end=" ")
    obj.info()



    #def info(self):
    #    print(f'Name: {self.name} '
    #          f'Age: {self.age} '
    #         f'Gender: {self.gender}'
    #         f'emp_id: {self.emp_id}'
    #          f'Position: {self.position}')