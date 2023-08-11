
# class creation
class Student:
    # class attribute
    faculty  = "MT"
    # init method
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    # display object attribute
    def student_info(self):
        print(f'Name:{self.name} Major:{self.major} GPA:{self.gpa}')



# object creation
s1 = Student("Bank" , "MIT" , 3.00)
s2 = Student("Mork" , "DBM" , 3.55)
# s3 = Student()

# display attributes object
print(s1.name, s1.major , s1.gpa)
print(s2.name, s2.major , s2.gpa)

# display with f-string
print(f'Name:{s1.name} Major:{s1.major} GPA:{s1.gpa}')
print(f'Name:{s2.name} Major:{s2.major} GPA:{s2.gpa}')

print(s1.faculty, s2.faculty)

# change data in object attribute
print(s1.major)
s1.major = "MG"
print(s1.major)

# object call method in class
s1.student_info()
s2.student_info()

# list

std_list = [] # std_list = [s1,s2]
std_list.append(s1)
std_list.append(s2)
# display number of object in list
print(len(std_list))

# for loop and list
for x in std_list:
    x.student_info()