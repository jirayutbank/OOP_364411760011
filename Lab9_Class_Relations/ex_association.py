from  ex_inherited import Teacher,Student

if __name__ == '__main__':
    # create object

    s1 = Student("S001", "Best", 21, "MIT", 3.50)
    s2 = Student("S002", "Mork", 23, "MIT", 3.50)

    t1 = Teacher("T001","Fon",40,"MT")
    t2 = Teacher("T002", "Pong", 43, "MT")

    s1.add_advisor(t1)
    s1.add_advisor(t2)

    t1.add_advisee(s1)
    t1.add_advisee(s2)

    s1.display_advisor()
    t1.display_advisee()