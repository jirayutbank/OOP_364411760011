from Model import Student, Vaccine, Vaccine_Passport


def display_vaccine():
    print("Vaccines list: ")
    n = 1
    for x in Vaccine.all_vaccine:
        print(f'\t{n}. {x}')
        n = n+1


#get student info
id = int(input("Enter student id? : "))
name = input("Enter student name? : ")
major = input("Enter student major? : ")
age = int(input("How old are you? : "))
weight = float(input("Enter your wieght(kg.): "))
height = int(input("Enter your height(kg.): "))

s = Student(id, name, major, age, weight, height)
#s.info()
#create vaccinated passport object
s_passport = Vaccine_Passport(s)

n = int(input("How many are you vaccinated?: "))
for x in range(n):

    display_vaccine()

    v = int(input(f'select 1- {len(Vaccine.all_vaccine)}: '))
    s_passport.add_vaccinated(Vaccine(Vaccine.all_vaccine[v-1]))

    date = input("Date(dd/mm/yyyy): ")
    s_passport.add_date(date)

s_passport.info()