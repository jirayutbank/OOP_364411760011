class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def employee_info(self):
        print(f'Employee name: {self.name} Salary: {self.__salary}')

    #getter and setter methods
    def get_salary(self): #read data from attribute
        return self.__salary

    def set_salary(self,new_salary): #update data in attribute
        self.__salary = new_salary

#class end

#creat Object
emp = Employee("Jirayut",10000)
emp.employee_info()

# access to public member
print(emp.name)
#print(emp.__salary)

#name mangling
print(emp._Employee__salary)

# call to getter and setter method
print(emp.get_salary())
emp.set_salary(20000)
emp.employee_info()

