class Student:
    def __init__(self,id,name,major,age,weight,height):
        #attribute
        self.id = id
        self.name = name
        self.major = major
        self.age = age
        self.weight = weight
        self.height = height

    def info(self):
        print(f'\tStudent ID: {self.id}\n ' 
              f'\tStudent Name: {self.name}\n ' 
              f'\tMajor: {self.major}\n ' 
              f'\tAge: {self.age}\n '
              f'\tWeight: {self.weight}\n '
              f'\tHeight: {self.height} ')

class Vaccine:
    all_vaccine = ["sinovac" , "astrazeneca" , "johnson&johnson" ,
                   "moderna" , "sinopharm" , "pfizer"]
    def __init__(self,vacc_name):
        self.__vacc_name = vacc_name

        # getter and setter
    def get_vacc_name(self):
        return self.__vacc_name
    def set_vacc_name(self,new_vacc_name):
        self.__vacc_name = new_vacc_name
    def info(self):
        print(f'Vaccine: {self.__vacc_name}')

class Vaccine_Passport:
    def __init__(self,Student):
        self.student = Student
        self.vaccinated = list()
        self.date = list()

    def add_vaccinated(self,vac):
        self.vaccinated.append(vac)

    def add_date(self,date):
        self.date.append(date)

    def info(self):
        # 1.display student info
        print("Student information: ")
        self.student.info()
        # 2.display vaccine info
        if len(self.vaccinated) == 0:
            print(f'\tNo vaccinated data.')
        else:
            #n = 0
            for x in range(len(self.vaccinated)):
                print(f'\tvaccine {x+1}:\t{self.vaccinated[x].get_vacc_name()} \tdate: {self.date[x]}')
